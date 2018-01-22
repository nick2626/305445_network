import sys
import socket 
import os

TCP_IP = "127.0.0.1"
TCP_PORT = 5005
FILE_NAME = 'IMG_6484.jpg'

print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT
print "Image:", FILE_NAME


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((TCP_IP,TCP_PORT))
sock.listen(10)

while 1:
    data,addr = sock.accept()
    newpath = r'upload/' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    fileUpload = open(newpath + FILE_NAME, "wb")
    Data = data.recv(1024)
    while Data:
        fileUpload.write(Data)
        Data = data.recv(1024)
    print "Upload Completed"
sock.close()
