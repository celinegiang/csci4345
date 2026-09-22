# import socket tools
from socket import *

# create a socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    # create a message
    msg = input()

    # send the message, using the socket
    ### send(__msg___, __destination__)
    dest = ('127.0.0.1', 12345)
    # encode the message into bytes
    msg = msg.encode()
    clientSocket.sendto(msg, dest)

    if msg.decode() == 'exit':
        break
