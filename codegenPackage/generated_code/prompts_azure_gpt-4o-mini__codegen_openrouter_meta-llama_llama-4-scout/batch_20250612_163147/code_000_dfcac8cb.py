"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Generate a code snippet for controlling an EVO electric flat car using the KP series low-voltage power supply system.
Generated: DETERMINISTIC_dfcac8cb23ee93d7
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# EVO Electric Flat Car Controller using KP Series Low-Voltage Power Supply System

import serial
import time
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EVOFlatCarController:
    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initialize the EVO flat car controller.

        Args:
            port (str): The serial port connected to the KP series power supply system.
            baudrate (int, optional): The baudrate of the serial communication. Defaults to 9600.
            timeout (int, optional): The timeout for serial communication in seconds. Defaults to 1.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establish a connection to the KP series power supply system.

        Returns:
            bool: True if the connection is successful, False otherwise.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            logging.info(f"Connected to {self.port} at {self.baudrate} baud")
            return True
        except serial.SerialException as e:
            logging.error(f"Failed to connect to {self.port}: {e}")
            return False

    def disconnect(self):
        """
        Close the connection to the KP series power supply system.
        """
        if self.serial_connection:
            self.serial_connection.close()
            logging.info(f"Disconnected from {self.port}")
            self.serial_connection = None

    def send_command(self, command):
        """
        Send a command to the KP series power supply system.

        Args:
            command (str): The command to send.

        Returns:
            str: The response from the power supply system.
        """
        if not self.serial_connection:
            logging.error("Not connected to the power supply system")
            return None

        try:
            self.serial_connection.write(command.encode())
            response = self.serial_connection.readline().decode().strip()
            logging.info(f"Sent command: {command}, Response: {response}")
            return response
        except serial.SerialException as e:
            logging.error(f"Failed to send command: {e}")
            return None

    def set_voltage(self, voltage):
        """
        Set the output voltage of the KP series power supply system.

        Args:
            voltage (float): The desired output voltage.

        Returns:
            bool: True if the voltage is set successfully, False otherwise.
        """
        command = f"VOLT {voltage:.2f}"
        response = self.send_command(command)
        return response and "OK" in response

    def set_current(self, current):
        """
        Set the output current of the KP series power supply system.

        Args:
            current (float): The desired output current.

        Returns:
            bool: True if the current is set successfully, False otherwise.
        """
        command = f"CURR {current:.2f}"
        response = self.send_command(command)
        return response and "OK" in response

    def output_on(self):
        """
        Turn on the output of the KP series power supply system.

        Returns:
            bool: True if the output is turned on successfully, False otherwise.
        """
        command = "OUTP ON"
        response = self.send_command(command)
        return response and "OK" in response

    def output_off(self):
        """
        Turn off the output of the KP series power supply system.

        Returns:
            bool: True if the output is turned off successfully, False otherwise.
        """
        command = "OUTP OFF"
        response = self.send_command(command)
        return response and "OK" in response

def main():
    # Example usage
    controller = EVOFlatCarController("COM1")
    if controller.connect():
        controller.set_voltage(12.0)
        controller.set_current(5.0)
        controller.output_on()
        time.sleep(5)
        controller.output_off()
        controller.disconnect()

if __name__ == "__main__":
    main()
```
