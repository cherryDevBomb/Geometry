
from matplotlib.lines import Line2D
CANVAS_SIZE=7


class Point2D:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y

    #Given three colinear points P, self, R , the function checks if point self lies on line segment [PR]
    def onSegment(self, P, R):
        if (self.x <= max([P.x, R.x]) and (self.x >= min([P.x, R.x])) and (self.y <= max([P.y, R.y])) and (self.y >= min([P.y, R.y]))):
            return True
        return False
    

    #To find orientation of ordered triplet (p, q, r).
    # The function returns following values
    # 0 --> p, q and r are colinear
    # 1 --> Clockwise
    # 2 --> Counterclockwise
    def orientation(self, P, R):
        val = (self.y - P.y) * (R.x - self.x) - (self.x - P.x) * (R.y - self.y);
     
        if (val == 0):
            return 0       #colinear
        elif (val > 0):
            return 1       #clockwise
        elif (val < 0):
            return 2       #counterclockwise



class Vector2D:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y


class myLine2D:
    # two points
    A=0
    B=0

    def __init__(self,A,B):
        self.A=A
        self.B=B

    def fromCoords(self, Ax,Ay,Bx,By):
        A = Point2D(Ax, Ay)
        B = Point2D(Bx, By)
        return myLine2D(A,B)

    def addToDrawing(self,ax):
        if not self.isParallelTo(Xmin):
            P1 = self.intersectionPointWith(Xmin)
            P2 = self.intersectionPointWith(Xmax)
            xdata=[P1.x,P2.x]
            ydata=[P1.y,P2.y]
            ax.add_line(Line2D(xdata, ydata,color='black'))
        else:
            P1 = self.intersectionPointWith(Ymin)
            P2 = self.intersectionPointWith(Ymax)
            ax.add_line(Line2D(xdata, ydata,color='black'))


    def intersectionPointWith(self,L):
        # TODO

        a1 = self.B.y - self.A.y
        b1 = self.A.x - self.B.x
        c1 = self.B.x * self.A.y - self.A.x * self.B.y

        a2 = L.B.y - L.A.y
        b2 = L.A.x - L.B.x
        c2 = L.B.x * L.A.y - L.A.x * L.B.y

        if ( b1 == 0 and b2 == 0):
            return -1   #LINES ARE THE SAME

        elif (b1 != 0 and b2 != 0):
            m1 = -a1 / b1
            n1 = -c1 / b1

            m2 = -a2 / b2
            n2 = -c2 / b2

            if (m1 != m2):
                x = (n2 - n1) / (m1 - m2)
                y = m1 * x + n1
            else:
                return -1   #LINES ARE PARALLEL

        elif (b1 != 0 and b2 == 0):
            m1 = -a1 / b1
            n1 = -c1 / b1

            x = -c2 / a2
            y = m1 * x + n1


        elif (b1 == 0 and b2 != 0):
            m2 = -a2 / b2
            n2 = -c2 / b2

            x = -c1 / a1
            y = m2 * x + n2


        return Point2D(x, y)



    def intersectionPointWith2(self,X,Y):
        tmp = myLine2D(X,Y)
        return self.intersectionPointWith(tmp)


    def isParallelTo(self,L):
        # TODO
        a1 = self.B.y - self.A.y
        b1 = self.A.x - self.B.x
        #c1 = -self.A.x * a1 + self.A.y * (-b1)
        c1 = self.B.x * self.A.y - self.A.x * self.B.y

        a2 = L.B.y - L.A.y
        b2 = L.A.x - L.B.x
        c2 = L.B.x * L.A.y - L.A.x * L.B.y

        if (a1*b2 == a2*b1) and (b1*c2 != b2*c1):
            return True
        return False


    def getDirectionVector(self):
        # TODO
        a = self.B.y - self.A.y
        b = self.A.x - self.B.x

        return Vector2D(-b, a)


    def areOnSameSide(self, X, Y):
        # TODO
        check = ((self.A.y - self.B.y)*(X.x - self.A.x) + (self.B.x - self.A.x)*(X.y - self.A.y))*((self.A.y - self.B.y)*(Y.x - self.A.x) + (self.B.x - self.A.x)*(Y.y - self.A.y))
        if check < 0:
            return False
        else:
            return True


    def intersectsSegment(self,C,D):
        #TODO
        A = self.A
        B = self.B

        o1 = B.orientation(A, C)
        o2 = B.orientation(A, D)
        o3 = D.orientation(C, A)
        o4 = D.orientation(C, B)

        #General case
        if (o1 != o2 and o3 != o4):
            return True
     
        #Special Cases
        #A, B, C are colinear and C lies on segment AB
        if (o1 == 0 and C.onSegment(A,B)):
            return True
     
        #A, B, D are colinear and D lies on segment AB
        if (o2 == 0 and D.onSegment(A, B)):
            return True
     
        #C, D, A are colinear and A lies on segment CD
        if (o3 == 0 and A.onSegment(C, D)):
            return True
     
        #C, D, B are colinear and B lies on segment CD
        if (o4 == 0 and B.onSegment(C, D)):
            return True
     
        return False #Doesn't fall in any of the above cases


# canvas border
# corners:
AA = Point2D(0, 0)
BB = Point2D(0, CANVAS_SIZE)
CC = Point2D(CANVAS_SIZE, 0)
DD = Point2D(CANVAS_SIZE, CANVAS_SIZE)
# sides:
Xmin = myLine2D(AA, BB)
Xmax = myLine2D(DD, CC)
Ymin = myLine2D(AA, CC)
Ymax = myLine2D(DD, BB)


def test():

    l = myLine2D(Point2D(4,5), Point2D(5,3))
    l = myLine2D(Point2D(2.5,4.5), Point2D(3.5,5.5))
    

    print(l.intersectionPointWith(Xmin).x, l.intersectionPointWith(Xmin).y)
    print(l.intersectionPointWith(Xmax).x, l.intersectionPointWith(Xmax).y)


    print(l.intersectionPointWith(Ymin).x, l.intersectionPointWith(Ymin).y)
    print(l.intersectionPointWith(Ymax).x, l.intersectionPointWith(Ymax).y)

