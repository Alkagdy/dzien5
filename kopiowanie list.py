wynik = 3

lista_a = ["zero", "jeden", wynik]
print("lista a:", lista_a)

wynik = 43
print("lista a po zmianie:", lista_a)
print()

lista_b = lista_a.copy()
print("Lista b skopoiowana z a:", lista_b )

print("Dodajemy element do listy a")
lista_a.append("nowy")
print(lista_a)
print(lista_b)

print(id(lista_a))
print(id(lista_b))
