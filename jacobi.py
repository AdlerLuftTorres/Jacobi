import numpy
import math
import random
import sys
from mpi4py import MPI
comm=MPI.COMM_WORLD
rank = MPI.COMM_WORLD.Get_rank()

n = int (sys.argv[1])

A = []
b = numpy.zeros(n)
x0 = numpy.random.randint(10,size=(n))
x1 = numpy.zeros(n)
print('x1 = ')
print(x1)
print('x0 = ')
print(x0)


def creamatriz(n):
	A=numpy.random.randint(10,size=(n,n))
	return (A)
def matrizmasuno(A):
	matriz=[]
	i=0
	j=0
	for i in range(n):
		matriz.append([])
		for j in range (n):
			matriz[i].append(1+(A[i][j]))
	matriz = numpy.array(matriz)
	return(matriz)

def diagonal(A):
	D=[]
	i=0
	j=0
	for i in range(n):
		D.append([])
		for j in range (n):
			if i==j:
				D[i].append(A[i][j])
			else:
				D[i].append(0)
	D = numpy.array(D)
	return (D)

def resto(A):
	R=[]
	i=0
	j=0
	for i in range(n):
		R.append([])
		for j in range (n):
			if i==j:
				R[i].append(0)
			else:
				R[i].append(A[i][j])
	R = numpy.array(R)
	return (R)
def alamenosuno(M):
	matriz=[]
	i=0
	j=0
	for i in range(n):
		matriz.append([])
		for j in range (n):
			if i==j:
				matriz[i].append(1/float((M[i][j])))
			else:
				matriz[i].append(0)
	matriz = numpy.array(matriz)
	return (matriz)

def vetorxmatriz(v,M):
	F=numpy.matmul(v,M)
	return (F)

A = matrizmasuno(creamatriz(n))
print('A = ')
print(A)
D = diagonal(A)
print('D = ')
print(D)
R = resto(A)
print('R = ')
print(R)

while(numpy.array_equal(x0,x1)==False):
	x1=vetorxmatriz((b-(vetorxmatriz(x0,R))),alamenosuno(D))
	x0=x1
	#print('dentro de while x0= ')
	#print(x0)
	#print('dentro de while x1= ')
	#print(x1)
print('soluciones=')
print(x1)
