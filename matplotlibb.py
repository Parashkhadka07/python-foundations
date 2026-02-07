import matplotlib.pyplot as plt
import numpy as np

data=np.linspace(-10,10,10)
# x=np.sin(data)
# y=np.cos(data)

# plt.plot(x)

## methods to add title , and lables in axis
# plt.xlabel("angles")
# plt.ylabel("values")
# plt.title("Sine wave")


## to plot the parabola 
y=data**2 + 2*data + 2
plt.plot(data,y,"b+") ## this is to change the or assigh the colour and symbol we wanted "b+" where b means blue and + means symbol used in the plot to plot the graph must be +
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.title("parabola")
plt.show()