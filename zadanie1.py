#program usuwajacy duplikaty z listy

lista = [10,20,30,40,20,45,54,45,50,90,100]

lista_bez_duplikatow = []

for num in lista:
    if num not in lista_bez_duplikatow:
        lista_bez_duplikatow.append(num)

    print(lista_bez_duplikatow)
    