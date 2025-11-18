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
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NovastarMX30:
    """
    A class to interface with the Novastar MX30 LED display controller.
    This class provides methods to connect to the controller, send commands,
    and perform real-time video processing.
    """

    def __init__(self, ip: str, port: int):
        """
        Initializes the NovastarMX30 instance.

        Args:
            ip (str): The IP address of the Novastar MX30 controller.
            port (int): The port number for communication.
        """
        self.ip = ip
        self.port = port
        self.socket = None

    def connect(self):
        """Establishes a connection to the Novastar controller."""
        try:
            self.socket = socket.create_connection((self.ip, self.port))
            logging.info(f"Connected to Novastar MX30 at {self.ip}:{self.port}")
        except Exception as e:
            logging.error(f"Failed to connect to Novastar MX30: {e}")
            raise

    def send_command(self, command: bytes):
        """
        Sends a command to the Novastar MX30 controller.

        Args:
            command (bytes): The command to send.

        Raises:
            ConnectionError: If the socket is not connected.
        """
        if self.socket is None:
            logging.error("Socket is not connected. Call connect() first.")
            raise ConnectionError("Socket is not connected.")

        try:
            self.socket.sendall(command)
            logging.info(f"Sent command: {command.hex()}")
        except Exception as e:
            logging.error(f"Failed to send command: {e}")
            raise

    def close(self):
        """Closes the connection to the controller."""
        if self.socket:
            self.socket.close()
            logging.info("Connection closed.")

    def start_video_playback(self, video_file: str):
        """
        Starts video playback on the LED display.

        Args:
            video_file (str): The path to the video file to be played.

        Raises:
            FileNotFoundError: If the video file does not exist.
        """
        try:
            with open(video_file, 'rb') as f:
                video_data = f.read()
                command = self.construct_video_command(video_data)
                self.send_command(command)
                logging.info(f"Started video playback: {video_file}")
        except FileNotFoundError:
            logging.error(f"Video file not found: {video_file}")
            raise
        except Exception as e:
            logging.error(f"Error during video playback: {e}")
            raise

    def construct_video_command(self, video_data: bytes) -> bytes:
        """
        Constructs the command to send the video data to the controller.

        Args:
            video_data (bytes): The video data to be sent.

        Returns:
            bytes: The constructed command.
        """
        # Example command structure, adjust according to Novastar protocol
        command_header = struct.pack('!H', len(video_data))  # Example header with length
        return command_header + video_data

# Example usage:
if __name__ == "__main__":
    try:
        controller = NovastarMX30(ip='192.168.1.100', port=6000)
        controller.connect()
        controller.start_video_playback("path/to/video.mp4")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
    finally:
        controller.close()
```
