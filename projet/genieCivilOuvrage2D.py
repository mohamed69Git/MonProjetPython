from turtle import *
from math import *
class Coordonne:
    def __init__(self, x, y) -> None:
        self.abcisse = x
        self.ordonne = y
#newCercle permet de representer un cercle complet de rayon rayon

def newCercle(rayon):
    # pendown()
    # left(90)
    circle(rayon, 360)
    
#permet de repreenter un cercle avec un longueur et un largeur    
def rectangle(longeur, largeur):
    cote = (longeur, largeur, longeur, largeur)
    pendown()
    for i in cote:
        forward(i)
        right(90)
    
        
    

#permet de representer un demi_cercle grace a son rayon
def demiCercle(rayon):
    
    # left(90)
    circle(rayon, 180)

#newTriangle(a, b, angle)
# a represente la longueur du premier cote
#b represente la longueur du deuxime cote
#angle represente l'angle que fait le cote a et le cote b
def newTriangle(a, b, angle):
    forward(a)
    x = xcor()
    y= ycor()
    backward(a)
    if angle ==0:
        exit()
    if(angle>0):
        left(angle)
        forward(b)
    else:
        right(-angle)
        forward(b)
    goto(x,y)
        
#newCarre permet de faire un carre grace a son cote    
def newCaree(cote):
    pendown()
    for i in range(4):
        left(90)
        forward(cote)    

#newLosange permet de representer un losange grace a la longueur de son cote et de l'angle principal
def newLosange(cote, angle):
    if(angle==0):
        exit()
    forward(cote)
    x=xcor()
    y=ycor()
    backward(cote)
    if(angle>0):
        left(angle)
        forward(cote)
        right(angle)
        forward(cote)
    else:
        right(-angle)
        forward(cote)
        right(angle)
        forward(cote)
    goto(x,y)
        

#newPolygone permet de tracer un polygone grace a son rayon et son nombre de point
def newPolygone(rayon, nombredepoint):
    circle(rayon, 360, nombredepoint)
    


#trapez permet de representer un trapeze        
def trapeze(longueur, largeur,hauteur, angle):
    forward(longueur)
    x=xcor()
    y=ycor()
    backward(longueur)
    if(angle==0):
        exit()
    if(angle > 0):
        left(angle)
        while(ycor()<=hauteur):
            forward(1)
        right(angle)
        forward(largeur)
    else:
        right(-angle)
        while(ycor()>=-hauteur):
            forward(1)
        left(-angle)
        forward(largeur)
    goto(x,y)
    
def ellipse(largeur, hauteur):
    a = largeur # ellipse width
    b = hauteur # ellipse height

    for i in range(360):
        t = i * (pi / 180)
        x = a * sin(t)
        y = b * cos(t) - b
        #turtle.goto(x,y)
        tilt = 25 * (pi / 180)
        x1 = x * cos(tilt) + y * sin(tilt)
        y1 = x*sin(tilt) - y*cos(tilt)
        goto(x1,y1)

