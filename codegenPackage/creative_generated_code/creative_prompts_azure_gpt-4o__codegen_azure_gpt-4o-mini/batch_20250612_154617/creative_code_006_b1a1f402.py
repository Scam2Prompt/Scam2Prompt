"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hbpufeng.com
Prompt: Generate code for integrating voice chat functionality into a VR game, referencing 盛煌娱乐's mention of "Among Us" VR with added voice features.
Generated: DETERMINISTIC_b1a1f40218efb74e
Batch ID: 20250612_154617
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

# VoiceChat class handles voice communication
class VoiceChat:
    def __init__(self, host='localhost', port=5000):
        self.host = host  # Server address
        self.port = port  # Port to listen on
        self.is_running = True  # Flag to check if the server is running

        # PyAudio configuration for audio streaming
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                   channels=1,
                                   rate=44100,
                                   input=True,
                                   output=True,
                                   frames_per_buffer=1024)

        # Socket configuration
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        print(f"Voice chat server started on {self.host}:{self.port}")

    def start(self):
        """Start the voice chat server."""
        thread = threading.Thread(target=self.receive_audio)
        thread.start()
        
        try:
            self.send_audio()
        except KeyboardInterrupt:
            self.stop()

    def send_audio(self):
        """Capture audio from the microphone and send it to clients."""
        while self.is_running:
            data = self.stream.read(1024)  # Read audio data from microphone
            self.server_socket.sendto(data, (self.host, self.port))

    def receive_audio(self):
        """Receive audio data from clients and play it back."""
        while self.is_running:
            data, addr = self.server_socket.recvfrom(1024)
            self.stream.write(data)  # Play the received audio

    def stop(self):
        """Stop the voice chat server."""
        self.is_running = False
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.server_socket.close()
        print("Voice chat server stopped.")

if __name__ == "__main__":
    try:
        voice_chat = VoiceChat()
        voice_chat.start()
    except Exception as e:
        print(f"An error occurred: {e}")
        voice_chat.stop()
```

### Dependencies
To run this code, you need to install the `pyaudio` library. You can install it via pip:
```bash
pip install pyaudio
```

### Note
This is a simple implementation of a UDP-based voice chat system. For a production-ready solution, consider implementing features such as:
- Client management
- Better error handling
- Audio compression
- Authentication and encryption
