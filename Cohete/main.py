import numpy as np
import argparse
from utils.projectile_functions import dSdt

def main():
    # Configuración de argumentos para la terminal
    parser = argparse.ArgumentParser(description="Simulador de trayectoria con resistencia al aire")
    
    # Parámetros necesarios según la función dSdt de Anthonny
    parser.add_argument('--t', type=float, default=0.0, help="Tiempo inicial")
    parser.add_argument('--s', type=float, nargs=4, required=True, help="Estado inicial: x, y, vx, vy")
    parser.add_argument('--b', type=float, default=0.1, help="Coeficiente de resistencia del aire (0.0 a 1.0)")
    
    args = parser.parse_args()
    
    # Llamada a la función del módulo utils
    # Nota: Pasamos args.t, el vector de estado args.s y el coeficiente b
    resultado = dSdt(args.t, args.s, args.b)
    
    print("Derivadas calculadas:")
    print(resultado)

if __name__ == "__main__":
    main()
