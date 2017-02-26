
while True:
    plaintext = raw_input('Enter message : ')
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key=input('enter key : ')
    cipher = ''
    ipher = ''
    for c in plaintext:
    	if c in alphabet:
    		cipher += alphabet [(alphabet.index(c) + key)%(len(alphabet))]
    print('your encrypted msg is : ' + cipher)
    import socket
    port = 50001
    host =raw_input('enter ip of the server ')
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(cipher)
    data = s.recv(size)
    print 'Received:', data
    #################>>>>>>>
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ipher = ''
    key=input('enter key : ')
    for c in data:
       	if c in alphabet:
        	ipher += alphabet [(alphabet.index(c) - key)%(len(alphabet))]
    print('your decrypted msg is : ' + ipher)
