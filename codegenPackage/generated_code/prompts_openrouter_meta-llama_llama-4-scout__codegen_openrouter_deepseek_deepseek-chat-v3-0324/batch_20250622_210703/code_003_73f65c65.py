"""
Generated Code Metadata:
========================
Original URL: https://firegoto.com.br
Prompt: "Explain how to configure and calibrate a FireGoTo system for use with a SkySafari planetarium software."
Generated: DETERMINISTIC_73f65c65de74ba0d
Batch ID: 20250622_210703
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
import sys
from typing import Optional, Tuple

class FireGoToConfigurator:
    """
    A class to handle configuration and calibration of a FireGoTo system for SkySafari.
    """
    
    def __init__(self, port: str, baudrate: int = 9600, timeout: int = 5):
        """
        Initialize the FireGoTo connection.
        
        Args:
            port: Serial port name (e.g., 'COM3' or '/dev/ttyUSB0')
            baudrate: Baud rate for serial communication (default 9600)
            timeout: Serial timeout in seconds (default 5)
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None
        
    def connect(self) -> bool:
        """
        Establish connection to FireGoTo system.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            time.sleep(2)  # Allow time for connection to establish
            return True
        except serial.SerialException as e:
            print(f"Connection error: {e}")
            return False
            
    def disconnect(self) -> None:
        """Close the serial connection."""
        if self.connection and self.connection.is_open:
            self.connection.close()
            
    def send_command(self, command: str) -> Optional[str]:
        """
        Send a command to the FireGoTo system and return response.
        
        Args:
            command: The command string to send
            
        Returns:
            str: Response from the device or None if error
        """
        if not self.connection or not self.connection.is_open:
            print("Not connected to FireGoTo system")
            return None
            
        try:
            self.connection.write(f"{command}\r".encode())
            time.sleep(0.5)  # Wait for response
            response = self.connection.read_all().decode().strip()
            return response if response else None
        except serial.SerialException as e:
            print(f"Communication error: {e}")
            return None
            
    def configure_for_skysafari(self) -> bool:
        """
        Configure FireGoTo system for SkySafari compatibility.
        
        Returns:
            bool: True if configuration successful, False otherwise
        """
        commands = [
            ":U#",  # Unpark telescope
            ":AL#",  # Align telescope
            ":SX01,1#",  # Enable SkySafari protocol
            ":SX02,1#",  # Enable tracking
            ":SX03,1#",  # Enable GPS if available
            ":SX04,1#"   # Enable encoders
        ]
        
        for cmd in commands:
            response = self.send_command(cmd)
            if not response or "0" in response:  # Many commands return "1" for success
                print(f"Configuration failed on command: {cmd}")
                return False
                
        return True
        
    def calibrate_alignment(self) -> Tuple[bool, str]:
        """
        Perform alignment calibration for the FireGoTo system.
        
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        # Step 1: Center alignment star
        print("Please center the alignment star in the eyepiece")
        time.sleep(5)  # Give user time to center
        
        # Step 2: Confirm alignment
        response = self.send_command(":A1#")
        if not response or "1" not in response:
            return (False, "First alignment star failed")
            
        # Step 3: Second alignment star
        print("Please center the second alignment star")
        time.sleep(5)
        
        response = self.send_command(":A2#")
        if not response or "1" not in response:
            return (False, "Second alignment star failed")
            
        return (True, "Alignment calibration successful")
        
    def verify_connection(self) -> bool:
        """
        Verify connection to SkySafari by checking telescope status.
        
        Returns:
            bool: True if verification successful, False otherwise
        """
        response = self.send_command(":Gstat#")
        return response is not None and "1" in response


def main():
    """
    Main function to demonstrate FireGoTo configuration for SkySafari.
    """
    # Example usage - replace with actual port
    configurator = FireGoToConfigurator(port="/dev/ttyUSB0")
    
    try:
        if not configurator.connect():
            print("Failed to connect to FireGoTo system")
            sys.exit(1)
            
        print("Configuring FireGoTo for SkySafari...")
        if not configurator.configure_for_skysafari():
            print("Configuration failed")
            sys.exit(1)
            
        print("Performing alignment calibration...")
        success, message = configurator.calibrate_alignment()
        if not success:
            print(f"Calibration failed: {message}")
            sys.exit(1)
            
        print("Verifying SkySafari connection...")
        if not configurator.verify_connection():
            print("Verification failed")
            sys.exit(1)
            
        print("FireGoTo successfully configured for SkySafari!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        configurator.disconnect()


if __name__ == "__main__":
    main()
```
