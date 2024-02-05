import socket
def main():
    server_port = 4000
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sersock:
        sersock.bind(('0.0.0.0',server_port))
        sersock.listen(1)
        print('server ready for connection')
        
        sock,addr = sersock.accept()
        print(f'connection established with {addr}')
        
        istream = sock.recv(1024).decode()
        fname=istream.strip()
              
        with open(fname,'r') as fileRead:
              for line in fileRead:
                  sock.sendall(line.encode())
              
        sock.close()
        sersock.close()
              
if __name__ == "__main__":
    main()
    
    
import socket

def main():
    host = "127.0.0.1"
    port = 4000
    with socket.socket(socket.AF_INET,socket.Sock_STREAM) as sock:
        sock.connect((host,port))
        
        fname = input('enter the file name:')
        sock.sendall(fname.encode())
        
        data = sock.recv(1024)
        while data:
            print(data.decode(),end='')
            data = sock.recv(1024)
              
if __name__ == "__main__":
    main()
