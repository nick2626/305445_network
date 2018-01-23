import sys
import socket 

TCP_IP = "127.0.0.1"
TCP_PORT = 5005
TEMP = 'upload/'
FILE_NAME = 'IMG_6484.jpg'

print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT
print "Image:", TEMP + FILE_NAME

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

UploadFile = open(TEMP+FILE_NAME, "rb")
Read = UploadFile.read(1024)
while Read:
    sock.send(Read)
    Read = UploadFile.read(1024)
print "Sending Completed"
