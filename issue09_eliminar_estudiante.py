#issue09_eliminar_estudiante.py
estudiantes = ["saul", "helen", "edson", "yasi"]

nombre = input("Ingrese el nombre del estudiante a eliminar : ")

if nombre in estudiantes :
    confirmar = input(f"Desea eliminar a {nombre}? (S/N):").upper()
    if confirmar == "S":
        estudiantes.remove(nombre)
        print(f"{nombre} ha sido eliminado")
    else :
        print("Operacion cancelada")
else :
       print("El estudiante no se encuentra en la lista ")
print("Lista actualizada:", estudiantes)