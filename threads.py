import threading


def pruebas():
    for x in range(1000):
        print("El programa esta comenzando")


def backgroundwork():
    for x in range(1000):
        print("El programa esta trabajando aun.")


def mastrabajo():
    for x in range(1000):
        print("El programa esta funcionando correctamente")


def finprograma():
    print("El programa finalizo sin ninguno error")


# comienzo del hilo de ejecucion creando un nuevo objeto Thread

thread1 = threading.Thread(target=pruebas)
thread2 = threading.Thread(target=backgroundwork)
thread3 = threading.Thread(target=mastrabajo)

# los hilos de ejecucion comienzan y se ejecutan en paralelo
thread1.start()
thread2.start()
thread3.start()

# la funcion join se encarga de que lo que le sigue, no se ejecute hasta que el hilo halla finalizado
thread1.join()
thread2.join()
thread3.join()

# en este caso, esta funcion se ejecuta solamente cuando los 3 hilos se ha terminado de ejecutar
finprograma()
