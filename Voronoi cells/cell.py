import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
from matplotlib.widgets import Button

from line2d import *
from polygon import *

#
# DATA
#
points=[]
lines=[]
startPoint=Point2D(0,0)
start=True
cell=Polygon([AA,BB,DD,CC])

#
# GUI
#
CANVAS_SIZE=7
fig = plt.figure(figsize=(CANVAS_SIZE, CANVAS_SIZE))
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])#, frameon=False, aspect=1)
ax.set_xticks([])
ax.set_yticks([])




def perpendicularBisector(A,B):
    AB=myLine2D(A,B)
    v=AB.getDirectionVector()
    mid=Point2D((A.x+B.x)/2,(A.y+B.y)/2)
    vperp=Vector2D(-v.y,v.x)
    P=Point2D(mid.x+vperp.x,mid.y+vperp.y)
    perpBisector=myLine2D(mid,P)
    return perpBisector



def drawAll():
    ax.cla()

    for l in lines:
        l.addToDrawing(ax)


    if not start:
        circle = Circle((startPoint.x,startPoint.y), 0.005, color='red')
        ax.add_artist(circle)
        
        for pt in points:
            circle = Circle((pt.x,pt.y), 0.005, color='blue')
            ax.add_artist(circle)
            
    cell.draw(ax)

    fig.canvas.draw()

    
def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    if event.inaxes != axcutReset:
        global start,startPoint
        if start:
            startPoint=Point2D(event.xdata,event.ydata)
            start=False
        else:
            newP=Point2D(event.xdata,event.ydata)
            points.append(newP)
            
            l=perpendicularBisector(newP,startPoint)
            lines.append(l)

            global cell
            cell=cell.clipp(l, startPoint)
        drawAll()


def reset(event):
    print("reset!")
    points.clear()
    lines.clear()
    global cell
    cell=Polygon([AA,BB,DD,CC])
    global start
    start=True
    fig.suptitle("")
    drawAll()

def hover(event):
    if event.inaxes == axcut:
        print("OK")


axcutReset = plt.axes([0.05, 0.9, 0.1, 0.05])
bcutReset = Button(axcutReset, 'Reset', color='lightgray', hovercolor='red')
bcutReset.on_clicked(reset)

fig.canvas.mpl_connect('button_release_event', onclick)

mng = plt.get_current_fig_manager()
mng.window.resizable(False, False)
drawAll()
plt.show()
