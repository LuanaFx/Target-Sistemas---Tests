from math import sqrt
list=[]
N=int(input("Digite o numero que deseja encontrar"))
i=0

while i <= N:
    seq=((1+sqrt(5))**i-(1-sqrt(5))**i)/(2**i*sqrt(5))
    seq=int(seq)
    list.append(seq)
    i+=1
if N in list:
    print("O número pertence a seuquencia")
else:
    print("O número não pertence a seuquencia")