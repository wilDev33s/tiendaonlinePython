# Importar el módulo PyMySQL
import pymysql

def conexion_db():
    # Datos Conexión base datos
    HOST = "localhost"
    PORT = 3306
    USER = "misiontic_uis"
    PSW = "misiontic.uis"
    DB = "db_tiendaonline"

    conexion = pymysql.connect(host=HOST,
                                port=PORT,
                                user=USER,
                                passwd=PSW,
                                db=DB)

    return conexion