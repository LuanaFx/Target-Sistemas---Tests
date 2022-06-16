from math import sqrt
list=[67836.43,36678.66,29229.88,27165.48,19849.53]
listSum = sum(list)
percent=[]
i=0

while i <= 4:
   percent.append((list[i]/listSum)*100)
   i+=1
print("O faturamento em % dos estados: SP, RJ, MG, ES e OUTROS, respectivamente é:")
print(*percent)