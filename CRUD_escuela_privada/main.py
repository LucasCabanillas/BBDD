from BD.conexion import Conexion
import funciones # Importar el módulo que contiene la función buscarPorDni
import os #Libreria con comandos del sistema
def menuPrincipal():
    # Limpiar la consola
    os.system("cls")
    continuar = True
    while(continuar):
        
        print("Escuela Privada")
        print("[1]. Ingresar datos")
        print("[2]. Modificar datos")
        print("[3]. Mostrar datos alumnos")
        print("[4]. Mostrar datos profesores")
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
    #Menu mostrar alumnos
    if opcion==3:
        # Limpiar la consola
        os.system("cls")
        print("Que datos desea ver?")
        print("[1]. Buscar por legajo")
        print("[2]. Buscar por DNI")
        #adentro opciones para mostrar alumnos
        print("[3]. Buscar por Nombre")
        #adentro opciones para mostrar alumnos 
        print("[4]. buscar por apellido")
        print("[5]. Buscar por genero")
        print("[6]. Volver al menu principal")
        opcion2 = int(input("Seleccione una opción: "))

        if(opcion2 ==1):
            comandoSQL = "legajo"
            dato= input("Ingresar legajo: ")
            #Legajo alumno
            if len(dato) !=5 or not dato.isdigit():
                while(len(dato) !=5 or not dato.isdigit()):
                    print("El legajo debe contener 5 digitos.")
                    dato = input("Ingrese el legajo: ")
            funciones.buscarEspecifico(dato, comandoSQL)

        #DNI alumno
        elif opcion2 == 2:
            comandoSQL = "dni"
            dato = input("Ingrese el DNI: ")
            if len(dato) !=8 or not dato.isdigit():
                while(len(dato) !=8 or not dato.isdigit()):
                    print("El DNI debe contener 8 digitos.")
                    dato = input("Ingrese el DNI: ")
            funciones.buscarEspecifico(dato, comandoSQL)

        #Nombre alumno
        elif(opcion2 ==3):
            comandoSQL="nombre"
            dato = input("Ingrese el nombre: ")
            if(dato.isdigit()):
                print("Porfavor solo ingresar caracteres.")
            funciones.buscarEspecifico(dato.title(), comandoSQL)

        #Apellido alumno
        elif(opcion2 ==4):
            comandoSQL = "apellido"
            dato= input("Ingresar apellido: ")
            if(dato.isdigit()):
                print("Porfavor solo ingresar caracteres.")
            funciones.buscarEspecifico(dato.title(), comandoSQL)

        #Genero alumno
        if(opcion2 ==5):
            comandoSQL = "genero"
            dato= input("Ingresar genero (masculino, femenino, etc): ")
            if(dato.isdigit()):
                print("Porfavor solo ingresar caracteres.")
            funciones.buscarEspecifico(dato.title(), comandoSQL)
    
    #Menu Buscar Profesor
    if(opcion == 4):
        # Limpiar la consola
        os.system("cls")
        print("Que datos desea ver?")
        print("[1]. Buscar por legajo")
        print("[2]. Buscar por DNI")
        #adentro opciones para mostrar alumnos
        print("[3]. Buscar por Nombre")
        #adentro opciones para mostrar alumnos 
        print("[4]. buscar por apellido")
        print("[5]. Buscar por matricula")
        print("[6]. Volver al menu principal")
        opcion2 = int(input("Seleccione una opción: "))

        #Legajo profesor
        if(opcion2 == 1):
            comandoSQL = "idProfesor"
            dato = input ("Ingresar legajo: ")
            while(not dato.isdigit()):
                print("porfavor solo ingresar numeros")
                dato = input ("Ingresar legajo: ")
            funciones.buscarEspecificoProfesor(dato, comandoSQL)
                

        #DNI profesor
        elif(opcion2 == 2):
            comandoSQL = "dni"
            dato = input("Ingresar DNI: ")
            if  len(dato) !=8 or not dato.isdigit():
                while(len(dato) !=8 or not dato.isdigit()):
                    print("El legajo debe contener 8 digitos.")
                    dato = input("Ingrese el legajo: ")
            funciones.buscarEspecificoProfesor(dato, comandoSQL)

        #Nombre profesor
        elif(opcion2 == 3):
            comandoSQL = "nombre"
            dato = input("Ingresar nombre: ")
            if(dato.isdigit()):
                print("Porfavor solo ingresar caracteres.")
            funciones.buscarEspecifico(dato.title(), comandoSQL)

        #Apellido profesor
        elif(opcion2 == 4):
            comandoSQL = "apellido"
            dato = input("Ingresar apellido")
            if(dato.isdigit()):
                print("Porfavor solo ingresar caracteres.")
            funciones.buscarEspecifico(dato.title(), comandoSQL)
        
        #Matricula profesor
        elif(opcion2 == 5):
        #INVESTIGAR
        #INVESTIGAR
            pass
menuPrincipal()