from scipy.integrate import odeint
import math
# Escribir una función que acepte la ecuación diferencial, las condiciones
# iniciales, el tamaño del paso y el intervalo de tiempo, y devuelva la
# solución numérica utilizando RK4.


def introducir_variables():
    global tk, dt, yk, n, t, y, y_inicial
    tk = float(input("Ingrese el tiempo inicial: "))
    dt = float(input("Ingrese la dt: "))
    yk = float(input("Ingrese la condicion inicial: "))
    n = float(input("Ingrese la cantidad de pasos: "))
    t = 0
    y = 0
    y_inicial = yk
    return tk, dt, yk, n, t, y, y_inicial


introducir_variables()


def ecuacion(t, y):
    return math.sin(t) - y/t  #aca se introduce la ecuacion


ecuacion(t, y)

for pasos in range(5):
    t = tk
    y = yk
    k1 = dt * ecuacion(t, y)

    y = yk + k1/2
    t = tk + dt/2
    k2 = dt * ecuacion(t, y)

    y = yk + k2/2
    t = tk + dt/2
    k3 = dt * ecuacion(t, y)

    y = yk + k3
    t = tk + dt
    k4 = dt * ecuacion(t, y)

    y_resultado = yk + ((k1 + (2 * k2) + (2 * k3) + k4) / 6)

    yk = y_resultado

    tk = tk + dt

    print(y_resultado)

# Para comparar los resultados
resultado = odeint(ecuacion, yk, [tk, n])[-1]
print(resultado)

