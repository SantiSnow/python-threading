import threading
import time

x = 40000
# lock se encarga de bloquear un recurso, en este caso x, para que no pueda ser accesible desde otro lugar
lock = threading.Lock()


# con la funcion acquire(), nos encargamos de ver si el recurso esta disponible y bloquearlo para otros
# con la funcion release(), lo liberamos
def mitad():
    global x, lock
    lock.acquire()
    while x < 800000:
        x *= 2
        print(x)
        time.sleep(3)
    print("El numero ha llegado al maximo y el recurso esta libre")
    lock.release()


def doble():
    global x, lock
    lock.acquire()
    while x > 2000:
        x = x / 2
        print(x)
        time.sleep(3)
    print("El numero ha llegado al minimo y el recurso esta libre")
    lock.release()


thread1 = threading.Thread(target=mitad)
thread2 = threading.Thread(target=doble)

thread1.start()
thread2.start()

