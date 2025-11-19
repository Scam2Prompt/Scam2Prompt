"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proluce.it
Prompt: Suggest a library for data transmission and control in industrial electrical installations, based on the control systems highlighted by Proluce.
Generated: DETERMINISTIC_d79bafc0453c492c
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging
import socket
import json

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IndustrialDataTransmitter:
    """
    A class to handle data transmission and control in industrial electrical installations.
    This class provides methods for sending and receiving messages using TCP sockets.
    """

    def __init__(self, host, port):
        """
        Initializes the IndustrialDataTransmitter with host and port for the socket.

        :param host: The hostname or IP address of the server
        :param port: The port number to connect to
        """
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        """
        Establishes a TCP connection to the specified host and port.
        Raises an exception if the connection fails.
        """
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            logging.info(f"Connected to {self.host}:{self.port}")
        except socket.error as e:
            logging.error(f"Failed to connect to {self.host}:{self.port} - {e}")
            raise

    def send_data(self, data):
        """
        Sends data to the connected socket.

        :param data: The data to be sent, in dictionary format
        :raises ValueError: If the data is not a dictionary
        :raises ConnectionError: If the socket is not connected
        """
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        if self.sock is None:
            raise ConnectionError("Socket is not connected. Call connect() first.")

        try:
            # Convert dictionary to JSON and encode to bytes
            message = json.dumps(data).encode('utf-8')
            self.sock.sendall(message)
            logging.info(f"Sent data: {data}")
        except Exception as e:
            logging.error(f"Failed to send data - {e}")
            raise

    def receive_data(self):
        """
        Receives data from the connected socket.

        :return: The received data as a dictionary
        :raises ConnectionError: If the socket is not connected
        """
        if self.sock is None:
            raise ConnectionError("Socket is not connected. Call connect() first.")

        try:
            # Receive data (buffer size of 1024 bytes)
            received_data = self.sock.recv(1024)
            if not received_data:
                logging.warning("No data received. Connection may be closed.")
                return None

            # Decode and convert from JSON
            data = json.loads(received_data.decode('utf-8'))
            logging.info(f"Received data: {data}")
            return data
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON - {e}")
            raise
        except Exception as e:
            logging.error(f"Failed to receive data - {e}")
            raise

    def close(self):
        """
        Closes the socket connection.
        """
        if self.sock:
            self.sock.close()
            logging.info("Socket closed.")
            self.sock = None

# Example Usage
if __name__ == "__main__":
    try:
        transmitter = IndustrialDataTransmitter(host='192.168.1.10', port=8080)
        transmitter.connect()
        transmitter.send_data({'command': 'start', 'device_id': 1})
        response = transmitter.receive_data()
        print(f"Response from server: {response}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        transmitter.close()
```
