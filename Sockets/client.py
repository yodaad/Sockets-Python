# Importacion de las librerias requeridas

import socket


# Instanciacion de un objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Puerto de conexion
port = 5100

# Conexion con el servidor
s.connect(('127.0.0.1', port))

i = 0

while i < 3:

    request = input("Ingrese el numero telefonico a consultar: ")
    s.send(request.encode())

    # Recibir data del servidor y decodificarla
    print(s.recv(1024).decode())
    
    i =+ 1

