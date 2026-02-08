import matplotlib.pyplot as plt
import numpy as np

# data=np.linspace(-10,10,10)
# x=np.sin(data)
# y=np.cos(data)

# plt.plot(x)

## methods to add title , and lables in axis
# plt.xlabel("angles")
# plt.ylabel("values")
# plt.title("Sine wave")


# ## to plot the parabola 
# y=data**2 + 2*data + 2
# plt.plot(data,y,"b+") ## this is to change the or assigh the colour and symbol we wanted "b+" where b means blue and + means symbol used in the plot to plot the graph must be +
# plt.xlabel("x-values")
# plt.ylabel("y-values")
# plt.title("parabola")
# plt.show()

# ### bar plot

# values=np.linspace(1,20,6)
# subjects=["math","english","science","computer","GK","parash"]
# plt.bar(subjects,values)
# plt.xlabel("subjects")
# plt.ylabel("marks")
# plt.title("students marks analysis")
# plt.show()


## for pie chart 

# values=np.linspace(1,20,6)
# subjects=["math","english","science","computer","GK","parash"]
# plt.pie(values,labels=subjects,autopct="%1.1f%%",startangle=90)
# plt.title("pie chart of student data")
# plt.show()


## for scatter plot
# x=np.linspace(0,50,500)
# y=np.sin(x)
# z=np.cos(x)
# plt.scatter(x,y,color="blue",alpha=0.8,s=200,label="sin function")# here color gives the color to the piont ,alpha gives the visibility wjich is 1 to 1 and s gives the size of the point  and label gives the label to those point so that we understand which color is which
# plt.scatter(x,z,color="red",alpha=0.3,s=200,label="cos function")
# plt.legend()# this function activates those lables inside the scatter function
# plt.xlabel("Angles")
# plt.ylabel("values")
# plt.title("scatter graph")
# plt.show()