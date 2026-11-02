"""
EJERCICIO BÁSICO 3
Enunciado: Leer 'registro_sistema.log' y contar cuántos mensajes
hay de cada tipo: INFO, WARNING, ERROR. Mostrar el resumen.
"""

ruta = "registro_sistema.log"

contador_info = 0
contador_warning = 0
contador_error = 0

with open(ruta, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if not linea:
            continue                      # ignorar líneas vacías

        if "INFO" in linea:
            contador_info += 1
        elif "WARNING" in linea:
            contador_warning += 1
        elif "ERROR" in linea:
            contador_error += 1

total = contador_info + contador_warning + contador_error

print("RESUMEN DEL REGISTRO")
print("=" * 30)
print(f"INFO    : {contador_info}")
print(f"WARNING : {contador_warning}")
print(f"ERROR   : {contador_error}")
print("-" * 30)
print(f"TOTAL   : {total}")