from socket import *
import os
from time import time 
import sys 

BUFSIZE = 1024                     # Buffer size
serverName = "127.0.0.1"           # Server IP(localhost)
serverPort = 12345                 # Server Port number
ADDRESS = (serverName, serverPort) # forming tuple of server IP and port

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

#Creating client socket
clientSocket = socket(AF_INET,SOCK_STREAM)

# uncomment the next line to disable Nagle's algorithm 
# clientSocket.setsockopt(IPPROTO_TCP, TCP_NODELAY, True)

# uncomment the next line to disable Delayed ACK  
# clientSocket.setsockopt(IPPROTO_TCP, TCP_QUICKACK, True)

#starting the timer
start = time()
clientSocket.connect(ADDRESS) # 3 whay handshake's first handshake,i.e connection setup 

# Sending the server, name of the book
clientSocket.send(books[message].encode())

fileName = "../received_files/tcp/"+books[message].split("/")[-1][:-4] + "_TCP"+ "_" + str(os.getpid())+".txt"
with open(fileName, "wb") as f:
    print("file opened") 
    try:
        while(True):
            chunk = clientSocket.recv(BUFSIZE) # receiving the file in chunks of buffer size
            if not chunk:
                break 
            f.write(chunk)                     # Writing the chunk to the file
    except:
        print("An exception occured")
f.close()
print("File received Successfully, closing the connection ...")
clientSocket.close() #closing the connection
end = time()
print("Time Elapsed : {} seconds".format (end - start))
