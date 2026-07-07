import numpy as np
import argparse
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from utils.projectile_functions import dSdt


def main():
    parser = argparse.ArgumentParser(
        description="Simulador de trayectoria con resistencia al aire"
    )
    parser.add_argument('--v', type=float, default=1.0,
                         help="Velocidad inicial")
    parser.add_argument('--b', type=float, default=0.0,
                         help="Coeficiente de resistencia del aire (0.0 a 1.0)")
    parser.add_argument('--tmax', type=float, default=2.0,
                         help="Tiempo máximo de vuelo")
    parser.add_argument('--angulos', type=float, nargs='+', default=[40, 45, 50],
                         help="Lista de ángulos de lanzamiento en grados")

    args = parser.parse_args()

    plt.figure()
    for angulo in args.angulos:
        theta = angulo * np.pi / 180
        sol = solve_ivp(
            dSdt, [0, args.tmax],
            y0=[0, args.v * np.cos(theta), 0, args.v * np.sin(theta)],
            t_eval=np.linspace(0, args.tmax, 1000),
            args=(args.b,)
        )
        plt.plot(sol.y[0], sol.y[2], label=fr'$\theta_0={angulo}^{{\circ}}$')

    plt.ylim(bottom=0)
    plt.legend()
    plt.xlabel('$x/g$', fontsize=20)
    plt.ylabel('$y/g$', fontsize=20)
    plt.savefig('trayectoria.png')
    plt.show()


if __name__ == "__main__":
    main()
