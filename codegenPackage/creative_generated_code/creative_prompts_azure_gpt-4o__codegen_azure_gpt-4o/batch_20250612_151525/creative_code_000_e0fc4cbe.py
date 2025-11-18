"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Write code to create a local multiplayer game interface inspired by SCATTER HITAM, allowing players to connect via a local network and collaborate or compete in real-time.
Generated: DETERMINISTIC_e0fc4cbe4d0b7bdc
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import threading
import tkinter as tk

# Constants
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port for communication
BUFFER_SIZE = 1024  # Size of data buffer
ENCODING = 'utf-8'  # Encoding for communication

# Server class (Handles multiplayer game hosting)
class GameServer:
    def __init__(self):
        self.clients = []  # List of connected clients
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        try:
            self.server_socket.bind((HOST, PORT))
            self.server_socket.listen(5)  # Allow up to 5 simultaneous connections
            print(f"Server started on {HOST}:{PORT}")
            threading.Thread(target=self.accept_connections).start()
        except Exception as e:
            print(f"Error starting server: {e}")
            self.server_socket.close()

    def accept_connections(self):
        while True:
            try:
                client_socket, addr = self.server_socket.accept()
                print(f"New connection from {addr}")
                self.clients.append(client_socket)
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
            except Exception as e:
                print(f"Error accepting connections: {e}")
                continue

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(BUFFER_SIZE).decode(ENCODING)
                if data:
                    print(f"Received: {data}")
                    self.broadcast(data, client_socket)
            except Exception as e:
                print(f"Error handling client: {e}")
                self.clients.remove(client_socket)
                client_socket.close()
                break

    def broadcast(self, message, source_socket):
        # Send messages to all clients except the source
        for client in self.clients:
            if client != source_socket:
                try:
                    client.send(message.encode(ENCODING))
                except Exception as e:
                    print(f"Error broadcasting message: {e}")
                    self.clients.remove(client)

# Client class (Handles local player connection)
class GameClient:
    def __init__(self, player_name):
        self.player_name = player_name
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gui = None

    def connect_to_server(self):
        try:
            self.client_socket.connect((HOST, PORT))
            print(f"Connected to server at {HOST}:{PORT}")
            threading.Thread(target=self.receive_messages).start()
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def send_message(self, message):
        try:
            self.client_socket.send(message.encode(ENCODING))
        except Exception as e:
            print(f"Error sending message: {e}")

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(BUFFER_SIZE).decode(ENCODING)
                if data:
                    print(f"Message from server: {data}")
                    self.gui.append_message(data)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def close_connection(self):
        self.client_socket.close()

# GUI Class (Game interface for players)
class GameGUI:
    def __init__(self, client):
        self.client = client
        self.root = tk.Tk()
        self.root.title(f"Scatter Hitam - Player: {self.client.player_name}")
        self.setup_ui()

    def setup_ui(self):
        # Chat display
        self.chat_display = tk.Text(self.root, state='disabled', width=50, height=20)
        self.chat_display.grid(row=0, column=0, padx=10, pady=10)
        # Input field
        self.input_field = tk.Entry(self.root, width=40)
        self.input_field.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        # Close button
        self.close_button = tk.Button(self.root, text="Exit", command=self.close_connection)
        self.close_button.grid(row=2, column=0, padx=10, pady=10)

    def send_message(self):
        message = self.input_field.get()
        if message:
            self.client.send_message(f"{self.client.player_name}: {message}")
            self.input_field.delete(0, tk.END)

    def append_message(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + '\n')
        self.chat_display.config(state='disabled')

    def close_connection(self):
        self.client.close_connection()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

# Main function
def main():
    user_role = input("Enter role (server/client): ").strip().lower()
    if user_role == "server":
        server = GameServer()
        server.start_server()
    elif user_role == "client":
        player_name = input("Enter your player name: ").strip()
        client = GameClient(player_name)
        client.connect_to_server()
        gui = GameGUI(client)
        client.gui = gui
        gui.run()
    else:
        print("Invalid role. Please enter 'server' or 'client'.")

# Entry point
if __name__ == "__main__":
    main()
```
