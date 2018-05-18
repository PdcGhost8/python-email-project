print "This is the TCPClient"
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

sentence = raw_input('Input lowercase sentence:')
print('----- hello there', sentence)
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('your message has been received', modifiedSentence.decode())

print "Client is closing the Socket"
clientSocket.close()
print "Socket is closed have a nice day"

