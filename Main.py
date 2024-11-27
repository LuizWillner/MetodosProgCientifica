import math
# from metodos.euler import euler
from metodos.runge_kutta_4 import runge_kutta_4
from metodos.runge_kutta_fehlberg import runge_kutta_fehlberg
from metodos.preditor_corretor_4 import preditor_corretor_4


def f(t, y):
    y_ = math.sin(t) + math.e**(-t) # inserir expressão aqui
    return y_

if __name__ == "__main__":
    res = None 
    
    # res = runge_kutta_4(
    #     t0=0,
    #     w0=1,
    #     h=0.25,
    #     tfinal=1,
    #     f=f
    # )
    
    res = runge_kutta_fehlberg(
        t0=0,
        w0=0,
        h=0.135,
        tfinal=1,
        tol=10**(-4),
        hmax=0.25,
        hmin=0.02,
        f=f   
    )
    
    # res = preditor_corretor_4(
    #     t=(2, 2.25,        2.5,         2.75,      3),
    #     w=(1, 1.449986427, 1.833319345, 2.17855937),
    #     h=0.25,
    #     tfinal=3,
    #     tol=10**(-4),
    #     hmax=0.25,
    #     hmin=0.025,
    #     f=f
    # )
    
    # res = preditor_corretor_4(
    #     t=0.0,
    #     w=0.5,
    #     h=0.2,
    #     tfinal=2,
    #     tol=10**(-5),
    #     hmax=0.2,
    #     hmin=0.01,
    #     f=f
    # )
    
    print()
    print(res)