import matplotlib.pyplot as plt


x_axis = []
y_axis = []
dt = 0.125

x = 1

t = 0


for contador in range(10):
    x_axis.append(t)
    y_axis.append(x)
    x = x + dt*(t - x)
    t = t + dt
    contador = contador + 0.1
    print(x)
    print(t)


plt.xlabel("Tiempo")
plt.ylabel("x(t)")
plt.plot(x_axis, y_axis)
plt.show()

