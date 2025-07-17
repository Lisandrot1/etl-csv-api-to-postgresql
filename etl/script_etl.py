
from db.conexion import get_connection
conexion = get_connection()



try:
    with conexion: 
        with conexion.cursor() as cursor:
            cursor.execute('show tables')
            datos = cursor.fetchall()
            print(datos)
except Exception as e:
    print(f'Ocurrio algo {e}')
finally:
    conexion.close()