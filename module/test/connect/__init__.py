from time import sleep
from random import randint
def connect():
    connection_time = randint(4, 50)
    connected = "Connected"
    cannot_connect = "Can't connect"
    sleep(connection_time)
    if connection_time >= 25:
        print(f"Result: {cannot_connect}")
    else:
        print(f"Result: {connected}")
