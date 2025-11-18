"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simice-tec-elevators.cz
Prompt: Provide code examples for interfacing with frequency converters like Vacon or Variodyn for elevator systems, as highlighted on Simice-TEC-Elevators.
Generated: DETERMINISTIC_d505c47167a7288f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example demonstrating interfacing with frequency converters (like Vacon or Variodyn) for elevator systems via Modbus TCP, which is commonly used for industrial communication:

```python
import socket
import struct

class FrequencyConverterInterface:
    """
    Interface to communicate with frequency converters via Modbus TCP.
    This example demonstrates reading and writing registers for elevator systems.
    """

    def __init__(self, ip_address: str, port: int = 502):
        """
        Initialize the connection to the frequency converter.

        :param ip_address: IP address of the frequency converter
        :param port: Modbus TCP port (default is 502)
        """
        self.ip_address = ip_address
        self.port = port
        self.sock = None

    def connect(self):
        """
        Establish a connection to the frequency converter.
        """
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(5)  # Set timeout for socket operations
            self.sock.connect((self.ip_address, self.port))
        except socket.error as e:
            raise ConnectionError(f"Failed to connect to frequency converter at {self.ip_address}:{self.port}. Error: {e}")

    def close(self):
        """
        Close the connection to the frequency converter.
        """
        if self.sock:
            self.sock.close()
            self.sock = None

    def read_registers(self, unit_id: int, register_address: int, quantity: int) -> list:
        """
        Read registers from the frequency converter.

        :param unit_id: Modbus Unit ID (slave address)
        :param register_address: Starting register address
        :param quantity: Number of registers to read
        :return: List of register values
        """
        try:
            function_code = 3  # Function code for reading holding registers
            # Construct Modbus TCP frame
            transaction_id = 1  # Transaction ID
            protocol_id = 0     # Modbus protocol
            length = 6          # Length of remaining message
            frame = struct.pack(">HHHBBHH", transaction_id, protocol_id, length, unit_id, function_code, register_address, quantity)

            self.sock.sendall(frame)  # Send request

            # Receive response (8 bytes header + quantity of registers * 2 bytes)
            response = self.sock.recv(1024)  # Adjust buffer size as needed
            if len(response) < 9 + quantity * 2:
                raise ValueError("Incomplete response received from frequency converter.")

            # Extract register values from response
            values = []
            for i in range(quantity):
                value = struct.unpack(">H", response[9 + i * 2:11 + i * 2])[0]
                values.append(value)
            return values
        except socket.error as e:
            raise CommunicationError(f"Error reading registers: {e}")

    def write_register(self, unit_id: int, register_address: int, value: int):
        """
        Write a single register to the frequency converter.

        :param unit_id: Modbus Unit ID (slave address)
        :param register_address: Register address to write to
        :param value: Value to write to the register
        """
        try:
            function_code = 6  # Function code for writing a single register
            # Construct Modbus TCP frame
            transaction_id = 1  # Transaction ID
            protocol_id = 0     # Modbus protocol
            length = 6          # Length of remaining message
            frame = struct.pack(">HHHBBHH", transaction_id, protocol_id, length, unit_id, function_code, register_address, value)

            self.sock.sendall(frame)  # Send request

            # Receive response (should match the request but with confirmation)
            response = self.sock.recv(1024)  # Adjust buffer size as needed
            if len(response) < len(frame):
                raise ValueError("Incomplete response received from frequency converter.")
        except socket.error as e:
            raise CommunicationError(f"Error writing register: {e}")


# Custom exceptions for better error handling
class ConnectionError(Exception):
    pass


class CommunicationError(Exception):
    pass


# Example usage
if __name__ == "__main__":
    try:
        converter = FrequencyConverterInterface(ip_address="192.168.1.100")
        converter.connect()

        # Read registers (example: read 5 registers from address 100)
        registers = converter.read_registers(unit_id=1, register_address=100, quantity=5)
        print(f"Read registers: {registers}")

        # Write a value to a specific register (example: write value 123 to address 101)
        converter.write_register(unit_id=1, register_address=101, value=123)
        print("Write operation completed successfully.")

        converter.close()
    except ConnectionError as ce:
        print(f"Connection error: {ce}")
    except CommunicationError as comm_e:
        print(f"Communication error: {comm_e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

This code is designed to be clean, modular, and reusable. It includes detailed comments for clarity and error handling for robustness.
