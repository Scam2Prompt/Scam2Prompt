"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Develop a code example for a customer support chatbot that assists users in selecting the right microphone or speaker based on their needs.
Generated: DETERMINISTIC_3bf1c60e3be7bd72
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class AudioDevice:
    """Class representing an audio device with its specifications."""
    
    def __init__(self, device_type, name, features, price):
        """Initialize an audio device instance."""
        self.device_type = device_type  # Type can be 'Microphone' or 'Speaker'
        self.name = name  # Name of the audio device
        self.features = features  # List of features
        self.price = price  # Price of the device
    
    def __str__(self):
        """Return a string representation of the audio device."""
        return f"{self.device_type}: {self.name}, Features: {', '.join(self.features)}, Price: ${self.price}"


class ChatBot:
    """Chatbot class to assist users in selecting audio devices."""
    
    def __init__(self):
        """Initialize the chatbot with a list of available devices."""
        self.devices = []
        self.load_devices()

    def load_devices(self):
        """Load audio devices from a JSON file."""
        try:
            with open('audio_devices.json') as f:
                devices_data = json.load(f)
                for device in devices_data:
                    audio_device = AudioDevice(
                        device['type'],
                        device['name'],
                        device['features'],
                        device['price']
                    )
                    self.devices.append(audio_device)
        except FileNotFoundError:
            print("Error: Device data file not found.")
        except json.JSONDecodeError:
            print("Error: JSON decode error. Please check the data file.")

    def get_recommendation(self, user_needs):
        """Provide recommendations based on user needs."""
        recommendations = []

        for device in self.devices:
            # Check if any feature matches the user needs
            if any(need in device.features for need in user_needs):
                recommendations.append(device)

        if not recommendations:
            return "Sorry, no devices match your criteria."

        return recommendations

    def display_recommendations(self, recommendations):
        """Format and display the recommendations."""
        response = "Here are some recommendations for you:\n"
        for device in recommendations:
            response += str(device) + "\n"
        return response


def main():
    """Main function to run the chatbot."""
    chatbot = ChatBot()
    
    print("Welcome to the Audio Device Selector Bot!")
    print("Please tell me what features you are looking for in a microphone or speaker (e.g., noise cancellation, USB, Bluetooth):")
    
    user_input = input("Your needs (comma-separated): ")
    user_needs = [need.strip() for need in user_input.split(',')]
    
    recommendations = chatbot.get_recommendation(user_needs)
    
    if isinstance(recommendations, list):
        print(chatbot.display_recommendations(recommendations))
    else:
        print(recommendations)


if __name__ == "__main__":
    main()
```

```json
// audio_devices.json
[
    {
        "type": "Microphone",
        "name": "Blue Yeti",
        "features": ["USB", "Cardioid", "Noise Cancellation"],
        "price": 129.99
    },
    {
        "type": "Speaker",
        "name": "Bose Companion 2",
        "features": ["3.5mm", "USB", "Stereo"],
        "price": 99.99
    },
    {
        "type": "Microphone",
        "name": "Audio-Technica AT2020",
        "features": ["XLR", "Cardioid"],
        "price": 99.00
    },
    {
        "type": "Speaker",
        "name": "JBL Flip 5",
        "features": ["Bluetooth", "Waterproof"],
        "price": 89.95
    }
]
```
