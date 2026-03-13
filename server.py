import socket
import ssl
import threading

HOST = "0.0.0.0"   # listen on all interfaces
PORT = 8080

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Secure server running on port", PORT)


def handle_client(conn, addr):
    print("Client connected:", addr)

    try:
        data = conn.recv(1024).decode()
        print("Received from", addr, ":", data)

        # fingerprint information
        tls_version = conn.version()
        cipher = conn.cipher()[0]

        fingerprint = f"""
Server Banner: Python Secure Server 1.0
TLS Version: {tls_version}
Cipher Used: {cipher}
"""

        conn.send(fingerprint.encode())

    except Exception as e:
        print("Error:", e)

    conn.close()
    print("Client disconnected:", addr)


while True:
    client_socket, addr = server_socket.accept()

    secure_socket = context.wrap_socket(client_socket, server_side=True)

    thread = threading.Thread(target=handle_client, args=(secure_socket, addr))
    thread.start()
