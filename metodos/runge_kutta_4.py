from typing import Callable


def runge_kutta_4(
    t0: float | int,
    w0: float | int, 
    h: float | int, 
    tfinal: float | int, 
    f: Callable[[float, float], float]
) -> list[tuple]:
    
    resultados: list[tuple] = []
    resultados.append((t0, w0))
    
    ti = t0
    wi = w0
    i = 0
    
    print(f'h={h:.4f}')
    print()
    print(f't0 = {t0:.4f}')
    print(f'w0 = {w0:.8f}')
    print()
    
    while ti < tfinal:
        print(f'============{i+1}a iteração (i={i})=============')
        
        # k1
        compart_t = ti
        compart_y = wi
        k1 = h * f(compart_t, compart_y)
        print(f'k1 = h * f({compart_t:.4f}; {compart_y:.8f}) = {k1:.8f}')
        
        # k2
        compart_t = ti + h/2
        compart_y = wi + (1/2)*k1
        k2 = h * f(compart_t, compart_y)
        print(f'k2 = h * f({compart_t:.4f}; {compart_y:.8f}) = {k2:.8f}')
        
        # k3
        compart_t = ti + h/2
        compart_y = wi + (1/2)*k2
        k3 = h * f(compart_t, compart_y)
        print(f'k3 = h * f({compart_t:.4f}; {compart_y:.8f}) = {k3:.8f}')
        
        # k4
        compart_t = ti + h
        compart_y = wi + k3
        k4 = h * f(compart_t, compart_y)
        print(f'k4 = h * f({compart_t:.4f}; {compart_y:.8f}) = {k4:.8f}')
        
        # w(i+1)
        wi = wi + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        ti = ti + h
        i += 1
        
        print()
        print(f't{i} = {ti:.4f}')
        print(f'w{i} = {wi:.8f}')
        print()
        
        resultados.append((ti, wi))
        
    return resultados
