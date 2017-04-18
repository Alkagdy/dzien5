lista = [1,2,3,4,5,6,7,8,9]

lista2 = []
for element in lista:
    lista2.append(element*element)

print(lista2)
#**2 to do kwadratu
lista3 = [element**2 for element in lista]
print(lista3)

#chce elementy podniesione d okwadratu ktore sa zawarte w mojej liscie i podzielne przez 3
lista4 = [element**2 for element in lista if element%3==0]
print(lista4)