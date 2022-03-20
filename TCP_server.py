import socket

HOST = "192.168.86.47"      # IP of the server
PORT = 55555    # Port the server communicates on

address = (HOST, PORT)  # address holds the IP and port that is used to create the server
server_socket = socket.create_server(address)   # The server is initialized here
print("Server started")
server_socket.listen()      # The listen() function allows the server to receive connections
print("Server accepting connections")
connections, conn_address = server_socket.accept()  # The accept() function allows the server to accept the connections received

data = None

with connections:
    print(f"Connected to ip: {str(conn_address[0])} via port: {str(conn_address[1])}")  # Prints client connection information
    while True:
        data = connections.recv(2048)   # Data is received and stored
        print(f"Data recieved: {data.decode()}")    # decode() is used to be able to display the data
        if data == None:
            print("No data recieved")
            break
        connections.sendall(data)   # sendall is used to return the data back to the client
        print("Data has been returned")
        break