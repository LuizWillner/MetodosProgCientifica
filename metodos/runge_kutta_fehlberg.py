from typing import Callable


def runge_kutta_fehlberg(
    t0: float | int, 
    w0: float | int,
    h: float | int, 
    tfinal: float | int, 
    tol: float | int, 
    f: Callable[[float, float], float], 
    hmax: float | int | None = None, 
    hmin: float | int | None = None
) -> list[tuple]:
    
    resultados: list[tuple] = []
    resultados.append((t0, w0))
    
    ti = t0
    wi = w0
    i = 0
    
    print(f'h={h:.4f}')
    print(f'hmáx={hmax:.4f}')
    print(f'hmin={hmin:.4f}')
    print(f'tol = {tol:.8f}')
    print()
    
    recalcular = False
    
    while ti < tfinal:
        if not recalcular:
            print(f'============{i+1}a iteração (i={i})=============')
        else: 
            print(f'============RECALCULAR {i+1}a iteração (i={i})=============')
            
        print(f't{i} = {ti:.4f}')
        print(f'w{i} = {wi:.8f}')
        print(f'h = {h:.4f}')
        print()
        
        compart_t = ti
        compart_y = wi
        k1 = h * f(compart_t, compart_y)
        print(f'k1 = f({compart_t:.4f}; {compart_y:.8f}) = {k1:.8f}')
        
        compart_t = ti + h/4
        compart_y = wi + (1/4)*k1
        k2 = h * f(compart_t, compart_y)
        print(f'k2 = f({compart_t:.4f}; {compart_y:.8f}) = {k2:.8f}')
        
        compart_t = ti + (3/8)*h
        compart_y = wi + (3/32)*k1 + (9/32)*k2
        k3 = h * f(compart_t, compart_y)
        print(f'k3 = f({compart_t:.4f}; {compart_y:.8f}) = {k3:.8f}')
        
        compart_t = ti + (12/13)*h
        compart_y = wi + (1932/2197)*k1 - (7200/2197)*k2 + (7296/2197)*k3
        k4 = h * f(compart_t, compart_y)
        print(f'k4 = f({compart_t:.4f}; {compart_y:.8f}) = {k4:.8f}')
        
        compart_t = ti + h
        compart_y = wi + (439/216)*k1 - 8*k2 + (3680/513)*k3 - (845/4104)*k4
        k5 = h * f(compart_t, compart_y)
        print(f'k5 = f({compart_t:.4f}; {compart_y:.8f}) = {k5:.8f}')
        
        compart_t = ti + h/2
        compart_y = wi - (8/27)*k1 + 2*k2 - (3544/2565)*k3 + (1859/4104)*k4 - (11/40)*k5
        k6 = h * f(compart_t, compart_y)
        print(f'k6 = f({compart_t:.4f}; {compart_y:.8f}) = {k6:.8f}')
        
        
        wnext_ = wi + (16/135)*k1 + (6656/12825)*k3 + (28561/56430)*k4 - (9/50)*k5 + (2/55)*k6
        wnext = wi + (25/216)*k1 + (1408/2565)*k3 + (2197/4104)*k4 - (1/5)*k5
        print()
        print(f't{i+1} = {ti+h:.4f}')
        print(f'w~{i+1} = {wnext_:.8f}')
        print(f'w{i+1} = {wnext:.8f}')
        
        errotrunc = (1/h) * abs(wnext_ - wnext)
        q = 0.84*( (tol*h) / (abs(wnext_ - wnext)) )**(1/4)
        print()
        print(f'errotrunc = {errotrunc:.8f}')
        print(f'q = {q:.8f}')
        
        if q >= 1:
            print(f'q >= 1 -> Aproximação aceitável. Avançar iteração com h maior q*h < hmax (={hmax})')
            h = q * h
            if hmax is not None and h > hmax:
                h = hmax
            print(f'hnovo = {h:.8f}')
            recalcular = False
            wi = wnext
            ti = ti + h
            i += 1
            resultados.append((ti, wi))
        else:
            print(f'q < 1 -> Aproximação não aceitável. Recalcular iteração com h menor q*h > hmin (={hmin})')
            h = q * h
            if hmin is not None and h < hmin:
                h = hmin
            print(f'hnovo = {h:.8f}')
            recalcular = True
        
        print()
    
    return resultados
