"""
Generated Code Metadata:
========================
Original URL: https://www.association-easycap.fr
Prompt: Develop a program that interfaces with the Unitable or Whizz’Table equipment mentioned by Association Easy'cap, ensuring compatibility with drone technology.
Generated: DETERMINISTIC_f2233c0ca4842f71
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial
import json
from typing import Optional, Dict, Any
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EquipmentType(Enum):
    """Enumeration for supported equipment types."""
    UNITABLE = "Unitable"
    WHIZZ_TABLE = "Whizz'Table"

class DroneEquipmentInterface:
    """
    A class to interface with Unitable or Whizz'Table equipment for drone technology.
    
    Attributes:
        port (str): The serial port to connect to the equipment.
        baudrate (int): The baud rate for serial communication.
        timeout (float): The timeout for serial communication.
        equipment_type (EquipmentType): The type of equipment being interfaced.
        serial_conn (serial.Serial): The serial connection object.
    """
    
    def __init__(
        self,
        port: str,
        baudrate: int = 9600,
        timeout: float = 1.0,
        equipment_type: EquipmentType = EquipmentType.UNITABLE
    ):
        """
        Initialize the DroneEquipmentInterface.
        
        Args:
            port: The serial port to connect to the equipment.
            baudrate: The baud rate for serial communication. Default is 9600.
            timeout: The timeout for serial communication. Default is 1.0.
            equipment_type: The type of equipment. Default is Unitable.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.equipment_type = equipment_type
        self.serial_conn: Optional[serial.Serial] = None

    def connect(self) -> bool:
        """
        Establish a serial connection to the equipment.
        
        Returns:
            bool: True if connection is successful, False otherwise.
        """
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            logger.info(f"Connected to {self.equipment_type.value} on {self.port}")
            return True
        except serial.SerialException as e:
            logger.error(f"Failed to connect to {self.equipment_type.value}: {e}")
            return False

    def disconnect(self) -> None:
        """Close the serial connection if it is open."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            logger.info(f"Disconnected from {self.equipment_type.value}")

    def send_command(self, command: str) -> Optional[str]:
        """
        Send a command to the equipment and return the response.
        
        Args:
            command: The command string to send.
            
        Returns:
            Optional[str]: The response from the equipment, or None if failed.
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            logger.error("Serial connection is not open")
            return None

        try:
            self.serial_conn.write(command.encode('utf-8'))
            response = self.serial_conn.readline().decode('utf-8').strip()
            logger.debug(f"Command '{command}' received response: '{response}'")
            return response
        except serial.SerialException as e:
            logger.error(f"Error sending command '{command}': {e}")
            return None

    def get_status(self) -> Optional[Dict[str, Any]]:
        """
        Get the current status of the equipment.
        
        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the status, or None if failed.
        """
        response = self.send_command("STATUS")
        if response is None:
            return None

        try:
            status = json.loads(response)
            return status
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse status response: {e}")
            return None

    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.disconnect()

# Example usage
if __name__ == "__main__":
    # Replace with actual port and equipment type
    PORT = "/dev/ttyUSB0"
    EQUIPMENT_TYPE = EquipmentType.UNITABLE

    with DroneEquipmentInterface(PORT, equipment_type=EQUIPMENT_TYPE) as interface:
        status = interface.get_status()
        if status:
            print(f"Equipment Status: {status}")
        else:
            print("Failed to retrieve equipment status")
```
