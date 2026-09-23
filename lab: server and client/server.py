# import socket tools
from socket import *

# create a socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# make this socket bound to a port 
serverSocket.bind(('0.0.0.0', 12345))

# TASK 1: give your server any custom behavior
def process(msg):
    return msg.upper()

while True:
    # receive a message
    msg, clientAddr = serverSocket.recvfrom(2048)
    msg = msg.decode()

    # print the message
    print(msg)

    if msg == 'exit':
        break

    # TASK 1
    reply = process(msg)

    # TASK 2A: send the response back to the client
    serverSocket.sendto(reply.encode(), clientAddr)