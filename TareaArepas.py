# Introducción del programa
print("Buenas, vamos a hacer arepas!")
print("Le voy a solicitar los ingredientes y usted me va a indicar las cantidades, para saber la masa final de la arepa.")

# Solicitar al usuario la cantidad de harina, agua y sal en gramos, para tener la medida en los mismos valores
Harina = input("Indiqueme la cantidad de harina que desea utlizar en gramos: \n-> ")
Agua = input("Indiqueme la cantidad de agua que desea utilizar en mililitros: \n-> ")
# El agua se pide en mililitros porque en agua gramos y mililitros es la misma cantidad
Sal = input("Indiqueme la cantidad de sal que desea utilizar en gramos: \n-> ")

#  Convertir los valores de string a float para realizar las operaciones
Harina = float(Harina)
Agua  = float(Agua)
Sal = float(Sal)

#  Realizar la operación para saber la masa final de la arepa
Masa_Total = Harina + Agua + Sal

#  Imprimir el resultado del usuario 
print(f"La cantidad de masa total para la arepa es: {Masa_Total} gramos!")
