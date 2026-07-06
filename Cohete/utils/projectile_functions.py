import numpy as np
def dSdt(t, S, B):
    """
    Define el sistema de ecuaciones diferenciales para el movimiento
    del proyectil con resistencia al aire.
    Parametros:
        t (float): Tiempo
        S (list): Estado actual [x, vx, y, vy]
        B (float): Coeficiente de resistencia del aire. Varía de 0.0 a 1.0
    Retorna:
        list: Derivadas [dx/dt, dvx/dt, dy/dt, dvy/dt]
    """
    
    x, vx, y, vy = S
    return [vx,
            -B*np.sqrt(vx**2+vy**2)*vx,
            vy,
            -1-B*np.sqrt(vx**2+vy**2)*vy]
