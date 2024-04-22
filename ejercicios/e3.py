def contarpal(texto):
  # Dividir el texto por espacios
  palabras = texto.split()
  # Cuenta el numero de palabras
  nump = len(palabras)
  return nump

# Ejemplo de uso
texto = "Solo puedes rellenar este formulario una vez ponte en contacto con el."

resultado = contarpal(texto)
print("El número de palabras en el texto es:", resultado)