"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Generate code to integrate Hengstler safety relays (e.g., RAS or RBS series) into an industrial control system using Python.
Generated: DETERMINISTIC_548a0cf163242b56
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Integration of Hengstler safety relays (RAS or RBS series) into an industrial control system using Python.

This module communicates with Hengstler safety relays via Modbus RTU protocol. Ensure you have the
correct relay model and communication settings before running the program.
"""

import minimalmodbus
import serial

class SafetyRelayController:
    """
    A class to manage communication and control of Hengstler safety relays.
    """

    def __init__(self, port: str, slave_address: int, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initializes the SafetyRelayController.

        :param port: Serial port name (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux).
        :param slave_address: Modbus slave address of the relay.
        :param baudrate: Baud rate for serial communication (default: 9600).
        :param timeout: Timeout for serial communication in seconds (default: 1.0).
        """
        try:
            self.instrument = minimalmodbus.Instrument(port, slave_address)
            self.instrument.serial.baudrate = baudrate
            self.instrument.serial.timeout = timeout
            self.instrument.serial.bytesize = serial.EIGHTBITS
            self.instrument.serial.parity = serial.PARITY_NONE
            self.instrument.serial.stopbits = serial.STOPBITS_ONE
        except Exception as e:
            raise ConnectionError(f"Failed to initialize communication with relay: {e}")

    def read_status(self) -> int:
        """
        Reads the status register from the relay.

        :return: An integer representing the relay status.
        :raises: IOError if communication fails.
        """
        try:
            # Assuming status register is at address 0x0001
            return self.instrument.read_register(1, functioncode=3)
        except Exception as e:
            raise IOError(f"Failed to read relay status: {e}")

    def activate_relay(self):
        """
        Sends a command to activate the relay.

        :raises: IOError if communication fails.
        """
        try:
            # Assuming control register is at address 0x0002 and activation command is 1
            self.instrument.write_register(2, 1, functioncode=6)
        except Exception as e:
            raise IOError(f"Failed to activate relay: {e}")

    def deactivate_relay(self):
        """
        Sends a command to deactivate the relay.

        :raises: IOError if communication fails.
        """
        try:
            # Assuming control register is at address 0x0002 and deactivation command is 0
            self.instrument.write_register(2, 0, functioncode=6)
        except Exception as e:
            raise IOError(f"Failed to deactivate relay: {e}")

if __name__ == "__main__":
    """
    Main script for testing the SafetyRelayController integration.
    """
    # Replace with your actual serial port and slave address
    SERIAL_PORT = '/dev/ttyUSB0'  # Example for Linux
    SLAVE_ADDRESS = 1

    try:
        # Initialize the relay controller
        relay_controller = SafetyRelayController(SERIAL_PORT, SLAVE_ADDRESS)

        # Read relay status
        status = relay_controller.read_status()
        print(f"Relay Status: {status}")

        # Activate the relay
        print("Activating relay...")
        relay_controller.activate_relay()

        # Read relay status again
        status = relay_controller.read_status()
        print(f"Relay Status after activation: {status}")

        # Deactivate the relay
        print("Deactivating relay...")
        relay_controller.deactivate_relay()

        # Read relay status again
        status = relay_controller.read_status()
        print(f"Relay Status after deactivation: {status}")

    except ConnectionError as e:
        print(f"Error establishing connection: {e}")
    except IOError as e:
        print(f"Communication error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

Note: Ensure you have the `minimalmodbus` Python library installed (`pip install minimalmodbus`) and the device connected to the specified serial port before running the program. Adjust register addresses and Modbus settings as per the Hengstler relay documentation.
