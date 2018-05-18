#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


print "This is the TCPServer"

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
clientNumber =0;
while True:
    clientNumber = clientNumber + 1
    print "\nReady to serve#" + repr(clientNumber) + " Client\n" 
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(('----- Message Received from the TCPClient:', sentence)) 
    capitalizedSentence = sentence.upper()
    print(('+++++++ Message processed by the server:', capitalizedSentence))
    connectionSocket.send( capitalizedSentence.encode())
    print(('+++++++ After sending out the capitalizedSentence of ',))
    capitalizedSentence.decode()
    print "TCPServer is closing the connectionSocket"
    connectionSocket.close()
    print "TCP closed the ConnectionSocket" 
