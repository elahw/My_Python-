# import necessary module
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# load data from file
# you can replace this using with open
#data1 = np.loadtxt("a.txt")
first_2000 = [1, 3, 4, 5,  6,  7,  12, 14]
second_2000 =[5, 6, 8, 11, 15, 16, 19, 22]
third_2000 = [3, 5, 6,  7,  9, 12, 20, 30]

# print to check data
print first_2000
print second_2000
print third_2000

# new a figure and set it into 3d
fig = plt.figure()
ax = fig.gca(projection='3d')

# set figure information
ax.set_title("3D_Curve")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# draw the figure, the color is r = read
figure = ax.plot(first_2000, second_2000, third_2000, c='r')

plt.show()
