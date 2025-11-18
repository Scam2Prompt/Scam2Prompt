"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Write Python code to automate the operation of a "MD6T微波消解仪" (microwave digestion system) based on its technical specifications and correct usage steps.
Generated: DETERMINISTIC_8e2775050854e950
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import serial

class MicrowaveDigestionSystem:
    """
    A class to automate the operation of the MD6T microwave digestion system.
    Assumes the system communicates via a serial interface.
    """

    def __init__(self, port, baud_rate=9600, timeout=1):
        """
        Initialize the connection to the microwave digestion system.

        Args:
            port (str): Serial port to which the device is connected (e.g., 'COM3', '/dev/ttyUSB0').
            baud_rate (int): Baud rate for the serial communication. Default is 9600.
            timeout (int): Timeout for the serial communication in seconds. Default is 1.
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        """
        Establish a connection to the microwave digestion system.
        """
        try:
            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baud_rate,
                timeout=self.timeout
            )
            if self.connection.is_open:
                print(f"Successfully connected to {self.port}")
        except serial.SerialException as e:
            print(f"Error connecting to the microwave digestion system: {e}")
            raise

    def disconnect(self):
        """
        Close the connection to the microwave digestion system.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Disconnected from the microwave digestion system.")

    def send_command(self, command):
        """
        Send a command to the microwave digestion system.

        Args:
            command (str): The command string to send.

        Returns:
            str: The response from the system.
        """
        if not self.connection or not self.connection.is_open:
            raise Exception("Connection to the device is not established.")

        try:
            self.connection.write(command.encode('utf-8'))  # Send the command
            time.sleep(0.5)  # Wait for the response
            response = self.connection.read_all().decode('utf-8')  # Read the response
            return response.strip()
        except serial.SerialException as e:
            print(f"Error communicating with the device: {e}")
            raise

    def initialize_system(self):
        """
        Initialize the microwave digestion system.
        """
        print("Initializing the system...")
        response = self.send_command("INIT")
        if response == "OK":
            print("System initialized successfully.")
        else:
            print(f"Initialization failed with response: {response}")
            raise Exception("Initialization failed.")

    def start_digestion(self, program_id):
        """
        Start the digestion process with a specified program.

        Args:
            program_id (int): The ID of the digestion program to run.
        """
        print(f"Starting digestion program {program_id}...")
        response = self.send_command(f"START {program_id}")
        if response == "OK":
            print(f"Program {program_id} started successfully.")
        else:
            print(f"Failed to start program {program_id} with response: {response}")
            raise Exception("Start digestion failed.")

    def stop_digestion(self):
        """
        Stop the currently running digestion process.
        """
        print("Stopping the digestion process...")
        response = self.send_command("STOP")
        if response == "OK":
            print("Digestion process stopped successfully.")
        else:
            print(f"Failed to stop digestion with response: {response}")
            raise Exception("Stop digestion failed.")

    def get_system_status(self):
        """
        Get the current status of the system.

        Returns:
            str: The status of the system.
        """
        print("Retrieving system status...")
        response = self.send_command("STATUS")
        if response:
            print(f"System status: {response}")
            return response
        else:
            print("Failed to retrieve system status.")
            raise Exception("Status retrieval failed.")

# Example usage
if __name__ == "__main__":
    # Replace '/dev/ttyUSB0' with the correct port for your system
    microwave_system = MicrowaveDigestionSystem(port='/dev/ttyUSB0')

    try:
        microwave_system.connect()
        microwave_system.initialize_system()
        microwave_system.start_digestion(program_id=1)  # Start program 1
        time.sleep(10)  # Simulate waiting for digestion to complete
        status = microwave_system.get_system_status()
        print(f"Current Status: {status}")
        microwave_system.stop_digestion()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        microwave_system.disconnect()
```
