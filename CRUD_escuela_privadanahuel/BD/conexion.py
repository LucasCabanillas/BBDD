import mysql.connector
#importo la libreria error desde la libreria mysql.connector
from mysql.connector import Error

class Conexion():
    # #constructor
    @staticmethod #método estático  no requiere acceso a ninguna instancia de la clase ni a sus atributos o métodos
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