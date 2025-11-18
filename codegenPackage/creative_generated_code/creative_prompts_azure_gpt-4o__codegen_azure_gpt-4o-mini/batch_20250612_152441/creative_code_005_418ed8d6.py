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
# IPTV Package Customization Module
# This module allows users to customize their IPTV packages by adding or removing channels.

class Channel:
    """Represents a single IPTV channel."""
    
    def __init__(self, channel_id: int, name: str):
        self.channel_id = channel_id
        self.name = name

    def __repr__(self):
        return f"Channel(id={self.channel_id}, name='{self.name}')"


class IPTVPackage:
    """Represents a user's IPTV package."""
    
    def __init__(self, package_name: str):
        self.package_name = package_name
        self.channels = []  # List to hold Channel objects

    def add_channel(self, channel: Channel):
        """Adds a channel to the IPTV package."""
        if channel in self.channels:
            raise ValueError(f"Channel '{channel.name}' is already in the package.")
        self.channels.append(channel)

    def remove_channel(self, channel: Channel):
        """Removes a channel from the IPTV package."""
        try:
            self.channels.remove(channel)
        except ValueError:
            raise ValueError(f"Channel '{channel.name}' is not in the package.")

    def list_channels(self):
        """Returns a list of channels in the IPTV package."""
        return self.channels

    def __repr__(self):
        return f"IPTVPackage(name='{self.package_name}', channels={self.channels})"


def main():
    """Main function to demonstrate IPTV package customization."""
    try:
        # Create some channels
        channel1 = Channel(1, "News Channel")
        channel2 = Channel(2, "Sports Channel")
        channel3 = Channel(3, "Movie Channel")

        # Create a new IPTV package
        user_package = IPTVPackage("Premium Package")

        # Add channels to the package
        user_package.add_channel(channel1)
        user_package.add_channel(channel2)

        print("Channels after adding:")
        print(user_package.list_channels())

        # Attempt to add a duplicate channel
        try:
            user_package.add_channel(channel1)
        except ValueError as e:
            print(e)

        # Remove a channel from the package
        user_package.remove_channel(channel2)

        print("Channels after removal:")
        print(user_package.list_channels())

        # Attempt to remove a channel that is not in the package
        try:
            user_package.remove_channel(channel3)
        except ValueError as e:
            print(e)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
