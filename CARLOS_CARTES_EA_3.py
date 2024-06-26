rut = [ ]
dineroRecaudado = 0
asientosSinModificar = [
    [1,2,3,4,5,6,7,8,9,10],
    [11,12,13,14,15,16,17,18,19,20],
    [21,22,23,24,25,26,27,28,29,30],
    [31,32,33,34,35,36,37,38,39,40],
    [41,42,43,44,45,46,47,48,49,50]      
]
asientosConsiderandoCompra = [
    [1,2,3,4,5,6,7,8,9,10],
    [11,12,13,14,15,16,17,18,19,20],
    [21,22,23,24,25,26,27,28,29,30],
    [31,32,33,34,35,36,37,38,39,40],
    [41,42,43,44,45,46,47,48,49,50]
]
def eleccion1 (x):
    if x == 1:
        print("Ha ingresado a la opción de comprar entradas")
        cantidadDeEntradas = int(input("¿Comprará 1 o 2 entradas? "))
        while cantidadDeEntradas<1 or 2< cantidadDeEntradas:
             cantidadDeEntradas= int(input("Debe comprar entre 1 o 2 entradas")) 
        for compra in range(cantidadDeEntradas):
            print("\t ESCENARIO")
            for imprimir in asientosSinModificar:
                    print(imprimir)
            print("\tEscenario con asientos comprados")
            for imprimir4 in asientosConsiderandoCompra:
                  print(imprimir4)
            selección = int(input("Indique cuál asiento desea comprar "))
            if 0 <= selección < 11:
                    asientosConsiderandoCompra[0][selección-1] = "x"
                    dineroRecaudado = dineroRecaudado + 100000
            if 11 <= selección < 21:
                    asientosConsiderandoCompra[1][selección-11] = "x"
                    dineroRecaudado = dineroRecaudado + 100000
            if 21 <= selección < 31:
                    asientosConsiderandoCompra[2][selección-21] = "x"
                    dineroRecaudado = dineroRecaudado + 50000
            if 31<= selección < 41:
                    asientosConsiderandoCompra[3][selección-31] = "x"
                    dineroRecaudado = dineroRecaudado + 50000
            if 41 <= selección < 51:
                    asientosConsiderandoCompra[4][selección-41] = "x"
                    dineroRecaudado = dineroRecaudado + 50000
            usuario = int(input("Ingrese su rut, sin incluir digito verificador "))
            while 100000 <= usuario <= 9999999:  
                    usuario = int(input("Ingrese un rut válido "))
            rut.append(usuario)
            print("Ha comprado la entrada de manera éxitosa")
    if x==2:
            print("Ha ingresado a la opción de ver puestos disponibles")
            for imprimir2 in asientosConsiderandoCompra:
                print(imprimir2)
    if x==3:
         print("Ha ingresado a la opción de ver los rut registrados")
         for imprimir3 in rut:
              print(imprimir3)
    if x==4:
         print("Ha ingresado a la opción de ver las ganancias totales las cuales son de ", dineroRecaudado, " pesos")
    if x==5:
         print("Ha ingreaso a la opción de salir del programa, hasta la próxima")

volveraMenu = 2

while volveraMenu != 1:
    menu = int(input("Bienvenido al portal para comprar entradas\nIngrese a cuál menú de la operación que desea llevar\n1 Comprar entradas\n2 Mostrar puestos restantes disponibles\n3 Mostrar ruts registrados\n4 Ganancias totales\n5 Salir del programa\n"))
    while menu<1 or 5<menu:
        menu = int(input("Ingrese una opción válida "))
    eleccion1(menu)
    volveraMenu = int(input("Si desea salir marque 1, sino ingrese cualquier número "))
