registroDeClientes = []
hayOtro = True
costoTotal = 0

while (hayOtro):
    cliente = input("Ingrese el nombre del cliente: ")
    producto = input("Ingrese el nombre del producto: ")
    costo = float(input("Ingrese el costo del producto ($0.00): "))
    
    registroActual = dict(cliente=cliente, producto=producto, costo=costo)
    registroDeClientes.append(registroActual)

    comprobacion = input("¿Desea continuar ingresando clientes? (si/no): ")

    while(not(comprobacion=="si" or comprobacion=="no")):
        comprobacion = input("¿Desea continuar ingresando clientes? (si/no): ")

    if(comprobacion== "si"):
        hayOtro = True      
    else:
        hayOtro = False

for registro in registroDeClientes:
    print(registro)
    costoTotal += registro['costo']
    
print("El monto total de los productos es: $" + str(costoTotal))