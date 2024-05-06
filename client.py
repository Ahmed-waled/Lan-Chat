import socket
import threading
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

server.connect((IP_address, Port))

username = input("enter your username: ")

server.send(username.encode())


def ResponseMessage():
    while True:
        message = server.recv(2048).decode()
        if message:
            print(message)


def SendMessage():
    while True:
        try:
            message = "<" + username + "> : " + input()
            server.send(message.encode())

        except:
            message = f"{username}" + " disconnected!!"
            server.send(message.encode())


# while True:
sendThread = threading.Thread(target=SendMessage)
responseThread = threading.Thread(target=ResponseMessage)
sendThread.start()
responseThread.start()
