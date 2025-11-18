"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Provide code to interface with Hengstler high-voltage relays (e.g., 507 or 509 series) for switching in electrical systems.
Generated: DETERMINISTIC_55f56428ab425056
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
import serial

# Configure logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HengstlerRelay:
    """
    A class to interface with Hengstler high-voltage relays.
    
    Attributes:
        port (str): The serial port to which the relay is connected.
        baudrate (int): The baud rate for serial communication.
        timeout (int): The timeout for serial communication.
    """
    
    def __init__(self, port: str, baudrate: int = 9600, timeout: int = 1):
        """
        Initializes the HengstlerRelay class with the specified serial port parameters.
        
        Args:
            port (str): Serial port for connecting to the relay.
            baudrate (int, optional): Baud rate for the serial connection. Default is 9600.
            timeout (int, optional): Timeout for serial communication in seconds. Default is 1.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None
        self._connect()

    def _connect(self):
        """Establishes a serial connection to the relay."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            logging.info(f"Connected to relay on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            logging.error(f"Failed to connect to relay: {e}")
            raise

    def switch_on(self):
        """Sends command to switch the relay ON."""
        self._send_command('ON')

    def switch_off(self):
        """Sends command to switch the relay OFF."""
        self._send_command('OFF')

    def _send_command(self, command: str):
        """
        Sends a command to the relay and checks for acknowledgment.
        
        Args:
            command (str): The command to send ('ON' or 'OFF').
        """
        if command not in ['ON', 'OFF']:
            logging.error("Invalid command. Use 'ON' or 'OFF'.")
            return
        
        try:
            self.serial_connection.write(command.encode('utf-8'))
            logging.info(f"Sent command: {command}")
            time.sleep(0.1)  # Short delay to allow for processing
            response = self.serial_connection.readline().decode('utf-8').strip()
            if response == 'ACK':
                logging.info(f"Command '{command}' acknowledged.")
            else:
                logging.warning(f"Unexpected response: {response}")
        except Exception as e:
            logging.error(f"Error sending command '{command}': {e}")
            raise

    def close(self):
        """Closes the serial connection to the relay."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            logging.info("Serial connection closed.")

# Example usage:
if __name__ == "__main__":
    try:
        relay = HengstlerRelay(port='/dev/ttyUSB0')  # Update with your actual port
        relay.switch_on()
        time.sleep(5)  # Keep the relay on for 5 seconds
        relay.switch_off()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        relay.close()
```
