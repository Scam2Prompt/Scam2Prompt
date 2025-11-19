"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Write a Python script that communicates with the Saturn precision spray nozzle to adjust flow rates based on user input.
Generated: DETERMINISTIC_0d8c13c28c00b836
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial  # For serial communication with the nozzle
import sys     # For system exit in case of errors

def connect_to_nozzle(port, baud_rate=9600):
    """
    Establishes a connection to the Saturn precision spray nozzle.

    Args:
        port (str): The serial port to connect to (e.g., 'COM3' or '/dev/ttyUSB0').
        baud_rate (int): The baud rate for the serial communication.

    Returns:
        serial.Serial: The serial connection object.

    Raises:
        Exception: If the connection fails.
    """
    try:
        # Initialize serial connection
        connection = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connected to nozzle on port {port} at baud rate {baud_rate}.")
        return connection
    except Exception as e:
        print(f"Error connecting to nozzle: {e}")
        sys.exit(1)

def send_flow_rate_command(connection, flow_rate):
    """
    Sends a command to the nozzle to adjust the flow rate.

    Args:
        connection (serial.Serial): The serial connection to the nozzle.
        flow_rate (float): The desired flow rate in liters per minute.

    Raises:
        ValueError: If the flow rate is out of the acceptable range.
        Exception: If the command fails to send.
    """
    # Validate flow rate (example range: 0.1 to 10.0 liters per minute)
    if not (0.1 <= flow_rate <= 10.0):
        raise ValueError("Flow rate must be between 0.1 and 10.0 liters per minute.")

    # Construct the command string (example format: "SET_FLOW:3.5")
    command = f"SET_FLOW:{flow_rate:.2f}\n"

    try:
        # Send the command over the serial connection
        connection.write(command.encode('utf-8'))
        print(f"Flow rate command sent: {command.strip()}")
    except Exception as e:
        print(f"Error sending flow rate command: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the Saturn precision spray nozzle.
    """
    # User input for serial port and flow rate
    port = input("Enter the serial port (e.g., COM3 or /dev/ttyUSB0): ").strip()
    try:
        flow_rate = float(input("Enter the desired flow rate (liters per minute): ").strip())
    except ValueError:
        print("Invalid flow rate. Please enter a numeric value.")
        sys.exit(1)

    # Connect to the nozzle
    connection = connect_to_nozzle(port)

    # Send the flow rate command
    try:
        send_flow_rate_command(connection, flow_rate)
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    # Close the connection
    connection.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
```
