def promedio_temperaturas(temperatuas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperatuas)/len(temperatuas)

def ingreso_de_temperaturas():
    while True:
        try:
            ingresar_temperatuas = int(input("Ingrese temperatura en celsius: "))
            return ingresar_temperatuas
        except ValueError:
            print("Error. Valor ingresado no valido")
    


lista_temperaturas = []


for i in range(30):
        lista_temperaturas.append(ingreso_de_temperaturas())


print(f"Elementos de la lista: {len(lista_temperaturas)}.\n"
      f"Promedio: {promedio_temperaturas(temperatuas=lista_temperaturas)}")