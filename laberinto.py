from pyswip import Prolog
import numpy as np
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Laberinto")
wn.setup(700,700)

prolog = Prolog()
prolog.consult("laberinto.pl")


#######################################Trasformar txt a una matriz y encontrar la solucion del laberinto############
def leer(texto):
    if texto == None:
        pass
    else:
        return np.loadtxt("laberinto.txt",str,skiprows=0)

def revisarfila(matriz,matriz2,fila):
    for f in range(len(matriz)):
            matriz2.append(matriz[fila][f])
    return matriz2

def revisarcolumna(matriz,matriz2,colum):

    for f in range(len(matriz)):
            matriz2.append(matriz[f][colum])
    return matriz2

def eliminarespacios(lista):
    if lista == []:
        return []
    else:
        for i in range(len(lista)-1, -1, -1):
            if lista[i] == "*":
                del lista[i]
    return lista

def conectar(lista):
    if lista == []:
        return []
    else:
        for i in range(len(lista)):
            if lista[i]!= "|": 
                if lista[i+1]!= "|":       
                    prolog.assertz("conect("+lista[i]+", "+lista[i+1]+")")
    return lista
                    

conectar(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar(eliminarespacios(revisarfila(leer(""),[],2)))
conectar(eliminarespacios(revisarfila(leer(""),[],4)))
conectar(eliminarespacios(revisarfila(leer(""),[],6)))
conectar(eliminarespacios(revisarfila(leer(""),[],8)))
conectar(eliminarespacios(revisarfila(leer(""),[],10)))
conectar(eliminarespacios(revisarfila(leer(""),[],12)))

for sol in prolog.query("sol()"): 
    for x in sol:
        print(sol)          
        
        
 
##########################################Dibujar Laberinto##############################
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

niveles = []


nivel_1 = []
nivel_1.append(revisarfila(leer(""),[],0))
nivel_1.append(revisarfila(leer(""),[],1))
nivel_1.append(revisarfila(leer(""),[],2))
nivel_1.append(revisarfila(leer(""),[],4))
nivel_1.append(revisarfila(leer(""),[],6))
nivel_1.append(revisarfila(leer(""),[],8))
nivel_1.append(revisarfila(leer(""),[],10))
nivel_1.append(revisarfila(leer(""),[],12))
nivel_1.append(revisarfila(leer(""),[],13))
nivel_1.append(revisarfila(leer(""),[],14))
niveles.append(nivel_1)

def iniciar_lab(nivel):
    for fila in range(len(nivel)):
        for column in range(len(nivel[fila])):
            barra = nivel[fila][column]
            screen_x = -288 + (column * 24)
            screen_y = 288 - (fila * 24)
            if barra == "*":
                pen.goto(screen_x, screen_y)
                pen.color("black")
                pen.stamp() 
            elif barra == "|":
                pen.goto(screen_x, screen_y)
                pen.color("white")
                pen.stamp() 
            elif barra == "i":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "2":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "3":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "4":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "10":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "16":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "22":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "21":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "15":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "14":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "20":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "26":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "27":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "28":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "34":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "33":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "32":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra == "f":
                pen.goto(screen_x, screen_y)
                pen.color("red")
                pen.stamp()
            elif barra != "i" or "2" or "3" or "4" or "10" or "16" or "22" or "21" or "15" or "14" or "20" or "26" or "27" or "28" or "34" or "33" or "32" or "f":
                pen.goto(screen_x, screen_y)
                pen.color("white")
                pen.stamp()
                         
            
pen = Pen()

iniciar_lab(niveles[0])

turtle.done()