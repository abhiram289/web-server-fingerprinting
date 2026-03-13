# TLS Secure Client–Server Fingerprinting (CN Mini Project)

This project implements a basic secure client–server communication system using **Python sockets and TLS (SSL)**. The server runs on a Linux machine and accepts connections from multiple clients. Communication between the server and clients is encrypted using TLS.

When a client connects and sends a message, the server responds with **fingerprinting information**, including details such as the server banner, TLS version, and cipher suite used for the secure connection.

The server is designed to handle multiple clients simultaneously using **threading**.

## Technologies Used

* Python (socket programming)
* TLS/SSL for secure communication
* Multithreading for handling multiple clients
* OpenSSL for certificate generation

## Status

 **In Progress**
