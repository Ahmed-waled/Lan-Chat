# import socket
# import select
# import sys
# from _thread import *
#
# MAX_NUMBER_OF_CLIENTS = 2
# clientsList = []
#
# mainServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mainServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# if len(sys.argv) != 3:
#     print("Not Enough Argument: {targetFile, IP address, Port}")
#     exit()
#
# IP_Address: str = sys.argv[1]
#
# PORT = int(sys.argv[2])
#
# mainServer.bind((IP_Address, PORT))
#
# # set MAX_NO of Clients
# mainServer.listen(MAX_NUMBER_OF_CLIENTS)
#
#
# def clientThread(connection, address):
#     connection.send("Welcome!")
#     message = connection.recv(2048)
#     while True:
#         if message is None:
#             remove(connection)  # client is broken
#             continue
#
#         messageSent = f"<{address[0]}> {message}"
#         # print(messageSent)
#         sendToAll(messageSent)
#
#
# def remove(connection):
#     clientsList.remove(connection)
#
#
# def sendToAll(message):
#     for client in clientsList:
#         client.send(message)
#
#
# def startChat():
#     while True:
#         response = mainServer.accept()  # get new response
#         connection, address = response  # extract both connection and address from connecting user
#         clientsList.append(connection)  # save client
#
#         print("user" + address[0] + " has connected")
#         start_new_thread(clientThread, (connection, address))
#
#     connection.close()
#     mainServer.close()


import socket
import threading

import select
from _thread import *
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
the first argument AF_INET is the address domain of the socket. This is used when we have an Internet Domain
with any two hosts
The second argument is the type of socket. SOCK_STREAM means that data or characters are read in a continuous flow
"""
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))
# binds the server to an entered IP address and at the specified port number. The client must be aware of these
# parameters
server.listen(100)
# listens for 100 active connections. This number can be increased as per convenience
list_of_clients = []


def clientthread(connection, addr):
    # sends a message to the client whose user object is conn
    while True:
        try:
            message = connection.recv(2048).decode()
            if message:
                print(message)
                broadcast(message)
            else:
                remove(connection)
            # prints the message and address of the user who just sent the message on the server terminal
        except:
            continue


def broadcast(message):
    for clients in list_of_clients:
        # if clients != connection:
        try:
            clients[0].send(message.encode())
        except:
            clients[0].close()
            remove(clients)


def remove(connection):
    if connection in list_of_clients:
        print(f"user {connection[1]} has disconnected")
        list_of_clients.remove(connection)


while True:
    connection, addr = server.accept()
    """
    Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
    the IP address of the client that just connected
    """
    connection.send("Welcome to this chatroom!".encode())

    username = connection.recv(2048)

    list_of_clients.append((connection, username))

    print(f"<{username.decode()}>" + " connected")

    # maintains a list of clients for ease of broadcasting a message to all available people in the chatroom
    # Prints the address of the person who just connected
    # start_new_thread(clientthread, (conn, addr))
    ClientThread = threading.Thread(target=clientthread, args=(connection, addr))
    ClientThread.start()
    # creates and individual thread for every user that connects

# conn.close()
# server.close()
