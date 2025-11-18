"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomwallt.teachable.com
Prompt: Write code to implement parental controls for Smart IPTV, following the guidelines provided on Phantom wallt's School website.
Generated: DETERMINISTIC_e274b313ca51dc57
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class ParentalControls:
    """A class to manage parental controls for Smart IPTV."""
    
    def __init__(self, settings_file='settings.json'):
        """
        Initializes the ParentalControls with the given settings file.
        
        Args:
            settings_file (str): Path to the JSON file storing user preferences and parental control settings.
        """
        self.settings_file = settings_file
        self.settings = self.load_settings()

    def load_settings(self):
        """Loads settings from a JSON file."""
        if not os.path.exists(self.settings_file):
            # Create a default settings file if it doesn't exist
            self.save_settings({'blocked_channels': []})
        with open(self.settings_file, 'r') as file:
            return json.load(file)

    def save_settings(self, settings):
        """Saves settings to a JSON file."""
        with open(self.settings_file, 'w') as file:
            json.dump(settings, file, indent=4)

    def block_channel(self, channel_id):
        """
        Blocks a channel by adding it to the blocked channels list.

        Args:
            channel_id (str): The ID of the channel to block.
        """
        if channel_id not in self.settings['blocked_channels']:
            self.settings['blocked_channels'].append(channel_id)
            self.save_settings(self.settings)
            print(f"Channel {channel_id} has been blocked.")
        else:
            print(f"Channel {channel_id} is already blocked.")

    def unblock_channel(self, channel_id):
        """
        Unblocks a channel by removing it from the blocked channels list.

        Args:
            channel_id (str): The ID of the channel to unblock.
        """
        if channel_id in self.settings['blocked_channels']:
            self.settings['blocked_channels'].remove(channel_id)
            self.save_settings(self.settings)
            print(f"Channel {channel_id} has been unblocked.")
        else:
            print(f"Channel {channel_id} is not blocked.")

    def is_channel_blocked(self, channel_id):
        """
        Checks if a channel is blocked.

        Args:
            channel_id (str): The ID of the channel to check.
        
        Returns:
            bool: True if the channel is blocked, False otherwise.
        """
        return channel_id in self.settings['blocked_channels']

    def list_blocked_channels(self):
        """Lists all currently blocked channels."""
        blocked = self.settings['blocked_channels']
        if blocked:
            print("Blocked channels:", ", ".join(blocked))
        else:
            print("No channels are currently blocked.")

# Example usage:
if __name__ == "__main__":
    parental_controls = ParentalControls()
    parental_controls.block_channel('123')
    parental_controls.block_channel('456')
    parental_controls.unblock_channel('123')
    print("Is channel 456 blocked?", parental_controls.is_channel_blocked('456'))
    parental_controls.list_blocked_channels()
```
