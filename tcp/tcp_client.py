from socket import *
import os
from time import time 
import sys 

BUFSIZE = 1024
serverName = "127.0.0.1"
serverPort = 12345
ADDRESS = (serverName, serverPort)

DELAYED_ACK = True
NAGLE = True 


books = {"1": "../novels/Heartsease.txt", "2": "../novels/Roget’s Thesaurus.txt", "3": "../novels/The 1991 CIA World Factbook.txt", "4":"../novels/The Conquest Of Peru.txt", "5": "../novels/War and Peace.txt"}
print("Select the book you want to request from the server, from the following list of books: ")
print("1: Heartsease")
print("2: Roget's Thesaurus")
print("3: The 1991 CIA World Factbook")
print("4: The Conquest Of Peru")
print("5: War and Peace")

message = input("Enter the book Number: ")

while (message not in books.keys()):
    print("Please choose a valid book number") 
    message = input("Enter the book Number: ")


DELAYED_ACK = 1 
NAGLE = 1
#Create socket object
DELAYED_ACK = int(sys.argv[2])
NAGLE = int(sys.argv[1])

clientSocket = socket(AF_INET,SOCK_STREAM)

if(NAGLE != 0 ): 
    clientSocket.setsockopt(IPPROTO_TCP, TCP_NODELAY, True)

if(DELAYED_ACK != 0):
    clientSocket.setsockopt(IPPROTO_TCP, TCP_QUICKACK, True)

start = time()
clientSocket.connect(ADDRESS)


clientSocket.send(books[message].encode())

fileName = "../received_files/tcp/"+books[message].split("/")[-1][:-4] + "_TCP"+ "_" + str(os.getpid())+".txt"
with open(fileName, "wb") as f:
    print("file opened") 
    try:
        while(True):
            print("Receiving data ...")
            chunk = clientSocket.recv(BUFSIZE)
            if not chunk:
                break 
            f.write(chunk)
    except:
        print("An exception occured")
f.close()
print("File received Successfully, closing the connection ...")
clientSocket.close()
end = time()
print("Time Elapsed : {} seconds".format (end - start))
