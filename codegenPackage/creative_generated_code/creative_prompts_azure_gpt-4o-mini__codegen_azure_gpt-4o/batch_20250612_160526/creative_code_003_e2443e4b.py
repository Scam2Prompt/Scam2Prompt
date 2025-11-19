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
"""
This script demonstrates how to control a Gantry CO2 laser with a rotary attachment for unique engraving tasks.
The code is based on typical specifications for Haotian Global CO2 laser machines, using Python to send G-code commands.
Ensure that the laser machine supports rotary attachments and the controller interprets G-code.
"""

import serial

def send_gcode_command(port, baud_rate, gcode_command):
    """
    Sends a G-code command to the laser machine via the specified serial port.
    
    Args:
        port (str): The name of the serial port (e.g., 'COM3' or '/dev/ttyUSB0').
        baud_rate (int): The baud rate for serial communication (e.g., 9600).
        gcode_command (str): The G-code command to send.
        
    Returns:
        None
    """
    try:
        # Establish serial connection
        with serial.Serial(port, baud_rate, timeout=1) as ser:
            if ser.is_open:
                print(f"Sending G-code: {gcode_command}")
                ser.write((gcode_command + '\n').encode('utf-8'))  # Send G-code
                response = ser.readline().decode('utf-8').strip()  # Read response
                print(f"Machine Response: {response}")
            else:
                print("Failed to open serial port.")
    except serial.SerialException as e:
        print(f"Serial communication error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def configure_rotary_attachment(port, baud_rate, diameter):
    """
    Configures the rotary attachment for engraving cylindrical objects.

    Args:
        port (str): The name of the serial port.
        baud_rate (int): The baud rate for serial communication.
        diameter (float): The diameter of the object to be engraved (in mm).

    Returns:
        None
    """
    try:
        # Calculate steps per rotation based on diameter
        steps_per_rotation = 360 / diameter
        # Command to configure rotary axis (example syntax, adjust as needed)
        rotary_config_command = f"$ROTARY={steps_per_rotation}"
        send_gcode_command(port, baud_rate, rotary_config_command)
    except Exception as e:
        print(f"Error configuring rotary attachment: {e}")

def execute_engraving_task(port, baud_rate, engraving_pattern):
    """
    Executes an engraving task using the laser machine.

    Args:
        port (str): The name of the serial port.
        baud_rate (int): The baud rate for serial communication.
        engraving_pattern (str): The G-code pattern for engraving.

    Returns:
        None
    """
    try:
        # Send engraving pattern (G-code commands)
        send_gcode_command(port, baud_rate, engraving_pattern)
    except Exception as e:
        print(f"Error executing engraving task: {e}")

if __name__ == "__main__":
    # Example usage of the script
    SERIAL_PORT = "COM3"  # Replace with your machine's serial port
    BAUD_RATE = 9600      # Replace with your machine's baud rate
    OBJECT_DIAMETER = 50  # Diameter of the object to be engraved in mm
    ENGRAVING_GCODE = "G1 X0 Y0 F1000"  # Example G-code for engraving
    
    print("Configuring rotary attachment...")
    configure_rotary_attachment(SERIAL_PORT, BAUD_RATE, OBJECT_DIAMETER)
    
    print("Executing engraving task...")
    execute_engraving_task(SERIAL_PORT, BAUD_RATE, ENGRAVING_GCODE)
```
