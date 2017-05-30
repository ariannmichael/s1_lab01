def maximo(lista):
	maior = lista[0]
	
	for i in range(1, len(lista), 1):
		if lista[i] > maior:
			maior = lista[i]

	return maior


def minimo(lista):
	menor = lista[0]

	for i in range(1, len(lista), 1):
		if lista[i] < menor:
			menor = lista[i]

	return menor
