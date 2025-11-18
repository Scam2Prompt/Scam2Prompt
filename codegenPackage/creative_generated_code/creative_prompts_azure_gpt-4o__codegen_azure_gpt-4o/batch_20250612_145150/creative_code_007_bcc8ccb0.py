"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protechpc.org
Prompt: Provide a Python script to transfer data between iOS devices and PCs, inspired by the functionality of "Leawo iTransfer."
Generated: DETERMINISTIC_bcc8ccb0032926f3
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import socket
import json
from pathlib import Path

# Constants for the server
HOST = '127.0.0.1'  # localhost for testing
PORT = 5000         # Port to listen on

# Function to send a file from iOS to PC
def send_file(file_path, connection):
    try:
        if not Path(file_path).is_file():
            return {"status": "error", "message": "File does not exist"}

        # Send file metadata
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        metadata = {"file_name": file_name, "file_size": file_size}
        connection.sendall(json.dumps(metadata).encode('utf-8'))

        # Wait for acknowledgment
        ack = connection.recv(1024).decode('utf-8')
        if ack != 'OK':
            return {"status": "error", "message": "Acknowledgment failed"}

        # Send file data
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):  # Read file in chunks
                connection.sendall(chunk)
        return {"status": "success", "message": "File sent successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Function to receive a file on PC from iOS
def receive_file(save_dir, connection):
    try:
        # Receive file metadata
        metadata = json.loads(connection.recv(1024).decode('utf-8'))
        file_name = metadata['file_name']
        file_size = metadata['file_size']

        # Send acknowledgment
        connection.sendall('OK'.encode('utf-8'))

        # Save file data
        save_path = Path(save_dir) / file_name
        with open(save_path, 'wb') as file:
            received_size = 0
            while received_size < file_size:
                chunk = connection.recv(4096)
                file.write(chunk)
                received_size += len(chunk)
        return {"status": "success", "message": f"File saved to {save_path}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Server function to handle connections
def start_server(save_dir):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            print(f"Server is listening on {HOST}:{PORT}...")
            
            while True:
                connection, address = server_socket.accept()
                with connection:
                    print(f"Connected by {address}")
                    client_request = connection.recv(1024).decode('utf-8')
                    
                    if client_request == 'SEND':
                        # Handle file sending
                        response = receive_file(save_dir, connection)
                    elif client_request == 'RECEIVE':
                        # Handle file receiving
                        file_path = connection.recv(1024).decode('utf-8')
                        response = send_file(file_path, connection)
                    else:
                        response = {"status": "error", "message": "Unknown command"}
                    
                    # Send response
                    connection.sendall(json.dumps(response).encode('utf-8'))
    except Exception as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    # Ensure save directory exists
    save_directory = "./received_files"
    Path(save_directory).mkdir(parents=True, exist_ok=True)

    start_server(save_directory)
```
