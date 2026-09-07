# estudiantes.py

# Lista de estudiantes con nombre, carrera y semestre
estudiantes = [
    {"nombre": "Ana Pérez", "carrera": "Ingeniería de Sistemas", "semestre": 3},
    {"nombre": "Luis Gómez", "carrera": "Ingeniería Civil", "semestre": 5},
    {"nombre": "María López", "carrera": "Medicina", "semestre": 2}
]

# Mostrar lista de estudiantes
print("Lista de estudiantes:")
for est in estudiantes:
    print(f"Nombre: {est['nombre']} | Carrera: {est['carrera']} | Semestre: {est['semestre']}")
