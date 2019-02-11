import matplotlib
import matplotlib.pyplot as plt
import math
from matplotlib import colors
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
from matplotlib.widgets import Button

#
# DATA
#
class Point2D:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Vector2D:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y

R=G=B=Point2D(0,0)
nr_points=0
points=[]

#
# GUI
#
CANVAS_SIZE=7
fig = plt.figure(figsize=(CANVAS_SIZE, CANVAS_SIZE))
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])#, frameon=False, aspect=1)
ax.set_xticks([])
ax.set_yticks([])

#
#  DATA METHODS
#
def my_scalar_product(u,v):
    # TODO
    return (u.x * v.x) + (u.y * v.y)


def my_norm(v):
    # TODO
    return math.sqrt(v.x**2 + v.y**2)


def right_oriented(u,v):
    # TODO
    product = u.x * v.y - u.y * v.x

    if product > 0:
        return True
    return False


def right_oriented_points(A,B,C):
    u=Vector2D(A.x-B.x, A.y-B.y)
    v=Vector2D(C.x-B.x, C.y-B.y)
    return right_oriented(u,v)

def angle(A,B,C):
    # TODO
    u = Vector2D(A.x-B.x, A.y-B.y)
    v =  Vector2D(C.x-B.x, C.y-B.y)

    scalarProduct = my_scalar_product(u, v)
    tmp = my_norm(u) * my_norm(v)

    return math.acos(scalarProduct / tmp)

#
#  THE GUI METHODS
#
def draw_all():
    ax.cla()

    if nr_points==1:
        circle = Circle((R.x,R.y), 0.005, color='r')
        ax.add_artist(circle)
    elif nr_points==2:
        circle = Circle((R.x,R.y), 0.005, color='r')
        ax.add_artist(circle)
        circle = Circle((G.x,G.y), 0.005, color='g')
        ax.add_artist(circle)

        xdata=[R.x,G.x]
        ydata=[R.y,G.y]
        ax.add_artist(Line2D(xdata, ydata,color='black'))

    elif nr_points==3:
        circle = Circle((R.x,R.y), 0.005, color='r')
        ax.add_artist(circle)
        circle = Circle((G.x,G.y), 0.005, color='g')
        ax.add_artist(circle)
        circle = Circle((B.x,B.y), 0.005, color='b')
        ax.add_artist(circle)
        
        xdata=[R.x,G.x,B.x]
        ydata=[R.y,G.y,B.y]
        ax.add_artist(Line2D(xdata, ydata,color='black'))

    fig.suptitle("")
    fig.canvas.draw()
    
def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    if event.inaxes != axcutReset:
        points.append(Point2D(event.xdata,event.ydata))

        global R,G,B,nr_points
        if nr_points<3:
            if nr_points==0:
                R=Point2D(event.xdata,event.ydata)
            elif nr_points==1:
                G=Point2D(event.xdata,event.ydata)
            elif nr_points==2:
                B=Point2D(event.xdata,event.ydata)
            nr_points=nr_points+1
            draw_all()
        if nr_points==3:
            a=angle(R,G,B)
            a=(a/(2*math.pi))*360
            msg="The angle is: "+str(a)+" degrees.\n"
            if right_oriented_points(R,G,B):
                msg=msg+"The basis is right oriented."
            else:
                msg=msg+"The basis is left oriented."
            fig.suptitle(msg)
            fig.canvas.draw()


def reset(event):
    print("reset!")
    global nr_points
    nr_points=0
    fig.suptitle("")
    draw_all()

def hover(event):
    if event.inaxes == axcut:
        print("OK")

axcutReset = plt.axes([0.05, 0.9, 0.1, 0.05])
bcutReset = Button(axcutReset, 'Reset', color='lightgray', hovercolor='red')
bcutReset.on_clicked(reset)

fig.canvas.mpl_connect('button_release_event', onclick)

mng = plt.get_current_fig_manager()
mng.window.resizable(False, False)
plt.show()
