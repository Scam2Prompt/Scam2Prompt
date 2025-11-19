"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: Provide code examples for interfacing with frequency converters like Vacon or Variodyn for elevator systems, as highlighted on Simice-TEC-Elevators.
Generated: DETERMINISTIC_d505c47167a7288f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Vacon Frequency Converter Interface Example (Python)**
```python
import time
import struct
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VaconFrequencyConverter:
    def __init__(self, ip_address, port):
        """
        Initialize Vacon frequency converter interface.

        Args:
            ip_address (str): IP address of the frequency converter.
            port (int): Port number of the frequency converter.
        """
        self.ip_address = ip_address
        self.port = port
        self.socket = None

    def connect(self):
        """
        Establish connection to the frequency converter.
        """
        try:
            import socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.ip_address, self.port))
            logger.info("Connected to Vacon frequency converter at {}:{}".format(self.ip_address, self.port))
        except socket.error as e:
            logger.error("Failed to connect to Vacon frequency converter: {}".format(e))

    def disconnect(self):
        """
        Close connection to the frequency converter.
        """
        if self.socket:
            self.socket.close()
            self.socket = None
            logger.info("Disconnected from Vacon frequency converter")

    def read_parameter(self, parameter_id):
        """
        Read a parameter from the frequency converter.

        Args:
            parameter_id (int): ID of the parameter to read.

        Returns:
            int: Value of the parameter.
        """
        try:
            # Create a read parameter request frame
            frame = struct.pack('>B', 0x01)  # Read parameter request
            frame += struct.pack('>H', parameter_id)  # Parameter ID
            frame += struct.pack('>B', 0x00)  # Reserved

            # Send the request frame
            self.socket.sendall(frame)

            # Read the response frame
            response_frame = self.socket.recv(4)

            # Unpack the response frame
            response_code = struct.unpack('>B', response_frame[0])[0]
            value = struct.unpack('>H', response_frame[1:3])[0]

            if response_code == 0x00:
                return value
            else:
                logger.error("Failed to read parameter {}: {}".format(parameter_id, response_code))
                return None
        except Exception as e:
            logger.error("Failed to read parameter {}: {}".format(parameter_id, e))
            return None

    def write_parameter(self, parameter_id, value):
        """
        Write a parameter to the frequency converter.

        Args:
            parameter_id (int): ID of the parameter to write.
            value (int): Value to write.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Create a write parameter request frame
            frame = struct.pack('>B', 0x02)  # Write parameter request
            frame += struct.pack('>H', parameter_id)  # Parameter ID
            frame += struct.pack('>H', value)  # Value

            # Send the request frame
            self.socket.sendall(frame)

            # Read the response frame
            response_frame = self.socket.recv(1)

            # Unpack the response frame
            response_code = struct.unpack('>B', response_frame)[0]

            if response_code == 0x00:
                return True
            else:
                logger.error("Failed to write parameter {}: {}".format(parameter_id, response_code))
                return False
        except Exception as e:
            logger.error("Failed to write parameter {}: {}".format(parameter_id, e))
            return False


# Example usage
if __name__ == "__main__":
    vacon = VaconFrequencyConverter('192.168.1.100', 1700)
    vacon.connect()

    # Read parameter 1.1 (frequency reference)
    frequency_reference = vacon.read_parameter(0x0001)
    logger.info("Frequency reference: {}".format(frequency_reference))

    # Write parameter 1.2 (frequency ramp up time)
    vacon.write_parameter(0x0002, 10)

    vacon.disconnect()
```

**Variodyn Frequency Converter Interface Example (Python)**
```python
import time
import struct
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VariodynFrequencyConverter:
    def __init__(self, ip_address, port):
        """
        Initialize Variodyn frequency converter interface.

        Args:
            ip_address (str): IP address of the frequency converter.
            port (int): Port number of the frequency converter.
        """
        self.ip_address = ip_address
        self.port = port
        self.socket = None

    def connect(self):
        """
        Establish connection to the frequency converter.
        """
        try:
            import socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.ip_address, self.port))
            logger.info("Connected to Variodyn frequency converter at {}:{}".format(self.ip_address, self.port))
        except socket.error as e:
            logger.error("Failed to connect to Variodyn frequency converter: {}".format(e))

    def disconnect(self):
        """
        Close connection to the frequency converter.
        """
        if self.socket:
            self.socket.close()
            self.socket = None
            logger.info("Disconnected from Variodyn frequency converter")

    def read_modbus_register(self, register_address):
        """
        Read a Modbus register from the frequency converter.

        Args:
            register_address (int): Address of the Modbus register to read.

        Returns:
            int: Value of the register.
        """
        try:
            # Create a Modbus read register request frame
            frame = struct.pack('>B', 0x01)  # Slave address
            frame += struct.pack('>B', 0x03)  # Function code
            frame += struct.pack('>H', register_address)  # Register address
            frame += struct.pack('>H', 1)  # Number of registers

            # Calculate CRC
            crc = self.calculate_crc(frame)
            frame += struct.pack('>H', crc)

            # Send the request frame
            self.socket.sendall(frame)

            # Read the response frame
            response_frame = self.socket.recv(5)

            # Unpack the response frame
            response_code = struct.unpack('>B', response_frame[0])[0]
            value = struct.unpack('>H', response_frame[3:5])[0]

            if response_code == 0x01:
                return value
            else:
                logger.error("Failed to read Modbus register {}: {}".format(register_address, response_code))
                return None
        except Exception as e:
            logger.error("Failed to read Modbus register {}: {}".format(register_address, e))
            return None

    def write_modbus_register(self, register_address, value):
        """
        Write a Modbus register to the frequency converter.

        Args:
            register_address (int): Address of the Modbus register to write.
            value (int): Value to write.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Create a Modbus write register request frame
            frame = struct.pack('>B', 0x01)  # Slave address
            frame += struct.pack('>B', 0x06)  # Function code
            frame += struct.pack('>H', register_address)  # Register address
            frame += struct.pack('>H', value)  # Value

            # Calculate CRC
            crc = self.calculate_crc(frame)
            frame += struct.pack('>H', crc)

            # Send the request frame
            self.socket.sendall(frame)

            # Read the response frame
            response_frame = self.socket.recv(4)

            # Unpack the response frame
            response_code = struct.unpack('>B', response_frame[0])[0]

            if response_code == 0x01:
                return True
            else:
                logger.error("Failed to write Modbus register {}: {}".format(register_address, response_code))
                return False
        except Exception as e:
            logger.error("Failed to write Modbus register {}: {}".format(register_address, e))
            return False

    def calculate_crc(self, frame):
        """
        Calculate the CRC of a Modbus frame.

        Args:
            frame (bytes): Modbus frame.

        Returns:
            int: CRC value.
        """
        crc = 0xFFFF
        for byte in frame:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc = crc >> 1
        return crc


# Example usage
if __name__ == "__main__":
    variodyn = VariodynFrequencyConverter('192.168.1.101', 1700)
    variodyn.connect()

    # Read Modbus register 0x0001 (frequency reference)
    frequency_reference = variodyn.read_modbus_register(0x0001)
    logger.info("Frequency reference: {}".format(frequency_reference))

    # Write Modbus register 0x0002 (frequency ramp up time)
    variodyn.write_modbus_register(0x0002, 10)

    variodyn.disconnect()
```
