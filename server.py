import socket

HOST = '127.0.0.1'  # Localhost
PORT = 8080         # Common port for local development

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address (host, port)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Allow 1 queued connection

print(f"Server running on http://{HOST}:{PORT}")

# Accept a single connection
client_connection, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Receive request (up to 1024 bytes)
request = client_connection.recv(1024).decode()
print("Request:")
print(request)

# Close the connection
client_connection.close()
