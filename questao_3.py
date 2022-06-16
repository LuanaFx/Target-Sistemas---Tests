import json
with open("dados.json", encoding='utf-8') as meu_json:
  dados = json.load(meu_json)
lista=[]
i=0
k=0
j=len(dados["dados"])

while i<j:
  if dados['dados'][i]['valor']!=0:
    lista.append(dados['dados'][i]['valor'])
  i+=1

max_value = max(lista)
print('Maximum value:', max_value)

min_value = min(lista)
print('Minimum value:', min_value)

i=0
j=len(dados["dados"])
soma=sum(lista)
media=soma/j

while i<j:
  if  dados['dados'][i]['valor']>media:
    k+=1
  i+=1
print("A empresa teve faturamento acima da media em", k, "dias" )