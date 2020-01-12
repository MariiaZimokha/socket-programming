from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
# .listen(1) - the number specifies the max number of connections
serverSocket.listen(1)
print('server is running')

while True:
    # accept() - creates a new socket in the server, 
    # dedicated to this particular client
    # The client and server then complete the handshaking, 
    # creating a TCP connection between the client and the server
    connectionSoket, addr = serverSocket.accept()
    sentence = connectionSoket.recv(1024).decode()
    connectionSoket.send(sentence.upper().encode())
    connectionSoket.close()
