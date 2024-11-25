from BD.conexion import Conexion
import buscadorEspecifico # Importar el módulo que contiene la función buscarPorDni
def menuPrincipal():
    continuar = True
    while(continuar):
        print("Escuela Privada")
        print("[1]. Ingresar datos")
        print("[2]. Modificar datos")
        print("[3]. Mostrar datos")
        print("[4]. Eliminar datos")
        print("[5]. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion <1 or opcion >5:
            print("Opción incorrecta, ingrese nuevamente")
        elif opcion == 5:
            continuar = False
            print("Saliendo del sistema")
            break
        else:
            ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    if opcion==3:
        print("Que datos desea ver?")
        print("[1]. Buscar por DNI")
    
        #adentro opciones para mostrar alumnos
        print("[2]. Bucar por Nombre")
        #adentro opciones para mostrar alumnos 
        print("[3]. Buscador especifico")
        print("[4]. Volver al menu principal")
        opcion2 = int(input("Seleccione una opción: "))

        if opcion2 == 1:
            comandoSQL = "dni"
            dni = input("Ingrese el DNI: ")
            if len(dni) !=8 or not dni.isdigit():
                while(len(dni) !=8 or not dni.isdigit()):
                    print("El DNI debe contener 8 digitos.")
                    dni = input("Ingrese el DNI: ")
                
            else:
                print("Usuario encontrado con exito.")
                
            buscadorEspecifico.buscarPorDni(dni, comandoSQL)
        elif(opcion2 ==2):
            comandoSQL="nombre"
            dni = input("Ingrese el Nombre: ")
            if(dni.isdigit):
                print("Porfavor solo ingresar caracteres.")
            else:
                print("Usuario encontrado.")
            buscadorEspecifico.buscarPorDni(dni, comandoSQL)
menuPrincipal()