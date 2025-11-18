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
import serial
import time

class HengstlerEncoderConfigurator:
    """
    A class to configure Hengstler S21 series encoders for high-precision angular measurement.

    This script assumes the encoder is connected via a serial interface.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initializes the serial connection to the encoder.

        :param port: Serial port to which the encoder is connected (e.g., 'COM3', '/dev/ttyUSB0').
        :param baudrate: Communication speed (default: 9600).
        :param timeout: Read timeout in seconds.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establishes a connection to the encoder via the specified serial port.
        """
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            print("Serial connection established.")
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to establish serial connection: {e}")

    def disconnect(self):
        """
        Closes the serial connection to the encoder.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Serial connection closed.")

    def send_command(self, command: str) -> str:
        """
        Sends a command to the encoder and retrieves the response.

        :param command: The command string to be sent (e.g., 'SET_PRECISION').
        :return: The response from the encoder.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise RuntimeError("Serial connection is not open.")

        try:
            self.serial_connection.write(command.encode('ascii') + b'\r\n')
            time.sleep(0.1)  # Brief pause for the encoder to process the command
            response = self.serial_connection.readline().decode('ascii').strip()
            return response
        except Exception as e:
            raise RuntimeError(f"Failed to send command '{command}': {e}")

    def configure_encoder(self, precision: int, frequency: int) -> None:
        """
        Configures the encoder with specified precision and frequency values.

        :param precision: Angular measurement precision (e.g., 16-bit or 18-bit).
        :param frequency: Signal frequency for sinus/cosinus output (e.g., 1000 Hz).
        """
        if precision not in [16, 18]:
            raise ValueError("Invalid precision value. Supported values: 16, 18.")
        if frequency <= 0:
            raise ValueError("Frequency must be a positive value.")

        # Example command format for configuring the encoder (adapt as necessary)
        precision_command = f"PREC {precision}"
        frequency_command = f"FREQ {frequency}"

        print(f"Configuring encoder with precision: {precision}-bit and frequency: {frequency} Hz")

        response = self.send_command(precision_command)
        if response != "OK":
            raise RuntimeError(f"Failed to set precision. Encoder response: {response}")

        response = self.send_command(frequency_command)
        if response != "OK":
            raise RuntimeError(f"Failed to set frequency. Encoder response: {response}")

        print("Encoder configured successfully.")

def main():
    """
    Main function to configure the Hengstler encoder.
    """
    # Define serial port and encoder settings
    serial_port = "/dev/ttyUSB0"  # Replace with actual port
    precision = 18  # 16-bit or 18-bit
    frequency = 1000  # Signal frequency in Hz

    # Instantiate the configurator
    configurator = HengstlerEncoderConfigurator(port=serial_port)

    try:
        # Connect to the encoder
        configurator.connect()

        # Configure the encoder
        configurator.configure_encoder(precision=precision, frequency=frequency)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Disconnect the encoder
        configurator.disconnect()

if __name__ == "__main__":
    main()
```
