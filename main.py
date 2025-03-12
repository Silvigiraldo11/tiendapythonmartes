nombreVendedor=None 
productos=[]
producto={}

opcion=100

print("Mercado")
print("********")
print("1. Crear lista mercado")
print("2. Ver Lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("Presiona 5 para salir")
while opcion != 5:
    opcion=int(input("Digita una opcion: "))
    if opcion == 1:
        print("Bienvenido a la creacion de tu lista de mercado")
        
        #creando claves y valores de un diccionario
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["precio"]=int(input("Digita el precio del producto: "))
        producto["cantidad"]=int(input("Cuantos elementos de este producto vas a llevar: "))
        producto["presentacion"]=input("Cual presentacion llevaras? ")
        
        #mostrando mi diccionario
        #print(producto)
        
        #poblando una lista (agrgando elementos a una lista)
        productos.append(producto)
        print(productos)
        
           
    elif opcion==2:
        #utilizanod ciclos FOR en python recorrer LISTAS
        ## lista plural, diccionario singular, variable iteradora o auxiliar es productoSeleccionado, solo funciona hasta recorrecor el arreglo
        for productoSeleccionado in productos:
            print(productoSeleccionado["nombre"])
            #print("ID: ",producto["id"])
            #print("Nombre: ",producto["nombre"])
            #print("Precio: ",producto["precio"])
            #print("Cantidad: ",producto["cantidad"])
            #print("Presentacion: ",producto["presentacion"])
            #print("********")
    elif opcion==3:
        #0. pregunta a quien va a editar
        productoCambio = int(input("Digita el ID del producto que deseas editar: "))
        #1. encontrar el producto a editar, crear bandera para que no se repita
        for productoBuscado in productos:
            if productoBuscado["id"]==productoCambio:
                print("Producto encontrado")
                break
            else:
                print("Producto no encontrado")
                #print(productoBuscado)
                #productoSeleccionado=productoBuscado
                #2. selecciono el producto 
                #3. accedo a las propiedaes del atributo que quiero modifica
                productoSeleccionado["nombre"]=input("Digita el nuevo nombre del producto: ")
                productoSeleccionado["precio"]=int(input("Digita el nuevo precio del producto: "))
                productoSeleccionado["cantidad"]=int(input("Cuantos elementos de este producto vas a llevar: "))
                productoSeleccionado["presentacion"]=input("Cual presentacion llevaras? ")
                print("Producto modificado")
                print(productoSeleccionado)
                break
        else:
            print("Producto no encontrado")
        #2. selecciono el producto 
        #3. accedo a las propiedaes del atributo que quiero modifica
        # buscar pop para eliminar un elemento de una lista
    elif opcion==4:
        print("estoy en la 4")
    else:
        print("Opcion no valida")
        