import socket, threading

AddressList = []
ClientList = []
UsernameList = []

def start():
    print("SERVER HAS STARTED")
    global AddressList, ClientList, UsernameList

    ServerCommandThread = threading.Thread(target = Server_Commands)
    ServerCommandThread.start()

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

def Handle_Users(client, address, chat_username):
    print("Connected to {}".format(address))
    print("Total amount of users connected: {}".format(threading.active_count() - 2))
    msg = ""
    DisconnectMessage = "!disconnect"

    while True:
        msg = client.recv(1024)
        msg = msg.decode()

        if msg != DisconnectMessage:   
            msg = chat_username + ": " + msg 
            print(msg)

            for x in ClientList:
                if x == client:
                    pass
                else:
                    x.send(msg.encode())
                    
        else:

            ClientList.remove(client)
            AddressList.remove(address)
            UsernameList.remove(chat_username)
            client.close()
            break


def Server_Commands():
    ServerSwitch = True

    while ServerSwitch:
        Server_Request = input()
        if Server_Request == "/userlist":
            print("[{}]USERNAME LIST:".format(threading.active_count() - 2))
            for x in UsernameList:
                print(x)
        elif Server_Request == "/addrlist":
            print("CONNECION ADDRESS LIST:")
            for x in AddressList:
                print(x)




if __name__ == "__main__":

    HEADER = 10
    PORT = 5050
    SERVERIP = '192.168.1.7'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVERIP, PORT))
    s.listen()
    start()

