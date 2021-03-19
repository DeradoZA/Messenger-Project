import socket, threading

def MessageReceiver():

    while True:
        ServerMsg = s.recv(1024)
        print(ServerMsg.decode())

def MessageSender():
    while True:
        message = input()

        if message == "!disconnect":
            print("Thanks for connecting!")
            s.close()
            break
        else:
            s.send(message.encode())

if __name__ == "__main__":

    HEADER = 10
    PORT = 5050
    SERVERIP = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVERIP, PORT))

    SendThread = threading.Thread(target = MessageSender)
    ReceiveThread = threading.Thread(target = MessageReceiver)
    ReceiveThread.setDaemon(True)

    SendThread.start()
    ReceiveThread.start()



    