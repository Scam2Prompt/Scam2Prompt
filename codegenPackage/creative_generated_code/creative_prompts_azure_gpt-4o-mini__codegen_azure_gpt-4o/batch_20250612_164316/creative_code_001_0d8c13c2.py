"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Write a Python script that communicates with the Saturn precision spray nozzle to adjust flow rates based on user input.
Generated: DETERMINISTIC_0d8c13c28c00b836
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

def connect_to_device(port: str, baud_rate: int = 9600) -> serial.Serial:
    """
    Establishes a connection to the Saturn precision spray nozzle device via serial communication.
    
    :param port: The COM port where the device is connected (e.g., 'COM3' or '/dev/ttyUSB0').
    :param baud_rate: The baud rate for serial communication. Default is 9600.
    :return: A serial connection object.
    """
    try:
        # Initialize serial connection
        connection = serial.Serial(port, baud_rate, timeout=2)
        print(f"Connected to device on port {port}")
        return connection
    except serial.SerialException as e:
        raise Exception(f"Failed to connect to device: {e}")

def validate_flow_rate(flow_rate: int) -> bool:
    """
    Validates the user-provided flow rate to ensure it's within the acceptable range.
    
    :param flow_rate: Flow rate value to validate.
    :return: True if valid, False otherwise.
    """
    # Assuming the valid range of flow rates is 0 to 100
    return 0 <= flow_rate <= 100

def send_flow_rate_command(connection: serial.Serial, flow_rate: int) -> None:
    """
    Sends the command to adjust the flow rate to the Saturn precision spray nozzle device.
    
    :param connection: The serial connection object.
    :param flow_rate: The desired flow rate value.
    """
    try:
        # Construct the command in the format expected by the device
        command = f"SET_FLOW_RATE:{flow_rate}\n"
        connection.write(command.encode('utf-8'))
        print(f"Flow rate command sent: {command.strip()}")
        
        # Read response from the device
        response = connection.readline().decode('utf-8').strip()
        if response == "ACK":
            print("Flow rate adjustment successful.")
        else:
            print(f"Device response: {response}")
    except Exception as e:
        raise Exception(f"Error sending command to device: {e}")

def main():
    """
    Main function to prompt the user for input and adjust the flow rate accordingly.
    """
    try:
        # User-specified port (update this as needed)
        device_port = input("Enter the device port (e.g., COM3 or /dev/ttyUSB0): ").strip()
        
        # Connect to the device
        connection = connect_to_device(device_port)
        
        while True:
            try:
                # Get user input for flow rate
                user_flow_rate = int(input("Enter desired flow rate (0-100, or -1 to exit): "))
                
                # Exit condition
                if user_flow_rate == -1:
                    print("Exiting program...")
                    break

                # Validate input
                if not validate_flow_rate(user_flow_rate):
                    print("Invalid flow rate! Please enter a value between 0 and 100.")
                    continue

                # Send command to device
                send_flow_rate_command(connection, user_flow_rate)

            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        
        # Close the connection
        connection.close()
        print("Device connection closed.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
