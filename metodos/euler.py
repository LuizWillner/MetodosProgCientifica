from typing import Callable


def euler(
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
        print(f'f({ti:.4f}, {wi:.8f}) = {f(ti, wi):.8f}')
        wi = wi + h * f(ti, wi)
        ti = ti + h
        i += 1
        print(f't{i} = {ti:.4f}')
        print(f'w{i} = {wi:.8f}')
        print()
        resultados.append((ti, wi))
        
    return resultados
