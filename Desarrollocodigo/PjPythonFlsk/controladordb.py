# Importar conexión a la base de datos
from conexiondb import conexion_db

# CRUD => Create - Read - Update - Delete

# Create =>
def insertar_datos(nombre, cantidad, categoria, precio):
    conexion = conexion_db()
    with conexion.cursor() as cursor:
        # sql = "INSERT INTO productos37(id, nombre, cantidad, categoria, precio) VALUES(NULL, 'Aceite', 60, 'Víveres', 6000)"
        sql = f"INSERT INTO productos37(id, nombre, cantidad, categoria, precio) VALUES(NULL, '{nombre}', {cantidad}, '{categoria}', {precio})"
        cursor.execute(sql)
        conexion.commit()
    conexion.close()
    return "Datos guardados..."

# Read =>
def leer_datos():
    conexion = conexion_db()
    rstDB = []
    # cursor = conexion.cursor()
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM productos37"
        # sql = "SELECT * FROM productos"
        cursor.execute(sql)
        # rstDB = []
        # rstDB = cursor.fetchone()
        rstDB = cursor.fetchall()
    conexion.close()
    return rstDB


# lee únicamente los datos respecto a un id
def leer_datos_id(id):
    conexion = conexion_db()
    rstDB = []
    # cursor = conexion.cursor()
    with conexion.cursor() as cursor:
        sql = f"SELECT * FROM productos37 WHERE id = {id}"
        # sql = "SELECT * FROM productos37"
        # sql = "SELECT * FROM productos"
        cursor.execute(sql)
        # rstDB = []
        rstDB = cursor.fetchone()
        # rstDB = cursor.fetchall()
    conexion.close()
    return rstDB



# Update =>
def actualizar_datos(id, nombre, cantidad, categoria, precio):
    conexion = conexion_db()
    with conexion.cursor() as cursor:
        # sql = "UPDATE productos37 SET nombre = 'Jabón', cantidad = 120, categoria = 'Aseo', precio = 3000 WHERE id = 7"
        sql = f"UPDATE productos37 SET nombre = '{nombre}', cantidad = {cantidad}, categoria = '{categoria}', precio = {precio} WHERE id = {id}"
        cursor.execute(sql)
        conexion.commit()
    conexion.close()
    return "Datos actualizados..."



# Delete =>
def  eliminar_datos(id):
    conexion = conexion_db()
    with conexion.cursor() as cursor:
        # sql = "DELETE FROM productos37 WHERE id = 9"
        sql = f"DELETE FROM productos37 WHERE id = {id}"
        cursor.execute(sql)
        conexion.commit()
    conexion.close()
    return "Datos eliminados..."




