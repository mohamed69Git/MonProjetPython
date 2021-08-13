import genieCivilOuvrage2D as mymodule
from turtle import *
from math import *
class Coordonne:
    def __init__(self, x, y) -> None:
        self.abcisse = x
        self.ordonne = y

A= Coordonne(-450, 250)                 #A est le point initial de depart de la facade se trouvant au coordonnees indiques 
"""
representer un rectangle avec une couleur de fond
"""
def rectangle(A: Coordonne, longeur, largeur, couleur):
    penup()
    goto(A.abcisse, A.ordonne)
    setheading(0)
    cote = (longeur, largeur, longeur, largeur)
    pendown()
    begin_fill()
    for i in cote:
        forward(i)
        right(90)
    right(90)
    color(couleur)
    end_fill()
    color("black")    
    
"""
dessiner la partie gauche de la facade
"""    
def partieGaucheFenetre(A: Coordonne):
    penup()
    goto(A.abcisse, A.ordonne)
    pendown()
    forward(10)
    right(90)
    forward(205)
    right(90)
    forward(10)
    left(90)
    begin_fill()
    forward(572)
    left(90)
    forward(510)
    left(90)
    forward(575+12)
    left(90)
    forward(500)
    left(90)
    forward(15)
    right(90)
    forward(10)
    color("lightgrey")
    end_fill()
    color("black")
    penup()
    left(90)
    forward(572)
    grandFenetre = Coordonne(xcor()+15, ycor())
    lesLongFenetre(Coordonne(grandFenetre.abcisse+37, grandFenetre.ordonne+5),10, 10, 65, 470, 150, 30, 125)    
    
"""
realiser toute la partie droite de la fenetre 
"""
def partieDroitFenetre(A: Coordonne):
    pendown()
    goto(A.abcisse, A.ordonne)
    setheading(0)
    begin_fill()
    forward(572)
    right(90)
    forward(510)
    right(90)
    forward(575+12)
    right(90)
    forward(575-75)
    right(90)
    forward(15)
    left(90)
    forward(15)
    grandFenetre = Coordonne(xcor(), ycor())
    color("lightgrey")
    end_fill()
    color("black")
    lesLongFenetre(Coordonne(grandFenetre.abcisse, grandFenetre.ordonne),10, 10, 65, 470, 150, 30, 125)


"""
Faire la representation de la partie superieur de la facade
"""    
def partieSuperieur(A: Coordonne):
    penup()
    goto(A.abcisse, A.ordonne)
    pendown()
    forward(901)
    A.abcisse = 451
    
    debutRec = Coordonne(xcor(), ycor())
    
    left(90)
    forward(55)
    left(90)
    countTwo = 271
    forward(countTwo)

    A.abcisse = (450/5)*2-1
    # tick = 0
    left(90)
    forward(55)
    backward(55)
    right(90)
    # tick = 361
    forward(361)
    A.abcisse = (-450/5)*2-1
        
    left(90)
    forward(55)
    backward(55)
    right(90)
    forward(270)
    A.abcisse = -451  
    left(90)
    forward(55)
    backward(55)
    chapeau(A)
    fenetreHaut(debutRec, countTwo)
    
#mettre en place le rectangle en bas de la facade
def bottomRectangle(A: Coordonne):
    penup()
    goto(A.abcisse, A.ordonne)
    forward(10)
    right(90)
    forward(205)
    right(90)
    forward(10)
    left(90)
    forward(572)
    left(90)
    forward(510)
    left(90)
    rectangle(Coordonne(xcor(), ycor()), 1349, 15, "white")

#Cette fonction permet de representer les longs fenetres
def lesLongFenetre(A: Coordonne,margeinit, margex, mySize, longueur, largeur, marge, margey):
    rectangle(Coordonne(A.abcisse, A.ordonne-marge),  largeur, longueur, "lightgrey")
    lesPetitesFenetre(Coordonne(A.abcisse, A.ordonne),margeinit, margex, mySize)
    fenetreSecond(Coordonne(A.abcisse, A.ordonne), margey, mySize)
    
    
    rectangle(Coordonne(A.abcisse+48+273/2, A.ordonne-marge),  largeur, longueur, "lightgrey")
    lesPetitesFenetre(Coordonne(A.abcisse, A.ordonne),margeinit, margex, mySize)
    fenetreSecond(Coordonne(A.abcisse, A.ordonne), margey, mySize)
    
    rectangle(Coordonne(A.abcisse+369, A.ordonne-marge),  largeur, longueur, "lightgrey")
    lesPetitesFenetre(Coordonne(A.abcisse, A.ordonne),margeinit, margex, mySize)
    fenetreSecond(Coordonne(A.abcisse, A.ordonne), margey, mySize)

#permet de dessiner les petits fenetres            
def lesPetitesFenetre(A: Coordonne,margeinit, margex, mySize):
    for i in range(4):
        if i == 0:
            
            rectangle(Coordonne(xcor()+margeinit, ycor()-margeinit), mySize, mySize, "white")
        elif(i==2):
            
            rectangle(Coordonne(xcor()-mySize, ycor()-mySize), mySize, mySize, "white")
        else:
            rectangle(Coordonne(xcor()+mySize, ycor()), mySize, mySize, "white")
    
        
#realise les fenetres secondaires rectangulaires en bas des quatre fenetres carres
def fenetreSecond(A: Coordonne,margey, mySize):
    
    for i in range(4):
        if i == 0:
            rectangle(Coordonne(xcor()-mySize, ycor()-margey), mySize, mySize*2, "white")
        elif(i==2):
            rectangle(Coordonne(xcor()-mySize, ycor()-mySize*2), mySize, mySize*2, "white")
        else:
            rectangle(Coordonne(xcor()+mySize, ycor()), mySize, mySize*2, "white")


#permet de representer le chapeau de la facade    
def chapeau(B: Coordonne):
    begin_fill()
    setheading(0)
    left(30)
    cote = 0
    pensize(1.5)

    cote = 156
    forward(cote)
    print(cote)
    B.abcisse+=cote
    
    pensize(2.5)
    right(60)
    forward(cote)
    backward(cote)
    pensize(1)
    left(30)
    pensize(1.5)
    forward(631)
    left(210)
    pensize(2)
    forward(cote)
    backward(cote)
    right(240)
    forward(cote)
    color("lightgreen")
    end_fill()
    color("black")


#permet de representer les petites fenetres en haut du chapeau de la facade    
def fenetreHaut(A: Coordonne, countwo):
    pensize(1)
    penup()
    goto(A.abcisse, A.ordonne)
    pendown()
    setheading(0)
    left(180)
    dec = countwo/7
    dessinerFenetre(3, dec, dec)
    startmiddlewindow = Coordonne(xcor()-dec, ycor())
    middleWindow(startmiddlewindow, dec)
    forward(dec)
    begin_fill()
    dessinerFenetre(3, dec, dec)
    goto(A.abcisse, A.ordonne)
    forward(countwo*2 + dec*9 + (dec/2-11))
    begin_fill()
    


#perment de dessiner des fenetres
def dessinerFenetre(nombredefenetre, dec, espacement):
    setheading(0)
    left(180)
    
    for i in range(nombredefenetre):
        if(i==0):
            forward(dec)
        else:
            forward(espacement)
        right(90)
        forward(40)
        left(90)
        forward(dec/2)
        left(90)
        forward(40)
        backward(40)
        right(90)
        forward(dec/2)
        left(90)
        forward(40)
        right(90)
            

#permet de mettre en place les fenetres au milieu de la facade        
def middleWindow(A: Coordonne, dec):
    setheading(0)
    left(180)
    forward(dec)
    dessinerFenetre(1,dec, dec)
    dessinerFenetre(3, dec, dec/2-13.7)
    dessinerFenetre(1, dec , dec)
    






#permet de representer le tableau se trouvant au dessus de la porte
def tableau(A: Coordonne):
    goto(A.abcisse, A.ordonne)
    setheading(0)
    left(90)
    forward(50)
    backward(50)
    setheading(0)
    right(90)
    forward(10)
    left(90)
    forward(205)
    
    left(90)
    forward(10)
    begin_fill()


#permet de creer des barres    
def createBar(nombrebar, longueur, espace):
    for i in range(nombrebar):
        setheading(0)
        left(180)
        forward(espace)
        left(90)
        forward(longueur)
        backward(longueur)


#permet de creer l'oreillle droite de la facade
def creerOreilleDroit(A: Coordonne):
    color("black")
    goto(A.abcisse, A.ordonne)
    setheading(0)
    forward(572)
    left(30)
    forward(100)
    left(60 + 90)
    forward(314*2 + 30)
    left(90)
    forward(50)
    color("lightgrey")
    end_fill()
    color("black")
    forward(10)   

#permet de creer l'oreille gauche de la facade    
def creerOreilleGauche(A: Coordonne):
    setheading(0)
    left(180)
    forward(313)
    setheading(0)
    right(30)
    forward(100)
    left(30)
    forward(572)
    left(90)
    forward(50)
    color("lightgrey")
    end_fill()
    backward(50)
    color("black")
    
#permet de dessiner des escalier
def escalier(longeurInitial, largeur):
    setheading(0)
    dimi = 4
    for i in range(6):
        pensize(4)
        left(180)
        forward(dimi)
        right(90)
        
        forward(largeur)
        left(90)
        forward(longeurInitial-dimi*2)
        left(90)    
        forward(largeur)
        if(i==0):
            pensize(1)
            right(90)
            forward(dimi)
            right(90)
            forward(88)
            backward(88)
            left(90)
            forward(15)
            right(90)
            forward(88)
            backward(88)
            setheading(0)
            forward(15+dimi)
            left(90)
            forward(largeur)
            right(90)
            forward(longeurInitial-dimi*2)
        else:    
            pensize(4)        
            backward(largeur)
            setheading(0)
            forward(longeurInitial-dimi*2)
        longeurInitial-=dimi*2
        pensize(1)
                
#permet de creer les barres des portes        
def barresPortes(A: Coordonne):
    pensize(1)
    goto(A.abcisse, A.ordonne)
    setheading(0)
    for i in range(3):
        createBar(1, 400, 15)
    setheading(0)
    left(180)
    forward(100) 
    for i in range(3):
        createBar(1, 400, 15)
    forward(400)
    left(90)
    forward(175)
    backward(145)
    begin_fill()
    left(90)
    forward(400)
    right(90)
    forward(115)
    right(90)
    forward(400)
    color("lightgrey")
    end_fill()
    color("black")
    left(90)
    forward(30)
    porteandAll(Coordonne(xcor(), ycor()))
    
#permet toute de regrouper tout les fonctions menant a realisation de toutes les portes    
def porteandAll(A: Coordonne):
    pensize(1)
    goto(A.abcisse, A.ordonne)
    setheading(0)
    left(180)
    forward(50)
    left(90)
    forward(12)
    backward(12)
    right(90)
    forward(75)
    left(90)
    forward(12)
    right(90)
    forward(50)
    right(90)
    forward(12)
    backward(12)
    right(90)
    forward(50)
    left(90)
    forward(170)
    quatrecarre = Coordonne(xcor(), ycor())
    begin_fill()
    mymodule.demiCercle(-37.5)
    petitcercle = Coordonne(xcor(), ycor())
    right(90)
    forward(75)
    backward(75)
    color("lightgrey")
    end_fill()
    color("black")
    left(90)
    forward(170)
    right(90)
    forward(75)
    backward(125)
    right(90)
    forward(12)
    backward(100)
    left(90)
    forward(15)
    right(90)
    forward(88)
    backward(88)

    escalier(145, 14.49)
    penup()
    goto(petitcercle.abcisse, petitcercle.ordonne)
    backward(37.5)
    left(90)
    forward(65)
    pendown()
    right(90)
    begin_fill()
    mymodule.newCercle(17)
    color("black")
    end_fill()
    penup()
    goto(xcor(), ycor()+120)
    rectangle(Coordonne(xcor(), ycor()), 30, 60, "white")
    rectangle(Coordonne(xcor()-30, ycor()), 30, 60, "white")
    penup()
    goto(quatrecarre.abcisse, quatrecarre.ordonne)
    pendown()
    rectangle(Coordonne(quatrecarre.abcisse, quatrecarre.ordonne),37.5, 79, "white")
    rectangle(Coordonne(quatrecarre.abcisse+37.5, quatrecarre.ordonne),37.5, 79, "white")
    rectangle(Coordonne(quatrecarre.abcisse, quatrecarre.ordonne-79),37.5, 79, "white")
    rectangle(Coordonne(quatrecarre.abcisse + 37.5, quatrecarre.ordonne-79),37.5, 79, "white")
        
"""
principal() est la ou on fait appel a tous les procedures qui menent a la realisation de la facade y sont regroupes
"""
def principal():
    partieSuperieur(Coordonne(A.abcisse, A.ordonne))
    creerOreilleGauche(A)
    tableau(Coordonne(xcor(), ycor()))
    pointDepart = Coordonne(xcor(), ycor())
    creerOreilleDroit(Coordonne(xcor(), ycor()))
    barresPortes(Coordonne(xcor(), ycor()))
    penup()
    goto(pointDepart.abcisse, pointDepart.ordonne)
    partieDroitFenetre(Coordonne(pointDepart.abcisse, pointDepart.ordonne))
    partieGaucheFenetre(Coordonne(pointDepart.abcisse, pointDepart.ordonne))
    bottomRectangle(Coordonne(pointDepart.abcisse, pointDepart.ordonne))
        
speed(0)      
principal()
penup()
goto(0, -400)
write("C'EST LA FIN, MERCI DE VOTRE AIMABLE ATTENTION!!!!!! BYE", True, align=CENTER, font=('Arial', 20, "normal"))
exitonclick()