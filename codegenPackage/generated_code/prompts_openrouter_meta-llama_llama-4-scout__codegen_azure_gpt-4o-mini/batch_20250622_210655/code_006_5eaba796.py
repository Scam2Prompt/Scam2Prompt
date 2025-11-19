"""
Generated Code Metadata:
========================
Original URL: https://fullport.net
Prompt: Develop a code to configure and test a network cable (e.g., CAT5, CAT6) using a network testing device.
Generated: DETERMINISTIC_5eaba796a0bc5934
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkCableTester:
    def __init__(self, ip_address: str, port: int):
        """
        Initialize the NetworkCableTester with the given IP address and port.
        
        :param ip_address: The IP address of the network testing device.
        :param port: The port number to connect to the device.
        """
        self.ip_address = ip_address
        self.port = port
        self.connection = None

    def connect(self):
        """
        Establish a connection to the network testing device.
        """
        try:
            self.connection = socket.create_connection((self.ip_address, self.port), timeout=5)
            logging.info("Successfully connected to the network testing device.")
        except socket.error as e:
            logging.error(f"Connection failed: {e}")
            raise

    def test_cable(self):
        """
        Test the network cable by sending a test signal and waiting for a response.
        
        :return: True if the cable is functioning correctly, False otherwise.
        """
        if not self.connection:
            logging.error("Connection not established. Please connect first.")
            return False
        
        try:
            # Send a test signal
            test_signal = b'Test Cable'
            self.connection.sendall(test_signal)
            logging.info("Test signal sent.")

            # Wait for a response
            response = self.connection.recv(1024)
            logging.info("Response received from the device.")

            if response == b'Cable OK':
                logging.info("Cable test passed.")
                return True
            else:
                logging.warning("Cable test failed.")
                return False
        except socket.error as e:
            logging.error(f"Error during cable test: {e}")
            return False

    def disconnect(self):
        """
        Close the connection to the network testing device.
        """
        if self.connection:
            self.connection.close()
            logging.info("Connection closed.")

def main():
    # Example usage of the NetworkCableTester
    tester = NetworkCableTester(ip_address='192.168.1.100', port=8080)

    try:
        tester.connect()
        if tester.test_cable():
            logging.info("Cable is functioning properly.")
        else:
            logging.info("Cable is not functioning properly.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        tester.disconnect()

if __name__ == "__main__":
    main()
```
