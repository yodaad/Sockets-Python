# Importacion de las librerias requeridas

import socket
import mysql.connector
import sys
import errno

#Valores para conectarse a la BD

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

# Uso del metodo bind
s.bind(('', port))
print("Socket conectado al puerto %s" %(port))

# Uso del metodo listen
s.listen(5)
print("Socket server escuchando")


while True:
    
    # Uso del metodo accept
    c, addr = s.accept()
    print("Se ha creado una conexion desde la direccion: ", addr)
        
    # Conexion con el cliente
    while True:

        data = c.recv(1024).decode() 
        
        mycursor = db.cursor()

        sql = "SELECT personas.dir_tel, personas.dir_nombre, personas.dir_direccion, ciudades.ciud_nombre FROM personas INNER JOIN ciudades ON personas.dir_ciud_id = ciudades.ciud_id WHERE personas.dir_tel = %s"

        mycursor.execute(sql, (data, ))

        results = mycursor.fetchall()

        try: 
            if mycursor.rowcount == 0:
                c.send(str("Persona dueña de ese número telefónico no existe").encode())            
            else:
                c.send(str(results).encode())
        except IOError as e:
            if e.errno == errno.EPIPE:
                break
       
        
    print("Socket server aun escuchando")





   

