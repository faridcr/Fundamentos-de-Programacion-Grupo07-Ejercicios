"""
EJERCICIO BÁSICO 1
Enunciado: Leer el archivo 'estudiantes.txt' y mostrar el nombre
y la nota de cada estudiante usando referencias a objetos (punteros
en Python).
Muestra además la identidad de memoria de cada objeto creado.
"""

ruta = "estudiantes.txt"

with open(ruta, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if not linea:
            continue                      # ignorar líneas vacías

        partes = linea.split(",")
        nombre = partes[0]                # referencia a un objeto str
        nota = float(partes[3])           # referencia a un objeto float

        # Otra variable que apunta al MISMO objeto (no es una copia)
        ref_nombre = nombre

        print(f"\n{nombre} -> {nota}")
        print(f"   id(nombre)       = {id(nombre)}")
        print(f"   id(nota)         = {id(nota)}")
        print(f"   ¿ref_nombre is nombre? {ref_nombre is nombre}")