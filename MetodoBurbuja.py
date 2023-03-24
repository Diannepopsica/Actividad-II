# Se solicita al usuario que ingrese el número de elementos de la lista.
n = int(input("Ingrese el número de elementos de la lista: "))
lista = [ ]

# Se ingresan uno por uno los elementos y se colocan en la lista.
for i in range(n):
    while True:
        elemento = int(input("Ingrese un elemento a la lista: "))
        if elemento not in lista:
            lista.append(elemento)
            break
        else:
            print("Este elemento ya se encuentra en la lista. Favor de ingresar un nuevo elemento.")

# Se imprime la lista original
print("\nEsta es la lista que usted ingresó sin ordenar:\n",lista)

# Se realiza el ordenamiento por el método de burbuja.
for i in range(n):
    for j in range(0, n-1):
        if lista[j] > lista[j+1]:
            numMayor = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = numMayor

# Se imprime la lista ordenada de menor a mayor.
print("\nLa lista queda ordenada de  la siguiente manera:\n",lista)

# Se le pide al usuario que ingrese el elemento que querrá buscar en la lista.
k = int(input("\n¿Cuál es el elemento que desea buscar?: "))

# Se realiza la búsqueda del elemento k en la lista.
x = 0
y = len(lista) - 1

if k not in lista:
    print("\nEl elemento que busca no se encuentra en la lista.")
else:
    while x <= y:
        medio = (x + y) // 2
        if lista[medio] == k:
            print("\nEl elemento", k, "se encuentra en la posición número", medio + 1)
            break
        elif lista[medio] < k:
            x = medio + 1
        else:
            y = medio - 1


