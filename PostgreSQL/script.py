import psycopg2


HOST = "localhost"
DATABASE = "postgres"
USER = "postgres"
PASSWORD = "*******"

try:
    conexion = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
    )
    print("Conexión exitosa a PostgreSQL")

except Exception as e:
    print("Error al conectar:", repr(e)) 


cursor = conexion.cursor()

# Valores del usuario
nombre = "Santiago Peñarredonda"
correo = "santiago.pena@gmail.com"

# Insertar 
insert_query = "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s);"
cursor.execute(insert_query, (nombre, correo))
conexion.commit()


# Modificar 
nuevo_correo_modificado = "santi.silva@yahoo.com"
insert_query = " UPDATE usuarios SET correo = %s WHERE id = %s"
cursor.execute(insert_query, (nuevo_correo_modificado, 4))
conexion.commit()
print("Usuario actualizado")


# Select usuarios para validar información
cursor.execute("SELECT id, nombre, correo, fecha_registro FROM usuarios;")
#devuelve todos los usuarios
usuarios = cursor.fetchall()

print("Usuarios en la BD:")
for usuario in usuarios:
    print(usuario)

# Cierre de conexión
cursor.close()
conexion.close()