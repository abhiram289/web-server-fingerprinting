import socket
import ssl

HOST = "10.237.41.25"
PORT = 8080

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_socket = context.wrap_socket(sock, server_hostname=HOST)

try:
    secure_socket.connect((HOST, PORT))

    message = input("\n🔹 Enter message to send: ")
    secure_socket.send(message.encode())

    response = secure_socket.recv(2048).decode()

    print("\n" + "="*50)
    print("         SERVER FINGERPRINT REPORT")
    print("="*50)

    print(response.strip())

    print("="*50)
    print("✅ Secure connection established successfully")
    print("="*50 + "\n")

except Exception as e:
    print("\n❌ Connection Failed:", e)

finally:
    secure_socket.close()
