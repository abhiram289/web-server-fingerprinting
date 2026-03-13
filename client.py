import socket
import ssl

HOST = "10.30.246.25"   # server IP
PORT = 8080

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

secure_socket = context.wrap_socket(sock, server_hostname=HOST)

secure_socket.connect((HOST, PORT))

message = input("Enter message: ")
secure_socket.send(message.encode())

response = secure_socket.recv(2048).decode()

print("\n--- Server Fingerprint ---")
print(response)

secure_socket.close()
