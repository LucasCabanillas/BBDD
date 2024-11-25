from BD.conexion import Conexion

def buscarPorDni(dni, comandoSQL):
    conexion_instancia = Conexion()  # Crear una instancia de la conexión
    conexion = conexion_instancia.conexionBD() # Obtener la conexión a la base de datos
    
    if conexion is None:
        print("Error: No se pudo establecer conexión con la base de datos.")
        return
    try:
        cursor = conexion.cursor()  # Crear un cursor
        query = f"SELECT legajo, nombre, apellido, email, direccion FROM escuela_privada.alumnos WHERE {comandoSQL} = %s"
        cursor.execute(query, (dni,))  # Ejecutar la consulta con el parámetro seguro (con tuplas y no como caracteres)
        resultados = cursor.fetchall()  # Obtener todos los registros encontrados tuplas


        if resultados:
            print("Resultados encontrados:")
            for legajo, nombre, apellido, email, direccion in resultados:
                print(f"Legajo: {legajo}, Nombre: {nombre}, Apellido: {apellido}, Email: {email}, Direccion: {direccion}")# f-strings permite insertar los valores de las variables dentro de la cadena directamente, de forma legible.
        else:
            print(f"No se encontraron registros con el DNI: {dni}")
        
    except Exception as e:
        print(f"Ocurrió un error durante la consulta: {e}")
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión





