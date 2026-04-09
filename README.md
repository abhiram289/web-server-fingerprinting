# TLS Secure Client–Server Fingerprinting

Implementation of a **secure client–server communication system** using **Python sockets with TLS (SSL)**. This project demonstrates encrypted communication along with basic **TLS fingerprinting techniques** to extract connection-level details


## Overview

This project simulates a secure network environment where:

* A **TLS-enabled server** listens for incoming client connections
* Multiple clients can connect simultaneously
* All communication is **encrypted using SSL/TLS**
* The server responds with **fingerprinting data** about the secure session


## Features

* **Secure Communication** using TLS/SSL
* **Multithreaded Server** to handle multiple clients concurrently
* **TLS Fingerprinting**, including:

  * TLS version
  * Cipher suite used
  * Server banner/info
* Lightweight and easy-to-understand implementation
* Uses **OpenSSL-generated certificates**


## How It Works

1. The server initializes a **TLS context** using SSL certificates
2. Clients establish a secure connection using **wrapped sockets**
3. Upon receiving a message from the client:

   * The server extracts TLS session details
   * Sends back fingerprinting information
4. Each client connection is handled in a **separate thread**


## Team

[abhiram289](https://github.com/abhiram289)
[nmsr21](https://github.com/NSMR21)
[majesticraven1](https://github.com/majesticraven1)





