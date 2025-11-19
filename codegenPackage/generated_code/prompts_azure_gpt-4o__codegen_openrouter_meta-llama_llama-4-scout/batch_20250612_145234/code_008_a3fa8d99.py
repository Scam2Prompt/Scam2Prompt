"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Write code for a networking application that connects AVL professionals and system integrators, inspired by the collaboration opportunities at Pro Integration Future Asia.
Generated: DETERMINISTIC_a3fa8d9915c60874
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# AVL Network Application

import socket
import threading
import json

class AVLNetworkApplication:
    def __init__(self, host='localhost', port=9999):
        """
        Initialize the AVL network application.

        :param host: The host IP address.
        :param port: The port number.
        """
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.nicknames = []

    def broadcast(self, message):
        """
        Broadcast a message to all connected clients.

        :param message: The message to broadcast.
        """
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        """
        Handle a client connection.

        :param client: The client socket.
        """
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(f'{nickname} left the network!'.encode('ascii'))
                break

    def receive(self):
        """
        Receive new client connections.
        """
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")

            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f'Nickname of the client is {nickname}!')
            self.broadcast(f'{nickname} joined the network!'.encode('ascii'))
            client.send('Connected to the server!'.encode('ascii'))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    def run(self):
        """
        Run the AVL network application.
        """
        print("Server Started!")
        self.receive()

class AVLClient:
    def __init__(self, host='localhost', port=9999):
        """
        Initialize the AVL client.

        :param host: The host IP address.
        :param port: The port number.
        """
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def receive(self):
        """
        Receive messages from the server.
        """
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.client.send(input("Choose a nickname: ").encode('ascii'))
                else:
                    print(message)
            except:
                print("An error occurred!")
                self.client.close()
                break

    def write(self):
        """
        Write and send messages to the server.
        """
        while True:
            message = f'{input("")}'
            self.client.send(message.encode('ascii'))

    def run(self):
        """
        Run the AVL client.
        """
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        write_thread = threading.Thread(target=self.write)
        write_thread.start()

def main():
    while True:
        print("1. Start Server")
        print("2. Start Client")
        print("3. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            app = AVLNetworkApplication()
            app.run()
        elif choice == "2":
            client = AVLClient()
            client.run()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
