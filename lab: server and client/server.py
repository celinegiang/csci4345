# import socket tools
from socket import *

# create a socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# make this socket bound to a port 
serverSocket.bind(('127.0.0.1', 12345))

# receive a message
msg = serverSocket.recvfrom(2048)

# print the message
print(msg)
