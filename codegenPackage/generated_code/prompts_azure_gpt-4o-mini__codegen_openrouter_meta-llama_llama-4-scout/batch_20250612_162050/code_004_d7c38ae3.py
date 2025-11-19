"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: How can I create a user-friendly interface for a text counselling service that accommodates individuals who prefer writing over speaking, similar to the model used by Text Counselling Online?
Generated: DETERMINISTIC_d7c38ae358a4e6b0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

class TextCounsellingService:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Counselling Service")

        # Create frames
        self.conversation_frame = tk.Frame(self.root)
        self.conversation_frame.pack(fill="both", expand=True)

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill="x")

        # Create conversation text box
        self.conversation_text = scrolledtext.ScrolledText(self.conversation_frame, width=50, height=20)
        self.conversation_text.pack(side="left", fill="both", expand=True)
        self.conversation_text.config(state="disabled")

        # Create input text box
        self.input_text = tk.Text(self.input_frame, width=40, height=5)
        self.input_text.pack(side="left", fill="x", expand=True)

        # Create send button
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side="left")

        # Create socket and connect to server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(("localhost", 8080))
        except ConnectionRefusedError:
            self.conversation_text.config(state="normal")
            self.conversation_text.insert("end", "Connection refused. Please try again later.\n")
            self.conversation_text.config(state="disabled")
            return

        # Start receiving messages from server
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def send_message(self):
        message = self.input_text.get("1.0", "end-1c")
        if message:
            try:
                self.client_socket.sendall(message.encode())
                self.conversation_text.config(state="normal")
                self.conversation_text.insert("end", "You: " + message + "\n")
                self.conversation_text.config(state="disabled")
                self.input_text.delete("1.0", "end")
            except Exception as e:
                self.conversation_text.config(state="normal")
                self.conversation_text.insert("end", "Error sending message: " + str(e) + "\n")
                self.conversation_text.config(state="disabled")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    self.conversation_text.config(state="normal")
                    self.conversation_text.insert("end", "Counsellor: " + message + "\n")
                    self.conversation_text.config(state="disabled")
            except Exception as e:
                self.conversation_text.config(state="normal")
                self.conversation_text.insert("end", "Error receiving message: " + str(e) + "\n")
                self.conversation_text.config(state="disabled")
                break

if __name__ == "__main__":
    root = tk.Tk()
    text_counselling_service = TextCounsellingService(root)
    root.mainloop()
```

```python
# Server code (counsellor_server.py)

import socket
import threading

class CounsellorServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.clients = []

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    # Handle message from client
                    print("Received message from client: " + message)
                    response = "Thank you for sharing that with me. How did that make you feel?"  # Example response
                    client_socket.sendall(response.encode())
            except Exception as e:
                print("Error handling client: " + str(e))
                self.clients.remove(client_socket)
                client_socket.close()
                break

    def start(self):
        print("Counsellor server started on " + self.host + ":" + str(self.port))
        while True:
            client_socket, address = self.server_socket.accept()
            print("New connection from " + str(address))
            self.clients.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

if __name__ == "__main__":
    counsellor_server = CounsellorServer("localhost", 8080)
    counsellor_server.start()
```
