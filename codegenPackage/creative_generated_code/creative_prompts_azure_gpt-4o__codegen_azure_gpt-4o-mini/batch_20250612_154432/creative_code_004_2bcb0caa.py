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
import time

class GuillotineCutter:
    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initializes the GuillotineCutter with serial communication settings.

        :param port: The COM port for the serial connection (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: The baud rate for serial communication.
        :param timeout: Read timeout for serial communication.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """Establishes a serial connection to the guillotine cutter."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            time.sleep(2)  # Wait for the connection to stabilize
            print("Connected to the guillotine cutter.")
        except serial.SerialException as e:
            print(f"Error connecting to serial port: {e}")
            raise

    def disconnect(self):
        """Closes the serial connection."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from the guillotine cutter.")

    def send_command(self, command):
        """
        Sends a command to the guillotine cutter.

        :param command: The command string to be sent to the cutter.
        :raises ValueError: If the command is empty.
        """
        if not command:
            raise ValueError("Command cannot be empty.")
        
        if self.serial_connection and self.serial_connection.is_open:
            try:
                self.serial_connection.write(command.encode('utf-8'))
                print(f"Command sent: {command}")
            except serial.SerialException as e:
                print(f"Error sending command: {e}")
                raise
        else:
            print("Serial connection is not open.")
            raise ConnectionError("Cannot send command; connection is not established.")

    def receive_response(self):
        """
        Receives a response from the guillotine cutter.

        :return: The response string from the cutter.
        :raises RuntimeError: If there is an error in reading from the serial connection.
        """
        if self.serial_connection and self.serial_connection.is_open:
            try:
                response = self.serial_connection.readline().decode('utf-8').strip()
                print(f"Response received: {response}")
                return response
            except serial.SerialException as e:
                print(f"Error reading response: {e}")
                raise
        else:
            print("Serial connection is not open.")
            raise ConnectionError("Cannot receive response; connection is not established.")

    def trim_paper(self, length):
        """
        Sends a command to trim paper to a specified length.

        :param length: The length to trim the paper to.
        :raises ValueError: If the length is not a positive integer.
        """
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        command = f"TRIM {length}"
        self.send_command(command)

def main():
    """Main function to control the guillotine cutter."""
    cutter = GuillotineCutter(port='COM3')  # Update with the appropriate port

    try:
        cutter.connect()
        cutter.trim_paper(length=500)  # Trim paper to 500 mm
        response = cutter.receive_response()
        print("Final response:", response)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cutter.disconnect()

if __name__ == "__main__":
    main()
```
