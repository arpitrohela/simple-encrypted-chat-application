
import socket
host=''
port=50001
backlog=5
size=1024
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
client,address=s.accept()
alphabet = "abcdefghijklmnopqrstuvwxyz"
ipher = ''
key=input('enter key : ')
for c in client.recv(size):
	if c in alphabet:
		ipher += alphabet [(alphabet.index(c) - key)%(len(alphabet))]
print('your decrypted msg is : ' + ipher)
while 1:
        plaintext = raw_input('Enter message : ')
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key=input('enter key : ')
        cipher = ''
        ipher = ''
        for c in plaintext:
            if c in alphabet:
               	cipher += alphabet [(alphabet.index(c) + key)%(len(alphabet))]
        print('your encrypted msg is : ' + cipher)
        client.send(cipher)
