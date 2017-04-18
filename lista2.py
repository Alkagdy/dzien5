lista = [1, "dwa", "trzy", 4]
for element in lista:
    print(element)


lista_z = [[1,2,3],[4,5,6],[7,8,9]]
for element in lista_z:
    for subelement in element:
        print(subelement)

print(lista[1:3])


#pop usuwa ostatni element z listy
x = lista.pop()
print(x)
print(lista)


