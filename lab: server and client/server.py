# import socket tools
from socket import *

# create a socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# make this socket bound to a port 
serverSocket.bind(('172.28.173.21', 12345))

# TASK 1: give your server any custom behavior

# TASK 2A: send a response back to the client

while True:
    # receive a message
    msg = serverSocket.recvfrom(2048)

    # print the message
    print(msg.decode())

    if msg.decode() == 'exit':
        break
