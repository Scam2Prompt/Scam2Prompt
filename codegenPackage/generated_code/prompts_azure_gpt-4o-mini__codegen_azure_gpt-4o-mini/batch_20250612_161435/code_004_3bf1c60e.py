"""
Generated Code Metadata:
========================
Original URL: https://cafelc.com
Prompt: Develop a code example for a customer support chatbot that assists users in selecting the right microphone or speaker based on their needs.
Generated: DETERMINISTIC_3bf1c60e3be7bd72
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class AudioDevice:
    """Class representing an audio device with its specifications."""
    
    def __init__(self, name, device_type, features):
        """
        Initialize an audio device.

        :param name: Name of the audio device
        :param device_type: Type of the device (microphone or speaker)
        :param features: List of features of the device
        """
        self.name = name
        self.device_type = device_type
        self.features = features

    def __str__(self):
        """Return a string representation of the audio device."""
        return f"{self.name} ({self.device_type}): {', '.join(self.features)}"


class Chatbot:
    """Class representing a customer support chatbot for audio devices."""
    
    def __init__(self):
        """Initialize the chatbot with a list of available audio devices."""
        self.devices = self.load_devices()

    def load_devices(self):
        """Load audio devices from a JSON file."""
        try:
            with open('audio_devices.json', 'r') as file:
                devices_data = json.load(file)
                return [AudioDevice(**device) for device in devices_data]
        except FileNotFoundError:
            print("Error: The audio devices file was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: The audio devices file is not a valid JSON.")
            return []

    def recommend_device(self, user_needs):
        """
        Recommend an audio device based on user needs.

        :param user_needs: Dictionary containing user requirements
        :return: List of recommended devices
        """
        recommendations = []
        for device in self.devices:
            if self.matches_requirements(device, user_needs):
                recommendations.append(device)
        return recommendations

    def matches_requirements(self, device, user_needs):
        """
        Check if a device matches the user's requirements.

        :param device: The audio device to check
        :param user_needs: Dictionary containing user requirements
        :return: True if the device matches, False otherwise
        """
        for key, value in user_needs.items():
            if key in device.features and value not in device.features[key]:
                return False
        return True

    def chat(self):
        """Start the chatbot interaction with the user."""
        print("Welcome to the Audio Device Chatbot!")
        user_needs = self.get_user_needs()
        recommendations = self.recommend_device(user_needs)

        if recommendations:
            print("Based on your needs, we recommend the following devices:")
            for device in recommendations:
                print(device)
        else:
            print("Sorry, we couldn't find any devices that match your needs.")

    def get_user_needs(self):
        """
        Get user needs through a simple text-based interface.

        :return: Dictionary of user requirements
        """
        needs = {}
        needs['type'] = input("What type of device are you looking for? (microphone/speaker): ").strip().lower()
        needs['features'] = input("Please list any specific features you need (comma-separated): ").strip().split(',')
        needs['features'] = [feature.strip() for feature in needs['features']]
        return needs


if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
```

**Note:** Ensure you have a `audio_devices.json` file in the same directory with the following structure for the code to work:

```json
[
    {
        "name": "Blue Yeti",
        "device_type": "microphone",
        "features": ["USB", "Cardioid", "Plug and Play"]
    },
    {
        "name": "Logitech Z623",
        "device_type": "speaker",
        "features": ["2.1 Channel", "THX Certified", "Subwoofer"]
    }
]
```
