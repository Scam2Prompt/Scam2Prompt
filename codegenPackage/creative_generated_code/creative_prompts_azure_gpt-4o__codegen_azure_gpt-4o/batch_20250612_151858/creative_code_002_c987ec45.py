"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.led-card.com
Prompt: Recommend an API or library for managing LED display power supplies, such as the MEANWell LRS-350-5, and provide example code for integration.
Generated: DETERMINISTIC_c987ec45e84ae910
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python example for managing LED display power supplies like the MEANWell LRS-350-5.
# Library used: PyModbus (a Modbus protocol library for Python)
# MEANWell LRS-350-5 supports control via Modbus RTU (serial communication).
# Ensure the power supply is set up for Modbus communication and connected via RS485.

# Import necessary modules
from pymodbus.client.sync import ModbusSerialClient
from pymodbus.exceptions import ModbusIOException

# Function to initialize the Modbus client
def initialize_modbus(port, baudrate=9600, timeout=1):
    """
    Initializes a Modbus RTU client for communication.
    :param port: The serial port (e.g., COM4, /dev/ttyUSB0).
    :param baudrate: Communication speed in bits per second.
    :param timeout: Timeout for the connection in seconds.
    :return: Initialized Modbus client.
    """
    try:
        client = ModbusSerialClient(
            method='rtu',  # Modbus RTU method
            port=port,
            baudrate=baudrate,
            timeout=timeout
        )
        if not client.connect():
            raise ConnectionError(f"Unable to connect to {port}. Check the connection and port settings.")
        return client
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Modbus client: {str(e)}")

# Function to read a specific register from the power supply
def read_register(client, address, unit_id):
    """
    Reads a single register value from the power supply using Modbus RTU.
    :param client: The Modbus client instance.
    :param address: The register address to read.
    :param unit_id: The Modbus unit ID of the power supply.
    :return: Value of the register.
    """
    try:
        response = client.read_holding_registers(address, 1, unit=unit_id)
        if response.isError():
            raise ModbusIOException(f"Error reading register {address} on unit {unit_id}.")
        return response.registers[0]
    except Exception as e:
        raise RuntimeError(f"Failed to read register: {str(e)}")

# Function to write to a specific register on the power supply
def write_register(client, address, value, unit_id):
    """
    Writes a value to a single register on the power supply using Modbus RTU.
    :param client: The Modbus client instance.
    :param address: The register address to write.
    :param value: The value to write to the register.
    :param unit_id: The Modbus unit ID of the power supply.
    :return: None.
    """
    try:
        response = client.write_register(address, value, unit=unit_id)
        if response.isError():
            raise ModbusIOException(f"Error writing value {value} to register {address} on unit {unit_id}.")
    except Exception as e:
        raise RuntimeError(f"Failed to write register: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace 'COM3' with your serial port, and set the correct unit_id and register values
    serial_port = 'COM3'
    modbus_unit_id = 1  # Typical Modbus unit ID for the device
    register_address = 0x0001  # Example register address
    register_value = 42  # Example value to write

    try:
        # Initialize Modbus client
        modbus_client = initialize_modbus(serial_port)

        # Write to a register
        print(f"Writing {register_value} to register {register_address}...")
        write_register(modbus_client, register_address, register_value, modbus_unit_id)
        print("Write operation successful.")

        # Read back the register value
        print(f"Reading back value from register {register_address}...")
        read_value = read_register(modbus_client, register_address, modbus_unit_id)
        print(f"Register {register_address} value: {read_value}")

    except Exception as error:
        print(f"Error: {error}")
    finally:
        # Ensure client is closed to release resources
        if modbus_client:
            modbus_client.close()
```
