#Ejercicio 2: Análisis de Temperaturas

# Crea un sistema que:
# 1. Solicite al usuario temperaturas diarias durante una semana
# 2. Calcule estadísticas (media, mediana, máx, mín)
# 3. Identifique días con temperaturas extremas (± 2 desviaciones estándar)
# 4. Muestre un gráfico de barras de las temperaturas
import matplotlib.pyplot as plt

temperaturas = {"lunes":0,"martes":0,"miercoles":0,"jueves":0,"viernes":0,
                "sabado":0,"domingo":0}
datos = True
while datos:
    try:
        print("Ingresa temperaturas para su analisis")
        temperaturas["lunes"] = int(input("Ingrese la temperatura del Lunes: "))
        temperaturas["martes"] = int(input("Ingrese la temperatura del Martes: "))
        temperaturas["miercoles"] = int(input("Ingrese la temperatura del Miercoles: "))
        temperaturas["jueves"] = int(input("Ingrese la temperatura del Jueves: "))
        temperaturas["viernes"] = int(input("Ingrese la temperatura del Viernes: "))
        temperaturas["sabado"] = int(input("Ingrese la temperatura del Sabado: "))
        temperaturas["domingo"] = int(input("Ingrese la temperatura del Domingo: "))
        datos = False
    except ValueError:
        print("Error. Intentalo nuevamente")

media = sum(temperaturas.values())/len(temperaturas.values())
print(media)
temperaturaMax= max(temperaturas.values())
temperaturaMin= min(temperaturas.values())
temperaturas2 = sorted(temperaturas.values())
print(temperaturas2)
varianza = sum((x - media) ** 2 for x in temperaturas2) / len(temperaturas2)
desviacion_estandar = varianza ** 0.5
limite_superior = media + 2 * desviacion_estandar
limite_inferior = media - 2 * desviacion_estandar

n = len(temperaturas)

if n % 2 == 0:
    mediana = (temperaturas2[n//2 - 1] + temperaturas2[n//2]) / 2
else:
    mediana = temperaturas2[n//2]

dias_extremos = {dia:temp for dia,temp in temperaturas.items() if temp > limite_superior or temp < limite_inferior}
print(dias_extremos)

dias = list(temperaturas.keys())
temps = list(temperaturas.values())
colores = ["red" if dia in dias_extremos.keys() else "blue" for dia in dias]

print("Media:", media)
print("Mediana:", mediana)
print("Máxima:", temperaturaMax)
print("Mínima:", temperaturaMin)
print("Días extremos:", dias_extremos)

plt.bar(dias,temps,color=colores)
plt.title("Temperaturas de la semana")
for i, t in enumerate(temps):
    plt.text(i, t, str(t), ha="center", va="bottom")
plt.show()
