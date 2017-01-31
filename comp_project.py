#Computer Science project
#Graphing calc
#Setting up PyGame
import math
import pygame
pygame.init()
#Jarvic Init
#Screen Size
w=600
h=600
e=600
nopixel=25
white=(255,255,255)
black=(0,0,0)
green=(0,0,0)
display=None
normalfont=pygame.font.SysFont("Arial",16)
titlefont=pygame.font.SysFont("Verdana",36)
def jarvic(nopixel,eq):
    global display
    display=pygame.display.set_mode((w+e,h))
    display=pygame.display.set_mode((w+e,h))
    pygame.display.set_caption("Jarvic")
    display.fill(white)
    #screen initialization
    def gridsquares(nopixel):#no. of pixels per grid
        display.set_clip(0,0,w,h)
        display.fill(white)
        for i in range(w/nopixel):
            xg=nopixel*i
            yg=nopixel*i
            pygame.draw.line(display,black,(xg,0),(xg,h),1)
            pygame.draw.line(display,black,(0,yg),(w,yg),1)
            #axes
            mx,my=w/(2*nopixel)*nopixel,h/(2*nopixel)*nopixel
            pygame.draw.line(display,black,(mx,0),(mx,h),3)
            pygame.draw.line(display,black,(0,my),(w,my),3)
            #boundary
            pygame.draw.line(display,black,(w,0),(w,h),5)
            display.set_clip(None)
    def graphjarvic(nopixel,eq):
        pygame.init()
        for i in range(w):
            for j in range(h):
                try:
                    x=w/(w-i)/float(nopixel)
                    y=h/(h-i)/float(nopixel)
                    nx=(x-(w/(w-(i+1))/float(nopixel)))
                    ny=(y-(w/(w-(i+1))/float(nopixel)))
                    p1=(w/(2+x*nopixel),h/(2+y*nopixel))
                    p2=(w/(2+nx*nopixel),h/(2+y*nopixel))
                
                    if eval(eq)==0:
                        pygame.draw.line(display,black,p1,p2,2)
                except:
                     pass
    nopixel=25
    #main logic function
    def mainfunctiondef():
        gridsquares(nopixel)
        #accepting equation
        token=True
        while token:
            pygame.display.update()
            #harvesting actions for execution
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    token=False
        pygame.quit()
    mainfunctiondef()
    graphjarvic(nopixel,eq)
    
    
#sl     
def l1(pt):
    l1=(2*g*pt[0]+2*f*pt[1]+c)
    return l1
def pdistp():
    pt=eval(raw_input("Enter pt coordinates"))
    d=abs(l1(pt))/math.sqrt(4*g*g+4*f*f)
    print "The distance b/w point and line is: ",d
    return pt
def ftpd():
    pt=eval(raw_input("Enter pt coordinates"))
    l1(pt)
    x=((-1*l1(pt)*2*g)+(pt[0]*(4*g*g+4*f*f)))/float(4*g*g+4*f*f)
    y=((-1*l1(pt)*2*f)+(pt[1]*(4*g*g+4*f*f)))/float(4*g*g+4*f*f)
    print "The foot of the perpendicular coordinates is: ",(x,y)
    return (x,y)
def ref():
    pt=eval(raw_input("Enter pt coordinates"))
    l1(pt)
    x=2*((-1*l1(pt)*2*g)+(pt[0]*(4*g*g+4*f*f)))/float(4*g*g+4*f*f)
    y=2*((-1*l1(pt)*2*f)+(pt[1]*(4*g*g+4*f*f)))/float(4*g*g+4*f*f)
    print "The reflection of the pt on the line is :",(x,y)
    return (x,y)
def ptposl():
    pt1=eval(raw_input("Enter pt 1 coordinates"))
    pt2=eval(raw_input("Enter pt 2 coordinates"))
    if l1(pt1)*l1(pt2)>0:
        print "The pts lie on the same side"
    elif l1(pt1)*l1(pt2)==0:
        print "one pt lies on the line"
    else:
        print "The pts lie on the opp sides"
#psl
def angle():
    if a+b==0:
         print "The angle between the lines is: 90"
    else:
        ang=math.degrees(math.atan(2*(math.sqrt(h*h-a*b))/a+b))
        print "The angle between the lines is: ",ang
def poi():
    x=float(b*g-h*f)/(h*h-a*b)
    y=float(a*f-g*h)/(h*h-a*b)
    print "The pt of intersection is: ",(x,y)
    return (x,y)
#conic
def s1(pt):
        s1=a*(pt[0]**2)+b*(pt[1]**2)+2*h*(pt[0]*pt[1])+2*g*(pt[0])+2*f*(pt[1])+c
        return s1
def t1(pt):
        t1='%f*(x*%f)+%f*(y*%f)+%f*(x*%f+y*%f)+%f*(x+%f)+%f*(y+%f)+%f'%(a,pt[0],b,pt[1],h,pt[0],pt[1],g,pt[0],f,pt[1],c)
        return t1
#circle
def dirc():
    print "director circle is a circle from which any 2 tgts drwan are always perpendicular to the circle"
    t='(%fx^2)+(%fy^2)+(%fx)+(%fy)+(%f)'%(a,b,2*g,2*f,2*c-g*g-f*f)
    print t+'=0'
    return t
def posptci():
    pt1=eval(raw_input("Enter pt coordinates"))
    Num=s1(pt1)
    if Num>0:
        print "The pt lies outside the circle"
    elif Num<0:
        print "The pt lies inside the circle"
    else:
        print "The pt lies on the circle"
    return pt1
def ltan():
    pt1=eval(raw_input("Enter pt coordinates"))
    if s1(pt1)>=0:
        len=math.sqrt(s1(pt1))
        print "The length of the tgt from given pt is: ",len
    else:
        print "Tgt cannot be drawn as pt lies inside the circle"
    return pt1
def mind():
    pt1=eval(raw_input("Enter pt coordinates"))
    mind=abs(math.sqrt((pt1[0]+g)**2+(pt1[1]+f)**2)-rad)
    print "minimum dist from the circle:",mind
    return pt1
def maxd():
    pt1=eval(raw_input("Enter pt coordinates"))
    maxd=math.sqrt((pt1[0]+g)**2+(pt1[1]+f)**2)+rad
    print "maximum dist from the circle:",maxd
    return pt1
def tangci():
     pt1=eval(raw_input("Enter coordinates of a point on the circle"))
     t=t1(pt1)
     print t
     return t
#parabola
def posptpa():
    pt1=eval(raw_input("Enter pt coordinates"))
    Num=s1(pt1)
    if Num>0:
        print "The pt lies outside the parabola"
    elif Num<0:
        print "The pt lies inside the parabola"
    else:
        print "The pt lies on the parabola"
    return pt1
def tangpa():
     pt1=eval(raw_input("Enter coordinates of a point on the parabola"))
     t=t1(pt1)
     print t
     return t
#hyperbola
def pospthyp():
    pt1=eval(raw_input("Enter pt coordinates"))
    Num=s1(pt1)
    if Num<0:
        print "The pt lies outside the hyperbola"
    elif Num>0:
        print "The pt lies inside the hyperbola"
    else:
        print "The pt lies on the hyperbola"
    return pt1
def tanghyp():
     pt1=eval(raw_input("Enter coordinates of a point on the hyperbola"))
     t=t1(pt1)
     print t 
     return t
#ellipse
def posptell():
    pt1=eval(raw_input("Enter pt coordinates"))
    Num=s1(pt1)
    if Num>0:
        print "The pt lies outside the ellipse"
    elif Num<0:
        print "The pt lies inside the ellipse"
    else:
        print "The pt lies on the ellipse"
    return pt1
def tangell():
     pt1=eval(raw_input("Enter coordinates of a point on the ellipse"))
     t=t1(pt1)
     print t
     return t
while(True):
    print """Hello I am J.A.R.V.I.C(Just A Rather Very Intelligent Calculator). Please select one of the two to continue.
    A for Algebraic Second Order Function
    B for Any General Function
    Any other can be entered to exit"""
    choice=raw_input()
    if choice.upper()=='A' :
        print """Now I request you to enter the coefficients one at a time: HERE WE GO!!!!"""
        a=float(raw_input("Enter coefficient of x^2"))
        b=float(raw_input("Enter coefficient of y^2"))
        h=float(raw_input("Enter coefficient of xy"))/2
        g=float(raw_input("Enter coefficient of x"))/2
        f=float(raw_input("Enter coefficient of y"))/2
        c=float(raw_input("Enter constant value"))
        eq='(%fx^2)+(%fy^2)+(%fxy)(%fx)+(%fy)+(%f)'%(a,b,2*g,2*h,2*f,2*c-g*g-f*f)
        if a*b*c+2*f*g*h-a*f**2-b*g**2-c*h**2==0:
            if a**2+b**2+h**2==0:
                print 'The equation you have typed is of a straight line' 
                if f==0:
                    slope="Infinity"
                    yint="Doesn't intersect y axis"
                    xint=-c/(2*g)
                elif g==0:
                    xint="Doesn't intersect x axis"
                    slope=0
                    yint=-c/(2*f)
                else:
                    slope=-g/f
                    yint=-c/(2*f)
                    xint=-c/(2*g)
                print "The slope of the straight line is",slope
                print "x_intercept:",xint
                print "y_intercept:",yint 
                while(True):
                    ch1=int(raw_input("""select one of the options to continue:
        1)perpendicular distance of a point from the line
        2)foot of perpendicularnfrom a point on the line
        3)reflection of a point wrt to the line
        4)position of 2 points wrt to the line
        5)plot the curve
        Any other can be entered to exit
        """))
                    if ch1==1:
                        pdistp()
                    elif ch1==2:
                        ftpd()
                    elif ch1==3:
                        ref()
                    elif ch1==4:
                        ptposl()
                    elif ch1==5:
                        jarvic(eq)
                    else:
                        break
            else:
                while(True):
                    ch1=int(raw_input("""The equation you have typed is of a pair of straight line, select one of the options to continue:
        1)angle b/w the lines
        2)point of intersection
        3)plot the curve
        Any other can be entered to exit
        """))
                    if ch1==1:
                        angle()
                    elif ch1==2:
                        poi()
                    elif ch1==3:
                        jarvic(eq)
                    else:
                        break
        else:
            if a==b and h==0 and (g**2+f**2-c>0):
                print "The equation you have typed is of a circle"
                rad=math.sqrt(g*g+f*f-c)
                cen=(-g,-f)
                print "The radius of the circle is: ",rad," and the center's coordinates is: ",cen
                while(True):
                    ch1=int(raw_input("""Select one of the options to continue:
        1)Director circle
        2)position of a point wrt to the circle
        3)length of tangent from  a point to a cirle
        4)minimum distance from a point to a circle
        5)maximum distance from a point to a circle
        6)tangent to the circle at a point on it
        7)plot the curve
        Any other can be entered to exit
        """))
                    if ch1==1:
                        dirc()
                    elif ch1==2:
                        posptci()
                    elif ch1==3:
                        ltan()
                    elif ch1==4:
                        mind()
                    elif ch1==5:
                        maxd()
                    elif ch1==6:
                        tangci()
                    elif ch1==7:
                        jarvic(nopixel,eq)
                    else:
                        break
            elif h*h==a*b:
                print "The equation you have typed is of a parabola"
                while(True):
                    ch1=int(raw_input("""Select one of the options to continue:
        1)position of a point wrt to the parabola
        2)tangent to the parabola at a point on it
        3)plot the curve
        Any other can be entered to exit
        """))
                    if ch1==1:
                        posptpa()
                    elif ch1==2:
                        tangpa()
                    elif ch1==3:
                        jarvic(eq)
                    else:
                        break
            elif h*h-a*b>0:
                print "The equation you have typed is of a hyperbola"
                while(True):
                    ch1=int(raw_input("""Select one of the options to continue:
        1)position of a point wrt to the hyperbola
        2)tangent to the hypbola at a point on it
        3)plot the curve
        Any other can be entered to exit
        """))
                    if ch1==1:
                        pospthyp()
                    elif ch1==2:
                        tanghyp()
                    elif ch1==3:
                        jarvic(eq)
                    else:
                        break
            else:
                print "The equation you have typed is of a ellipse"
                while(True):
                    ch1=int(raw_input("""Select one of the options to continue:
        1)position of a point wrt to the ellipse
        2)tangent to the ellipse at a point on it
        3)plot the curve
        Any other can be entered to exit
        """))
                    if ch1==1:
                        posptell()
                    elif ch1==2:
                        tangell()
                    elif ch1==3:
                        jarvic(nopixel,eq)
                    else:
                        break
    else:
        exit()
        
        
                

                        
                
                
            
