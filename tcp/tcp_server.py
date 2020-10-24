from socket import * 
from math import ceil
import os
from time import time
import sys

if(len(sys.argv) != 3):
    print("Enter 2 arguments ")
    print("1st Arg:  0: disabling nagle  1: enabling Nagle ")
    print("2nd Arg:  0: disabling Delayed Ack  1: enabling Delayed Ack ")



serverPort = 12345
BUFSIZE = 1024
HOST = ""

ADDRESS = (HOST,serverPort)



DELAYED_ACK = int(sys.argv[2])
NAGLE = int(sys.argv[1])


#Creating the socket object
serverSocket = socket(AF_INET,SOCK_STREAM)
if(NAGLE != 0): 
    serverSocket.setsockopt(IPPROTO_TCP, TCP_NODELAY, True)

if(DELAYED_ACK != 0):
    serverSocket.setsockopt(IPPROTO_TCP, TCP_QUICKACK, True)
#Binding to socket
serverSocket.bind(ADDRESS)

#Starting TCP listener
serverSocket.listen(1)

while True:
    
    print("Listening ...")
    #Starting the connection 
    clientSocket,ADDRESS = serverSocket.accept()
    start = time()
    print("Connected")
    #Message sent to client after successful connection
    file_name = clientSocket.recv(2048).decode()
    f = open(file_name, "rb")
    chunk = f.read(BUFSIZE)
    no_of_chunks = ceil(os.path.getsize(file_name)/BUFSIZE)
    curr_number = 1
    while(chunk):
        print("Sent chunk "+str(curr_number)+ " /"+ str(no_of_chunks))
        clientSocket.send(chunk)
        chunk = f.read(BUFSIZE)
        curr_number +=1
    f.close() 
    print("successfully sent the file, closing the connection")

    clientSocket.close()
    end = time ()
    print("Time Elapsed : {} seconds".format (end - start))