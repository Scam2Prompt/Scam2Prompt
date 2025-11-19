"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: Write Python code to simulate a digital radio service that breaks intercontinental barriers, as described in MIEC's solutions. Include features for broadcasting and receiving audio streams.
Generated: DETERMINISTIC_58e09a0162644023
Batch ID: 20250612_151934
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
import time
import wave
import pyaudio
import json
import os
from datetime import datetime
from queue import Queue

# Constants
BUFFER_SIZE = 4096
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
MAX_CLIENTS = 50
BROADCAST_PORT = 5000
CONTROL_PORT = 5001
METADATA_INTERVAL = 5  # seconds

class DigitalRadioServer:
    def __init__(self):
        self.clients = set()
        self.audio_queue = Queue()
        self.metadata = {
            'station_name': 'MIEC Global Radio',
            'current_track': 'Breaking Barriers - World Mix',
            'listeners': 0,
            'timestamp': datetime.utcnow().isoformat()
        }
        self.running = False
        self.audio_stream = None
        self.pyaudio = pyaudio.PyAudio()
        
        # Initialize sockets
        self.broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
        self.control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.control_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def start_server(self, host='0.0.0.0'):
        """Start the radio server with broadcasting and control services."""
        self.running = True
        
        # Start broadcasting thread
        broadcast_thread = threading.Thread(target=self._broadcast_audio)
        broadcast_thread.daemon = True
        broadcast_thread.start()
        
        # Start control server thread
        control_thread = threading.Thread(target=self._run_control_server, args=(host,))
        control_thread.daemon = True
        control_thread.start()
        
        # Start metadata update thread
        metadata_thread = threading.Thread(target=self._update_metadata)
        metadata_thread.daemon = True
        metadata_thread.start()
        
        print(f"Server started. Broadcasting on port {BROADCAST_PORT}, control on {CONTROL_PORT}")
        
    def stop_server(self):
        """Stop the radio server and clean up resources."""
        self.running = False
        if self.audio_stream:
            self.audio_stream.stop_stream()
            self.audio_stream.close()
        self.pyaudio.terminate()
        self.broadcast_socket.close()
        self.control_socket.close()
        print("Server stopped.")
        
    def _broadcast_audio(self):
        """Broadcast audio stream to all connected clients."""
        while self.running:
            if not self.audio_queue.empty():
                data = self.audio_queue.get()
                try:
                    self.broadcast_socket.sendto(data, ('<broadcast>', BROADCAST_PORT))
                except Exception as e:
                    print(f"Broadcast error: {e}")
            time.sleep(0.01)
            
    def _run_control_server(self, host):
        """Handle client connections and control commands."""
        self.control_socket.bind((host, CONTROL_PORT))
        self.control_socket.listen(MAX_CLIENTS)
        
        while self.running:
            try:
                client_socket, addr = self.control_socket.accept()
                threading.Thread(target=self._handle_client, args=(client_socket, addr)).start()
            except Exception as e:
                if self.running:
                    print(f"Control server error: {e}")
                    
    def _handle_client(self, client_socket, addr):
        """Handle individual client connections."""
        try:
            print(f"New connection from {addr}")
            self.clients.add(client_socket)
            
            # Send initial metadata
            client_socket.send(json.dumps(self.metadata).encode())
            
            while self.running:
                try:
                    data = client_socket.recv(BUFFER_SIZE)
                    if not data:
                        break
                        
                    # Process control commands (placeholder for future commands)
                    command = data.decode().strip()
                    if command == "GET_METADATA":
                        client_socket.send(json.dumps(self.metadata).encode())
                        
                except Exception as e:
                    print(f"Client {addr} error: {e}")
                    break
                    
        finally:
            self.clients.remove(client_socket)
            client_socket.close()
            print(f"Connection closed with {addr}")
            
    def _update_metadata(self):
        """Periodically update and broadcast metadata."""
        while self.running:
            self.metadata['listeners'] = len(self.clients)
            self.metadata['timestamp'] = datetime.utcnow().isoformat()
            
            # Broadcast to all clients
            for client in list(self.clients):
                try:
                    client.send(json.dumps(self.metadata).encode())
                except:
                    self.clients.remove(client)
                    
            time.sleep(METADATA_INTERVAL)
            
    def play_audio_file(self, filename):
        """Stream an audio file to broadcast."""
        try:
            wf = wave.open(filename, 'rb')
            
            self.audio_stream = self.pyaudio.open(
                format=self.pyaudio.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=False,
                input=True,
                frames_per_buffer=CHUNK
            )
            
            data = wf.readframes(CHUNK)
            while data and self.running:
                self.audio_queue.put(data)
                data = wf.readframes(CHUNK)
                
            wf.close()
        except Exception as e:
            print(f"Error playing audio file: {e}")
            
    def stream_live_audio(self):
        """Stream live audio from microphone."""
        try:
            self.audio_stream = self.pyaudio.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK
            )
            
            while self.running:
                data = self.audio_stream.read(CHUNK)
                self.audio_queue.put(data)
                
        except Exception as e:
            print(f"Error streaming live audio: {e}")

class DigitalRadioClient:
    def __init__(self):
        self.running = False
        self.audio_stream = None
        self.pyaudio = pyaudio.PyAudio()
        self.current_metadata = {}
        
    def start_client(self, server_host):
        """Start receiving audio stream from server."""
        self.running = True
        
        # Audio receiving thread
        audio_thread = threading.Thread(target=self._receive_audio)
        audio_thread.daemon = True
        audio_thread.start()
        
        # Control connection thread
        control_thread = threading.Thread(target=self._connect_to_control, args=(server_host,))
        control_thread.daemon = True
        control_thread.start()
        
        print("Client started. Receiving broadcast...")
        
    def stop_client(self):
        """Stop the client and clean up resources."""
        self.running = False
        if self.audio_stream:
            self.audio_stream.stop_stream()
            self.audio_stream.close()
        self.pyaudio.terminate()
        print("Client stopped.")
        
    def _receive_audio(self):
        """Receive and play audio stream."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', BROADCAST_PORT))
        
        self.audio_stream = self.pyaudio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            output=True,
            frames_per_buffer=CHUNK
        )
        
        while self.running:
            try:
                data, _ = sock.recvfrom(BUFFER_SIZE)
                self.audio_stream.write(data)
            except Exception as e:
                if self.running:
                    print(f"Audio receive error: {e}")
                    
        sock.close()
        
    def _connect_to_control(self, server_host):
        """Connect to control server for metadata updates."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            sock.connect((server_host, CONTROL_PORT))
            
            # Get initial metadata
            data = sock.recv(BUFFER_SIZE)
            self.current_metadata = json.loads(data.decode())
            print(f"Connected to {self.current_metadata['station_name']}")
            
            while self.running:
                try:
                    data = sock.recv(BUFFER_SIZE)
                    if not data:
                        break
                        
                    self.current_metadata = json.loads(data.decode())
                    print(f"Now playing: {self.current_metadata['current_track']} | Listeners: {self.current_metadata['listeners']}")
                    
                except Exception as e:
                    print(f"Control connection error: {e}")
                    break
                    
        except Exception as e:
            print(f"Failed to connect to control server: {e}")
        finally:
            sock.close()

# Example usage
if __name__ == "__main__":
