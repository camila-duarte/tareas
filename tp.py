# listas de los diferentes tiempos, utilizar un iterador para recorrer

# introducir la ecuacion diferencial
# introducir el valor inicial
# introducir dt (esto no debe variar)
# introducir tiempo inicial 0
# introducir el valor inicial en la ecuacion diferencial
# hallar k1 con la ecuacion diferencial y valores introducidos
# ya tenemos k1
# ahora k2
# ESTO VA A SER T EN MI ECU DIFERENCIAL agregar otra t en la cual el tiempo pase a ser t anterior + dt/2
# para y introducir el valor inicial de y pero ver como usar en las sgtes iteraciones que debe cambiar
# PERO PARA Y la formula es esa k anterior +dt/2 *k1 ESTO ES MI PRIMERA LINEA O SEA CON VALOR INICIAL
# ahora k3
# ESTO VA A SER T EN MI ECU DIFERENCIAL agregar otra t en la cual el tiempo pase a ser t anterior + dt/2
# para y introducir el valor inicial de y pero ver como usar en las sgtes iteraciones que debe cambiar
# PERO PARA Y la formula es esa k anterior +dt/2 *k2 ESTO ES MI PRIMERA LINEA O SEA CON VALOR INICIAL
# ahora k4
# ESTO VA A SER T EN MI ECU DIFERENCIAL agregar otra t en la cual el tiempo pase a ser t anterior + dt
# para y introducir el valor inicial de y pero ver como usar en las sgtes iteraciones que debe cambiar
# PERO PARA Y la formula es esa k anterior +dt*k3 ESTO ES MI PRIMERA LINEA O SEA CON VALOR INICIAL
# ahora para hallar k es (k1+2k2+2k3+k4)/6
# ESTO RECIEN ES k
# ahora, CON K escribir yk = yk(en este caso el inicial) +dt*k
# REPETIR TODO ESE PROCESO CON Y1 PARA HALLAR Y2


def introducir_ecuacion_diferencial():
    t = float(input("Ingresar el tiempo inicial: "))
    dt = float(input("Ingresar la delta t elegida: "))
    y = float(input("Ingresar la y inicial: "))
    return t, dt, y


k1 = input("Introducir la ecuacion: ")
print(k1)
t = float(input("Ingresar el tiempo inicial: "))
dt = float(input("Ingresar la delta t elegida: "))
y = float(input("Ingresar la y inicial: "))
# introducir_ecuacion_diferencial()
k1 = eval(k1)

print(k1)
for k in range(5):
    k1
    # print(k1)
    k2 = -2 * (t + (dt/2)) * (y + ((dt/2) * k1))
    # print(k2)
    k3 = -2 * (t + (dt/2)) * (y + ((dt/2) * k2))
    # print(k3)
    k4 = -2 * (t + dt) * (y + (dt * k3))
    # print(k4)
    y = (k1 + (2 * k2) + (2 * k3) + k4) / 6
    print(y)
    dt = dt + 1
    # print(dt)


