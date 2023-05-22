from scipy.integrate import odeint
import math  # Usar en caso te tener alguna funcion trigonometrica


# Introducir la ecuacion
def f(t, y):
    return -2*t*y


# Introducir los valores iniciales
def introducir_variables():
    global tk, dt, yk, n, t, y, y_inicial
    tk = float(input("Ingrese el tiempo inicial: "))
    dt = float(input("Ingrese la dt: "))
    yk = float(input("Ingrese la condicion inicial: "))
    n = int(input("Ingrese la cantidad de pasos: "))
    t = 0
    y = 0
    y_inicial = yk
    return tk, dt, yk, n, t, y, y_inicial


introducir_variables()


f(t, y)

# Siendo h el iterador que va a contar los pasos y
# siendo n la cantidad de pasos que debe realizar
for h in range(n):
    k1 = dt * f(tk, yk)

    k2 = dt * f(tk + dt/2, yk + k1/2)

    k3 = dt * f(tk + dt/2, yk + k2/2)

    k4 = dt * f(tk + dt, yk + k3)

    y_resultado = yk + ((k1 + (2 * k2) + (2 * k3) + k4) / 6)

    yk = y_resultado

    tk = tk + dt

    print(y_resultado)

# Para comparar los resultados
resultado = odeint(f, yk, [tk, n])[-1]
print(resultado)
