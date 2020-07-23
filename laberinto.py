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

def conectar(lista):
    if lista == []:
        return []
    else:
        for i in range(len(lista)):
            if lista[i]!= "|": 
                if lista[i+1]!= "|":       
                    return prolog.assertz("conect("+lista[i]+", "+lista[i+1]+")")


"""
A=np.loadtxt("laberinto.txt",str,skiprows=0)
print(A)
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

H=[]
I=[]
J=[]
K=[]
L=[]
M=[]

for f in range(len(A)):      #fila 3
    B.append(A[2][f])

for i in range(len(B)-1, -1, -1):
    if B[i] == "*":
        del B[i]

print(B)
for i in range(len(B)):
            if B[i]!= "|":
                if B[i+1]!= "|":  
                    a="conect("+B[i]+", "+B[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):     #fila5
    C.append(A[4][f])

for i in range(len(C)-1, -1, -1):
    if C[i] == "*":
        del C[i]

print(C)
for i in range(len(C)):
            if C[i]!= "|":
                if C[i+1]!= "|":  
                    a="conect("+C[i]+", "+C[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):     #fila7
    D.append(A[6][f])

for i in range(len(D)-1, -1, -1):
    if D[i] == "*":
        del D[i]

print(D)
for i in range(len(D)):
            if D[i]!= "|":
                if D[i+1]!= "|":  
                    a="conect("+D[i]+", "+D[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):     #fila9
    E.append(A[8][f])

for i in range(len(E)-1, -1, -1):
    if E[i] == "*":
        del E[i]

print(E)
for i in range(len(E)):
            if E[i]!= "|":
                if E[i+1]!= "|":  
                    a="conect("+E[i]+", "+E[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):     #fila11
    F.append(A[10][f])

for i in range(len(F)-1, -1, -1):
    if F[i] == "*":
        del F[i]

print(F)
for i in range(len(F)):
            if F[i]!= "|":
                if F[i+1]!= "|":  
                    a="conect("+F[i]+", "+F[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):     #fila13
    G.append(A[12][f])

for i in range(len(G)-1, -1, -1):
    if G[i] == "*":
        del G[i]

print(G)
for i in range(len(G)):
            if G[i]!= "|":
                if G[i+1]!= "|":  
                    a="conect("+G[i]+", "+G[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):      #columna 3
    H.append(A[f][2])

for i in range(len(H)-1, -1, -1):
    if H[i] == "*":
        del H[i]

print(H)
for i in range(len(H)):
            if H[i]!= "|":
                if H[i+1]!= "|":  
                    a="conect("+H[i]+", "+H[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):     #columna 5
    I.append(A[f][4])

for i in range(len(I)-1, -1, -1):
    if I[i] == "*":
        del I[i]

print(I)
for i in range(len(I)):
            if I[i]!= "|":
                if I[i+1]!= "|":  
                    a="conect("+I[i]+", "+I[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):     #columna 7
    J.append(A[f][6])

for i in range(len(J)-1, -1, -1):
    if J[i] == "*":
        del J[i]

print(J)
for i in range(len(J)):
            if J[i]!= "|":
                if J[i+1]!= "|":  
                    a="conect("+J[i]+", "+J[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):     #columna 9
    K.append(A[f][8])

for i in range(len(K)-1, -1, -1):
    if K[i] == "*":
        del K[i]

print(K)
for i in range(len(K)):
            if K[i]!= "|":
                if K[i+1]!= "|":  
                    a="conect("+K[i]+", "+K[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):     #columna 11
    L.append(A[f][10])

for i in range(len(L)-1, -1, -1):
    if L[i] == "*":
        del L[i]

print(L)
for i in range(len(L)):
            if L[i]!= "|":
                if L[i+1]!= "|":  
                    a="conect("+L[i]+", "+L[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)

for f in range(len(A)):     #columna 13
        M.append(A[f][12])

for i in range(len(M)-1, -1, -1):
    if M[i] == "*":
        del M[i]

print(M)
for i in range(len(M)):
            if M[i]!= "|":
                if M[i+1]!= "|":  
                    a="conect("+M[i]+", "+M[i+1]+")" 
                    prolog.assertz(str(a))
                    print(a)"""

print(leer(""))
print(revisarfila(leer(""),[],2))
print(eliminarespacios(revisarfila(leer(""),[],2)))
"""conectar(eliminarespacios(revisarcolumna(leer(""),[],2)))
conectar(eliminarespacios(revisarfila(leer(""),[],2)))
conectar(eliminarespacios(revisarcolumna(leer(""),[],4)))
conectar(eliminarespacios(revisarfila(leer(""),[],4)))
conectar(eliminarespacios(revisarcolumna(leer(""),[],6)))
conectar(eliminarespacios(revisarfila(leer(""),[],6)))
conectar(eliminarespacios(revisarcolumna(leer(""),[],8)))
conectar(eliminarespacios(revisarfila(leer(""),[],8)))
conectar(eliminarespacios(revisarcolumna(leer(""),[],10)))
conectar(eliminarespacios(revisarfila(leer(""),[],10)))
conectar(eliminarespacios(revisarcolumna(leer(""),[],12)))
conectar(eliminarespacios(revisarfila(leer(""),[],12)))
for result in prolog.query("conect(X,Y)"):
	print (str(result['X']) +" conecta con "+ str(result['Y']))
for sol in prolog.query("sol"):
    print(sol)"""
