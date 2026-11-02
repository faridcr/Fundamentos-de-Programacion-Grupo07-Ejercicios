"""
EJERCICIO BÁSICO 2
Enunciado: Crear un archivo de texto llamado 'notas_nuevas.txt'
y escribir en él los nombres de los estudiantes con notas >= 8.5.
Usar referencias explícitas para manipular los datos.
"""

ruta_entrada = "estudiantes.txt"
ruta_salida = "notas_nuevas.txt"

seleccionados = []                        # lista de tuplas (nombre, nota)

with open(ruta_entrada, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if not linea:
            continue                      # ignorar líneas vacías

        partes = linea.split(",")
        nombre = partes[0]                # referencia a un objeto str
        nota = float(partes[3])           # referencia a un objeto float

        if nota >= 8.5:
            seleccionados.append((nombre, nota))

# Referencia explícita: 'destino' apunta a la misma lista, no es una copia
destino = seleccionados
print(f"¿destino is seleccionados? {destino is seleccionados}")   # True

with open(ruta_salida, "w", encoding="utf-8") as f:
    f.write("ESTUDIANTES CON NOTA >= 8.5\n")
    f.write("=" * 30 + "\n")
    for nombre, nota in destino:
        f.write(f"{nombre}: {nota}\n")
        print(f"Guardado: {nombre} (id = {id(nombre)})")

print(f"\nTotal de registros con nota >= 8.5: {len(destino)}")