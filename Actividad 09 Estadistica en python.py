import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo
datos_calif = """nombre,matematicas,fisica,quimica,historia
Ana García,85,90,88,92
Luis Martínez,92,87,90,85
María López,88,92,85,90
Carlos Pérez,90,88,92,87
Elena Rodríguez,87,85,89,91
Pedro Sánchez,91,89,87,88
Laura Jiménez,89,91,90,89
Diego Torres,86,88,86,90
"""

# ESCRIBA SU SOLUCIÓN AQUÍ

def actualizar_base_de_datos(BOLETA,ruta,campos):
    with open(ruta,"w",encoding="utf-8",newline="") as f:
        f.seek(0)
        escritor = csv.DictWriter(f,fieldnames=campos)
        escritor.writeheader()
        for alumno in BOLETA:
            escritor.writerow(alumno)


def abrir_generar_archivo(ruta):
    with open(ruta, "a+", encoding="utf-8", newline="") as f:
        f.seek(0)
        contenido = f.read()

        if contenido == "":
            f.write(datos_calif)
            f.seek(0)
        f.seek(0)
        lector = csv.DictReader(f)
        calificaciones = list(lector)

    return calificaciones

def boleta_individual(alumnos):
    materias = ["Matematicas","Fisica","Quimica","Historia","Promedio"]
    calificaciones = []
    lista_de_alumnos = [alumno["nombre"] for alumno in alumnos]
    encontrado = True
    while encontrado:
        busqueda = input(f"Nombre del estudiante Lista de estudiantes:{lista_de_alumnos} (N para salir): ")
        if busqueda.lower() == "n":
            return

        for alumno in alumnos:
            if alumno["nombre"] == busqueda:
                encontrado = True
                calificaciones = [
                    alumno["matematicas"],
                    alumno["fisica"],
                    alumno["quimica"],
                    alumno["historia"],
                    float(alumno["promedio"])
                ]
                print("Nombre:", alumno["nombre"])
                print("Calificaciones:")
                print("Matemáticas:", alumno["matematicas"])
                print("Física:", alumno["fisica"])
                print("Química:", alumno["quimica"])
                print("Historia:", alumno["historia"])
                print("Promedio:", alumno["promedio"])
                plt.bar(materias, calificaciones, color="skyblue")
                plt.title(f"Boleta de {alumno['nombre']}")
                plt.ylabel("Calificación")
                plt.ylim(0, 100)
                for i, cal in enumerate(calificaciones):
                    plt.text(i, cal + 1, str(cal), ha="center")

                plt.show()
                break
def promedio(alumno):
    promiedin = float((alumno["matematicas"] + alumno["fisica"] + alumno["quimica"] + alumno["historia"])/4)
    return promiedin

def boleta_global(BOLETA):
    tabla_alumnos = []
    for alumno in BOLETA:
        fila = {
            "nombre": alumno["nombre"],
            "matematicas": alumno["matematicas"],
            "fisica": alumno["fisica"],
            "quimica": alumno["quimica"],
            "historia": alumno["historia"],
            "promedio": alumno["promedio"]
        }
        tabla_alumnos.append(fila)
    lista_estad = estadisticas_materias(BOLETA)
    estadisticas_por_materia = lista_estad[0]
    materia_mas_facil = lista_estad[1][0]
    materia_mas_dificil = lista_estad[1][1]

    tabla_global = {
        "boletas_alumnos": tabla_alumnos,
        "estadisticas_materias": estadisticas_por_materia,
        "materia_mas_facil": materia_mas_facil,
        "materia_mas_dificil": materia_mas_dificil
    }

    return tabla_global

def estadisticas_materias(boleta):
    mates = []
    fis = []
    quim = []
    his = []
    materias_globales = [{k:v for (k,v) in alumno.items() if k != "nombre" and k != "promedio"} for alumno in boleta]
    for materias in materias_globales:
        mates.append(materias["matematicas"])
        fis.append(materias["fisica"])
        quim.append(materias["quimica"])
        his.append(materias["historia"])
    facilDificil = facil_dificil(matematicas=mates,fisica=fis,quimica=quim,historia=his)
    return [{"matematicas":{"promedio": sum(mates)/len(mates),"max":max(mates),"min":min(mates)},
            "fisica":{"promedio": sum(fis)/len(fis),"max":max(fis),"min":min(fis)},
            "quimica":{"promedio": sum(quim)/len(quim),"max":max(quim),"min":min(quim)},
            "historia":{"promedio": sum(his)/len(his),"max":max(his),"min":min(his)}},facilDificil]


def facil_dificil(matematicas,fisica,quimica,historia):
    promedios = {"matematicas":sum(matematicas)/len(matematicas),
                 "fisica": sum(fisica)/len(fisica),
                 "quimica": sum(quimica)/len(quimica),
                 "historia":sum(historia)/len(historia)}
    nombre_facil = max(promedios, key=promedios.get)
    materia_mas_facil = {nombre_facil: promedios[nombre_facil]}
    nombre_dificil = min(promedios, key=promedios.get)
    materia_mas_dificil = {nombre_dificil: promedios[nombre_dificil]}
    return [materia_mas_facil,materia_mas_dificil]

def mostrar_reporte(tabla_global):
    alumnos = tabla_global["boletas_alumnos"]
    estadisticas = tabla_global["estadisticas_materias"]
    facil = tabla_global["materia_mas_facil"]
    dificil = tabla_global["materia_mas_dificil"]
    materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Promedio"]
    n_materias = len(materias)
    n_alumnos = len(alumnos)
    datos = []
    nombres = []
    for alumno in alumnos:
        cal = [
            alumno["matematicas"],
            alumno["fisica"],
            alumno["quimica"],
            alumno["historia"],
            float(alumno["promedio"])
        ]
        datos.append(cal)
        nombres.append(alumno["nombre"])
    x = np.arange(n_alumnos)
    ancho = 0.15
    fig, ax = plt.subplots(figsize=(12, 6))
    for i, materia in enumerate(materias):
        y = [datos[j][i] for j in range(n_alumnos)]
        ax.bar(x + i * ancho, y, width=ancho, label=materia)
        for j, val in enumerate(y):
            ax.text(x[j] + i * ancho, val + 0.5, str(round(val, 1)), ha='center', fontsize=8)

    ax.set_xticks(x + ancho * 2)  # centrar etiquetas
    ax.set_xticklabels(nombres, rotation=45, ha='right')
    ax.set_ylabel("Calificación")
    ax.set_title("Reporte Global de Calificaciones")
    ax.set_ylim(0, 100)
    ax.legend()
    facil_nombre = list(facil.keys())[0]
    facil_prom = list(facil.values())[0]
    dificil_nombre = list(dificil.keys())[0]
    dificil_prom = list(dificil.values())[0]

    ax.text(0, 95, f"Materia más fácil: {facil_nombre} ({facil_prom:.2f})", fontsize=10, color='green')
    ax.text(0, 90, f"Materia más difícil: {dificil_nombre} ({dificil_prom:.2f})", fontsize=10, color='red')

    plt.tight_layout()
    plt.show()


RUTA = r"calificaciones_competo.csv"
ENCABEZADOS = ["nombre","matematicas","fisica","quimica","historia","promedio"]
BOLETA = abrir_generar_archivo(RUTA)

for alumno in BOLETA:
    alumno["matematicas"] = int(alumno["matematicas"])
    alumno["fisica"] = int(alumno["fisica"])
    alumno["quimica"] = int(alumno["quimica"])
    alumno["historia"] = int(alumno["historia"])
    if "promedio" not in alumno:
        alumno["promedio"] = promedio(alumno)
    else:
        pass


while True:
    try:
        usuario = int(input(f"BASE DE DATOS DE ESTUDIANTES\n"
                            "¿Que acción quiere realizar?\n"
                            "1) Cargar lista de calificaciones globales\n"
                            "2) Cargas boleta individual \n"
                            "3) Actualiza base de datos\n "))
    except ValueError:
        print("Valor equivocado, vuelva a intentar")

    if usuario == 1:
        resultado = boleta_global(BOLETA=BOLETA)
        mostrar_reporte(resultado)
    elif usuario == 2:
        boleta_individual(BOLETA)
    elif usuario == 3:
        actualizar_base_de_datos(BOLETA=BOLETA,ruta=RUTA,campos=ENCABEZADOS)