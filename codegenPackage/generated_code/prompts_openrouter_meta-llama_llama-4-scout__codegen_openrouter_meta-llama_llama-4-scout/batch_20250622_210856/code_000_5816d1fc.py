"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Write a code snippet to implement a hearing aid connectivity feature that streams phone calls, TV, and music directly to Oticon hearing aids.
Generated: DETERMINISTIC_5816d1fc93a283e8
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import logging
import threading
from enum import Enum
from typing import Dict

# Define the HearingAidDevice class
class HearingAidDevice:
    def __init__(self, device_id: str, device_name: str):
        """
        Initialize a hearing aid device.

        Args:
        device_id (str): Unique identifier for the device.
        device_name (str): Name of the device.
        """
        self.device_id = device_id
        self.device_name = device_name
        self.is_connected = False

    def connect(self):
        """
        Establish a connection to the hearing aid device.
        """
        try:
            # Simulate connection establishment
            self.is_connected = True
            logging.info(f"Connected to {self.device_name} with ID {self.device_id}")
        except Exception as e:
            logging.error(f"Failed to connect to {self.device_name} with ID {self.device_id}: {str(e)}")

    def disconnect(self):
        """
        Terminate the connection to the hearing aid device.
        """
        try:
            # Simulate connection termination
            self.is_connected = False
            logging.info(f"Disconnected from {self.device_name} with ID {self.device_id}")
        except Exception as e:
            logging.error(f"Failed to disconnect from {self.device_name} with ID {self.device_id}: {str(e)}")


# Define the AudioSourceType Enum
class AudioSourceType(Enum):
    PHONE_CALL = 1
    TV = 2
    MUSIC = 3


# Define the AudioStreamer class
class AudioStreamer:
    def __init__(self, hearing_aid_device: HearingAidDevice):
        """
        Initialize an audio streamer for a hearing aid device.

        Args:
        hearing_aid_device (HearingAidDevice): The hearing aid device to stream audio to.
        """
        self.hearing_aid_device = hearing_aid_device
        self.audio_sources: Dict[AudioSourceType, bool] = {
            AudioSourceType.PHONE_CALL: False,
            AudioSourceType.TV: False,
            AudioSourceType.MUSIC: False,
        }

    def start_streaming(self, audio_source_type: AudioSourceType):
        """
        Start streaming audio from a specific source to the hearing aid device.

        Args:
        audio_source_type (AudioSourceType): The type of audio source to stream.
        """
        try:
            if not self.hearing_aid_device.is_connected:
                logging.error("Hearing aid device is not connected")
                return

            if self.audio_sources[audio_source_type]:
                logging.info(f"Audio source {audio_source_type} is already streaming")
                return

            # Simulate audio streaming
            self.audio_sources[audio_source_type] = True
            logging.info(f"Started streaming {audio_source_type.name} to {self.hearing_aid_device.device_name}")
        except Exception as e:
            logging.error(f"Failed to start streaming {audio_source_type.name} to {self.hearing_aid_device.device_name}: {str(e)}")

    def stop_streaming(self, audio_source_type: AudioSourceType):
        """
        Stop streaming audio from a specific source to the hearing aid device.

        Args:
        audio_source_type (AudioSourceType): The type of audio source to stop streaming.
        """
        try:
            if not self.hearing_aid_device.is_connected:
                logging.error("Hearing aid device is not connected")
                return

            if not self.audio_sources[audio_source_type]:
                logging.info(f"Audio source {audio_source_type} is not currently streaming")
                return

            # Simulate audio streaming termination
            self.audio_sources[audio_source_type] = False
            logging.info(f"Stopped streaming {audio_source_type.name} to {self.hearing_aid_device.device_name}")
        except Exception as e:
            logging.error(f"Failed to stop streaming {audio_source_type.name} to {self.hearing_aid_device.device_name}: {str(e)}")


# Define the HearingAidConnectivityManager class
class HearingAidConnectivityManager:
    def __init__(self):
        """
        Initialize a hearing aid connectivity manager.
        """
        self.hearing_aid_devices: Dict[str, HearingAidDevice] = {}
        self.audio_streamers: Dict[str, AudioStreamer] = {}

    def add_hearing_aid_device(self, device: HearingAidDevice):
        """
        Add a hearing aid device to the manager.

        Args:
        device (HearingAidDevice): The hearing aid device to add.
        """
        self.hearing_aid_devices[device.device_id] = device
        self.audio_streamers[device.device_id] = AudioStreamer(device)

    def remove_hearing_aid_device(self, device_id: str):
        """
        Remove a hearing aid device from the manager.

        Args:
        device_id (str): The ID of the hearing aid device to remove.
        """
        if device_id in self.hearing_aid_devices:
            del self.hearing_aid_devices[device_id]
            del self.audio_streamers[device_id]

    def start_streaming(self, device_id: str, audio_source_type: AudioSourceType):
        """
        Start streaming audio to a hearing aid device.

        Args:
        device_id (str): The ID of the hearing aid device to stream to.
        audio_source_type (AudioSourceType): The type of audio source to stream.
        """
        if device_id in self.audio_streamers:
            self.audio_streamers[device_id].start_streaming(audio_source_type)
        else:
            logging.error(f"Hearing aid device with ID {device_id} not found")

    def stop_streaming(self, device_id: str, audio_source_type: AudioSourceType):
        """
        Stop streaming audio to a hearing aid device.

        Args:
        device_id (str): The ID of the hearing aid device to stop streaming to.
        audio_source_type (AudioSourceType): The type of audio source to stop streaming.
        """
        if device_id in self.audio_streamers:
            self.audio_streamers[device_id].stop_streaming(audio_source_type)
        else:
            logging.error(f"Hearing aid device with ID {device_id} not found")


# Example usage
if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Create a hearing aid connectivity manager
    manager = HearingAidConnectivityManager()

    # Create a hearing aid device
    device = HearingAidDevice("12345", "Oticon Hearing Aid")

    # Add the hearing aid device to the manager
    manager.add_hearing_aid_device(device)

    # Connect to the hearing aid device
    device.connect()

    # Start streaming phone calls, TV, and music
    manager.start_streaming(device.device_id, AudioSourceType.PHONE_CALL)
    manager.start_streaming(device.device_id, AudioSourceType.TV)
    manager.start_streaming(device.device_id, AudioSourceType.MUSIC)

    # Stop streaming phone calls, TV, and music
    manager.stop_streaming(device.device_id, AudioSourceType.PHONE_CALL)
    manager.stop_streaming(device.device_id, AudioSourceType.TV)
    manager.stop_streaming(device.device_id, AudioSourceType.MUSIC)

    # Disconnect from the hearing aid device
    device.disconnect()

    # Remove the hearing aid device from the manager
    manager.remove_hearing_aid_device(device.device_id)
```
