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
from tkinter import messagebox

# Define constants
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5000       # Port to listen on

class GameServer:
    """Class to handle the game server allowing multiple clients to connect."""

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_sockets = []
        self.is_running = True

    def start(self):
        """Start the server to accept connections."""
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(5)
        print(f"Server started on {HOST}:{PORT}")

        while self.is_running:
            try:
                client_socket, addr = self.server_socket.accept()
                print(f"Connection from {addr}")
                self.client_sockets.append(client_socket)
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
            except Exception as e:
                print(f"Error accepting connections: {e}")
                break

    def handle_client(self, client_socket):
        """Handle communication with a connected client."""
        while self.is_running:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Received: {message}")
                    self.broadcast(message, client_socket)
            except Exception as e:
                print(f"Client error: {e}")
                break
        self.client_sockets.remove(client_socket)
        client_socket.close()

    def broadcast(self, message, source_socket):
        """Send a message to all connected clients except the sender."""
        for client in self.client_sockets:
            if client != source_socket:
                try:
                    client.send(message.encode())
                except Exception as e:
                    print(f"Error sending message: {e}")

    def stop(self):
        """Stop the server."""
        self.is_running = False
        self.server_socket.close()


class GameClient:
    """Class to handle the game client connecting to the server."""

    def __init__(self, master):
        self.master = master
        self.master.title("Local Multiplayer Game")
        self.is_running = True

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.create_widgets()

    def create_widgets(self):
        """Create the UI components for the game interface."""
        self.message_box = tk.Text(self.master, height=15, width=50)
        self.message_box.pack()

        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack()
        self.entry.bind('<Return>', self.send_message)

        self.connect_button = tk.Button(self.master, text="Connect", command=self.connect)
        self.connect_button.pack()

        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit_game)
        self.quit_button.pack()

    def connect(self):
        """Connect to the game server."""
        try:
            self.server_socket.connect((HOST, PORT))
            threading.Thread(target=self.receive_messages).start()
            messagebox.showinfo("Connection", "Connected to the game server.")
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))

    def send_message(self, event=None):
        """Send a message to the server."""
        message = self.entry.get()
        if message:
            self.server_socket.send(message.encode())
            self.entry.delete(0, tk.END)

    def receive_messages(self):
        """Receive messages from the server."""
        while self.is_running:
            try:
                message = self.server_socket.recv(1024).decode()
                if message:
                    self.message_box.insert(tk.END, message + "\n")
                    self.message_box.see(tk.END)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def quit_game(self):
        """Clean up and quit the game."""
        self.is_running = False
        self.server_socket.close()
        self.master.quit()


if __name__ == "__main__":
    # Start the server in a separate thread
    server = GameServer()
    threading.Thread(target=server.start, daemon=True).start()

    # Create the GUI for the client
    root = tk.Tk()
    client = GameClient(root)
    root.protocol("WM_DELETE_WINDOW", client.quit_game)
    root.mainloop()

    server.stop()  # Stop the server when done
```
