"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Generate a code snippet for a remote support tool that can assist users with troubleshooting issues on PCs and mobile devices, similar to the services offered by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_46d3c8513c5e4e86
Batch ID: 20250612_161700
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
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RemoteSupportTool:
    def __init__(self, host='0.0.0.0', port=8080):
        """Initialize the Remote Support Tool server."""
        self.host = host
        self.port = port
        self.server_socket = None

    def start_server(self):
        """Start the server to accept client connections."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        logging.info(f"Server started on {self.host}:{self.port}")

        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                logging.info(f"Connection established with {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
        except Exception as e:
            logging.error(f"Error in server: {e}")
        finally:
            self.shutdown_server()

    def handle_client(self, client_socket):
        """Handle communication with a connected client."""
        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.process_message(client_socket, message)
        except Exception as e:
            logging.error(f"Error handling client: {e}")
        finally:
            client_socket.close()
            logging.info("Client connection closed.")

    def process_message(self, client_socket, message):
        """Process received messages and send troubleshooting advice."""
        try:
            data = json.loads(message)
            command = data.get('command')
            response = self.execute_command(command)
            client_socket.send(json.dumps(response).encode('utf-8'))
        except json.JSONDecodeError:
            logging.warning("Invalid JSON received.")
            client_socket.send(json.dumps({'error': 'Invalid JSON format'}).encode('utf-8'))
        except Exception as e:
            logging.error(f"Error processing message: {e}")
            client_socket.send(json.dumps({'error': str(e)}).encode('utf-8'))

    def execute_command(self, command):
        """Execute troubleshooting commands based on the input from the client."""
        if command == 'check_os':
            return {'os': self.get_os_info()}
        elif command == 'check_disk_space':
            return {'disk_space': self.get_disk_space()}
        else:
            return {'error': 'Unknown command'}

    def get_os_info(self):
        """Retrieve OS information."""
        return os.name

    def get_disk_space(self):
        """Retrieve disk space information."""
        total, used, free = os.statvfs('/').f_frsize * os.statvfs('/').f_blocks, os.statvfs('/').f_frsize * os.statvfs('/').f_bfree, os.statvfs('/').f_frsize * os.statvfs('/').f_bavail
        return {'total': total, 'used': used, 'free': free}

    def shutdown_server(self):
        """Shutdown the server gracefully."""
        if self.server_socket:
            self.server_socket.close()
            logging.info("Server shut down.")

if __name__ == "__main__":
    support_tool = RemoteSupportTool()
    support_tool.start_server()
```
