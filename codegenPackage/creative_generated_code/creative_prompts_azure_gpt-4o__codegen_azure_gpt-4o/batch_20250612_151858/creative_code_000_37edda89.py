"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.led-card.com
Prompt: Write Python code to interface with a Novastar VX1000 LED video processor for controlling LED displays, referencing the specifications provided on LED-CARD's website.
Generated: DETERMINISTIC_37edda89abbf7dbb
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

class NovastarVX1000Controller:
    """
    A class to interface with the Novastar VX1000 LED video processor for controlling LED displays.
    """
    def __init__(self, ip_address, port):
        """
        Initializes the Novastar VX1000 Controller.

        :param ip_address: IP address of the VX1000 device.
        :param port: Port number to connect to the VX1000 device.
        """
        self.ip_address = ip_address
        self.port = port
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the VX1000 device.
        """
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((self.ip_address, self.port))
            print(f"Connected to Novastar VX1000 at {self.ip_address}:{self.port}")
        except socket.error as e:
            print(f"Failed to connect to the VX1000 device: {e}")
            self.connection = None

    def send_command(self, command):
        """
        Sends a command to the VX1000 device.

        :param command: The command string to send to the device.
        :return: The response from the device.
        """
        if not self.connection:
            raise ConnectionError("No connection established with the VX1000 device.")

        try:
            # Commands must be encoded to bytes before sending
            self.connection.sendall(command.encode('utf-8'))
            print(f"Command sent: {command}")

            # Receive and decode the response
            response = self.connection.recv(1024).decode('utf-8')
            print(f"Response received: {response}")
            return response
        except socket.error as e:
            print(f"Error sending command: {e}")
            return None

    def disconnect(self):
        """
        Closes the connection to the VX1000 device.
        """
        if self.connection:
            try:
                self.connection.close()
                print(f"Disconnected from Novastar VX1000 at {self.ip_address}:{self.port}")
            except socket.error as e:
                print(f"Error while disconnecting: {e}")
            finally:
                self.connection = None

    def set_brightness(self, level):
        """
        Sets the brightness of the LED display.

        :param level: Brightness level (e.g., 0-100).
        :return: Response from the device.
        """
        if not (0 <= level <= 100):
            raise ValueError("Brightness level must be between 0 and 100.")
        
        # Example command to set brightness, adjust as per VX1000 protocol documentation
        command = f"SET BRIGHTNESS {level}"
        return self.send_command(command)

    def set_input_source(self, source):
        """
        Sets the input source for the LED display.

        :param source: Input source identifier (e.g., HDMI, DVI, etc.).
        :return: Response from the device.
        """
        # Example command to set input source, adjust as per VX1000 protocol documentation
        command = f"SET INPUT SOURCE {source}"
        return self.send_command(command)

    def get_status(self):
        """
        Retrieves the status of the VX1000 device.

        :return: Status information from the device.
        """
        # Example command to retrieve status, adjust as per VX1000 protocol documentation
        command = "GET STATUS"
        return self.send_command(command)


# Example usage
if __name__ == "__main__":
    # Replace '192.168.0.100' and '5000' with the actual IP and port of your VX1000 device
    vx1000 = NovastarVX1000Controller(ip_address='192.168.0.100', port=5000)

    try:
        vx1000.connect()

        # Example commands
        vx1000.set_brightness(75)
        vx1000.set_input_source("HDMI")
        print(vx1000.get_status())

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        vx1000.disconnect()
```
