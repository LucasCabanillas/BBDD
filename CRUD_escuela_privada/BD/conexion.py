import mysql.connector
#importo la libreria error desde la libreria mysql.connector
from mysql.connector import Error

class Conexion():
    # #constructor
    # @staticmethod
        
    # def conexionBD():
    #     config = {
    #     'host': 'localhost',
    #     'user': 'root',
    #     'password': 'root',
    #     'database': 'escuela_privada'
    #     }
    #     try:
    #         # Crear la conexión
    #         conexion = mysql.connector.connect(**config)
    #         print("Conexión exitosa")

    #         # Crear un cursor para ejecutar consultas
    #         cursor = conexion.cursor()

    #         # Prueba de consulta
    #         cursor.execute("SHOW TABLES")
    #         for tabla in cursor:
    #             print(tabla)

    #     except mysql.connector.Error as e:
    #         print(f"Error al conectar a MySQL: {e}")
    #     finally:
    #         if 'conexion' in locals() and conexion.is_connected():
    #             #cursor.close()
    #             #conexion.close()
    #             print("Conexión ABIERTA") 
    # conexionBD()

    # Método para conectarse a la base de datos
    @staticmethod

    def conexionBD():
        try:
            # Establecer la conexión
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="escuela_privada",
                port=3306
            )
            return conexion  # Devuelve la conexión si es exitosa
        except Error as ex:
            # Imprime el error si ocurre
            print("Error al intentar la conexión: {0}".format(ex))
            return None