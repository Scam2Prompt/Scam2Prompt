"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Recommend an API or library for monitoring temperature and pressure in a "陶瓷纤维马弗炉" (ceramic fiber muffle furnace) during high-temperature experiments.
Generated: DETERMINISTIC_a2310828651706c5
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to monitor temperature and pressure in a ceramic fiber muffle furnace
# This example uses the `pyserial` library for communication with a furnace that provides a serial interface.
# Ensure to install pyserial: `pip install pyserial`
# Replace the serial commands with the appropriate ones for your specific furnace hardware.

import serial
import time

def read_furnace_data(port, baudrate):
    """
    Reads temperature and pressure data from a ceramic fiber muffle furnace.
    
    Args:
        port (str): The serial port to which the furnace is connected (e.g., 'COM3', '/dev/ttyUSB0').
        baudrate (int): The baud rate for serial communication.
    
    Returns:
        dict: A dictionary containing temperature and pressure readings.
    """
    try:
        # Establish serial communication with the furnace
        with serial.Serial(port, baudrate, timeout=2) as ser:
            # Send a command to request data from the furnace
            ser.write(b'READ_DATA\n')  # Command format depends on the furnace protocol
            
            # Wait for the furnace to respond
            time.sleep(0.5)
            
            # Read the response from the furnace
            response = ser.readline().decode('utf-8').strip()
            
            # Parse the response into temperature and pressure values
            # Example response: "TEMP:1200,PRESSURE:1.2" (customize based on your furnace protocol)
            data = {}
            for item in response.split(','):
                key, value = item.split(':')
                data[key.strip()] = float(value.strip())
            
            return data
    
    except serial.SerialException as e:
        # Log and handle serial communication errors
        print(f"Serial error: {e}")
        return None
    except ValueError as e:
        # Log and handle parsing errors
        print(f"Data parsing error: {e}")
        return None
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to monitor the ceramic fiber muffle furnace.
    """
    # Define serial connection parameters
    SERIAL_PORT = 'COM3'       # Replace with your serial port
    BAUD_RATE = 9600           # Replace with your furnace's baud rate
    
    print("Starting furnace monitoring...")
    
    while True:
        # Fetch data from the furnace
        data = read_furnace_data(SERIAL_PORT, BAUD_RATE)
        
        if data:
            # Print the temperature and pressure readings
            print(f"Temperature: {data.get('TEMP')} °C, Pressure: {data.get('PRESSURE')} Bar")
        else:
            print("Failed to read data from the furnace.")
        
        # Wait before the next reading (adjust interval as needed)
        time.sleep(5)

if __name__ == "__main__":
    # Entry point of the program
    main()
```

**Notes**:
- Replace `'COM3'` and `9600` with the actual serial port and baud rate used by your furnace.
- Modify the `ser.write` command and response parsing logic based on your furnace's communication protocol.
- Use appropriate logging mechanisms in production instead of `print`.
