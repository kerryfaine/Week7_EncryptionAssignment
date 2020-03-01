import socket
from certauth import certauth
#import os
#from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
#from cryptography.hazmat.backends import default_backend

HOST = '127.0.0.1'
PORT = 9500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((HOST, PORT))
    s.sendall(b'Hello')
    connectionData = s.recv(5120)

    cert = certauth()
    key = cert.validateMe(connectionData)
    
    secret = cert.encryptMe(key)
    s.sendall(secret.encode("utf-8"))
    
    response = s.recv(1024)
    if(response.decode("utf-8") == cert.go):
        s.sendall(b"Super Secret Stuff")
    
print(f'Connection Established from:  {repr(connectionData)}')
print(f'Security Status:  {repr(response)}')






