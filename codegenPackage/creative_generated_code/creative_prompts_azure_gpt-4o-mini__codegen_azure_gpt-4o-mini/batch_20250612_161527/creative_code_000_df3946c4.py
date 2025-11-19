"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: Generate a code snippet for integrating Discord Rich Presence to display KDE, distro, and kernel versions as described on MarcelDev's website.
Generated: DETERMINISTIC_df3946c410db1736
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import os
import json
import discord

class DiscordRichPresence:
    def __init__(self, client_id):
        """
        Initializes the Discord Rich Presence client.
        
        Args:
            client_id (str): The Discord application client ID.
        """
        self.client_id = client_id
        self.rpc = discord.RichPresence(client_id)
        self.rpc.start()

    def update_presence(self, state, details):
        """
        Updates the Discord Rich Presence.

        Args:
            state (str): The state to display.
            details (str): The details to display.
        """
        try:
            self.rpc.update(state=state, details=details, large_image="kde", small_image="linux")
        except Exception as e:
            print(f"Failed to update Discord Rich Presence: {e}")

    def get_system_info(self):
        """
        Retrieves KDE, distribution, and kernel version information.

        Returns:
            tuple: Containing KDE version, distribution name, and kernel version.
        """
        try:
            kde_version = os.popen("qdbus org.kde.plasma.desktop /Plasma/ActiveApp version").read().strip()
            distro_name = os.popen("lsb_release -d | cut -f2").read().strip()
            kernel_version = os.popen("uname -r").read().strip()
            return kde_version, distro_name, kernel_version
        except Exception as e:
            print(f"Failed to get system info: {e}")
            return "unknown", "unknown", "unknown"

    def run(self):
        """
        Main loop to continuously update the Rich Presence.
        """
        while True:
            kde_version, distro_name, kernel_version = self.get_system_info()
            state = f"KDE: {kde_version} | Distro: {distro_name} | Kernel: {kernel_version}"
            details = "Running KDE Plasma with Linux"
            self.update_presence(state, details)
            time.sleep(15)  # Update every 15 seconds

if __name__ == "__main__":
    DISCORD_CLIENT_ID = "YOUR_DISCORD_CLIENT_ID"  # Replace with your actual Discord Client ID
    rich_presence = DiscordRichPresence(DISCORD_CLIENT_ID)
    rich_presence.run()
```
