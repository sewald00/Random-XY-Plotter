###Seth Ewald
###Random (x,y) coordinate plotter
###02/20/2018

from random import randint
import numpy as np
import matplotlib.pyplot as plt

###Define the point class. Point will be assigned random x and y values upon init
class Point:
    def __init__(self):
        a=randint(0,10)
        b=randint(0,10)
        self.x=a
        self.y=b

###Create the empty lists that will hold the random (x,y) coordinates
listx=[]
listy=[]
listxy=[]

###Loop to append random x and y coordinates to lists
for x in range(8):
    p1=Point()
    ax=(p1.x)
    ay=(p1.y)
    axy=(p1.x,p1.y)
    listx.append(ax)
    listy.append(ay)
    listxy.append(axy)

###Write the random (x,y) coordinates to a file
f = open("coordinates.txt", "w")
f.write("\n".join(map(lambda x: str(x), listxy)))
f.close()

###Plot the random (x,y) coordinates to a scatter plat
plt.plot(listx,listy,'ro')
plt.show()