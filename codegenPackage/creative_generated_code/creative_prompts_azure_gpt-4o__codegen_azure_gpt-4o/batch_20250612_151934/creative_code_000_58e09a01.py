"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Write Python code to simulate a digital radio service that breaks intercontinental barriers, as described in MIEC's solutions. Include features for broadcasting and receiving audio streams.
Generated: DETERMINISTIC_58e09a0162644023
Batch ID: 20250612_151934
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
import pyaudio

# Constants for audio streaming
CHUNK_SIZE = 1024         # Number of frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 2              # Number of audio channels (stereo)
RATE = 44100              # Sampling rate (44.1 kHz)

# Constants for networking
SERVER_HOST = '0.0.0.0'   # Server to bind on all interfaces
SERVER_PORT = 5000        # Port for broadcasting
BUFFER_SIZE = 4096        # Socket buffer size

# Digital Radio Server
class RadioServer:
    def __init__(self):
        """Initialize the server and audio streaming."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = []  # List to store connected clients
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=FORMAT,
                                      channels=CHANNELS,
                                      rate=RATE,
                                      input=True,
                                      frames_per_buffer=CHUNK_SIZE)
    
    def start(self):
        """Start the server and listen for client connections."""
        self.server_socket.bind((SERVER_HOST, SERVER_PORT))
        self.server_socket.listen(5)  # Allow up to 5 connection requests
        print(f"Radio Server started at {SERVER_HOST}:{SERVER_PORT}")
        threading.Thread(target=self.broadcast_audio).start()  # Start audio broadcasting

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"New client connected: {client_address}")
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def broadcast_audio(self):
        """Continuously send audio data to all connected clients."""
        while True:
            try:
                audio_data = self.stream.read(CHUNK_SIZE)
                for client in self.clients:
                    try:
                        client.send(audio_data)
                    except socket.error:
                        # Handle client disconnection
                        self.clients.remove(client)
                        print("Disconnected client removed.")
            except Exception as e:
                print(f"Error during broadcasting: {e}")

    def handle_client(self, client_socket):
        """Handle individual client connection."""
        try:
            client_socket.send(b"Welcome to the Digital Radio Service!")
            while True:
                # Keep the connection open
                pass
        except socket.error:
            print("Client disconnected.")
        finally:
            client_socket.close()
            self.clients.remove(client_socket)

    def stop(self):
        """Stop the server and release resources."""
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        self.server_socket.close()
        print("Radio Server stopped.")

# Digital Radio Client
class RadioClient:
    def __init__(self, server_host, server_port):
        """Initialize the client and audio stream."""
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=FORMAT,
                                      channels=CHANNELS,
                                      rate=RATE,
                                      output=True,
                                      frames_per_buffer=CHUNK_SIZE)

    def start(self):
        """Connect to the server and receive audio streams."""
        try:
            self.client_socket.connect((self.server_host, self.server_port))
            print(f"Connected to Radio Server at {self.server_host}:{self.server_port}")
            while True:
                audio_data = self.client_socket.recv(BUFFER_SIZE)
                if not audio_data:
                    break
                self.stream.write(audio_data)
        except Exception as e:
            print(f"Error during reception: {e}")
        finally:
            self.stop()

    def stop(self):
        """Stop the client and release resources."""
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        self.client_socket.close()
        print("Radio Client stopped.")

# Entry point to test the implementation
if __name__ == "__main__":
    choice = input("Enter 'server' to start the Radio Server or 'client' to start the Radio Client: ").strip().lower()
    if choice == 'server':
        server = RadioServer()
        try:
            server.start()
        except KeyboardInterrupt:
            server.stop()
    elif choice == 'client':
        server_host = input("Enter the server IP address: ").strip()
        server_port = int(input("Enter the server port: ").strip())
        client = RadioClient(server_host, server_port)
        try:
            client.start()
        except KeyboardInterrupt:
            client.stop()
    else:
        print("Invalid choice. Please enter 'server' or 'client'.")
```
