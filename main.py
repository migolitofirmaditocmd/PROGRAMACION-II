# # ESCRIBA SU SOLUCIÓN AQUÍ
# def iniciarPrograma():
#     programa = True
#     iniciar = input("¿Iniciamos la calculadora de conversión? Y/N ")
#     if iniciar.lower() == "y":
#         programa = True
#     elif iniciar.lower() == "n":
#         programa = False
#         print("De acuerdo, terminando programa")
#         pass
#     else:
#         print("Caracter invalido, intentelo nuevamente")
#         iniciarPrograma()
#     return programa
#
# def valorInicial():
#     try:
#         valor = float(input("Ingrese el valor a convertir: "))
#     except ValueError:
#         print("Error: Entrada no válida, intente otra vez.")
#         valorInicial()
#     return valor
#
# def elegirConversion():
#     print("Seleccione la conversión: \n"
#           "1: km → millas\n"
#           "2: millas → km\n"
#           "3: kg → libras\n"
#           "4: libras → kg\n"
#           "5: cm → pulgadas\n"
#           "6: pulgadas → cm\n"
#           "7: metros → pies\n"
#           "8: pies → metros\n"
#           "9: litros → galones\n"
#           "10: galones → litros")
#     try:
#         opcion = int(input("Opción: "))
#     except:
#         print("Opción no válida.")
#         elegirConversion()
#     return opcion
# def convertir(valor, opcion):
#     if opcion == 1:
#         return valor * 0.621371, "millas"
#     elif opcion == 2:
#         return valor * 1.60934, "kilómetros"
#     elif opcion == 3:
#         return valor * 2.20462, "libras"
#     elif opcion == 4:
#         return valor * 0.453592, "kilogramos"
#     elif opcion == 5:
#         return valor * 0.393701, "pulgadas"
#     elif opcion == 6:
#         return valor * 2.54, "centímetros"
#     elif opcion == 7:
#         return valor * 3.28084, "pies"
#     elif opcion == 8:
#         return valor * 0.3048, "metros"
#     elif opcion == 9:
#         return valor * 0.264172, "galones"
#     elif opcion == 10:
#         return valor * 3.78541, "litros"
#     else:
#         return None, None
#
# programaIniciado = iniciarPrograma()
# valorsito = valorInicial()
# opcionsita = elegirConversion()
#
# while programaIniciado == True:
#     print(f"Instrucciones de uso del programa: \n"
#           f"1. Se solicitara al al usuario un valor numérico \n"
#           f"2. Se preguntara qué conversión desea (km a millas, kg a libras, etc.) \n"
#           f"3. Muestre el resultado \n"
#           f"4. Se preguntara si desea hacer otra conversión")
#     resultado, unidad = convertir(valorsito,opcionsita)
#     if resultado is None:
#         print("Conversión no válida.")
#     else:
#         print(f"Resultado: {resultado:.4f} {unidad}")
#
#     repetir = input("\n¿Desea hacer otra conversión? (s/n): ").lower()
#     if repetir != "s":
#         print("Programa finalizado.")
#         programaIniciado = False

import csv

ARCHIVO = "calificaciones.csv"
CAMPOS = ["nombre", "matematicas", "fisica", "quimica", "promedio"]


def calcular_promedio(m, f, q):
    return round((m + f + q) / 3, 2)


def crear_archivo_si_no_existe():
        datos_iniciales = [
            {"nombre": "Ana", "matematicas": 85, "fisica": 90, "quimica": 88},
            {"nombre": "Luis", "matematicas": 92, "fisica": 87, "quimica": 90},
            {"nombre": "María", "matematicas": 88, "fisica": 92, "quimica": 85},
            {"nombre": "Carlos", "matematicas": 90, "fisica": 88, "quimica": 92}
        ]

        with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CAMPOS)
            writer.writeheader()

            for e in datos_iniciales:
                e["promedio"] = calcular_promedio(
                    e["matematicas"], e["fisica"], e["quimica"]
                )
                writer.writerow(e)

        print("Archivo creado con estudiantes iniciales.")


def estudianteNuevo():
    nombre = input("Nombre: ")
    matematicas = int(input("Matemáticas: "))
    fisica = int(input("Física: "))
    quimica = int(input("Química: "))

    promedio = calcular_promedio(matematicas, fisica, quimica)

    return {
        "nombre": nombre,
        "matematicas": matematicas,
        "fisica": fisica,
        "quimica": quimica,
        "promedio": promedio
    }


def agregar_estudiante():
    nuevo = estudianteNuevo()

    with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writerow(nuevo)

    print("Estudiante agregado.")


def leer_estudiantes():
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def guardar_estudiantes(lista):
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(lista)


def editar_estudiante():
    estudiantes = leer_estudiantes()
    nombre_buscar = input("Nombre del estudiante a editar: ")

    encontrado = False

    for e in estudiantes:
        if e["nombre"].lower() == nombre_buscar.lower():
            print("Ingrese nuevas calificaciones:")
            m = int(input("Matemáticas: "))
            f = int(input("Física: "))
            q = int(input("Química: "))

            e["matematicas"] = m
            e["fisica"] = f
            e["quimica"] = q
            e["promedio"] = calcular_promedio(m, f, q)

            encontrado = True
            break

    if encontrado:
        guardar_estudiantes(estudiantes)
        print("Estudiante actualizado.")
    else:
        print("Estudiante no encontrado.")


def mejor_promedio():
    estudiantes = leer_estudiantes()

    if not estudiantes:
        print("No hay estudiantes.")
        return

    mejor = max(estudiantes, key=lambda e: float(e["promedio"]))
    print(f"Mejor promedio: {mejor['nombre']} ({mejor['promedio']})")


def mostrar_todos():
    estudiantes = leer_estudiantes()
    print("\n--- LISTA DE ESTUDIANTES ---")
    for e in estudiantes:
        print(
            f"{e['nombre']} | M:{e['matematicas']} "
            f"F:{e['fisica']} Q:{e['quimica']} "
            f"P:{e['promedio']}"
        )


#  PROGRAMA PRINCIPAL
crear_archivo_si_no_existe()

while True:
    print("\n=== SISTEMA DE CALIFICACIONES ===")
    print("1) Agregar estudiante")
    print("2) Editar estudiante")
    print("3) Ver mejor promedio")
    print("4) Mostrar todos")
    print("5) Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        editar_estudiante()
    elif opcion == "3":
        mejor_promedio()
    elif opcion == "4":
        mostrar_todos()
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.")