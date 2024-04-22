listan= [
   {
      "nombre": "pepito",
      "edad": 30
  },
  {
      "nombre": "marta",
      "edad": 30
  },
{
    "nombre": "pepito1",
    "edad": 30
}
  
]


print("Edad de la primera persona:",listan[0]["edad"])
print("Nombre de la segunda persona:", listan[1]["nombre"])
print()

for diccionario in listan:
    for clave, valor in diccionario.items():
        print(clave + ":", valor)
    print() 