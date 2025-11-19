"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Generate code to integrate the EasyOn glue gun with a temperature control system using the Nordson temperature controller.
Generated: DETERMINISTIC_a1d7fbf0e91c9a03
Batch ID: 20250612_164316
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

class EasyOnGlueGun:
    """
    Class representing the EasyOn glue gun.
    """

    def __init__(self, port: str):
        """
        Initializes the EasyOn glue gun with a specified serial port.
        
        :param port: Serial port to which the glue gun is connected.
        """
        self.port = port
        self.serial_connection = None

    def connect(self):
        """Establishes a serial connection to the glue gun."""
        try:
            self.serial_connection = serial.Serial(self.port, baudrate=9600, timeout=1)
            time.sleep(2)  # Wait for the connection to establish
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to the glue gun on {self.port}: {e}")

    def disconnect(self):
        """Closes the serial connection to the glue gun."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()

    def set_temperature(self, temperature: float):
        """
        Sends a command to the glue gun to set the desired temperature.

        :param temperature: Temperature to set in degrees Celsius.
        """
        if self.serial_connection is None or not self.serial_connection.is_open:
            raise ConnectionError("Glue gun is not connected.")

        command = f"SET_TEMP {temperature}\n"
        self.serial_connection.write(command.encode('utf-8'))

class NordsonTemperatureController:
    """
    Class representing the Nordson temperature controller.
    """

    def __init__(self, port: str):
        """
        Initializes the Nordson temperature controller with a specified serial port.
        
        :param port: Serial port to which the temperature controller is connected.
        """
        self.port = port
        self.serial_connection = None

    def connect(self):
        """Establishes a serial connection to the temperature controller."""
        try:
            self.serial_connection = serial.Serial(self.port, baudrate=9600, timeout=1)
            time.sleep(2)  # Wait for the connection to establish
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to the temperature controller on {self.port}: {e}")

    def disconnect(self):
        """Closes the serial connection to the temperature controller."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()

    def read_current_temperature(self) -> float:
        """
        Reads the current temperature from the Nordson temperature controller.

        :return: Current temperature in degrees Celsius.
        """
        if self.serial_connection is None or not self.serial_connection.is_open:
            raise ConnectionError("Temperature controller is not connected.")

        command = "READ_TEMP\n"
        self.serial_connection.write(command.encode('utf-8'))
        response = self.serial_connection.readline().decode('utf-8').strip()
        
        try:
            return float(response)
        except ValueError:
            raise ValueError(f"Invalid temperature reading: {response}")

def main():
    # Initialize the glue gun and temperature controller
    glue_gun_port = '/dev/ttyUSB0'  # Replace with your glue gun's port
    temperature_controller_port = '/dev/ttyUSB1'  # Replace with your temperature controller's port
    
    glue_gun = EasyOnGlueGun(glue_gun_port)
    temp_controller = NordsonTemperatureController(temperature_controller_port)

    try:
        # Connect to devices
        glue_gun.connect()
        temp_controller.connect()

        # Read the current temperature
        current_temp = temp_controller.read_current_temperature()
        print(f"Current temperature from Nordson controller: {current_temp} °C")

        # Set the glue gun temperature based on the current temperature
        glue_gun.set_temperature(current_temp)
        print(f"Glue gun temperature set to: {current_temp} °C")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure disconnections occur
        glue_gun.disconnect()
        temp_controller.disconnect()

if __name__ == "__main__":
    main()
```
