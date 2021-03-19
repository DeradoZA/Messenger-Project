import socket, threading

AddressList = []
ClientList = []

def start():
    print("SERVER HAS STARTED")
    global AddressList, ClientList
    while True:
        client, address = s.accept()

        thread = threading.Thread(target = Handle_Users, args = (client, address))
        thread.start()
        AddressList.append(address)
        ClientList.append(client)

        for x in ClientList:
            ServerMessage = "[SERVER] New user connected --> " + address[0]
            x.send(ServerMessage.encode())

## Introduce Username or ID system
## Setup a PM system
        

def Handle_Users(client, address):
    print("Connected to {}".format(address))
    print("Total amount of users connected: {}".format(threading.active_count() - 1))
    msg = ""

    while True:
        msg = client.recv(1024)

        if len(msg) > 0:   
            msg = address[0] + ": " + msg.decode() 
            print(msg)

            for x in ClientList:
                if x == client:
                    pass
                else:
                    x.send(msg.encode())
                    
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

