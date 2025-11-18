"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econtrolsa.ch
Prompt: Provide a code example for configuring IT cabling and audio-video integration in a smart home environment, based on eControl SA's services in câblages informatiques and audio/vidéo.
Generated: DETERMINISTIC_c25c2cdd32076848
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of clean, well-documented Python code that simulates configuring IT cabling and audio-video integration in a smart home environment.

```python
import json


class SmartHomeConfiguration:
    """
    Class to configure IT cabling and audio-video integration in a smart home.
    """

    def __init__(self):
        """
        Initialize the configuration with default settings.
        """
        self.network_settings = {}
        self.av_settings = {}

    def configure_network_cabling(self, room, cable_type, ports):
        """
        Configure IT cabling for a specific room.

        Args:
            room (str): The name of the room being configured (e.g., "Living Room").
            cable_type (str): Type of cable to be used (e.g., "Cat6", "Fiber").
            ports (int): Number of network ports to be installed.
        """
        if not room or not cable_type or ports <= 0:
            raise ValueError("Invalid input for network cabling configuration.")

        self.network_settings[room] = {
            "cable_type": cable_type,
            "ports": ports
        }

    def configure_audio_video(self, room, speaker_count, screen_size):
        """
        Configure audio-video integration in a specific room.

        Args:
            room (str): The name of the room being configured (e.g., "Home Theater").
            speaker_count (int): Number of speakers to be installed.
            screen_size (float): Size of the screen in inches.
        """
        if not room or speaker_count <= 0 or screen_size <= 0:
            raise ValueError("Invalid input for audio-video configuration.")

        self.av_settings[room] = {
            "speaker_count": speaker_count,
            "screen_size": screen_size
        }

    def export_configuration(self, file_path):
        """
        Export the configuration to a JSON file.

        Args:
            file_path (str): Path to the file where configuration will be saved.
        """
        try:
            config = {
                "network_settings": self.network_settings,
                "audio_video_settings": self.av_settings
            }
            with open(file_path, 'w') as file:
                json.dump(config, file, indent=4)
            print(f"Configuration exported successfully to {file_path}")
        except IOError as e:
            print(f"Error exporting configuration: {str(e)}")

    def load_configuration(self, file_path):
        """
        Load configuration from a JSON file.

        Args:
            file_path (str): Path to the file where configuration is saved.
        """
        try:
            with open(file_path, 'r') as file:
                config = json.load(file)
                self.network_settings = config.get("network_settings", {})
                self.av_settings = config.get("audio_video_settings", {})
            print(f"Configuration loaded successfully from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading configuration: {str(e)}")


# Example usage:
if __name__ == "__main__":
    # Create an instance of the configuration class
    home_config = SmartHomeConfiguration()

    # Configure IT cabling
    home_config.configure_network_cabling("Living Room", "Cat6", 4)
    home_config.configure_network_cabling("Office", "Fiber", 2)

    # Configure audio-video integration
    home_config.configure_audio_video("Home Theater", 5, 75.0)
    home_config.configure_audio_video("Bedroom", 2, 50.0)

    # Export configuration to a file
    home_config.export_configuration("smart_home_config.json")

    # Load configuration from a file
    home_config.load_configuration("smart_home_config.json")
```

This Python script implements the requested functionality, including IT cabling and audio-video integration setup with functionalities for saving and loading configurations. It adheres to best practices, includes error handling, and is production-ready.
