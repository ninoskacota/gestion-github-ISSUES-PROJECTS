materias = [
    "Matemáticas",
    "Programación",
    "Bases de Datos",
    "Física",
    "Algoritmos"
]

print("Lista original:")
for materia in materias:
    print(materia)

materias_ordenadas = sorted(materias, key=str.lower)
print("\nLista ordenada alfabéticamente:")
for materia in materias_ordenadas:
    print(materia) 