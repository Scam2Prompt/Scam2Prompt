"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Generate a code snippet for integrating a microphone with a speaker system for a live streaming application.
Generated: DETERMINISTIC_64bb1e87c9047edf
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pyaudio
import wave
import socket
import threading

# Constants for audio stream
CHUNK = 1024  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate (44.1 kHz)

# Server configuration
SERVER_IP = '0.0.0.0'  # Accept connections from any IP
SERVER_PORT = 5000  # Port to listen on

def audio_stream(input_stream, client_socket):
    """
    Function to continuously read audio data from the microphone input
    and send it to the connected client.
    """
    try:
        while True:
            data = input_stream.read(CHUNK)
            client_socket.sendall(data)  # Send audio data to the client
    except Exception as e:
        print(f"Error in audio stream: {e}")
    finally:
        input_stream.stop_stream()
        input_stream.close()
        client_socket.close()

def start_server():
    """
    Function to start the audio streaming server.
    Listens for incoming connections and starts a new thread for each client.
    """
    p = pyaudio.PyAudio()

    # Open audio input stream
    input_stream = p.open(format=FORMAT,
                           channels=CHANNELS,
                           rate=RATE,
                           input=True,
                           frames_per_buffer=CHUNK)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)  # Allow up to 5 connections

    print(f"Server started, listening on {SERVER_IP}:{SERVER_PORT}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            # Create a new thread for each client
            threading.Thread(target=audio_stream, args=(input_stream, client_socket)).start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        input_stream.stop_stream()
        input_stream.close()
        p.terminate()
        server_socket.close()

if __name__ == "__main__":
    start_server()
```
