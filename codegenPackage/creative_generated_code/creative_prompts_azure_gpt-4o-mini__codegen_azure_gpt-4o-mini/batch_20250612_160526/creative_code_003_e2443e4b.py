"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haotianglobal.com
Prompt: How can I utilize rotary attachments with a Gantry CO2 laser for unique engraving tasks? Provide a code example based on Haotian Global's specifications.
Generated: DETERMINISTIC_e2443e4bec7755ab
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import serial

class GantryLaserController:
    """
    A class to control a Gantry CO2 laser with rotary attachment capabilities.
    """

    def __init__(self, port, baudrate=9600):
        """
        Initialize the GantryLaserController.

        :param port: The serial port to which the laser is connected.
        :param baudrate: The communication speed for the serial connection.
        """
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.connect()

    def connect(self):
        """Establish the serial connection to the laser."""
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # Wait for the connection to stabilize
            print("Connected to laser on port:", self.port)
        except serial.SerialException as e:
            print("Error connecting to laser:", e)
            raise

    def send_command(self, command):
        """
        Send a command to the laser.

        :param command: The command string to send.
        """
        try:
            self.ser.write(f"{command}\n".encode())
            time.sleep(1)  # Wait for the command to be processed
        except Exception as e:
            print("Error sending command:", e)
            raise

    def set_rotary_attachment(self, enabled=True):
        """
        Enable or disable the rotary attachment.

        :param enabled: Boolean value to enable (True) or disable (False) the rotary attachment.
        """
        command = "ROTARY_ON" if enabled else "ROTARY_OFF"
        self.send_command(command)
        print(f"Rotary attachment set to: {'enabled' if enabled else 'disabled'}")

    def engrave(self, image_path):
        """
        Start the engraving process with the specified image.

        :param image_path: Path to the image file to be engraved.
        """
        self.send_command(f"ENGRAVE {image_path}")
        print(f"Engraving started for image: {image_path}")

    def disconnect(self):
        """Close the serial connection to the laser."""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Disconnected from laser.")

def main():
    """
    Main function to demonstrate rotary attachment usage with the Gantry CO2 laser.
    """
    try:
        laser = GantryLaserController(port="/dev/ttyUSB0")  # Adjust port as necessary
        laser.set_rotary_attachment(enabled=True)  # Enable rotary attachment
        laser.engrave("path/to/your/image.png")  # Specify your image path
    except Exception as e:
        print("An error occurred:", e)
    finally:
        laser.disconnect()

if __name__ == "__main__":
    main()
```
