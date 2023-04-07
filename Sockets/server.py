# Importacion de las librerias requeridas

import socket
import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "1834df",
    database = "sistemas_distribuidos_db"
)


# Instanciacion de un objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Puerto de conexion
port = 5100

# Uso de la primitiva bind
s.bind(('', port))
print("Socket conectado a %s" %(port))

# Uso de la primitiva listen
s.listen(5)
print("Socket escuchando")

c, addr = s.accept()
print("Conexion desde la direccion: ", addr)
    
# Conexion con el cliente
while True:

    data = c.recv(1024).decode() 
    
    mycursor = db.cursor()

    sql = "SELECT personas.dir_tel, personas.dir_nombre, personas.dir_direccion, ciudades.ciud_nombre FROM personas INNER JOIN ciudades ON personas.dir_ciud_id = ciudades.ciud_id WHERE personas.dir_tel = %s"

    mycursor.execute(sql, (data, ))

    results = mycursor.fetchall()

    if mycursor.rowcount == 0:
        c.send(str("Persona dueña de ese número telefónico no existe").encode())
        break
        
    for result in results:
        print(result) 
    
    c.send(str(result).encode())
    
   

