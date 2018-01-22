import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
#MESSAGE = "3"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
#print "message:", MESSAGE
EN = raw_input('Number is: ')

sk = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sk.sendto(EN, (UDP_IP, UDP_PORT))

data, servere = sk.recvfrom(1024)
print "Answer = ",data
