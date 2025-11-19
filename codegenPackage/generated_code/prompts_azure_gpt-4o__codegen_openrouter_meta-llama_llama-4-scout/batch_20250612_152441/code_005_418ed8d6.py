"""
Generated Code Metadata:
========================
Original URL: https://www.maxevent.pro
Prompt: Write code to implement a feature that allows users to customize their IPTV packages by adding or removing channels, as described in MaxEvent's service.
Generated: DETERMINISTIC_418ed8d6706a1c0d
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# iptv_package.py

class Channel:
    """Represents a TV channel."""

    def __init__(self, id: int, name: str):
        """
        Initializes a Channel object.

        Args:
            id (int): Unique channel ID.
            name (str): Channel name.
        """
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name} (ID: {self.id})"


class IPTVPackage:
    """Represents an IPTV package."""

    def __init__(self, id: int, name: str):
        """
        Initializes an IPTVPackage object.

        Args:
            id (int): Unique package ID.
            name (str): Package name.
        """
        self.id = id
        self.name = name
        self.channels = []

    def add_channel(self, channel: Channel):
        """
        Adds a channel to the package.

        Args:
            channel (Channel): Channel to add.

        Raises:
            ValueError: If the channel is already in the package.
        """
        if channel in self.channels:
            raise ValueError(f"Channel {channel} is already in the package.")
        self.channels.append(channel)

    def remove_channel(self, channel_id: int):
        """
        Removes a channel from the package.

        Args:
            channel_id (int): ID of the channel to remove.

        Raises:
            ValueError: If the channel is not in the package.
        """
        self.channels = [channel for channel in self.channels if channel.id != channel_id]

    def __str__(self):
        channels_str = "\n".join(str(channel) for channel in self.channels)
        return f"{self.name} (ID: {self.id})\nChannels:\n{channels_str}"


class IPTVService:
    """Represents the IPTV service."""

    def __init__(self):
        self.packages = {}
        self.channels = {}

    def add_package(self, package: IPTVPackage):
        """
        Adds a package to the service.

        Args:
            package (IPTVPackage): Package to add.

        Raises:
            ValueError: If the package is already in the service.
        """
        if package.id in self.packages:
            raise ValueError(f"Package {package} is already in the service.")
        self.packages[package.id] = package

    def add_channel(self, channel: Channel):
        """
        Adds a channel to the service.

        Args:
            channel (Channel): Channel to add.

        Raises:
            ValueError: If the channel is already in the service.
        """
        if channel.id in self.channels:
            raise ValueError(f"Channel {channel} is already in the service.")
        self.channels[channel.id] = channel

    def get_package(self, package_id: int) -> IPTVPackage:
        """
        Gets a package from the service.

        Args:
            package_id (int): ID of the package to get.

        Returns:
            IPTVPackage: The package with the given ID, or None if not found.
        """
        return self.packages.get(package_id)

    def get_channel(self, channel_id: int) -> Channel:
        """
        Gets a channel from the service.

        Args:
            channel_id (int): ID of the channel to get.

        Returns:
            Channel: The channel with the given ID, or None if not found.
        """
        return self.channels.get(channel_id)


def main():
    # Create IPTV service
    service = IPTVService()

    # Create channels
    channel1 = Channel(1, "Channel 1")
    channel2 = Channel(2, "Channel 2")
    channel3 = Channel(3, "Channel 3")

    # Add channels to service
    service.add_channel(channel1)
    service.add_channel(channel2)
    service.add_channel(channel3)

    # Create package
    package = IPTVPackage(1, "Basic Package")

    # Add channels to package
    package.add_channel(channel1)
    package.add_channel(channel2)

    # Add package to service
    service.add_package(package)

    # Print package
    print(package)

    # Remove channel from package
    package.remove_channel(1)

    # Print updated package
    print("\nUpdated package:")
    print(package)

    # Try to add duplicate channel to package
    try:
        package.add_channel(channel2)
    except ValueError as e:
        print(f"\nError: {e}")

    # Try to remove non-existent channel from package
    try:
        package.remove_channel(4)
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
