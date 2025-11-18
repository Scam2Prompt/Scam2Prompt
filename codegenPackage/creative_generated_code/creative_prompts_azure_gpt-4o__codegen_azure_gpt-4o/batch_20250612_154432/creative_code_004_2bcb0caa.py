"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Write a script to control Hengstler guillotine cutters (e.g., Guillotine cutter F series) for precise paper trimming in a manufacturing setup.
Generated: DETERMINISTIC_2bcb0caa9f101328
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import serial

class GuillotineCutterController:
    """
    A class to control Hengstler Guillotine Cutters for precise paper trimming in a manufacturing setup.

    Attributes:
        port (str): Serial port to which the cutter is connected.
        baud_rate (int): Communication baud rate.
        timeout (int): Timeout for serial communication.
    """
    def __init__(self, port: str, baud_rate: int = 9600, timeout: int = 2):
        """
        Initializes a GuillotineCutterController instance with serial communication parameters.

        Args:
            port (str): The serial port to which the cutter is connected.
            baud_rate (int): The baud rate for communication.
            timeout (int): Timeout duration for communication in seconds.
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        """
        Establishes a serial connection with the cutter.
        """
        try:
            self.connection = serial.Serial(port=self.port, baudrate=self.baud_rate, timeout=self.timeout)
            print("Connection established with the Guillotine Cutter.")
        except serial.SerialException as e:
            print(f"Failed to connect to Guillotine Cutter: {e}")
            raise

    def disconnect(self):
        """
        Closes the serial connection with the cutter.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Connection closed with the Guillotine Cutter.")

    def send_command(self, command: str):
        """
        Sends a command to the cutter.

        Args:
            command (str): The command string to send.

        Returns:
            str: The response from the cutter.
        """
        if not self.connection or not self.connection.is_open:
            raise ConnectionError("No active connection to the cutter. Please connect first.")
        
        try:
            self.connection.write(command.encode('utf-8'))
            print(f"Command sent: {command}")
            response = self.connection.readline().decode('utf-8').strip()
            print(f"Response received: {response}")
            return response
        except serial.SerialTimeoutException as e:
            print(f"Timeout occurred while sending command: {e}")
            raise
        except Exception as e:
            print(f"Error occurred while sending command: {e}")
            raise

    def trim_paper(self, length: float):
        """
        Sends a command to the cutter to trim paper to a specific length.

        Args:
            length (float): The length to which the paper should be trimmed, in millimeters.

        Returns:
            str: The response from the cutter.
        """
        if length <= 0:
            raise ValueError("Length must be greater than 0.")
        
        command = f"TRIM {length}"
        return self.send_command(command)


# Example usage:
if __name__ == "__main__":
    try:
        cutter = GuillotineCutterController(port="/dev/ttyUSB0")  # Replace with the correct serial port
        cutter.connect()

        # Trim paper to 300mm length
        response = cutter.trim_paper(300.0)
        print(f"Cutter response: {response}")

    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        cutter.disconnect()
```
