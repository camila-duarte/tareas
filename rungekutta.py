import math

# > h) d^2y/dt^2 - 4dy/dt + 4y = e^(-t), y(0) = 0, dy/dt(0) = 1  
# Introducir la ecuacion


def primera_derivada(t, y):
    return -y + math.e**(-t)

def segunda_derivada(t, y, z): 
    return  4*primera_derivada(t, y) - 4*y + math.e**(-t)

4*primera_derivada(t,y) - 4x+ e


# Introducir los valores iniciales
def introducir_variables():
    global tk, dt, y0, n, t, y, z0
    # tk <- Es el tiempo inicial que luego va cambiando con dt
    tk = float(input("Ingrese el tiempo inicial: "))
    # dt <- Es el tamanho de los pasos del tiempo (delta t) del
    # cual depende la presicion del resultado
    dt = float(input("Ingrese la dt: "))
    # Es el valor de y en el tiempo inicial
    y0 = float(input("Ingrese la condicion inicial: "))
    z0 = float(input("Ingrese la condicion inicial de la primera derivada: "))
    # Es la cantidad de resultados de y que se quiere
    n = int(input("Ingrese la cantidad de pasos: "))
    t = 0
    y = 0
    return tk, dt, y0, n, t, y, z0

z = primera_derivada(tk, y0)

introducir_variables()

# Siendo h el iterador que va a contar los pasos y
# siendo n la cantidad de pasos que debe realizar
for h in range(n):
    k1 = dt * z(tk, y0, z0)

    k2 = dt * f(tk + dt/2, y0 + k1/2, )

    k3 = dt * f(tk + dt/2, y0 + k2/2)

    k4 = dt * f(tk + dt, y0 + k3)

    yk = y0 + ((k1 + (2 * k2) + (2 * k3) + k4) / 6)

    y0 = yk

    tk = tk + dt

    print(yk)