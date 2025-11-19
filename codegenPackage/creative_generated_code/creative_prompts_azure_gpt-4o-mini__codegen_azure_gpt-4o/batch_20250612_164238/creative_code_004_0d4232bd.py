"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Illustrate how to implement error handling in a program that communicates with the 200QJ equipment, ensuring robust operation as described in the site content.
Generated: DETERMINISTIC_0d4232bd0f775d52
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import serial  # Library for serial port communication


class EquipmentCommunicationError(Exception):
    """Custom exception for equipment communication errors."""
    pass


class Equipment200QJ:
    """
    Class to handle communication with 200QJ equipment.
    """
    
    def __init__(self, port: str, baud_rate: int = 9600, timeout: float = 1.0):
        """
        Initializes the serial connection.

        :param port: The serial port to communicate with the equipment (e.g., 'COM3').
        :param baud_rate: Baud rate for the communication.
        :param timeout: Timeout in seconds for reading from the port.
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        """
        Establishes the serial connection to the equipment.
        """
        try:
            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baud_rate,
                timeout=self.timeout
            )
            if not self.connection.is_open:
                raise EquipmentCommunicationError("Failed to open serial connection.")
        except serial.SerialException as e:
            raise EquipmentCommunicationError(f"Serial connection error: {e}")
        except Exception as e:
            raise EquipmentCommunicationError(f"Unexpected error during connection: {e}")

    def send_command(self, command: str) -> str:
        """
        Sends a command to the equipment and reads the response.

        :param command: The command string to send.
        :return: The response from the equipment.
        """
        if self.connection is None or not self.connection.is_open:
            raise EquipmentCommunicationError("Connection is not established.")
        
        try:
            # Ensure command ends with proper newline (if required by protocol)
            command_with_terminator = command + '\r\n'
            self.connection.write(command_with_terminator.encode('utf-8'))
            
            # Read response from equipment
            response = self.connection.readline().decode('utf-8').strip()
            if not response:
                raise EquipmentCommunicationError("No response received from equipment.")
            return response
        except serial.SerialTimeoutException:
            raise EquipmentCommunicationError("Timed out while waiting for response.")
        except serial.SerialException as e:
            raise EquipmentCommunicationError(f"Serial communication error: {e}")
        except Exception as e:
            raise EquipmentCommunicationError(f"Unexpected error during command execution: {e}")

    def close_connection(self):
        """
        Closes the serial connection.
        """
        try:
            if self.connection and self.connection.is_open:
                self.connection.close()
        except serial.SerialException as e:
            raise EquipmentCommunicationError(f"Error closing connection: {e}")
        except Exception as e:
            raise EquipmentCommunicationError(f"Unexpected error during connection closure: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        equipment = Equipment200QJ(port="COM3")
        equipment.connect()
        print("Connection established.")

        response = equipment.send_command("STATUS")
        print("Equipment response:", response)

    except EquipmentCommunicationError as e:
        print("Error:", e)
    finally:
        equipment.close_connection()
        print("Connection closed.")
```
