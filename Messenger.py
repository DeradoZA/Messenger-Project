import socket, sys

if __name__ == "__main__":

    HEADER = 10
    PORT = 5050
    SERVERIP = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVERIP, PORT))
    message = ""

    while True:
        message = input()

        if message == "!disconnect":
            print("Thanks for connecting!")
            s.close()
            break
        else:
            s.send(message.encode())

    