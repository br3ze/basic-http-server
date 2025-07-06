import socket
import threading
import os

HOST = '127.0.0.1' # Localhost
PORT = 8080        # Common port for local development
WEB_ROOT = './www'

# Create and bind server socket
# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsocket(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5) # Can queue up to 5 connections

print(f"Serving files from {WEB_ROOT}")
print(f"Server running on http://{HOST}:{PORT}")

# Function to handle one client
def handle_client(client_connection):
    try:
        request = client_connection.recv(1024).decode()
        print("Request:")
        print(request)

         # --- Parse the request line --- 
        try:
            request_line = request.splitlines()[0]
            method, path, _ = request_line.split()
        except ValueError:
            # Bad request format
            client_connection.close()
            return
        
         # --- Decide status and content ---
        if path == "/":
            status_line = "HTTP/1.1 200 OK\r\n"
            body = "<h1>Welcome to the Home Page</h1>"
        elif path == "/about":
            status_line = "HTTP/1.1 200 OK\r\n"
            body = "<h1>About this Server</h1><p>It's built with raw Python sockets!</p>"
        else:
            status_line = "HTTP/1.1 404 Not Found\r\n"
            body = "<h1>404 Not Found</h1>"

        # --- Build response ---
        http_response = (
            f"{status_line}"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(body.encode())}\r\n"
            "\r\n"
            f"{body}"
        )

        # Send Response
        client_connection.sendall(http_response.encode())
    finally:
        # Close the connection
        client_connection.close()

# Main loop; Accept and spawn a thread per client
while True:
    client_conn, client_addr = server_socket.accept() # Accept a single connection
    print(f"Connected by {client_addr}")
    client_thread = threading.Thread(target=handle_client, args=(client_conn,))
    client_thread.start()
