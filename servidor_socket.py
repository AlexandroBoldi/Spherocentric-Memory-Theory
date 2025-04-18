# Servidor TCP/IP para integração com sistemas externos
import socket

HOST = '127.0.0.1'
PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Conectado por {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Recebido:', data.decode())
            conn.sendall(b'ACK')