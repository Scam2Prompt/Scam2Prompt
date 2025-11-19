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
import platform
import os
from pypresence import Presence

# Constants for Discord Rich Presence
CLIENT_ID = "your_client_id_here"  # Replace with your Discord application's client ID
UPDATE_INTERVAL = 15  # How often to update presence in seconds

def get_system_info():
    """
    Retrieves the KDE version, distro name, and kernel version.
    Returns a dictionary with the information.
    """
    try:
        # Get KDE version by running the 'plasmashell --version' command
        kde_version = (
            os.popen("plasmashell --version")
            .read()
            .strip()
            .split("\n")[0]
            .replace("plasmashell", "")
            .strip()
        )
        
        # Get distro name using platform module
        distro = " ".join(platform.dist()) if hasattr(platform, "dist") else platform.system()
        
        # Get kernel version using platform module
        kernel_version = platform.release()
        
        return {
            "kde_version": kde_version,
            "distro": distro,
            "kernel_version": kernel_version,
        }
    except Exception as e:
        print(f"Error while retrieving system info: {e}")
        return {
            "kde_version": "Unknown",
            "distro": "Unknown",
            "kernel_version": "Unknown",
        }

def update_presence(rpc, system_info):
    """
    Updates Discord Rich Presence with the given system information.
    :param rpc: Active Presence object
    :param system_info: Dictionary containing system information
    """
    try:
        rpc.update(
            state=f"Distro: {system_info['distro']}",
            details=f"Kernel: {system_info['kernel_version']}",
            large_image="kde",  # Custom image key from Discord's Rich Presence assets
            large_text=f"KDE {system_info['kde_version']}",
        )
    except Exception as e:
        print(f"Error while updating presence: {e}")

def main():
    """
    Main function to initialize Discord Rich Presence and handle updates.
    """
    try:
        # Initialize Discord Rich Presence
        rpc = Presence(CLIENT_ID)
        rpc.connect()
        print("Connected to Discord RPC.")

        while True:
            # Get system information and update presence
            system_info = get_system_info()
            update_presence(rpc, system_info)
            
            # Wait for the specified interval before updating again
            time.sleep(UPDATE_INTERVAL)
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Disconnect from Discord RPC gracefully
        try:
            rpc.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
```

**Note:** Replace `"your_client_id_here"` with your Discord application's client ID and ensure you have the `pypresence` library installed (`pip install pypresence`). You may also need to configure assets in your Discord application for the `large_image` key (`kde`).
