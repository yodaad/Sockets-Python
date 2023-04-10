# Importacion de las librerias requeridas

import socket


# Instanciacion de un objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Puerto de conexion
port = 5100

# Conexion con el servidor
s.connect(('192.168.80.19', port))

i = 0

while i < 3:

    request = input(f"Ingrese el numero telefonico {i + 1} a consultar: ")
    s.send(request.encode())

    # Recibir data del servidor y decodificarla
    print(f"Informacion del {request}: ",s.recv(1024).decode())
    
    i += 1

s.close()

