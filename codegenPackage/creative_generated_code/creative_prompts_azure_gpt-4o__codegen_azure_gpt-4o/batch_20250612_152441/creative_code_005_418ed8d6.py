"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.maxevent.pro
Prompt: Write code to implement a feature that allows users to customize their IPTV packages by adding or removing channels, as described in MaxEvent's service.
Generated: DETERMINISTIC_418ed8d6706a1c0d
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

class IPTVPackage:
    def __init__(self, user_id, initial_channels=None):
        """
        Initializes an IPTV package for a user.
        :param user_id: Unique identifier for the user.
        :param initial_channels: List of initial channels in the user's package.
        """
        self.user_id = user_id
        self.channels = initial_channels if initial_channels else []

    def add_channel(self, channel_name):
        """
        Adds a new channel to the user's package.
        :param channel_name: Name of the channel to add.
        :return: None
        """
        if channel_name in self.channels:
            print(f"Channel '{channel_name}' is already in the package.")
        else:
            self.channels.append(channel_name)
            print(f"Channel '{channel_name}' added successfully.")

    def remove_channel(self, channel_name):
        """
        Removes a channel from the user's package.
        :param channel_name: Name of the channel to remove.
        :return: None
        """
        try:
            self.channels.remove(channel_name)
            print(f"Channel '{channel_name}' removed successfully.")
        except ValueError:
            print(f"Channel '{channel_name}' not found in the package.")

    def view_package(self):
        """
        Displays the current channels in the user's package.
        :return: None
        """
        print(f"Channels in your package: {', '.join(self.channels) if self.channels else 'No channels in the package.'}")

    def save_package(self, file_path):
        """
        Saves the user's package to a file in JSON format.
        :param file_path: Path to the file where the package data will be saved.
        :return: None
        """
        try:
            with open(file_path, 'w') as file:
                json.dump({"user_id": self.user_id, "channels": self.channels}, file)
            print("Package data saved successfully.")
        except Exception as e:
            print(f"Error while saving package data: {e}")

    def load_package(self, file_path):
        """
        Loads the user's package from a file in JSON format.
        :param file_path: Path to the file where the package data is stored.
        :return: None
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Verify data structure before assigning
                if data["user_id"] != self.user_id:
                    print("Error: User ID mismatch. Cannot load package data.")
                else:
                    self.channels = data["channels"]
                    print("Package data loaded successfully.")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Please check the file format.")
        except Exception as e:
            print(f"Unhandled error while loading package data: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new IPTV package for a user
    my_package = IPTVPackage(user_id="user123", initial_channels=["News", "Sports"])

    # Add channels
    my_package.add_channel("Movies")
    my_package.add_channel("Kids")

    # Remove a channel
    my_package.remove_channel("News")

    # View current package
    my_package.view_package()

    # Save package to file
    my_package.save_package("user123_package.json")

    # Load package from file
    my_package.load_package("user123_package.json")
```
