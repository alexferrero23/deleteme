import sys

mi_nombre = sys.argv[1]

def saludar():
    print(f"Hola, soy un programa de Python, encantado {mi_nombre}")
    print("¡Hola, mundo!")

if __name__ == "__main__":
    saludar()