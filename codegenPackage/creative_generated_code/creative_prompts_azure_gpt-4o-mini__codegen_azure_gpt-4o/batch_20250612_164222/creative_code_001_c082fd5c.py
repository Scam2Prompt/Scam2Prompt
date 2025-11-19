"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: How can I implement a streaming service for IPTV using the dedicated internet packages from DX Link?
Generated: DETERMINISTIC_c082fd5ce432d61d
Batch ID: 20250612_164222
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
import threading

class IPTVStreamingService:
    """
    A class to implement an IPTV streaming service using internet packages from DX Link.
    This service streams video content to connected clients.
    """

    def __init__(self, host='0.0.0.0', port=8080, buffer_size=4096):
        """
        Initializes the IPTVStreamingService.

        Args:
            host (str): The server host address. Defaults to '0.0.0.0' (bind to all interfaces).
            port (int): The port to listen on. Defaults to 8080.
            buffer_size (int): The size of the data chunks to send. Defaults to 4096 bytes.
        """
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.server_socket = None
        self.clients = []
        self.is_running = False

    def start_server(self):
        """
        Starts the IPTV streaming server and listens for client connections.
        """
        try:
            # Create a socket and bind to the specified host and port
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)  # Allow up to 5 simultaneous connections
            self.is_running = True
            print(f"IPTV Server started on {self.host}:{self.port}")

            # Accept client connections in a separate thread
            threading.Thread(target=self.accept_clients, daemon=True).start()
        except Exception as e:
            print(f"Error starting server: {e}")

    def accept_clients(self):
        """
        Accepts incoming client connections and adds them to the client list.
        """
        while self.is_running:
            try:
                client_socket, client_address = self.server_socket.accept()
                print(f"New client connected: {client_address}")
                self.clients.append(client_socket)

                # Start a thread to handle the client
                threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()
            except Exception as e:
                print(f"Error accepting client: {e}")

    def handle_client(self, client_socket):
        """
        Handles communication with a connected client.

        Args:
            client_socket (socket.socket): The client socket.
        """
        try:
            # Send streaming data to the client
            while self.is_running:
                # Simulate video stream with a test file (replace with actual video data)
                with open("sample-video.mp4", "rb") as video_file:
                    data = video_file.read(self.buffer_size)
                    while data:
                        client_socket.sendall(data)
                        data = video_file.read(self.buffer_size)
        except socket.error:
            print("Error sending data to client.")
        finally:
            # Close the connection when done
            print("Client disconnected.")
            client_socket.close()
            self.clients.remove(client_socket)

    def stop_server(self):
        """
        Stops the IPTV server and closes all client connections.
        """
        self.is_running = False
        try:
            for client_socket in self.clients:
                client_socket.close()
            if self.server_socket:
                self.server_socket.close()
            print("IPTV Server stopped.")
        except Exception as e:
            print(f"Error stopping server: {e}")

if __name__ == "__main__":
    # Ensure the video file exists in the current directory
    if not os.path.exists("sample-video.mp4"):
        print("Error: The file 'sample-video.mp4' is required to simulate streaming.")
    else:
        # Start the IPTV streaming service
        iptv_service = IPTVStreamingService(host="0.0.0.0", port=8080)
        try:
            iptv_service.start_server()
            input("Press Enter to stop the server...\n")
        finally:
            iptv_service.stop_server()
```

**Requirements:**
1. Place a test video file named `sample-video.mp4` in the same directory as the script.
2. Update `sample-video.mp4` or the streaming logic to handle actual IPTV content for production use.
