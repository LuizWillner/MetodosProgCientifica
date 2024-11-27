from typing import Callable

from metodos.runge_kutta_4 import runge_kutta_4


def preditor_corretor_4(
    t: float | int | list[float | int] | tuple[float | int], 
    w: float | int | list[float | int] | tuple[float | int], 
    h: float | int, 
    tfinal: float | int, 
    tol: float | int, 
    f: Callable[[float, float], float], 
    hmax: float | int | None = None, 
    hmin: float | int | None = None
):
    # TODO: Somente primeira iteração implementada. Implementar o resto.
    
    if not isinstance(t, type(w)):
        raise ValueError('Params t e w devem ser do mesmo tipo')
    elif isinstance(t, (int, float)):
        res_rk = runge_kutta_4(t0=t, w0=w, h=h, tfinal=tfinal)
        t0, w0 = t, w
        t1, w1 = res_rk[1][0], res_rk[1][1]
        t2, w2 = res_rk[2][0], res_rk[2][1]
        t3, w3 = res_rk[3][0], res_rk[3][1]
        t4 = res_rk[4][0] 
    elif isinstance(t, (list, tuple)):
        try:
            t0, w0 = t[0], w[0]
            t1, w1 = t[1], w[1]
            t2, w2 = t[2], w[2]
            t3, w3 = t[3], w[3]
            t4 = t[4]
        except IndexError:
            raise ValueError('t e w não possuem elementos suficientes. t deve ter pelo menos 5 elementos e w 4 elementos') 
        
    else:
        raise ValueError('Tipo de t e/ou w não suportado')
    
    resultados: list[tuple] = []
    resultados.append((t0, w0))
    
    recalcular = False
    
    print(f'h={h:.4f}')
    print(f'hmáx={hmax:.4f}')
    print(f'hmin={hmin:.4f}')
    print(f'tol = {tol:.8f}')
    print()
    
    print(f't0 = {t0:.4f}\tw0 = {w0:.8f}')
    print(f't1 = {t1:.4f}\tw1 = {w1:.8f}')
    print(f't2 = {t2:.4f}\tw2 = {w2:.8f}')
    print(f't3 = {t3:.4f}\tw3 = {w3:.8f}')
    print(f't4 = {t4:.4f}')
    
    # Preditor (explícito): Adams-Bashforth de 4 passos (ordem 4)
    print()
    print('Preditor (explícito): Adams-Bashforth de 4 passos (ordem 4)')
    
    f3 = f(t3, w3)
    print(f'f3 = {f3:.8f}')
    
    f2 = f(t2, w2)
    print(f'f2 = {f2:.8f}')
    
    f1 = f(t1, w1)
    print(f'f1 = {f1:.8f}')
    
    f0 = f(t0, w0)
    print(f'f0 = {f0:.8f}')
    
    w4_pred = w3 + (h/24)*(55*f3 - 59*f2 + 37*f1 - 9*f0)
    print(f'w4_pred = {w4_pred:.8f}')
    
    # Corretor (implícito): Adams-Moulton de 3 passos (ordem 4)
    print()
    print('Corretor (implícito): Adams-Moulton de 3 passos (ordem 4)')
    
    f4 = f(t4, w4_pred)
    print(f'f4 = {f4:.8f}')
    
    w4_corr = w3 + (h/24)*(9*f4 + 19*f3 - 5*f2 + f1)
    print(f'w4_corr = {w4_corr:.8f}')
    
    # Ajuste do passo h
    print()
    print('# Ajuste do passo h')
    
    errotrunc = (19/270) * abs(w4_corr - w4_pred)/h
    q = 1.5 * ( (tol*h) / (abs(w4_corr - w4_pred)) )**(1/4)
    print(f'errotrunc = {errotrunc:.8f}')
    print(f'q = {q:.8f}')
    
    if q >= 1:
        print(f'q >= 1 -> Aproximação aceitável. Avançar iteração com o mesmo h')
        wi = w4_corr
        ti = t4
        recalcular = False
        resultados.append((ti, wi))
    else:
        print(f'q < 1 -> Aproximação não aceitável. Recalcular iteração com h menor q*h > hmin (={hmin})')
        h = q * h if q*h > hmin else hmin
        print(f'hnovo = {h:.8f}')
        recalcular = True
    
    return resultados
