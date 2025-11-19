"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Develop a simple program to interface with the Nordson DuraDrum bulk melter for monitoring temperature and pressure.
Generated: DETERMINISTIC_d7e016a1ba729acb
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import json
import logging
from time import sleep

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NordsonDuraDrumInterface:
    """
    A class to interface with the Nordson DuraDrum bulk melter for monitoring temperature and pressure.
    """

    def __init__(self, host: str, port: int):
        """
        Initializes the NordsonDuraDrumInterface with the specified host and port.

        :param host: The IP address of the Nordson DuraDrum.
        :param port: The port number to connect to.
        """
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the Nordson DuraDrum.
        """
        try:
            self.connection = socket.create_connection((self.host, self.port))
            logging.info("Connected to Nordson DuraDrum at %s:%d", self.host, self.port)
        except Exception as e:
            logging.error("Failed to connect to Nordson DuraDrum: %s", e)
            raise

    def disconnect(self):
        """
        Closes the connection to the Nordson DuraDrum.
        """
        if self.connection:
            self.connection.close()
            logging.info("Disconnected from Nordson DuraDrum.")

    def get_status(self):
        """
        Retrieves the current temperature and pressure from the Nordson DuraDrum.

        :return: A dictionary containing temperature and pressure.
        :raises RuntimeError: If there is an error in communication.
        """
        try:
            # Send a request for status
            self.connection.sendall(b'GET_STATUS\n')
            response = self.connection.recv(1024).decode('utf-8')
            status = json.loads(response)
            logging.info("Received status: %s", status)
            return status
        except Exception as e:
            logging.error("Error retrieving status: %s", e)
            raise RuntimeError("Failed to get status from Nordson DuraDrum.")

    def monitor(self, interval: int):
        """
        Continuously monitors the temperature and pressure at specified intervals.

        :param interval: Time in seconds between each status check.
        """
        try:
            while True:
                status = self.get_status()
                temperature = status.get('temperature')
                pressure = status.get('pressure')
                logging.info("Current Temperature: %s °C, Current Pressure: %s psi", temperature, pressure)
                sleep(interval)
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error("Monitoring error: %s", e)
        finally:
            self.disconnect()

if __name__ == "__main__":
    # Example usage
    HOST = '192.168.1.100'  # Replace with the actual IP address of the Nordson DuraDrum
    PORT = 12345             # Replace with the actual port number

    try:
        melter = NordsonDuraDrumInterface(HOST, PORT)
        melter.connect()
        melter.monitor(interval=5)  # Monitor every 5 seconds
    except Exception as e:
        logging.critical("Critical error: %s", e)
```
