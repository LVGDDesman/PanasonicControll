import socket
import sys

ip = "192.168.54.10"
port = 49152

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")

while True:
	data, address = s.recvfrom(4096)
	with open("./frames/frames.jpeg", "a+") as frame:
		frame.write(data)
