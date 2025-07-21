# Dashboard personalizado para organizar mis tareas de POO
# Autor: Tatiana Aguilar
# Fecha: Julio 2025

import os
import subprocess

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix/Linux/macOS
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el script: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    semanas = {
        '1': 'Semana 9',
        '2': 'Semana 10',
        '3': 'Semana 11',
        '4': 'Semana 12',
        '5': 'Semana 13',
        '6': 'Semana 14',
        '7': 'Semana 15',
        '8': 'Semana 16'
    }

    while True:
        print("\nPanel de Tareas - Programación Orientada a Objetos")
        for key in semanas:
            print(f"{key} - {semanas[key]}")
        print("0 - Salir")

        eleccion = input("Selecciona una semana o '0' para salir: ")
        if eleccion == '0':
            print("Saliendo del programa.")
            break
        elif eleccion in semanas:
            mostrar_sub_menu(os.path.join(ruta_base, semanas[eleccion]))
        else:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_sub_menu(ruta_semana):
    if not os.path.exists(ruta_semana):
        print(f"La carpeta '{ruta_semana}' no existe. Créala primero.")
        return

    sub_carpetas = [f.name for f in os.scandir(ruta_semana) if f.is_dir()]

    while True:
        print(f"\nSubmenú - {os.path.basename(ruta_semana)}")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Volver al menú principal")

        eleccion = input("Selecciona una subcarpeta o '0' para regresar: ")
        if eleccion == '0':
            break
        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_semana, sub_carpetas[idx]))
            else:
                print("Opción inválida.")
        except ValueError:
            print("Debes escribir un número.")

def mostrar_scripts(ruta_subcarpeta):
    scripts = [f.name for f in os.scandir(ruta_subcarpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\nScripts en {os.path.basename(ruta_subcarpeta)}:")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Volver")
        print("9 - Volver al menú principal")

        eleccion = input("Elige un script: ")
        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(scripts):
                ruta_script = os.path.join(ruta_subcarpeta, scripts[idx])
                codigo = mostrar_codigo(ruta_script)
                if codigo:
                    ejecutar = input("¿Ejecutar el script? (1: Sí / 0: No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    input("Presiona Enter para continuar...")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Debes escribir un número.")

if __name__ == "__main__":
    mostrar_menu()
