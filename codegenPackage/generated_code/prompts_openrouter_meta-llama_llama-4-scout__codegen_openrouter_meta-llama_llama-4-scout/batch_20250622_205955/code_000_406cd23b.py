"""
Generated Code Metadata:
========================
Original URL: https://k7play.top
Prompt: Write a Python code snippet to implement a simple streaming service like K7 Play, with features like multi-device support and content categorization.
Generated: DETERMINISTIC_406cd23b0161378a
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# streaming_service.py

from enum import Enum
from typing import Dict, List

class ContentType(Enum):
    """Content type enumeration"""
    MOVIE = 1
    TV_SHOW = 2
    MUSIC = 3

class Device:
    """Device class"""
    def __init__(self, device_id: str, device_type: str):
        """
        Initialize a device

        Args:
        - device_id (str): Unique device ID
        - device_type (str): Device type (e.g., smartphone, tablet, etc.)
        """
        self.device_id = device_id
        self.device_type = device_type
        self.playback_history = []

    def play_content(self, content: str):
        """Play content on the device"""
        self.playback_history.append(content)

class StreamingService:
    """Streaming service class"""
    def __init__(self):
        """
        Initialize the streaming service
        """
        self.devices: Dict[str, Device] = {}
        self.content_catalog: Dict[ContentType, List[str]] = {
            ContentType.MOVIE: [],
            ContentType.TV_SHOW: [],
            ContentType.MUSIC: []
        }

    def register_device(self, device_id: str, device_type: str):
        """
        Register a new device

        Args:
        - device_id (str): Unique device ID
        - device_type (str): Device type (e.g., smartphone, tablet, etc.)
        """
        if device_id not in self.devices:
            self.devices[device_id] = Device(device_id, device_type)
            print(f"Device {device_id} registered successfully")
        else:
            print(f"Device {device_id} already registered")

    def add_content(self, content_type: ContentType, content: str):
        """
        Add content to the catalog

        Args:
        - content_type (ContentType): Type of content
        - content (str): Content title
        """
        if content_type in self.content_catalog:
            self.content_catalog[content_type].append(content)
            print(f"Content '{content}' added to {content_type.name} catalog")
        else:
            print(f"Invalid content type: {content_type}")

    def play_content_on_device(self, device_id: str, content_type: ContentType, content: str):
        """
        Play content on a registered device

        Args:
        - device_id (str): Unique device ID
        - content_type (ContentType): Type of content
        - content (str): Content title
        """
        if device_id in self.devices:
            if content in self.content_catalog[content_type]:
                self.devices[device_id].play_content(content)
                print(f"Playing {content} on device {device_id}")
            else:
                print(f"Content '{content}' not found in {content_type.name} catalog")
        else:
            print(f"Device {device_id} not registered")

    def get_device_playback_history(self, device_id: str):
        """
        Get playback history for a registered device

        Args:
        - device_id (str): Unique device ID

        Returns:
        - List[str]: Playback history for the device
        """
        if device_id in self.devices:
            return self.devices[device_id].playback_history
        else:
            print(f"Device {device_id} not registered")
            return []

def main():
    streaming_service = StreamingService()

    # Register devices
    streaming_service.register_device("device1", "smartphone")
    streaming_service.register_device("device2", "tablet")

    # Add content to catalog
    streaming_service.add_content(ContentType.MOVIE, "Movie 1")
    streaming_service.add_content(ContentType.TV_SHOW, "TV Show 1")
    streaming_service.add_content(ContentType.MUSIC, "Song 1")

    # Play content on devices
    streaming_service.play_content_on_device("device1", ContentType.MOVIE, "Movie 1")
    streaming_service.play_content_on_device("device2", ContentType.TV_SHOW, "TV Show 1")

    # Get device playback history
    print("Device 1 playback history:", streaming_service.get_device_playback_history("device1"))
    print("Device 2 playback history:", streaming_service.get_device_playback_history("device2"))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
