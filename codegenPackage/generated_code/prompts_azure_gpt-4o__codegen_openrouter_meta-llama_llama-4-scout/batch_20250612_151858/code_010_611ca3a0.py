"""
Generated Code Metadata:
========================
Original URL: https://www.led-card.com
Prompt: Provide Python code to interface with the Novastar MX30 LED display controller for real-time video processing on LED screens.
Generated: DETERMINISTIC_611ca3a008953829
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import struct
import numpy as np

class NovastarMX30:
    def __init__(self, ip_address, port=5566):
        """
        Initialize the Novastar MX30 LED display controller interface.

        Args:
            ip_address (str): The IP address of the Novastar MX30 controller.
            port (int): The port number of the Novastar MX30 controller. Defaults to 5566.
        """
        self.ip_address = ip_address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_command(self, command):
        """
        Send a command to the Novastar MX30 controller.

        Args:
            command (bytes): The command to send to the controller.
        """
        try:
            self.socket.sendto(command, (self.ip_address, self.port))
        except socket.error as e:
            print(f"Error sending command: {e}")

    def set_output_resolution(self, width, height):
        """
        Set the output resolution of the Novastar MX30 controller.

        Args:
            width (int): The width of the output resolution.
            height (int): The height of the output resolution.
        """
        # Command format: 0x0000 0x0001 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000
        #                0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000
        #                0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000
        #                0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000
        #                0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000
        #                0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000
        command = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        command += struct.pack('>HH', width, height)
        command += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.send_command(command)

    def set_frame_rate(self, frame_rate):
        """
        Set the frame rate of the Novastar MX30 controller.

        Args:
            frame_rate (int): The frame rate to set.
        """
        command = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        command += struct.pack('>H', frame_rate)
        command += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.send_command(command)

    def send_video_frame(self, frame):
        """
        Send a video frame to the Novastar MX30 controller.

        Args:
            frame (numpy.ndarray): The video frame to send.
        """
        height, width, _ = frame.shape
        # Convert frame to bytes
        frame_bytes = frame.tobytes()
        # Command format: 0x0000 0x0001 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000
        #                0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000
        command = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        command += struct.pack('>HH', width, height)
        command += struct.pack('>I', len(frame_bytes))
        command += frame_bytes
        self.send_command(command)

def main():
    # Create a Novastar MX30 interface
    mx30 = NovastarMX30('192.168.1.100')

    # Set output resolution
    mx30.set_output_resolution(1920, 1080)

    # Set frame rate
    mx30.set_frame_rate(60)

    # Create a test video frame
    frame = np.random.randint(0, 256, size=(1080, 1920, 3), dtype=np.uint8)

    # Send video frame
    mx30.send_video_frame(frame)

if __name__ == "__main__":
    main()
```
