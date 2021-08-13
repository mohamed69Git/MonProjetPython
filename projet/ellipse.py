from turtle import *
from math import *

class Coordonne:
    def __init__(self, x, y) -> None:
        self.abcisse = x
        self.ordonne = y


"""
tracerJoins(Coordonner(x,y), abcisseDeDepar)

Cette fonction permet de representer toute les joins grace au Coordonne qui lui ont ete fourni
Les cordonne doivent etre tres bien respectes

"""
def tracerJoins(A: Coordonne, abcisseOr):
    diviseur = abs(A.abcisse-abcisseOr)
    difficultCordinate = [250.303, 277.819106,292.658477, 299.6346, 292.658477, 277.819106, 250.303]
    onePart = diviseur/8
    for cordinate in difficultCordinate:
        # speed(0)
        if(onePart== (diviseur/8)):
            penup()
            goto(xcor() + (diviseur/8)*0.3, 202.3030214)
            pendown()
            goto(A.abcisse+onePart, A.ordonne)
            goto(A.abcisse+onePart, cordinate)
            goto(A.abcisse+onePart, A.ordonne)
            
        if(onePart/(diviseur/8) %2):
            pendown()
            goto(A.abcisse+onePart, A.ordonne)
            goto(A.abcisse+onePart, cordinate)
            goto(A.abcisse+onePart, A.ordonne)
        if(onePart/(diviseur/8) %2==0):
            goto(A.abcisse+onePart, cordinate)
            goto(A.abcisse+onePart, A.ordonne)
            goto(A.abcisse+onePart, cordinate)
        if(xcor() == abcisseOr-(diviseur/8)):
            goto(abcisseOr-(diviseur/8)+ (diviseur/8)*0.73, 202.3030214)
            penup()
            goto(abcisseOr , A.ordonne)
            pendown()
            goto(A.abcisse, A.ordonne)
        onePart+=diviseur/8
    

"""
superRectangle(A: Coordonne, largeur)
permet de creer deux rectangle dont l'un est sur l'autre, le plus petit sur le plus grand, 
    grace au coordonne qui sont passe en parametre , et la largeur
"""
def superRectangle(A: Coordonne, largeur):
    color("skyblue")
    setheading(0)
    penup()
    goto(A.abcisse, A.ordonne)
    begin_fill()
    pendown()
    forward(largeur)
    right(90)
    forward(largeur/2)
    left(90)
    forward(largeur/2)
    right(90)
    forward(largeur/2)
    
    right(90)
    forward(largeur*3)
    right(90)
    forward(largeur/2)
    right(90)
    forward(largeur/2)
    left(90)
    forward(largeur/2)
    right(90)
    forward(largeur)
    end_fill()


"""
pont_complet() cree toutle les trois demi cercles puis fait appel a la fonction tracerJoins()
qui lui ajoutera toute les joins necessaire, la fonction superRectangle() pour la realisation complete du pont
"""
def pont_complet():
    
    ellipseWidth = 240 # largeur de l'ellipse
    ellipseHeigth = 150 # hauteur de l'ellipse
    inclinaisonDroit = 0.000000000000002 #l'inclinaison droit de l'ellipse
    pensize(5)
    bridge = [540,  59, -422] #les trois abcisse qui determinent le debut et la fin de chaque ellipse
    for pont in bridge:   
        color("skyblue")
        for i in range(1,360):
            t = i * (pi / 180)
            x = ellipseWidth * sin(t)+pont
            y = ellipseHeigth * cos(t) - ellipseHeigth
            tilt =(pi / 90)*inclinaisonDroit
            x1 = (x * cos(tilt) + y * sin(tilt))
            y1 = (x*sin(tilt) - y*cos(tilt))
            if (i >= 90 and i <=270):
                goto(x1,y1)
                pendown()
            else:
                penup()
            if i == 90:    
                coorX = xcor()
            if i == 270:
                coorXF = xcor()
                coorYF=ycor()
                if(pont !=-422):
                    superRectangle(Coordonne(xcor(), ycor()), 65)
        pendown()                
        tracerJoins(Coordonne(coorXF, coorYF), coorX)


def principal():
    pont_complet()            
            
if __name__=='__main__':
    pont_complet()
    
    
exitonclick()