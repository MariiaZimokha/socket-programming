# socket-programming

### TCP
Before the client and server can start to send data to each other, they first need to handshake and establish a TCP connection. One end of the TCP connection is attached to the client socket and the other end is attached to a server socket. When creating the TCP connection, we associate with it the client socket address (IP address and port number) and the server socket address (IP address and port number).

With the server process running, the client process can initiate a TCP connection to the server. This is done in the client program by creating a TCP socket. When the client creates its TCP socket, it specifies the address of the welcoming socket in the server, namely, the IP address of the server host and the port number of the socket. After creating its socket, the client initiates a three-way handshake and establishes a TCP connection with the server.
During the three-way handshake, the client process knocks on the welcoming door of the server process. When the server “hears” the knocking, it creates a new socket that is dedicated to that particular client. 

![TCP-server-has-2-sockets](/assets/TCP-server-has-2-sockets.png?raw=true)


Simple application:
The client sends one line of data to the server, the server capitalizes the line and sends it back to the client. 

![TCP](/assets/TCP.png?raw=true)

Image above highlights the main socket-related activity of the client and server that communicate over the TCP transport service.


### UDP

Before the sending process can push a packet of data out the socket door, when using UDP, it must first attach a destination address to the packet. After the packet passes through the sender’s socket, the Internet will use this destination address to route the packet through the Internet to the socket in the receiving process.

![UDP](/assets/UDP.png?raw=true)

Image above highlights the main socket-related activity of the client and server that communicate over the UDP transport service.