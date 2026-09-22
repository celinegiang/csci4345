# import socket tools
from socket import *

# create a socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# create a message
msg = "hi"

# send the message, using the socket
### send(__msg___, __destination__)
