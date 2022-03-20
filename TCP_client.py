import socket

HOST = "192.168.86.47"  # This is the IP of the server host, change this to run the file
PORT = 55555  # This is the port used by the server. It must match the port the server has opened

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Defines the IP and connection type, we are using TCP so we use socket.SOCK_STREAM
server_socket.connect((HOST, PORT))     # Connects the client to the server
user_input = input("Please enter a message: ")
server_socket.sendall(user_input.encode())      # Sends this data to the server
data = server_socket.recv(2048)     # Receives response from the server

print(f"Data returned: {data.decode()}")