import socket, threading

AddressList = []
ClientList = []
UsernameList = []

def start():
    print("SERVER HAS STARTED")
    global AddressList, ClientList, UsernameList

    while True:
        client, address = s.accept()
        cUsername = client.recv(1024).decode()

        thread = threading.Thread(target = Handle_Users, args = (client, address, cUsername))
        thread.start()
        AddressList.append(address)
        ClientList.append(client)
        UsernameList.append(cUsername)

        for x in ClientList:
            ServerMessage = "[SERVER] New user connected --> " + cUsername
            x.send(ServerMessage.encode())

## Introduce Username or ID system
## Setup a PM system
        

def Handle_Users(client, address, chat_username):
    print("Connected to {}".format(address))
    print("Total amount of users connected: {}".format(threading.active_count() - 1))
    msg = ""

    while True:
        msg = client.recv(1024)

        if len(msg) > 0:   
            msg = chat_username + ": " + msg.decode() 
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
    s.bind(('192.168.1.7', PORT))
    s.listen()
    start()

