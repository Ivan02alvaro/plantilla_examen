import os

base_dir = os.path.dirname(os.path.abspath(__file__))

class Config:
    # Configuración base para la aplicación Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'examen-2025'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False