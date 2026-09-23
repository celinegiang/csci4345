# import socket tools
from socket import *

# create a socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    # create a message
    msg = input()

    # send the message, using the socket
    ### send(__msg___, __destination__)
    dest = ('192.168.4.41', 12345)
    # encode the message into bytes
    msg = msg.encode()
    clientSocket.sendto(msg, dest)

    if msg.decode() == 'exit':
        break

    # TASK 2B: receive a response from server
    reply, serverAddr = clientSocket.recvfrom(2048)
    print(reply.decode())