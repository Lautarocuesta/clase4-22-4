def agregar_tarea(tareas):
  descripcion = input("Ingrese la descripción de la tarea: ")
  fecha = input("Ingrese la fecha límite de la tarea (dd/mm/aaaa): ")
  prioridad = input("Ingrese la prioridad de la tarea: ")
  tarea = {"Descripción": descripcion, "Fecha límite": fecha, "Prioridad": prioridad}
  tareas.append(tarea)
  print("Tarea agregada con éxito.")

def mostrar_tareas(tareas):
  if not tareas:
      print("No hay tareas agregadas.")
  else:
      print("Lista de tareas:")
      for idx, tarea in enumerate(tareas, start=1):
          print(f"Tarea {idx}: {tarea}")

def main():
  tareas = []

  while True:
      print("\nMenú:")
      print("1. Agregar tarea")
      print("2. Mostrar lista de tareas")
      print("3. Salir")

      opcion = input("Seleccione una opción: ")

      if opcion == "1":
          agregar_tarea(tareas)
      elif opcion == "2":
          mostrar_tareas(tareas)
      elif opcion == "3":
          print("Saliendo del programa...")
          break
      else:
          print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
  main()
