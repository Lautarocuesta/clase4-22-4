numeros = [1, 2, 3, 4, 5]

resultasuma = list(map(lambda x: x + 5, numeros))

resultapot = list(map(lambda x: x ** 3, numeros))


print("Lista de números:", numeros)
print("Resultado de sumar 5 a cada número:", resultasuma)
print("Resultado de elevar al cubo cada número:", resultapot)