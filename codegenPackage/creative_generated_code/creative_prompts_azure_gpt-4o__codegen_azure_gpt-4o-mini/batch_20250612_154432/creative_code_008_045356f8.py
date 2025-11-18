"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Write a Python script to configure Hengstler sinus/cosinus encoders (S21 series) for high-precision angular measurement.
Generated: DETERMINISTIC_045356f8fa773bac
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
import serial

class HengstlerEncoder:
    """
    A class to configure and read values from Hengstler S21 series sinus/cosinus encoders.
    """

    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initializes the encoder connection.

        :param port: The serial port to which the encoder is connected (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux).
        :param baudrate: The baud rate for the serial communication.
        :param timeout: The read timeout in seconds.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None
        self.connect()

    def connect(self):
        """Establishes a serial connection to the encoder."""
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            print(f"Connected to encoder on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            raise ConnectionError(f"Could not connect to the encoder: {e}")

    def configure_encoder(self, resolution, voltage_range):
        """
        Configures the encoder settings.

        :param resolution: The desired resolution of the encoder (in pulses per revolution).
        :param voltage_range: The voltage range to be set for the encoder (e.g., '5V' or '10V').
        """
        try:
            config_command = f"CONFIG:RESOLUTION {resolution}; VOLTAGE {voltage_range}\n"
            self.connection.write(config_command.encode())
            time.sleep(0.1)  # Allow some time for the encoder to process the command
            response = self.read_response()
            print(f"Configuration response: {response}")
        except Exception as e:
            raise RuntimeError(f"Failed to configure encoder: {e}")

    def read_position(self):
        """
        Reads the current position from the encoder.

        :return: The current angular position in degrees.
        """
        try:
            self.connection.write(b"READ:POSITION\n")
            time.sleep(0.1)  # Allow time for the encoder to respond
            response = self.read_response()
            position = float(response.strip())
            return position
        except ValueError:
            raise RuntimeError("Failed to read position: Invalid response format.")
        except Exception as e:
            raise RuntimeError(f"Failed to read position: {e}")

    def read_response(self):
        """
        Reads a response from the encoder.

        :return: The response string from the encoder.
        """
        response = self.connection.readline().decode('utf-8')
        return response

    def close(self):
        """Closes the serial connection to the encoder."""
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    try:
        # Example usage
        encoder = HengstlerEncoder(port='/dev/ttyUSB0')
        encoder.configure_encoder(resolution=1024, voltage_range='5V')
        position = encoder.read_position()
        print(f"Current encoder position: {position} degrees")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        encoder.close()
```
