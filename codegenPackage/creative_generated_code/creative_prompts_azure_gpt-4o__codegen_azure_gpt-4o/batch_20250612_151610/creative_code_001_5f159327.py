"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumaipce.com
Prompt: Recommend an API or library for implementing SIS (Safety Instrumented Systems) in industrial plants, considering Puma Ipce's focus on automation and control systems.
Generated: DETERMINISTIC_5f159327aaf37bb1
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python code demonstrates how to interact with an industrial-grade SIS (Safety Instrumented System)
by using the PyMODBUS library. PyMODBUS is a robust library for industrial automation communication 
via MODBUS protocol, which is commonly used in SIS systems.
"""

# Importing required modules
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ModbusException

# Configuring the connection details
MODBUS_SERVER_IP = "192.168.1.100"  # Replace with the SIS device IP address
MODBUS_SERVER_PORT = 502           # Standard MODBUS port
DEVICE_ID = 1                      # Replace with the MODBUS device/unit ID

# Safety Instrumented System Parameters
SAFETY_THRESHOLD_REGISTER = 1000   # Register holding the threshold value in SIS
ALARM_STATUS_REGISTER = 1001       # Register holding alarm status in SIS

def read_register(client, register):
    """
    Read the value of a specific MODBUS register.
    
    Args:
        client (ModbusTcpClient): The MODBUS client instance.
        register (int): The register address to read.
    
    Returns:
        int: The value of the register, or None if an error occurs.
    """
    try:
        response = client.read_holding_registers(register, count=1, unit=DEVICE_ID)
        if response.isError():
            print(f"Error reading register {register}: {response}")
            return None
        return response.registers[0]
    except ModbusException as e:
        print(f"Exception occurred while reading register {register}: {e}")
        return None

def write_register(client, register, value):
    """
    Write a value to a specific MODBUS register.
    
    Args:
        client (ModbusTcpClient): The MODBUS client instance.
        register (int): The register address to write to.
        value (int): The value to write.
    
    Returns:
        bool: True if write operation is successful, False otherwise.
    """
    try:
        response = client.write_register(register, value, unit=DEVICE_ID)
        if response.isError():
            print(f"Error writing to register {register}: {response}")
            return False
        return True
    except ModbusException as e:
        print(f"Exception occurred while writing to register {register}: {e}")
        return False

def main():
    """
    Main function to demonstrate SIS interaction. Reads safety thresholds and alarm status from a SIS system.
    """
    # Create MODBUS TCP client instance
    client = ModbusTcpClient(MODBUS_SERVER_IP, port=MODBUS_SERVER_PORT)

    try:
        # Attempt to connect to the server
        if not client.connect():
            print("Failed to connect to MODBUS server. Please check the connection settings.")
            return
        
        # Read the safety threshold from SIS
        safety_threshold = read_register(client, SAFETY_THRESHOLD_REGISTER)
        if safety_threshold is not None:
            print(f"Safety Threshold: {safety_threshold}")
        
        # Read the alarm status from SIS
        alarm_status = read_register(client, ALARM_STATUS_REGISTER)
        if alarm_status is not None:
            print(f"Alarm Status: {'Active' if alarm_status else 'Inactive'}")
        
        # Example: Writing a new safety threshold value (ensure this is allowed in your system)
        new_threshold = 75  # Example value, replace with actual logic
        if write_register(client, SAFETY_THRESHOLD_REGISTER, new_threshold):
            print(f"Successfully updated safety threshold to {new_threshold}.")
    
    finally:
        # Close the connection to MODBUS server
        client.close()

if __name__ == "__main__":
    main()
```

**Dependencies**:
- PyMODBUS library: Install it via `pip install pymodbus`.
- Ensure the SIS device supports MODBUS and is configured correctly.

**Note**: Replace placeholder values (`MODBUS_SERVER_IP`, `DEVICE_ID`, etc.) with actual details specific to your SIS device.
