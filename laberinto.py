from pyswip import Prolog
import numpy as np
prolog = Prolog()
prolog.consult("laberinto.pl")



def leer(texto):
    if texto == None:
        pass
    else:
        return np.loadtxt("laberinto.txt",str,skiprows=0)

def revisarfila(matriz,matriz2,fila):
    if matriz == []:
        return []
    else:
        for f in range(len(matriz)):
            matriz2.append(matriz[fila][f])
    return matriz2

def revisarcolumna(matriz,matriz2,colum):
    if matriz == []:
        return []
    else:
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

def conectar1(lista):
        if lista[1]!= "|": 
            if lista[2]!= "|":       
                return prolog.assertz("conect("+lista[1]+", "+lista[2]+")")

def conectar2(lista):
        if lista[2]!= "|": 
            if lista[3]!= "|":       
                return prolog.assertz("conect("+lista[2]+", "+lista[3]+")")

def conectar3(lista):
        if lista[3]!= "|": 
            if lista[4]!= "|":       
                return prolog.assertz("conect("+lista[3]+", "+lista[4]+")")

def conectar4(lista):
        if lista[4]!= "|": 
            if lista[5]!= "|":       
                return prolog.assertz("conect("+lista[4]+", "+lista[5]+")")

def conectar5(lista):
        if lista[5]!= "|": 
            if lista[6]!= "|":       
                return prolog.assertz("conect("+lista[5]+", "+lista[6]+")")
     
def conectar6(lista):
        if lista[6]!= "|": 
            if lista[7]!= "|":       
                return prolog.assertz("conect("+lista[6]+", "+lista[7]+")")

def conectar7(lista):
        if lista[7]!= "|": 
            if lista[8]!= "|":       
                return prolog.assertz("conect("+lista[7]+", "+lista[8]+")")

def conectar8(lista):
        if lista[8]!= "|": 
            if lista[9]!= "|":       
                return prolog.assertz("conect("+lista[8]+", "+lista[9]+")")

def conectar9(lista):
        if lista[9]!= "|": 
            if lista[10]!= "|":       
                return prolog.assertz("conect("+lista[9]+", "+lista[10]+")")
                    

print(leer(""))
conectar1(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar2(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar3(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar4(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar5(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar6(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar7(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar8(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar9(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar1(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar2(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar3(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar4(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar5(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar6(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar7(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar8(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar9(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar1(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar2(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar3(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar4(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar5(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar6(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar7(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar8(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar9(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar1(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar2(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar3(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar4(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar5(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar6(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar7(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar8(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar9(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar1(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar2(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar3(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar4(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar5(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar6(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar7(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar8(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar9(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar1(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar2(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar3(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar4(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar5(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar6(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar7(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar8(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar9(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar1(eliminarespacios(revisarfila(leer(""),[],2)))
conectar2(eliminarespacios(revisarfila(leer(""),[],2)))
conectar3(eliminarespacios(revisarfila(leer(""),[],2)))
conectar4(eliminarespacios(revisarfila(leer(""),[],2)))
conectar5(eliminarespacios(revisarfila(leer(""),[],2)))
conectar6(eliminarespacios(revisarfila(leer(""),[],2)))
conectar7(eliminarespacios(revisarfila(leer(""),[],2)))
conectar8(eliminarespacios(revisarfila(leer(""),[],2)))
conectar9(eliminarespacios(revisarfila(leer(""),[],2)))
conectar1(eliminarespacios(revisarfila(leer(""),[],4)))
conectar2(eliminarespacios(revisarfila(leer(""),[],4)))
conectar3(eliminarespacios(revisarfila(leer(""),[],4)))
conectar4(eliminarespacios(revisarfila(leer(""),[],4)))
conectar5(eliminarespacios(revisarfila(leer(""),[],4)))
conectar6(eliminarespacios(revisarfila(leer(""),[],4)))
conectar7(eliminarespacios(revisarfila(leer(""),[],4)))
conectar8(eliminarespacios(revisarfila(leer(""),[],4)))
conectar9(eliminarespacios(revisarfila(leer(""),[],4)))
conectar1(eliminarespacios(revisarfila(leer(""),[],6)))
conectar2(eliminarespacios(revisarfila(leer(""),[],6)))
conectar3(eliminarespacios(revisarfila(leer(""),[],6)))
conectar4(eliminarespacios(revisarfila(leer(""),[],6)))
conectar5(eliminarespacios(revisarfila(leer(""),[],6)))
conectar6(eliminarespacios(revisarfila(leer(""),[],6)))
conectar7(eliminarespacios(revisarfila(leer(""),[],6)))
conectar8(eliminarespacios(revisarfila(leer(""),[],6)))
conectar9(eliminarespacios(revisarfila(leer(""),[],6)))
conectar1(eliminarespacios(revisarfila(leer(""),[],8)))
conectar2(eliminarespacios(revisarfila(leer(""),[],8)))
conectar3(eliminarespacios(revisarfila(leer(""),[],8)))
conectar4(eliminarespacios(revisarfila(leer(""),[],8)))
conectar5(eliminarespacios(revisarfila(leer(""),[],8)))
conectar6(eliminarespacios(revisarfila(leer(""),[],8)))
conectar7(eliminarespacios(revisarfila(leer(""),[],8)))
conectar8(eliminarespacios(revisarfila(leer(""),[],8)))
conectar9(eliminarespacios(revisarfila(leer(""),[],8)))
conectar1(eliminarespacios(revisarfila(leer(""),[],10)))
conectar2(eliminarespacios(revisarfila(leer(""),[],10)))
conectar3(eliminarespacios(revisarfila(leer(""),[],10)))
conectar4(eliminarespacios(revisarfila(leer(""),[],10)))
conectar5(eliminarespacios(revisarfila(leer(""),[],10)))
conectar6(eliminarespacios(revisarfila(leer(""),[],10)))
conectar7(eliminarespacios(revisarfila(leer(""),[],10)))
conectar8(eliminarespacios(revisarfila(leer(""),[],10)))
conectar9(eliminarespacios(revisarfila(leer(""),[],10)))
conectar1(eliminarespacios(revisarfila(leer(""),[],12)))
conectar2(eliminarespacios(revisarfila(leer(""),[],12)))
conectar3(eliminarespacios(revisarfila(leer(""),[],12)))
conectar4(eliminarespacios(revisarfila(leer(""),[],12)))
conectar5(eliminarespacios(revisarfila(leer(""),[],12)))
conectar6(eliminarespacios(revisarfila(leer(""),[],12)))
conectar7(eliminarespacios(revisarfila(leer(""),[],12)))
conectar8(eliminarespacios(revisarfila(leer(""),[],12)))
conectar9(eliminarespacios(revisarfila(leer(""),[],12)))


for sol in prolog.query("sol"):
    print(sol)
    
