# Importar módulo de flask
from flask import Flask, render_template, redirect, url_for, request
# Importar conexión con la base de datos desde controlador
import controladordb

# Crear una variable para establecer la aplicación desde flask
app = Flask(__name__)




# Ruta principal cuando abro el proyecto de página web con flask
@app.route('/')
def index(rstDB = None):
    if rstDB != None:
        rstDB = "Valor variable rstDB"
    else:
        # conexion = conexion_db()
        # cursor = conexion.cursor()
        # sql = "SELECT * FROM productos"
        # cursor.execute(sql)
        # rstDB = []
        # # rstDB = cursor.fetchone()
        # rstDB = cursor.fetchall()
        # conexion.close()
        # rstDB = "conexion"
        rstDB = controladordb.leer_datos()
    # return "<br> <h1>Hola Tripulantes</h1> <br> <h2>Aprendiendo Flask...</h2>"
    return render_template('index.html',
                            rstDB = rstDB)


@app.route('/registrar_productos')
def registrar_productos():
    return render_template('registrar_productos.html')

@app.route('/guardar_datos', methods = ['GET', 'POST'])
def guardar_datos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        categoria = request.form['categoria']
        precio = request.form['precio']
        rstDB = controladordb.insertar_datos(nombre, cantidad, categoria, precio)
        # return f"<h1>{rstDB}</h1>"
        return render_template('guardar_datos.html',
                                rstDB = rstDB)
    return redirect(url_for('index'))


@app.route('/editar_productos', methods = ['GET', 'POST'])
def editar_productos():
    if request.method == 'POST':
        id = request.form['id']
        rstDB = controladordb.leer_datos_id(id)
        return render_template('editar_productos.html',
                                rstDB = rstDB)
    return redirect(url_for('index'))

@app.route('/actualizar_datos', methods = ['GET', 'POST'])
def actualizar_datos():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        categoria = request.form['categoria']
        precio = request.form['precio']
        rstDB = controladordb.actualizar_datos(id, nombre, cantidad, categoria, precio)
        # return f"<h1>{rstDB}</h1>"
        return render_template('actualizar_datos.html',
                                rstDB = rstDB)
    return redirect(url_for('index'))



@app.route('/confirmar_eliminar_datos', methods = ['GET', 'POST'])
def confirmar_eliminar_datos():
    if request.method == 'POST':
        id = request.form['id']
        rstDB = controladordb.leer_datos_id(id)
        return render_template('confirmar_eliminar_datos.html',
                                rstDB = rstDB)
    return redirect(url_for('index'))



@app.route('/eliminar_datos', methods = ['GET', 'POST'])
def eliminar_datos():
    if request.method == 'POST':
        id = request.form['id']
        rstDB = controladordb.eliminar_datos(id)
        # return f"<h1>{rstDB}</h1>"
        return render_template('eliminar_datos.html',
                                rstDB = rstDB)
    return redirect(url_for('index'))



@app.route('/informacion')
def informacion():
    # return "<br> <h1>Información</h1>  <br> <h2>Aprendiendo ando...</h2>"
    return render_template('informacion.html')

@app.route('/contenido')
def contenido():
    return render_template('contenido.html')

@app.route('/contactenos')
@app.route('/contactenos/<nombre>')
@app.route('/contactenos/<nombre>/<apellido>')
@app.route('/contactenos/<nombre>/<apellido>/<telefono>')
@app.route('/contactenos/<nombre>/<apellido>/<telefono>/<email>')
def contactenos(nombre = None, apellido = None,
                telefono = None, email = None):

    if nombre != None and apellido != None and telefono != None and email != None:
        txtNomb = f"{nombre}"
        txtApel = f"{apellido}"
        txtTel = f"{telefono}"
        txtEmail = f"{email}"

    elif nombre != None and apellido != None and telefono != None:
        txtNomb = f"{nombre}"
        txtApel = f"{apellido}"
        txtTel = f"{telefono}"
        txtEmail = "..."

    elif nombre != None and apellido != None:
        txtNomb = f"{nombre}"
        txtApel = f"{apellido}"
        txtTel = "..."
        txtEmail = "..."

    elif nombre != None:
        txtNomb = f"{nombre}"
        txtApel = "..."
        txtTel = "..."
        txtEmail = "..."
    else:
        txtNomb = "Wilmer"
        txtApel = "Naranjo"
        txtTel = "321 111 1111"
        txtEmail = "wil.itech@gmail.com"
    
    # return f"""
    # <br> 
    # <h1>Información</h1>
    # <br>
    # <p>
    #     Nombre: {txtNomb}<br>
    #     Apellido: {txtApel} <br>
    #     Teléfono: {txtTel} <br>
    #     E-mail: {txtEmail} <br>
    # </p>
    # """
    return render_template('contactenos.html',
                            txtNomb = txtNomb,
                            txtApel = txtApel,
                            txtTel = txtTel,
                            txtEmail = txtEmail)

# Establecer el fichero principal
if __name__ == '__main__':
    app.run(debug=True)
