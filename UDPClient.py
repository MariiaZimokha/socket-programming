from socket import *
serverName = '127.0.0.1'
serverPort = 12000
# AF_INET - IPv4 address
# SOCK_DGRAM - UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input a sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
# recvfrom - receive data from the socket
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()