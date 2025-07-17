import psycopg2
from dotenv import dotenv_values

def get_connection():
    config = dotenv_values('.env')
    conexion = psycopg2.connect(
        user= config.get('DB_USER'),
        password= config.get('DB_PASSWORD'),
        host= config.get('DB_HOST'),
        database= config.get('DB_DATABASE'),
        port= config.get('DB_PORT'),
    )
    return conexion

