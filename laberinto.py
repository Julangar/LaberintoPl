from pyswip import Prolog
import numpy as np
prolog = Prolog()
prolog.consult("laberinto.pl")

def leer(texto):
    if texto == None:
        pass
    else:
        return np.loadtxt("laberinto.txt",str,skiprows=0)

def revisarfila(matriz,matriz2):
    if matriz == []:
        return []
    else:
        for f in range(len(matriz)):
            matriz2.append(matriz[1][f])
    return matriz2

def revisarcolumna(matriz,matriz2):
    if matriz == []:
        return []
    else:
        for f in range(len(matriz)):
            matriz2.append(matriz[f][1])
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
                if lista[i]!= "-":
                    if lista[i+1]!= "|":  
                        if lista[i+1]!= "-":  
                            return prolog.assertz("conect("+lista[i]+", "+lista[i+1]+")")


"""
A=np.loadtxt("laberinto.txt",str,skiprows=0)
print(A)
B=[]
for f in range(len(A)):
    B.append(A[1][f])

print(B)

for i in range(len(B)-1, -1, -1):
    if B[i] == "*":
        del B[i]

print(B)
print(B[1])
print(B[2])
for i in range(len(B)):
            if B[i]!= "|":
                if B[i+1]!= "|":  
                    a="conect("+B[i]+", "+B[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)
"""


print(leer(""))
print(revisarfila(leer(""),[]))
print(eliminarespacios(revisarfila(leer(""),[])))
conectar(eliminarespacios(revisarfila(leer(""),[])))
conectar(eliminarespacios(revisarcolumna(leer(""),[])))
for result in prolog.query("conect(X,Y)"):
	print (str(result['X']) +" conecta con "+ str(result['Y']))
for sol in prolog.query("sol"):
    print(sol)
