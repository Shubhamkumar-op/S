import socket 
import sys

def main():
    print('enter the file name')
    filename = input().strip()
    
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sersock:
        sersock.bind(('localhost',4000))
        sersock.listen()
        
        print("server ready for connection")
        
        with sersock.accept() as (sock,addr), sock.makefile('r') as file_read:
            print(f'connection is sucessful and waiting for client request form {addr}')
            
            file_read.readline()
            
            try:
                with open(fiename,'r') as content_read, sock.makefile('w') as pwrite:
                    for line in content_read:
                        pwrite.write(line)
            except FileNotFoundError:
                print(f"error: file '{filename}' not found.")
                      
if __name__ == "__main__":
    main()
    
    
import socket

def main():
    server_port = 4444
    
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sock:
        sock.bind(('0.0.0.0',server_port))
        print('waiting...')
        
        data , addr =sock.recvfrom(256)
        message = data.decode()
        
        print(f'{addr[0]}:{addr[1]} - {message}')
        
if __name__ == "__main__":
    main()
