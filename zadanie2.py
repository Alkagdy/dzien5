#zmien stringa w liste wyrazow (przecinki usuwamy)

zdanie = "Ala ma kota, kot ma Ale"
#usuwanie przecinka z zdania
zdanie = zdanie.replace(',','')

lista = zdanie.split()
print(lista)

