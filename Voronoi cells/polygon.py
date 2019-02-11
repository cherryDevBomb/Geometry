
from matplotlib.lines import Line2D
from matplotlib.patches import Circle

from line2d import *


def perpendicularBisector(A,B):
    AB=myLine2D(A,B)
    v=AB.getDirectionVector()
    mid=Point2D((A.x+B.x)/2,(A.y+B.y)/2)
    vperp=Vector2D(-v.y,v.x)
    P=Point2D(mid.x+vperp.x,mid.y+vperp.y)
    perpBisector=myLine2D(mid,P)
    return perpBisector


class Polygon:
    points=[]

    def __init__(self,points):
        self.points=points

    def fromPoints(self,A,B,C,D):
        points.append(A)
        points.append(B)
        points.append(C)
        points.append(D)


    def draw(self,ax):
        n=len(self.points)
        
        for i in range(n):
            circle = Circle((self.points[i].x,self.points[i].y), 0.005, color='green')
            ax.add_artist(circle)

        for i in range(n-1):
            xdata=[self.points[i].x,self.points[i+1].x]
            ydata=[self.points[i].y,self.points[i+1].y]
            ax.add_line(Line2D(xdata, ydata,color='green',linewidth=3))

        if n>2:
            xdata=[self.points[n-1].x,self.points[0].x]
            ydata=[self.points[n-1].y,self.points[0].y]
            ax.add_line(Line2D(xdata, ydata,color='green',linewidth=3))

    #
    # we assume that the polygon is convex
    # => at most 2 intersection points
    # 
    def clipp(self,L,In):
        # TODO

        pnts = []

        #----------------------------------------------
        #verlangert L     (L should intersect with sides)
        if not L.isParallelTo(Xmin):
            P1 = L.intersectionPointWith(Xmin)
            P2 = L.intersectionPointWith(Xmax)
        else:
            P1 = L.intersectionPointWith(Ymin)
            P2 = L.intersectionPointWith(Ymax)

        L = myLine2D(P1, P2)
        print(L.A.x, L.A.y, L.B.x, L.B.y)


        #----------------------------------------------
        if len(self.points) > 2:
            i = 0
            while (i < len(self.points)-1):
                if (L.intersectsSegment(self.points[i], self.points[i+1])):
                    intersect = L.intersectionPointWith2(self.points[i], self.points[i+1])
                    pnts.append(intersect)
                    self.points.insert(i+1, intersect)
                    i += 1
                i += 1

        #-----------------------------------------------
        #Points of Polygon that will be deleted

        if (L.intersectsSegment(self.points[len(self.points)-1], self.points[0])):
            intersect = L.intersectionPointWith2(self.points[len(self.points) - 1], self.points[0])
            pnts.append(intersect)
            self.points.insert(0, intersect)

        pnts_to_delete = []
        i = 0
        while (i < len(self.points)):
            if self.points[i] not in pnts:
                if L.areOnSameSide(self.points[i], In) == False:
                    pnts_to_delete.append(self.points[i])
            i += 1

        i = 0
        for pnt in range(len(pnts_to_delete)):
            i = 0
            while (i < len(self.points)):
                if (pnts_to_delete[pnt].x == self.points[i].x and pnts_to_delete[pnt].y == self.points[i].y):
                    del self.points[i]
                    i -= 1
                i += 1

        return self


def test():
    A = Point2D(0,0)
    B = Point2D(0,7)
    C = Point2D(7,7)
    D = Point2D(7,0)

    poly = Polygon([A, B, C, D])
    In = Point2D(3,4)
    p1 = Point2D(2,5)
    l1 = perpendicularBisector(p1, In)
    print(l1.A.x, l1.A.y, l1.B.x, l1.B.y)
    poly = poly.clipp(l1, In)

    print()
    for p in poly.points:
        print(p.x, p.y)

    p2 = Point2D(5,6)
    l2 = perpendicularBisector(p2, In)
    print(l2.A.x, l2.A.y, l2.B.x, l2.B.y)
    poly = poly.clipp(l2, In)

    print()
    for p in poly.points:
        print(p.x, p.y)

    p3 = Point2D(4, 2)
    l3 = perpendicularBisector(p3, In)
    print(l3.A.x, l3.A.y, l3.B.x, l3.B.y)
    poly = poly.clipp(l3, In)

    print()
    for p in poly.points:
        print(p.x, p.y)
