#listy

#deklarowanie listy

lista =["trzy", "jeden"]
print(lista)
lista1 =[2,3,4,9,0,3,4]
print(lista1)

lista2 = list("kwiatek")
print(lista2)

el_string = ''.join(lista2)
print(el_string)

lista3 =[1, "dwa", 3.0, range(3), [0,1]]
print(lista3)
print(len(lista3))

print(lista3[2])
print(lista3 [4][0])

#wprowadzanie nowych danych do listy
lista3[1] = "osiem"
print(lista3)
