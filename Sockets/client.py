# Importacion de las librerias requeridas

import socket


# Instanciacion de un objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Puerto de conexion
port = 5100

# Conexion con el servidor
s.connect(('192.168.80.19', port))

# Recibir data del servidor y decodificarla
print(s.recv(1024).decode())

s.close()