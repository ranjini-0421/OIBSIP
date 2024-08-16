import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    connected = True
    while connected:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            print(message)
        else:
            connected = False
            client_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    connected = True
    while connected:
        message = input()
        if message.lower() == 'exit':
            connected = False
            client_socket.close()
        else:
            client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
