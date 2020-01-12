from socket import *
serverName = '127.0.0.1'
serverPort = 12000
# AF_INET - IPv4 address
# SOCK_STREAM - TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# initiate TCP connection between client and server.
# After .connect is executed, the three-way handshake is performed
# and TCP connection is established 
clientSocket.connect((serverName, serverPort))

sentence = raw_input('Input a sentence: ')
clientSocket.send(sentence.encode())
modifiedSentance = clientSocket.recv(1024)
print('From server: ', modifiedSentance.decode())
clientSocket.close()