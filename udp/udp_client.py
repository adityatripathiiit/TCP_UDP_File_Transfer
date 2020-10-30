from socket import *
import os
import sys
from time import time 


BUFSIZE = 32
serverName = "127.0.0.1"
serverPort = 12345
ADDRESS = (serverName, serverPort)
TIMEOUT = 2


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

start = time()
clientSocket = socket(AF_INET,SOCK_DGRAM)
# clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFSIZE)
clientSocket.sendto(books[message].encode(),ADDRESS) 


fileName = "../received_files/udp/"+books[message].split("/")[-1][:-4] + "_UDP"+ "_" + str(os.getpid())+".txt"

with open(fileName, "wb") as f:
    print("file opened") 
    try:
        while(True):
            # print("Receiving data ...")
            clientSocket.settimeout(TIMEOUT)
            chunk,ADDRESS = clientSocket.recvfrom(BUFSIZE)
            # print(ADDRESS)
            f.write(chunk)
    except timeout:
        f.close()
        print("File received Successfully, closing the connection ...")
        clientSocket.close()
        end = time()
        print("Time Elapsed : {} seconds".format (end - start -TIMEOUT))
        