def palindromo(palabra):
  palabra = palabra.lower().replace(" ", "")

  # Indices para comparar extremos
  izquierda = 0
  derecha = len(palabra) - 1

  
  while izquierda < derecha:
    if palabra[izquierda] != palabra[derecha]:
          return False
  izquierda += 1
  derecha -= 1
  return True


#palabras
p1 = "oso"
p2 = "plomo"

print(f"¿'{p1}' es un palíndromo? {palindromo(p1)}")
print(f"¿'{p2}' es un palíndromo? {palindromo(p2)}")