import socket, threading, sys

def start():
    print("SERVER HAS STARTED")
    while True:
        client, address = s.accept()

        thread = threading.Thread(target = Handle_Users, args = (client, address))
        thread.start()

def Handle_Users(client, address):
    print("Connected to {}".format(address))
    print("Total amount of users connected: {}".format(threading.active_count() - 1))
    msg = ""

    while True:
        msg = client.recv(1024)

        if len(msg) > 0:    
            print(msg.decode())
        else:
            client.close()
            break


if __name__ == "__main__":

    HEADER = 10
    PORT = 5050
    SERVERIP = socket.gethostbyname(socket.gethostname())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVERIP, PORT))
    s.listen()
    start()

