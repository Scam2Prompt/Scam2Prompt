"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Write code to automate adhesive dispensing using Nordson's MiniSquirt machine for small-scale operations.
Generated: DETERMINISTIC_f686a7123d223226
Batch ID: 20250612_151525
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

class AdhesiveDispensingSystem:
    """
    AdhesiveDispensingSystem controls Nordson's MiniSquirt machine to automate adhesive dispensing.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initialize the dispensing system by establishing a serial connection.
        
        :param port: Serial port to which the MiniSquirt machine is connected.
        :param baudrate: Communication speed (baud rate). Default is 9600.
        :param timeout: Timeout for serial communication. Default is 1.0 seconds.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        """
        Establish a connection with the MiniSquirt machine.
        """
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            print(f"Connected to MiniSquirt machine on port {self.port}")
        except serial.SerialException as e:
            print(f"Error connecting to MiniSquirt machine: {e}")
            raise

    def disconnect(self):
        """
        Close the serial connection.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Disconnected from MiniSquirt machine.")

    def send_command(self, command: str):
        """
        Send a command to the MiniSquirt machine.
        
        :param command: Command string to send to the machine.
        :return: Response from the machine.
        """
        try:
            if not self.connection or not self.connection.is_open:
                raise ConnectionError("Connection to MiniSquirt machine is not established.")
            
            # Send the command
            self.connection.write(f"{command}\n".encode('utf-8'))
            
            # Read the response
            response = self.connection.readline().decode('utf-8').strip()
            return response
        except Exception as e:
            print(f"Error sending command '{command}': {e}")
            raise

    def dispense(self, duration: float, amount: float):
        """
        Dispense adhesive based on specified duration and amount.
        
        :param duration: Duration in seconds for dispensing.
        :param amount: Amount of adhesive to dispense (machine-specific units).
        """
        try:
            # Construct the dispense command
            command = f"DISPENSE DURATION={duration} AMOUNT={amount}"
            response = self.send_command(command)
            
            # Log the response
            print(f"Dispense command response: {response}")
        except Exception as e:
            print(f"Error during dispensing operation: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    machine_port = "COM3"  # Replace with the actual port connected to the MiniSquirt machine
    
    # Instantiate the adhesive dispensing system
    dispenser = AdhesiveDispensingSystem(port=machine_port)
    
    try:
        dispenser.connect()
        
        # Example dispensing operation: dispense for 2 seconds with an amount of 5 units
        dispenser.dispense(duration=2.0, amount=5.0)
        
    finally:
        dispenser.disconnect()
```
