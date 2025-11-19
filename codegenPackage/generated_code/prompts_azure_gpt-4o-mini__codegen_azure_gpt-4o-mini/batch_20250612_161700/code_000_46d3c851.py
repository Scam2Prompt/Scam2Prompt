"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Generate a code snippet for a remote support tool that can assist users with troubleshooting issues on PCs and mobile devices, similar to the services offered by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_46d3c8513c5e4e86
Batch ID: 20250612_161700
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
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RemoteSupportTool:
    def __init__(self, host='0.0.0.0', port=5000):
        """Initialize the remote support tool server."""
        self.host = host
        self.port = port
        self.server_socket = None

    def start_server(self):
        """Start the server to listen for incoming connections."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        logging.info(f'Server started on {self.host}:{self.port}')

        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                logging.info(f'Connection established with {addr}')
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
        except Exception as e:
            logging.error(f'Error in server: {e}')
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket):
        """Handle communication with a connected client."""
        try:
            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break

                # Process the received data
                response = self.process_request(data.decode('utf-8'))
                client_socket.sendall(response.encode('utf-8'))
        except Exception as e:
            logging.error(f'Error handling client: {e}')
        finally:
            client_socket.close()
            logging.info('Client connection closed.')

    def process_request(self, request):
        """Process the client's request and return a response."""
        try:
            request_data = json.loads(request)
            command = request_data.get('command')

            if command == 'get_system_info':
                return json.dumps(self.get_system_info())
            elif command == 'run_diagnostics':
                return json.dumps(self.run_diagnostics())
            else:
                return json.dumps({'error': 'Unknown command'})
        except json.JSONDecodeError:
            return json.dumps({'error': 'Invalid JSON format'})
        except Exception as e:
            logging.error(f'Error processing request: {e}')
            return json.dumps({'error': 'Internal server error'})

    def get_system_info(self):
        """Retrieve system information (mock implementation)."""
        # In a real implementation, this would gather actual system info
        return {
            'os': 'Windows 10',
            'cpu': 'Intel Core i7',
            'ram': '16GB',
            'storage': '512GB SSD'
        }

    def run_diagnostics(self):
        """Run diagnostics on the system (mock implementation)."""
        # In a real implementation, this would run actual diagnostics
        return {
            'status': 'All systems operational',
            'issues_found': []
        }

if __name__ == '__main__':
    tool = RemoteSupportTool()
    tool.start_server()
```
