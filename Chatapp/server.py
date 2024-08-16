import socket
import threading


HOST = '127.0.0.1'
PORT = 12345

clients = []

def handle_client(client_socket):
    connected = True
    while connected:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            connected = False
            clients.remove(client_socket)
            client_socket.close()
        else:
            print(f"Received: {message}")
            broadcast(message, client_socket)

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message.encode('utf-8'))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()



