from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Crea la clase/modelo de tu base de datos
class Pelicula(db.Model):
    __tablename__ ='peliculas'
    id= db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100), nullable=False)
    fecha_lanzamiento=db.Column(db.DateTime,nullable=False)
    duracion=db.Column(db.Integer,nullable=False)
    genero=db.Column(db.String(50),nullable=False)
    director=db.Column(db.String(100),nullable=False)


   