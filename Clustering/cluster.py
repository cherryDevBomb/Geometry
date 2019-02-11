 #k-Means Algorithm (CLUSTER POINTS)

import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
from matplotlib.widgets import Button
from math import sqrt

class Point:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
#
# DATA
#
points = []
cluster1 = []
cluster2 = []
cluster3 = []
centers = []

#
# GUI
#
CANVAS_SIZE = 6
fig = plt.figure(figsize=(CANVAS_SIZE, CANVAS_SIZE))
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
ax.set_xticks([])
ax.set_yticks([])


def MyDistance(a,b):
    # TODO
    x1 = a.x
    x2 = b.x

    y1 = a.y
    y2 = b.y

    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distance


def determine_clusters():
    # TODO
    for p in points:       
        dR = MyDistance(p, centers[0])
        dG = MyDistance(p, centers[1])
        dB = MyDistance(p, centers[2])
        if dR == min([dR, dG, dB]):
            cluster1.append(p)
        elif dG == min([dR, dG, dB]):
            cluster2.append(p)
        else:
            cluster3.append(p)


def update_centers():
    # TODO

    # Red POINT
    R = Point(0, 0)             #Mittelpunkt von ClusterR(1)
    for p in cluster1:
        R.x += p.x
        R.y += p.y

    R.x = R.x / len(cluster1)
    R.y = R.y / len(cluster1)

    # Green POINT
    G = Point(0, 0)                 #Mittelpunkt von ClusterG(2)
    for p in cluster2:
        G.x += p.x
        G.y += p.y

    G.x = G.x / len(cluster2)
    G.y = G.y / len(cluster2)

    # Blue POINT
    B = Point(0, 0)                 #Mittelpunkt von ClusterB(3)
    for p in cluster3:
        B.x += p.x
        B.y += p.y

    B.x = B.x / len(cluster3)
    B.y = B.y / len(cluster3)

    #update CENTERS list
    centers[0] = R
    centers[1] = G
    centers[2] = B



def draw_points():
    ax.cla()

    for pt in points:
        circle = Circle((pt.x,pt.y), 0.005, color='black')
        ax.add_artist(circle)

    fig.suptitle("")          
    fig.canvas.draw()


def draw_clusters():
    ax.cla()

    for pt in cluster1:
        circle = Circle((pt.x,pt.y), 0.005, color='red')
        ax.add_artist(circle)
        
    for pt in cluster2:
        circle = Circle((pt.x,pt.y), 0.005, color='green')
        ax.add_artist(circle)

    for pt in cluster3:
        circle = Circle((pt.x,pt.y), 0.005, color='blue')
        ax.add_artist(circle)

    fig.suptitle("")
    fig.canvas.draw()


def draw_centers():
    #ax.cla(}

    if len(centers)>0:
        circle = Circle((centers[0].x,centers[0].y), 0.005, color='pink')
        ax.add_artist(circle)

        if len(centers)>1:
            circle = Circle((centers[1].x,centers[1].y), 0.005, color='lightgreen')
            ax.add_artist(circle)

            if len(centers)>2:
                circle = Circle((centers[2].x,centers[2].y), 0.005, color='lightblue')
                ax.add_artist(circle)

    fig.suptitle("")
    fig.canvas.draw()
    

def onclick(event):
    if (event.inaxes != axcutReset) and (event.inaxes != axcutUpdate):
        print(event.xdata, event.ydata)
        centers.append(Point(event.xdata,event.ydata))
        draw_centers()


def reset(event):
    #empty the DATA lists
    del cluster1[:]
    del cluster2[:]
    del cluster3[:]
    del centers[:]

    print("reset!")

    fig.suptitle("")
    draw_points()


def update(event):
    print("update!")
    if(len(centers)==3):
        #update clusters for next iteration
        del cluster1[:] 
        del cluster2[:]
        del cluster3[:]
        determine_clusters()
        draw_clusters()
        update_centers()
        draw_centers()
    else:
        fig.suptitle('Mark three initial centers!', fontsize=12)
        fig.canvas.draw()


def hover(event):
    if event.inaxes == axcut:
        print("OK")


def read_points():
    with open("points.txt") as file:
        for line in file:
            line = line.strip()
            line = line.split()
            points.append(Point(float(line[0]),float(line[1])))


axcutReset = plt.axes([0.05, 0.9, 0.1, 0.05])
bcutReset = Button(axcutReset, 'Reset', color='lightgray', hovercolor='red')
bcutReset.on_clicked(reset)

axcutUpdate = plt.axes([0.05, 0.82, 0.1, 0.05])
bcutUpdate = Button(axcutUpdate, 'Update', color='lightgray', hovercolor='red')
bcutUpdate.on_clicked(update)

fig.canvas.mpl_connect('button_release_event', onclick)

mng = plt.get_current_fig_manager()
mng.window.resizable(False, False)

read_points()
draw_points()
plt.show()
