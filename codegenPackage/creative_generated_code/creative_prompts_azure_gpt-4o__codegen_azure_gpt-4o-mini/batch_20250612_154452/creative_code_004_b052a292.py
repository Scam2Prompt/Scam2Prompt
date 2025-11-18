"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.flyvirtualfrontier.net
Prompt: Develop a custom ACARS system similar to WILDCARS, focusing on practical flight tracking and integration with multiple flight simulation platforms.
Generated: DETERMINISTIC_b052a292ca13962f
Batch ID: 20250612_154452
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
import time
from typing import Dict, Any

class ACARSMessage:
    """Class to represent an ACARS message."""
    
    def __init__(self, message_type: str, content: Dict[str, Any]):
        self.message_type = message_type
        self.content = content

    def to_json(self) -> str:
        """Convert the ACARS message to a JSON string."""
        return json.dumps({
            'type': self.message_type,
            'content': self.content
        })

class FlightTracker:
    """Class to track flights and send ACARS messages."""
    
    def __init__(self):
        self.flights = {}

    def update_flight(self, flight_id: str, position: Dict[str, float]):
        """Update flight position in the tracker."""
        self.flights[flight_id] = position

    def get_flight_info(self, flight_id: str) -> Dict[str, Any]:
        """Get information about a specific flight."""
        return {'flight_id': flight_id, 'position': self.flights.get(flight_id, None)}

class ACARSServer:
    """Class to create an ACARS server."""
    
    def __init__(self, host: str, port: int):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        self.flight_tracker = FlightTracker()

    def start(self):
        """Start the ACARS server."""
        print("ACARS Server started. Waiting for connections...")
        while True:
            try:
                client_socket, address = self.server_socket.accept()
                print(f"Connection established with {address}")
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
            except Exception as e:
                print(f"Error accepting connection: {e}")

    def handle_client(self, client_socket: socket.socket):
        """Handle communication with a connected client."""
        with client_socket:
            while True:
                try:
                    data = client_socket.recv(1024).decode()
                    if not data:
                        break
                    
                    self.process_message(data)
                except Exception as e:
                    print(f"Error while handling client: {e}")
                    break

    def process_message(self, message: str):
        """Process incoming messages from clients."""
        try:
            acars_msg = json.loads(message)
            if acars_msg['type'] == 'update':
                self.flight_tracker.update_flight(acars_msg['content']['flight_id'], acars_msg['content']['position'])
                print(f"Flight updated: {acars_msg['content']}")
            else:
                print(f"Unknown message type: {acars_msg['type']}")
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON message: {e}")
        except KeyError as e:
            print(f"Missing key in message: {e}")

if __name__ == "__main__":
    try:
        # Customize host and port as needed
        HOST, PORT = '127.0.0.1', 5000
        acars_server = ACARSServer(HOST, PORT)
        acars_server.start()
    except Exception as e:
        print(f"Server failed to start: {e}")
```

This code implements a simple ACARS system that can track flights and process messages. It uses sockets for client-server communication, and messages are processed in a separate thread for each client connection. The code is structured, documented, and includes error handling to ensure robustness. Adjust the host and port as needed for your specific environment.
