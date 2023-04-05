# Importacion de las librerias requeridas

import socket


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

# Conexion con el cliente
while True:
    
    c, addr = s.accept()
    print("Conexion desde ", addr)
    
    c.send("Gracias por conectarse".encode())
    
    c.close()
    
    break

