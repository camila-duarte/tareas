import matplotlib.pyplot as plt

# Listas para la grafica de dt_1
x1_axis = []
y1_axis = []

# Listas para la grafica de dt_2
x2_axis = []
y2_axis = []

# Listas para la grafica de dt_3
x3_axis = []
y3_axis = []

# Listas para la grafica de dt_4
x4_axis = []
y4_axis = []

# Valores de dt dados en el ejercicio
dt_1 = 1
dt_2 = 0.5
dt_3 = 0.25
dt_4 = 0.125

# Valor inicial
x_1 = 1
x_2 = 1
x_3 = 1
x_4 = 1

# Tiempo inicial
t_1 = 0
t_2 = 0
t_3 = 0
t_4 = 0

for contador in range(10):

    # Para dt = 1
    x1_axis.append(t_1)
    y1_axis.append(x_1)
    x_1 = x_1 + dt_1*(t_1 - x_1)
    t_1 = t_1 + dt_1
    # En caso de querer ver los resultados:
    # print(x_1)
    # print(t_1)

    # Para dt = 0.5
    x2_axis.append(t_2)
    y2_axis.append(x_2)
    x_2 = x_2 + dt_1*(t_2 - x_2)
    t_2 = t_2 + dt_2
    contador = contador + 0.1

    # En caso de querer ver los resultados:
    # print(x_2)
    # print(t_2)

    # Para dt = 0.25
    x3_axis.append(t_3)
    y3_axis.append(x_3)
    x_3 = x_3 + dt_3*(t_3 - x_3)
    t_3 = t_3 + dt_3

    # En caso de querer ver los resultados:
    # print(x_1)
    # print(t_1)

    # Para dt = 0.5
    x4_axis.append(t_4)
    y4_axis.append(x_4)
    x_4 = x_4 + dt_4*(t_4 - x_4)
    t_4 = t_1 + dt_4

    # En caso de querer ver los resultados:
    # print(x_4)
    # print(t_4)

valor_aproximado_1 = float(y1_axis[-1])
valor_aproximado_2 = float(y2_axis[-1])
valor_aproximado_3 = float(y3_axis[-1])
valor_aproximado_4 = float(y4_axis[-1])
print(valor_aproximado_1)
print(valor_aproximado_2)
print(valor_aproximado_3)
print(valor_aproximado_4)




# plt.xlabel("Tiempo")
# plt.ylabel("x(t)")
# plt.plot(x1_axis, y1_axis, label='dt = 1')
# plt.plot(x2_axis, y2_axis, label='dt = 0.5')
# plt.plot(x3_axis, y3_axis, label='dt = 0.25')
# plt.plot(x4_axis, y4_axis, label='dt = 0.125')
# plt.legend()
# plt.show()
