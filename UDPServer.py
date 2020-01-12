from socket import *
import json

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', serverPort))
print("The server is running")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    # modifiedMessage = message.decode().upper()
    dictionary = {}
    for elem in message.decode():
        if(elem in dictionary):
            dictionary[elem] += 1
        else:
            dictionary[elem] = 1

    print(dictionary)
    serverSocket.sendto(json.dumps(dictionary).encode(), clientAddress)