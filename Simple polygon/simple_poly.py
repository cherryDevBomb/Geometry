#import matplotlib
#matplotlib.use('GTK')
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
from matplotlib.widgets import Button
 
class Point:
    x=0;
    y=0;
    def __init__(self,x,y):
        self.x=x
        self.y=y


CANVAS_SIZE=7

points=[]

fig = plt.figure(figsize=(CANVAS_SIZE, CANVAS_SIZE))
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])#, frameon=False, aspect=1)
ax.set_xticks([])
ax.set_yticks([])


def isCrossing(a,b,c,d):
    # TODO
	det  = (a.x - b.x)*(d.y - c.y) - (d.x - c.x)*(a.y - b.y)

	det1 = (d.x - b.x)*(d.y - c.y) - (d.x - c.x)*(d.y - b.y)
	det2 = (a.x - b.x)*(d.y - b.y) - (d.x - b.x)*(a.y - b.y)

	t0 = det1 / det
	s0 = det2 / det

	if (t0 >= 0 and t0 <= 1) and (s0 >= 0 and s0 <= 1):
		return True

	return False


def isSimplePolygon():
    # TODO
    for i in range(len(points) - 1):
    	if i == len(points) - 1 or i == 0 or i+1 == len(points) - 1:
    			continue
    	if isCrossing(points[i], points[i+1], points[0], points[len(points)-1]):
    		return False

    for i in range(len(points) - 1):
    	for j in range(len(points) - 1):
    		if i == j or i == j+1 or i+1 == j:
    			continue
    		if (isCrossing(points[i], points[i+1], points[j], points[j+1])):
    			return False

    return True


def draw_all():
    ax.cla()

    for pt in points:
        circle = Circle((pt.x,pt.y), 0.005, color='r')
        ax.add_artist(circle)

    xdata=[pt.x for pt in points]
    ydata=[pt.y for pt in points]
    ax.add_artist(Line2D(xdata, ydata,color='b'))

    n=len(points)
    if n>2:
        xdata=[points[n-1].x,points[0].x]
        ydata=[points[n-1].y,points[0].y]
        ax.add_line(Line2D(xdata, ydata,color='g'))

    fig.suptitle("")
    fig.canvas.draw()
    
def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    if event.inaxes != axcutReset and event.inaxes != axcutCheck:
        points.append(Point(event.xdata,event.ydata))#(event.xdata,event.ydata))
        #points.append((event.x,event.y))
        draw_all()


def reset(event):
    print("reset!")
    del points[:]
    fig.suptitle("")
    draw_all()

def check(event):
    print("check!")
    if isSimplePolygon():
        fig.suptitle('The polygon is simple!', fontsize=12)
    else:
        fig.suptitle('The polygon is not simple!', fontsize=12)
    fig.canvas.draw()
    #draw_all()

def hover(event):
    if event.inaxes == axcut:
        print("OK")

axcutReset = plt.axes([0.05, 0.9, 0.1, 0.05])
bcutReset = Button(axcutReset, 'Reset', color='lightgray', hovercolor='red')
bcutReset.on_clicked(reset)

axcutCheck = plt.axes([0.05, 0.82, 0.1, 0.05])
bcutCheck = Button(axcutCheck, 'Check', color='lightgray', hovercolor='red')
bcutCheck.on_clicked(check)


#fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('button_release_event', onclick)

mng = plt.get_current_fig_manager()
mng.window.resizable(False, False)
plt.show()
