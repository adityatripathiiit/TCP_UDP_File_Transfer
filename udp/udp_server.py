from socket import *
import os
from time import time,sleep
from math import ceil 
import sys 

serverPort = 12345
BUFSIZE = 32
HOST = ""
ADDRESS = (HOST,serverPort)

serverSocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind(ADDRESS)


while True:
    print("Waiting for File Name...")
    file_name,ADDRESS = serverSocket.recvfrom(2048)
    start = time()
    file_name  = file_name.decode()
    f = open(file_name,"rb")
    chunk = f.read(BUFSIZE)
    # no_of_chunks = ceil(os.path.getsize(file_name)/BUFSIZE)
    # curr_number = 1
    print(ADDRESS)
    while(chunk):
        # print("Sent chunk "+str(curr_number)+ " /"+ str(no_of_chunks))
        serverSocket.sendto(chunk,ADDRESS)
        chunk = f.read(BUFSIZE)
        # sleep(100/1000000)
        # curr_number +=1
    f.close() 
    print("successfully sent the file")
    end = time()
    print("Time Elapsed : {} seconds".format (end - start))

serverSocket.close()
    
    