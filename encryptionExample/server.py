import socket
from certauth import certauth

HOST = '127.0.0.1'
PORT = 9500

serverName = 'DESKTOP-MLM0OMA'
key = 'Key456'  #To see example of 'bad handshake' set the upper case K to lower case k

cert = certauth()
cert.registerMe(serverName, key)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, PORT))
    s.listen()
    print(f"listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn: 
        print(f"Incoming connection from {addr}") 
        while True: 
            data = conn.recv(9500)
            if not data: 
                break 

            if data == b'Hello':
                conn.send(bytes(serverName, "utf-8"))

            elif data == b"Super Secret Stuff":
                print(f"Successful delivery of sensitive data from {addr}")
                break;

            else:
                oldSecret = data.decode("utf-8")
                newSecret = cert.encryptMe(key)
                if(oldSecret == newSecret):
                    print("Security Check Completed Successfully.")
                    conn.send(cert.go.encode("utf-8"))
                else: 
                    print("Security Check Failed.")
                    conn.send(cert.noGo.encode("utf-8"))

