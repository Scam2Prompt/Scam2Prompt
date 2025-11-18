"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3portal.com
Prompt: Generate code for creating a peer-to-peer (P2P) network that embodies the principles of Web3 as described on Lume Web, focusing on decentralization and user ownership.
Generated: DETERMINISTIC_45509dd7805bf574
Batch ID: 20250612_154703
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
import json
import os


class Peer:
    def __init__(self, host='127.0.0.1', port=5000):
        """Initialize the Peer with given host and port."""
        self.host = host
        self.port = port
        self.peers = set()
        self.server_socket = self.create_server_socket()

    def create_server_socket(self):
        """Create a server socket to listen for incoming connections."""
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"Listening for connections on {self.host}:{self.port}")
            return server_socket
        except Exception as e:
            print(f"Error creating server socket: {e}")
            raise

    def accept_connections(self):
        """Accept incoming connections and start a new thread for each."""
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Connection from {address} has been established.")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        """Handle communication with the connected client."""
        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.process_message(message)
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()

    def process_message(self, message):
        """Process incoming messages from other peers."""
        try:
            data = json.loads(message)
            if 'peers' in data:
                self.peers.update(data['peers'])
            print(f"Updated peers list: {self.peers}")
        except json.JSONDecodeError:
            print("Received non-JSON message.")

    def broadcast(self, message):
        """Broadcast a message to all connected peers."""
        for peer in self.peers:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(peer)
                    s.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message to {peer}: {e}")

    def start(self):
        """Start the Peer and accept incoming connections."""
        threading.Thread(target=self.accept_connections, daemon=True).start()
        print("Peer is now running.")
        

def main():
    """Main function to start the peer-to-peer network."""
    host = os.getenv('PEER_HOST', '127.0.0.1')  # Use environment variable or default to localhost
    port = int(os.getenv('PEER_PORT', 5000))     # Use environment variable or default port 5000

    peer = Peer(host, port)
    peer.start()

    # Keep the script running
    try:
        while True:
            command = input("Enter 'exit' to quit: ")
            if command.lower() == 'exit':
                break
    except KeyboardInterrupt:
        pass
    finally:
        print("Shutting down the peer...")

if __name__ == '__main__':
    main()
```

This code implements a simple peer-to-peer networking application in Python that embodies decentralization principles by allowing peers to communicate and share their lists of connected peers. The application includes error handling, threading for concurrency, and basic JSON message processing.
