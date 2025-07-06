import socket

HOST = '127.0.0.1'  # Localhost
PORT = 8080         # Common port for local development

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
# Bind the socket to the address (host, port)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Allow 1 queued connection

print(f"Server running on http://{HOST}:{PORT}")

while True:
  client_connection, client_address = server_socket.accept()
  request = client_connection.recv(1024).decode()
  print("Request:")
  print(request)

  # Basic HTTP response
  http_response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html\r\n"
    "\r\n"
    "<html><body><h1>Hello, World!</h1></body></html>"
    )

client_connection.sendall(http_response.encode())
client_connection.close()
