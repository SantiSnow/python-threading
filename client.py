# cliente que se conecta al socket anterior

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(('127.0.0.1', 55555))

recibido = socket.recv(2048)

print(recibido.decode())
