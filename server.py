import socket
import threading
import sys

MAX_NUMBER_OF_CLIENTS = 2
clientsList = []

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set socket options to allow reusing the address
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Check if command-line arguments are provided correctly
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

# Get IP address and port number from command-line arguments
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

# Bind the socket to the specified IP address and port number
server.bind((IP_address, Port))

# Listen for incoming connections
server.listen(MAX_NUMBER_OF_CLIENTS)

# Define a function to handle communication with each client
def clientSide(connection, addr):
    # Receive and broadcast messages to/from the client
    while True:
        try:
            message = connection.recv(2048).decode()
            if message:
                print(message)
                broadcast(message)
            else:
                remove(connection)
        except:
            continue

# Define a function to broadcast messages to all clients
def broadcast(message):
    for clients in clientsList:
        try:
            clients[0].send(message.encode())
        except:
            clients[0].close()
            remove(clients)

# Define a function to remove disconnected clients
def remove(connection):
    if connection in clientsList:
        print(f"user {connection[1]} has disconnected")
        clientsList.remove(connection)

# Main loop to accept incoming client connections
while True:
    # Accept incoming connection
    connection, addr = server.accept()

    # Send welcome message to the client
    connection.send("Welcome to this chatroom!".encode())

    # Receive username from the client
    username = connection.recv(2048)

    # Add the client to the list of clients
    clientsList.append((connection, username))

    # Print a message indicating that the client has connected
    print(f"<{username.decode()}>" + " connected")

    # Create a new thread to handle communication with the client
    clientSide = threading.Thread(target=clientSide, args=(connection, addr))
    clientSide.start()
