from flask import Flask, render_template, request, redirect, url_for
from config import Config
from datetime import datetime
from models import db,Pelicula # Recuerda adicionar la importación de tu modelo aquí
app = Flask(__name__)
# Carga la configuración de la aplicación
app.config.from_object(Config)

# Inicializa la base de datos
db.init_app(app)

# Crea la base de datos y las tablas
with app.app_context():
    db.create_all()

"""

Aquí puedes agregar las rutas de tu aplicación. Las rutas que deberás crear son:
1. Ruta para mostrar una lista de registros.
2. Ruta para agregar un registro.
3. Ruta para ver un registro existente.
4. Ruta para eliminar un registro.

Como recomendación, puedes usar la ruta raíz ('/') para mostrar la lista de registros. Las demás rutas dependerá de tu comodidad para estructurar tu aplicación.
"""
@app.route('/')
def index():
    peliculas=Pelicula.query.all()
    return render_template('index.html',peliculas=peliculas)

@app.route('/agregar',methods=['GET','POST'])
def agregar():
    if request.method=='POST':
        nombre=request.form['nombre']
        fecha_lanzamiento=datetime.strptime(request.form['fecha_lanzamiento'],'%Y-%m-%d')
        duracion=request.form['duracion']
        genero=request.form['genero']
        director=request.form['director']

        nueva_pelicula=Pelicula(nombre=nombre,fecha_lanzamiento=fecha_lanzamiento,duracion=duracion,genero=genero,director=director)
        
        db.session.add(nueva_pelicula)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('agregar_pelicula.html')



@app.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    pelicula=Pelicula.query.get_or_404(id)
    if request.method=='POST':
        pelicula.nombre=request.form['nombre']
        pelicula.fecha_lanzamiento=datetime.strptime(request.form['fecha_lanzamiento'],'%Y-%m-%d')
        pelicula.duracion=request.form['duracion']
        pelicula.genero=request.form['genero']
        pelicula.director=request.form['director']


        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar_pelicula.html',pelicula=pelicula)




@app.route('/eliminar/<int:id>')
def eliminar(id):
    pelicula=Pelicula.query.get_or_404(id)
    db.session.delete(pelicula)
    db.session.commit()
    return redirect(url_for('index'))


# Levanta la aplicación
if __name__ == '__main__':
    app.run(debug=True)