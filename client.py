import socket
import threading
import sys

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Check if command-line arguments are provided correctly
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

# Get IP address and port number from command-line arguments
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

# Connect to the server using the specified IP address and port number
server.connect((IP_address, Port))

# Get username from the user
username = input("Enter your username: ")

# Send the username to the server
server.send(username.encode())


# Define a function to handle receiving messages from the server
def ResponseMessage():
    while True:
        # Receive and print messages from the server
        message = server.recv(2048).decode()
        if message:
            print(message)


# Define a function to handle sending messages to the server
def SendMessage():
    while True:
        try:
            # Get user input and send it to the server
            message = "<" + username + "> : " + input()
            server.send(message.encode())

        except:
            # Handle exceptions such as disconnection
            message = f"{username}" + " disconnected!!"
            server.send(message.encode())


# Create and start threads for sending and receiving messages
sendThread = threading.Thread(target=SendMessage)
responseThread = threading.Thread(target=ResponseMessage)
sendThread.start()
responseThread.start()
