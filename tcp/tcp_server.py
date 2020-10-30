from socket import * 
from math import ceil
import os
from time import time,sleep
import sys


serverPort = 12345      # Server IP(localhost)
BUFSIZE = 1024          # Buffer size     
HOST = ""               

ADDRESS = (HOST,serverPort)




#Creating the socket object
serverSocket = socket(AF_INET,SOCK_STREAM)

# uncomment the next line to disable Nagle's algorithm 
# serverSocket.setsockopt(IPPROTO_TCP, TCP_NODELAY, True)

# uncomment the next line to disable Delayed ACK  
# serverSocket.setsockopt(IPPROTO_TCP, TCP_QUICKACK, True)

#Binding to socket
serverSocket.bind(ADDRESS)

#Starting TCP listener
serverSocket.listen(1)

while True:
    
    print("Listening ...")
    #Starting the connection 
    clientSocket,ADDRESS = serverSocket.accept()
    start = time()  #starting the timer
    print("Connected")
    # Receiving filename from the client
    file_name = clientSocket.recv(2048).decode()
    f = open(file_name, "rb")
    chunk = f.read(BUFSIZE)
    # print(ADDRESS)
    while(chunk):
        clientSocket.send(chunk)   # Sending the chunk to the client
        chunk = f.read(BUFSIZE)    # Reading the file in chunks 
        # Uncomment the next line to add a sleep of 100 us to the server after every packet trasfer
        # sleep(100/1000000)
    f.close() 
    print("successfully sent the file, closing the connection")

    clientSocket.close()
    end = time ()
    print("Time Elapsed : {} seconds".format (end - start))