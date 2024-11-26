from BD.conexion import Conexion
import os

def buscarEspecificoProfesor(dato, comandoSQL):
    conexion_instacia = Conexion() #Creo una instancia de la conexión
    conexion = conexion_instacia.conexionBD() #Crear una instancia de la conexión

    # si conoxios es vacio o nada entra a la validacion
    if (conexion is None):
        print("Error: No se pudo establecer conexión con la base de datos.")
        return
    
    #Utilizamos un manejo de ecepciones
    try:
        cursor = conexion.cursor() #Creo el cursor
        #instruccion sql
        query = f"SELECT idProfesor, nombre, apellido, telefono, email, dni, matricula, direccion, horas, sueldo FROM escuela_privada.profesores WHERE {comandoSQL}= %s"# f-strings permite insertar los valores de las variables dentro de la cadena directamente, de forma legible.
        cursor.execute(query, (dato,)) # Ejecutar la consulta con el parámetro seguro (con tuplas(no mificables) y no como caracteres)
        resultados = cursor.fetchall()

        if(resultados):#Mustro el encontrado
            # Limpiar la consola
            os.system("cls")
            print("Datos encontrados.")
            for idProfesor, nombre, apellido, telefono, email, dni, matricula, direccion, horas, sueldo in resultados:
                print(f"Legajo: {idProfesor}, Nombre: {nombre}, Apellido: {apellido}, DNI: {dni}, Matricula: {matricula}, Telefono: {telefono}, Email: {email}, Direccion: {direccion}, Horas: {horas}, Sueldo: {sueldo}") 
        else:
            # Limpiar la consola
            os.system("cls")
            print(f"No se encontraron registros con: {dato}")
            
    except Exception as e:
        print(f"Ocurrió un error durante la consulta: {e}")
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión



def buscarEspecifico(dato, comandoSQL):
    conexion_instancia = Conexion()  #Creo una instancia de la conexión
    conexion = conexion_instancia.conexionBD() #Obtengo la conexión a la base de datos

    # si conoxios es vacio o nada entra a la validacion
    if (conexion is None):
        print("Error: No se pudo establecer conexión con la base de datos.")
        return
    
    #Utilizamos un manejo de ecepciones
    try:
        print(dato)
        cursor = conexion.cursor()  # Crear un cursor
        query = f"SELECT legajo, nombre, apellido, email, direccion FROM escuela_privada.alumnos WHERE {comandoSQL} = %s"
        cursor.execute(query, (dato,))  # Ejecutar la consulta con el parámetro seguro (con tuplas y no como caracteres)
        resultados = cursor.fetchall()  # Obtener todos los registros encontrados tuplas


        if resultados:
            # Limpiar la consola
            os.system("cls")
            print("Datos encontrados:")
            for legajo, nombre, apellido, email, direccion in resultados:
                print(f"Legajo: {legajo}, Nombre: {nombre}, Apellido: {apellido}, Email: {email}, Direccion: {direccion}")# f-strings permite insertar los valores de las variables dentro de la cadena directamente, de forma legible.
        else:
            # Limpiar la consola
            os.system("cls")
            print(f"No se encontraron registros con: {dato}")
        
    except Exception as e:
        print(f"Ocurrió un error durante la consulta: {e}")
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión