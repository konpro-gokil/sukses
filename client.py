#program untuk client
import socket

handlerSocket = socket.socket()
serverIP = "1270.0.0.1"
serverPort = 2222

handlerSocket.connect((serverIP,serverPort))
print'terkoneksi ke server'

while True:
	message = handlerSocket.recv(1024)
	print'pesan dari server: ',message
	message = raw_input("masukan pesan anda: ")
	handlerSocketsend(message)
	pass

