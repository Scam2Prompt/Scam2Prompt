"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: Write a Python script to implement a Discord Rich Presence feature that displays KDE Plasma, distro, and kernel versions, as described on MarcelDev's website.
Generated: DETERMINISTIC_0e7b4213310d87b7
Batch ID: 20250612_154937
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://discord.com/developers/applications": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import platform
import time
from pypresence import Presence

# Discord client ID (replace with your application's client ID from https://discord.com/developers/applications)
DISCORD_CLIENT_ID = "YOUR_DISCORD_CLIENT_ID"

def get_kde_version():
    """
    Fetches the KDE Plasma version using the `plasmashell` --version command.
    Returns the version string if found, otherwise returns 'Unknown'.
    """
    try:
        result = os.popen("plasmashell --version").read().strip()
        # Extract version number (e.g., "plasmashell 5.27.5" -> "5.27.5")
        if result:
            return result.split()[-1]
    except Exception as e:
        # Log error for debugging purposes
        print(f"Error fetching KDE version: {e}")
    return "Unknown"

def get_distro_and_kernel():
    """
    Fetches the Linux distribution name and kernel version using platform library.
    Returns a tuple of strings (distro_name, kernel_version).
    """
    try:
        # Get distribution name and version
        distro_name = " ".join(platform.linux_distribution()[:2])  # Deprecated, replace with distro library if needed
        # Get kernel version
        kernel_version = platform.release()
        return distro_name, kernel_version
    except Exception as e:
        # Log error for debugging purposes
        print(f"Error fetching distro and kernel version: {e}")
    return "Unknown", "Unknown"

def main():
    """
    Main function to set up Discord Rich Presence and update KDE Plasma, distro, and kernel versions.
    """
    try:
        # Initialize Discord Rich Presence
        rpc = Presence(DISCORD_CLIENT_ID)
        rpc.connect()  # Connect to Discord

        # Fetch KDE Plasma, distro, and kernel information
        kde_version = get_kde_version()
        distro, kernel_version = get_distro_and_kernel()

        print("Successfully connected to Discord Rich Presence. Updating status...")

        while True:
            # Update Rich Presence with KDE Plasma, distro, and kernel information
            rpc.update(
                state=f"Distro: {distro}",
                details=f"Kernel: {kernel_version}",
                large_image="kde_logo",  # Replace with a valid asset name from your Discord app
                large_text=f"KDE Plasma {kde_version}",  # Tooltip text when hovering over the large image
                small_image="linux_logo",  # Replace with a valid asset name
                small_text="Linux Desktop Environment",  # Tooltip text for the small image
            )
            
            # Wait before updating the status again (e.g., every 15 seconds)
            time.sleep(15)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Closing Discord Rich Presence connection.")
        # Gracefully close the connection if needed (pypresence handles disconnect internally)
        rpc.close()

if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `YOUR_DISCORD_CLIENT_ID` with your Discord application's client ID from the [Discord Developer Portal](https://discord.com/developers/applications).
2. Ensure you have valid assets (e.g., `kde_logo` and `linux_logo`) uploaded to the Discord application settings for proper display.
3. This script uses `pypresence`, which can be installed via `pip install pypresence`.
4. The `platform.linux_distribution()` function is deprecated in Python 3.8+, so you may need to install the `distro` library (`pip install distro`) for more accurate Linux distro detection.
