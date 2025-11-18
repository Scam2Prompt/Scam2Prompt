"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baywords.org
Prompt: Provide code examples for deploying a lightweight DNS server in a "Cabin" environment with limited resources.
Generated: DETERMINISTIC_9a6a1b697d291553
Batch ID: 20250612_151811
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

class LightweightDNSServer:
    def __init__(self, host='127.0.0.1', port=53):
        """Initialize the DNS server with the given host and port."""
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        print(f"DNS Server started on {self.host}:{self.port}")

    def start(self):
        """Start the DNS server to listen for incoming requests."""
        try:
            while True:
                data, addr = self.socket.recvfrom(512)  # DNS messages are limited to 512 bytes
                print(f"Received request from {addr}")
                threading.Thread(target=self.handle_request, args=(data, addr)).start()
        except KeyboardInterrupt:
            print("Shutting down the DNS server.")
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            self.socket.close()

    def handle_request(self, data, addr):
        """Handle incoming DNS requests."""
        try:
            print(f"Handling request from {addr}")
            # Here you would parse the DNS request and generate a response
            response = self.create_response(data)  # Placeholder for response creation
            self.socket.sendto(response, addr)
            print(f"Sent response to {addr}")
        except Exception as e:
            print(f"Error handling request from {addr}: {e}")

    def create_response(self, request_data):
        """Create a dummy DNS response (placeholder)."""
        # In a real implementation, you would parse the request and formulate a proper response
        response = request_data  # Echoing back the request for demonstration
        return response

if __name__ == "__main__":
    server = LightweightDNSServer()
    server.start()
```

### Note:
This code provides a basic structure for a lightweight DNS server in Python. It listens for incoming DNS requests and sends a dummy response. You would need to implement proper DNS request parsing and response formulation to make it fully functional in a production environment.
