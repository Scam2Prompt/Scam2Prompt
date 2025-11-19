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
import serial
import time
import logging
from typing import Optional

class EVOFlatCarController:
    """
    Controller for EVO electric flat car using KP series low-voltage power supply.
    Handles communication via serial interface for motor control and status monitoring.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initialize the controller with serial connection parameters.
        
        Args:
            port: Serial port name (e.g., 'COM3' or '/dev/ttyUSB0')
            baudrate: Baud rate for serial communication (default: 9600)
            timeout: Serial read timeout in seconds (default: 1.0)
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn: Optional[serial.Serial] = None
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        """Configure and return a logger instance."""
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def connect(self) -> bool:
        """Establish serial connection to the power supply system."""
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            time.sleep(2)  # Allow time for connection to stabilize
            self.logger.info(f"Connected to {self.port} at {self.baudrate} baud")
            return True
        except serial.SerialException as e:
            self.logger.error(f"Failed to connect: {e}")
            return False

    def disconnect(self) -> None:
        """Close the serial connection if it's open."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            self.logger.info("Serial connection closed")

    def send_command(self, command: str) -> Optional[str]:
        """
        Send a command to the power supply system and return the response.
        
        Args:
            command: Command string to send (without checksum or terminator)
        
        Returns:
            Response from the device or None if error occurred
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            self.logger.error("Serial connection not established")
            return None

        try:
            # Add checksum and terminator (example format, adjust per protocol)
            full_command = f"${command}*{self._calculate_checksum(command)}\r\n"
            self.serial_conn.write(full_command.encode('ascii'))
            self.logger.debug(f"Sent command: {full_command.strip()}")

            # Read response (adjust based on actual protocol)
            response = self.serial_conn.readline().decode('ascii').strip()
            self.logger.debug(f"Received response: {response}")

            if not self._validate_response(response):
                self.logger.error("Invalid response received")
                return None

            return response
        except serial.SerialException as e:
            self.logger.error(f"Communication error: {e}")
            return None

    def _calculate_checksum(self, data: str) -> str:
        """Calculate simple XOR checksum for command validation."""
        checksum = 0
        for char in data:
            checksum ^= ord(char)
        return f"{checksum:02X}"

    def _validate_response(self, response: str) -> bool:
        """Validate the response format and checksum."""
        if not response or len(response) < 4:
            return False
        
        if response[0] != '$' or '*' not in response:
            return False

        # Extract checksum and verify
        try:
            cmd_part, checksum_part = response[1:].split('*', 1)
            expected_checksum = self._calculate_checksum(cmd_part)
            return checksum_part.upper() == expected_checksum
        except ValueError:
            return False

    def set_motor_speed(self, speed: int) -> bool:
        """
        Set motor speed (0-100%).
        
        Args:
            speed: Desired speed percentage (0-100)
        
        Returns:
            True if command was successful, False otherwise
        """
        if not 0 <= speed <= 100:
            self.logger.error("Speed must be between 0 and 100")
            return False

        response = self.send_command(f"SPD{speed:03d}")
        return response is not None and "ACK" in response

    def get_status(self) -> Optional[dict]:
        """
        Request and parse current system status.
        
        Returns:
            Dictionary of status parameters or None if failed
        """
        response = self.send_command("STATUS")
        if not response:
            return None

        try:
            # Example status parsing (adjust based on actual protocol)
            status_parts = response[1:].split('*')[0].split(',')
            return {
                'voltage': float(status_parts[0]),
                'current': float(status_parts[1]),
                'temperature': float(status_parts[2]),
                'fault_code': int(status_parts[3]) if status_parts[3] else 0
            }
        except (IndexError, ValueError) as e:
            self.logger.error(f"Failed to parse status: {e}")
            return None

    def emergency_stop(self) -> bool:
        """Trigger emergency stop and return success status."""
        response = self.send_command("ESTOP")
        return response is not None and "ACK" in response

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()
```
