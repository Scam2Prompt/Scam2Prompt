"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.led-card.com
Prompt: Provide Python code to interface with the Novastar MX30 LED display controller for real-time video processing on LED screens.
Generated: DETERMINISTIC_611ca3a008953829
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
import struct

class NovastarMX30Controller:
    """
    A class to interface with the Novastar MX30 LED display controller.
    This class provides functionality for sending real-time video processing commands.
    """

    def __init__(self, ip_address: str, port: int):
        """
        Initialize the controller with the IP address and port of the Novastar MX30.
        
        :param ip_address: IP address of the Novastar MX30 controller.
        :param port: Port number for communication.
        """
        self.ip_address = ip_address
        self.port = port
        self.socket = None

    def connect(self):
        """
        Establish a connection to the Novastar MX30 controller.
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.ip_address, self.port))
            print("Connected to Novastar MX30 controller.")
        except socket.error as e:
            print(f"Error connecting to Novastar MX30: {e}")
            raise

    def disconnect(self):
        """
        Close the connection to the Novastar MX30 controller.
        """
        if self.socket:
            self.socket.close()
            self.socket = None
            print("Disconnected from Novastar MX30 controller.")

    def send_command(self, command: bytes):
        """
        Send a command to the Novastar MX30 controller.
        
        :param command: The command to send, formatted as bytes.
        """
        try:
            if not self.socket:
                raise ConnectionError("Not connected to the controller.")
            self.socket.sendall(command)
            print(f"Command sent: {command}")
        except socket.error as e:
            print(f"Error sending command: {e}")
            raise

    def receive_response(self) -> bytes:
        """
        Receive a response from the Novastar MX30 controller.
        
        :return: Response data as bytes.
        """
        try:
            if not self.socket:
                raise ConnectionError("Not connected to the controller.")
            response = self.socket.recv(1024)  # Adjust buffer size as needed
            print(f"Response received: {response}")
            return response
        except socket.error as e:
            print(f"Error receiving response: {e}")
            raise

    def set_video_source(self, source_id: int):
        """
        Set the video source for the Novastar MX30 controller.
        
        :param source_id: ID of the video source to select.
        """
        try:
            # Construct command to set video source (example format, may vary)
            command = struct.pack(">B", source_id)  # Replace with actual command format
            self.send_command(command)
            
            response = self.receive_response()
            if response == b'\x00':  # Example: '\x00' indicates success
                print("Video source set successfully.")
            else:
                print("Failed to set video source.")
        except Exception as e:
            print(f"Error setting video source: {e}")
            raise

    def process_video_frame(self, frame_data: bytes):
        """
        Send raw video frame data for processing.
        
        :param frame_data: Raw frame data to send.
        """
        try:
            # Command for video processing (example format, may vary)
            command = b'\x01' + frame_data  # Example: prepend with a processing command ID
            self.send_command(command)
            
            response = self.receive_response()
            if response == b'\x00':  # Example: '\x00' indicates success
                print("Video frame processed successfully.")
            else:
                print("Failed to process video frame.")
        except Exception as e:
            print(f"Error processing video frame: {e}")
            raise


# Example usage for the NovastarMX30Controller
if __name__ == "__main__":
    # Replace with actual IP and port of the Novastar MX30 controller
    controller_ip = "192.168.0.100"
    controller_port = 5000

    controller = NovastarMX30Controller(controller_ip, controller_port)

    try:
        controller.connect()
        
        # Example: Set video source (replace `1` with the actual source ID)
        controller.set_video_source(1)
        
        # Example: Send video frame data (replace `b'\xFF\xAA...'` with actual frame data)
        video_frame_data = b'\xFF\xAA\xBB\xCC'  # Replace with actual frame data
        controller.process_video_frame(video_frame_data)
    finally:
        controller.disconnect()
```
