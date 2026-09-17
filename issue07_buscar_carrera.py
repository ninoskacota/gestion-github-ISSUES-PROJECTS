def datoscarr():
    return {
        "sistemas": ["Ana Pérez", "Luis Gómez", "Carla Ruiz"],
        "medicina": ["Pedro Sánchez", "María López"],
        "informatica": ["Jorge Torres", "Sofía Ramírez", "Diego Castro"],
        "economia": ["Elena Vargas"]
    }

def buscar(datos, carrera):
    return datos.get(carrera.lower())

def main():
    datos = datoscarr()
    carrera = input("Ingrese carrera: ")

    estudiantes = buscar(datos, carrera)

    if estudiantes:
        print(f"\nEstudiantes de {carrera}:")
        for i, nombre in enumerate(estudiantes, 1):
            print(f"{i}. {nombre}")
    else:
        print(f"\nLa carrera '{carrera}' no está registrada.")

main()