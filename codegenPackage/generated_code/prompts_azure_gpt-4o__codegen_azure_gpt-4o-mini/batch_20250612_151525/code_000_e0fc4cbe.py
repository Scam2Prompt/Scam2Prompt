"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Write code to create a local multiplayer game interface inspired by SCATTER HITAM, allowing players to connect via a local network and collaborate or compete in real-time.
Generated: DETERMINISTIC_e0fc4cbe4d0b7bdc
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import threading
import tkinter as tk
from tkinter import messagebox

# Constants for the game
HOST = '127.0.0.1'  # Localhost for testing; change to your local network IP for real use
PORT = 12345         # Port to listen on (non-privileged ports are > 1023)

class GameServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.running = True

    def start(self):
        """Start the server to accept incoming connections."""
        try:
            self.server_socket.bind((HOST, PORT))
            self.server_socket.listen()
            print(f"Server started on {HOST}:{PORT}")
            while self.running:
                client_socket, addr = self.server_socket.accept()
                print(f"Connection from {addr}")
                self.clients.append(client_socket)
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
        except Exception as e:
            print(f"Error starting server: {e}")
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket):
        """Handle communication with a connected client."""
        while self.running:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Received: {message}")
                    self.broadcast(message, client_socket)
                else:
                    break
            except Exception as e:
                print(f"Error handling client: {e}")
                break
        self.clients.remove(client_socket)
        client_socket.close()

    def broadcast(self, message, sender_socket):
        """Send a message to all connected clients except the sender."""
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except Exception as e:
                    print(f"Error sending message to client: {e}")

class GameClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Scatter Hitam - Client")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.create_widgets()

    def create_widgets(self):
        """Create the GUI components for the client."""
        self.text_area = tk.Text(self.master, state='disabled')
        self.text_area.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()
        self.entry.bind("<Return>", self.send_message)

        self.connect_button = tk.Button(self.master, text="Connect", command=self.connect)
        self.connect_button.pack()

    def connect(self):
        """Connect to the game server."""
        try:
            self.client_socket.connect((HOST, PORT))
            threading.Thread(target=self.receive_messages).start()
            self.text_area.config(state='normal')
            self.text_area.insert(tk.END, "Connected to the server.\n")
            self.text_area.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to server: {e}")

    def send_message(self, event=None):
        """Send a message to the server."""
        message = self.entry.get()
        if message:
            try:
                self.client_socket.send(message.encode('utf-8'))
                self.entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Send Error", f"Could not send message: {e}")

    def receive_messages(self):
        """Receive messages from the server."""
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.text_area.config(state='normal')
                    self.text_area.insert(tk.END, f"{message}\n")
                    self.text_area.config(state='disabled')
                else:
                    break
            except Exception as e:
                print(f"Error receiving message: {e}")
                break
        self.client_socket.close()

if __name__ == "__main__":
    # Start the server in a separate thread
    server = GameServer()
    threading.Thread(target=server.start, daemon=True).start()

    # Start the client GUI
    root = tk.Tk()
    client = GameClient(root)
    root.mainloop()
```

This code provides a basic local multiplayer game interface inspired by SCATTER HITAM, allowing players to connect via a local network and communicate in real-time. The server handles multiple clients, and the client has a simple GUI for sending and receiving messages.
