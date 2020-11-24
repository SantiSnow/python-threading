# sockets : un punto de una comunicacion "endpoints"

import socket

# AF_INET es un socket de comunicacion de internet, SOCK_STREAM indica modelo tdp
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ahora le pasamos una tupla al metodo bind, con el host y un puerto y luego lo ponemos a la escucha
socket1.bind(('127.0.0.1', 55555))
socket1.listen()

while True:
    client, address = socket1.accept()
    print("El servido se encuentra corriendo correctamente")
    print("Conectado a {}".format(address))
    client.send("Se ha conectado correctamente!".encode())
    client.close()

