"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econtrolsa.ch
Prompt: Generate a script to monitor and control electrical systems remotely, including functionalities for télésurveillance and dépannage, as described by eControl SA.
Generated: DETERMINISTIC_0c3fff3f536a68e9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
import socket
import threading
from datetime import datetime

# Set up logging configuration
logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class ElectricalSystem:
    """
    A class to represent an electrical system that can be monitored and controlled remotely.
    """

    def __init__(self, system_id):
        """
        Initializes the electrical system with a unique identifier.

        :param system_id: str - Unique identifier for the electrical system.
        """
        self.system_id = system_id
        self.status = "OFF"  # Initial status of the system
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def switch_on(self):
        """
        Switch on the electrical system.
        """
        with self.lock:
            self.status = "ON"
            logging.info(f"System {self.system_id} switched ON.")

    def switch_off(self):
        """
        Switch off the electrical system.
        """
        with self.lock:
            self.status = "OFF"
            logging.info(f"System {self.system_id} switched OFF.")

    def get_status(self):
        """
        Returns the current status of the electrical system.

        :return: str - Status of the system.
        """
        with self.lock:
            logging.info(f"System {self.system_id} status requested: {self.status}")
            return self.status


class RemoteMonitor:
    """
    A class to manage remote monitoring and control of electrical systems.
    """

    def __init__(self, host, port):
        """
        Initializes the remote monitor with host and port for the server.

        :param host: str - Hostname or IP address to bind the server.
        :param port: int - Port number to bind the server.
        """
        self.host = host
        self.port = port
        self.systems = {}  # Dictionary to hold electrical systems

    def add_system(self, system_id):
        """
        Adds a new electrical system for monitoring.

        :param system_id: str - Unique identifier for the electrical system.
        """
        self.systems[system_id] = ElectricalSystem(system_id)
        logging.info(f"System {system_id} added for monitoring.")

    def handle_client(self, client_socket):
        """
        Handles communication with a client.

        :param client_socket: socket.socket - The connected client socket.
        """
        try:
            request = client_socket.recv(1024).decode('utf-8')
            logging.info(f"Received request: {request}")

            # Simple command processing
            command = json.loads(request)
            system_id = command.get("system_id")
            action = command.get("action")

            if system_id not in self.systems:
                response = {"status": "ERROR", "message": "System not found"}
                logging.warning(f"System {system_id} not found.")
            else:
                system = self.systems[system_id]
                if action == "turn_on":
                    system.switch_on()
                    response = {"status": "OK", "message": "System turned ON"}
                elif action == "turn_off":
                    system.switch_off()
                    response = {"status": "OK", "message": "System turned OFF"}
                elif action == "status":
                    status = system.get_status()
                    response = {"status": "OK", "system_id": system_id, "current_status": status}
                else:
                    response = {"status": "ERROR", "message": "Invalid action"}
                    logging.warning(f"Invalid action requested: {action}")

            client_socket.send(json.dumps(response).encode('utf-8'))
            logging.info(f"Sent response: {response}")

        except Exception as e:
            logging.error(f"Error handling client: {e}")
            client_socket.send(json.dumps({"status": "ERROR", "message": "Internal server error"}).encode('utf-8'))
        finally:
            client_socket.close()

    def start_server(self):
        """
        Starts the server to listen for incoming client connections.
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        logging.info(f"Server listening on {self.host}:{self.port}")

        try:
            while True:
                client_socket, addr = server_socket.accept()
                logging.info(f"Accepted connection from {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
        except Exception as e:
            logging.error(f"Server error: {e}")
        finally:
            server_socket.close()


if __name__ == "__main__":
    monitor = RemoteMonitor(host='0.0.0.0', port=8080)
    # Example adding systems for monitoring
    monitor.add_system('System001')
    monitor.add_system('System002')
    
    # Start the server
    monitor.start_server()
```
