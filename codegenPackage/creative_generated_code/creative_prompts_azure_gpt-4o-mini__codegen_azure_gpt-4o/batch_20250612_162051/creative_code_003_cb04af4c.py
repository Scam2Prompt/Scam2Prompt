"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullport.net
Prompt: How can I implement a solution to switch between multiple HDMI sources using a KVM switch as described on FullPort?
Generated: DETERMINISTIC_cb04af4c21a33b87
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python-based implementation for controlling a KVM switch to switch between multiple HDMI sources using serial communication. Replace values like the serial port name and KVM-specific commands according to your device's documentation.

```python
import serial  # Library for serial communication
import time    # Library for adding delays

class KVMSwitchController:
    """
    A class to control a KVM switch for switching HDMI sources.
    """
    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initializes the KVM switch controller.

        Args:
            port (str): The serial port to communicate with the KVM switch.
            baudrate (int): The communication baud rate. Defaults to 9600.
            timeout (float): Timeout for serial communication. Defaults to 1.0 seconds.
        """
        try:
            self.serial_conn = serial.Serial(port, baudrate=baudrate, timeout=timeout)
            print(f"Connected to KVM switch on port {port}.")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to KVM switch on port {port}: {e}")

    def switch_source(self, source: int):
        """
        Switches the HDMI source via the KVM switch.

        Args:
            source (int): The source number to switch to (e.g., 1, 2, 3).

        Raises:
            ValueError: If the source number is invalid.
            RuntimeError: If communication with the KVM switch fails.
        """
        if not (1 <= source <= 4):  # Assuming 4 HDMI ports for the KVM switch
            raise ValueError("Invalid source number. Must be between 1 and 4.")
        
        try:
            # Prepare the command to switch the source (based on KVM switch documentation)
            command = f"SWITCH {source}\n".encode('utf-8')  # Replace "SWITCH" with actual command
            self.serial_conn.write(command)
            time.sleep(0.5)  # Pause for the KVM switch to process the command
            print(f"Switched to HDMI source {source}.")
        except Exception as e:
            raise RuntimeError(f"Failed to switch HDMI source: {e}")

    def close_connection(self):
        """
        Closes the serial connection to the KVM switch.
        """
        try:
            self.serial_conn.close()
            print("Disconnected from KVM switch.")
        except Exception as e:
            raise RuntimeError(f"Failed to close connection: {e}")


if __name__ == "__main__":
    # Replace 'COM3' with the appropriate serial port name used by your KVM switch
    kvm_port = 'COM3'
    kvm_switch = None
    
    try:
        # Initialize the KVM switch controller
        kvm_switch = KVMSwitchController(port=kvm_port)
        
        # Switch to HDMI source 1
        kvm_switch.switch_source(1)
        
        # Switch to HDMI source 2 (example)
        kvm_switch.switch_source(2)
        
        # Add more calls to switch_source() as needed to test other sources
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if kvm_switch:
            # Ensure the connection is closed
            kvm_switch.close_connection()
```

### Notes:
1. Replace `"SWITCH {source}\n"` with the actual command format required by your KVM switch. Check your device's manual/documentation for the proper command format.
2. Update the serial port (`COM3`) to the correct port based on your system and device configuration.
3. This code assumes the KVM switch supports serial communication. Ensure proper drivers and permissions for the serial port are configured.
4. The exception handling ensures the program gracefully handles connection errors or invalid commands.
