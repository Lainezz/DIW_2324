"""
Escribir un programa que gestione las facturas pendientes de 
cobro de una empresa. Las facturas se almacenarán en un diccionario 
donde la clave de cada factura será el número de factura y el 
valor el coste de la factura. El programa debe preguntar al 
usuario si quiere añadir una nueva factura, pagar una existente 
o terminar. Si desea añadir una nueva factura se preguntará por 
el número de factura y su coste y se añadirá al diccionario. 
Si se desea pagar una factura se preguntará por el número de 
factura y se eliminará del diccionario. Después de cada operación 
el programa debe mostrar por pantalla la cantidad cobrada hasta 
el momento y la cantidad pendiente de cobro.
"""
# key: value
print("Bienvenid@ a la gestion de users")

opc = 1
diccionarioUsers = {}
while opc != 0:
    print("1. Anadir user")
    print("0. Salir")
    opc = int(input("Qué desea hacer?"))
    
    
    if opc == 1:
        nombre = input("Introduzca su nombre")
        dni = input("Introduzca su dni")
        edad = int(input("Introduzca su edad"))
        
        diccionarioUsers[dni] = {"nombre": nombre, "edad": edad}
        
        for dni in diccionarioUsers:
            print("Info de: "+dni)
            print(diccionarioUsers[dni])
    elif opc == 0:
        print("Opción incorrecta...")