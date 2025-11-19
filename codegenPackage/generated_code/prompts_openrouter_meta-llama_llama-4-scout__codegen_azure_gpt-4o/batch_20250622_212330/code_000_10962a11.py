"""
Generated Code Metadata:
========================
Original URL: https://marceldev.github.io
Prompt: Write a Discord rich presence plugin for KDE Plasma that shows system info.
Generated: DETERMINISTIC_10962a119748471a
Batch ID: 20250622_212330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discord_kde_presence.py
# A Discord Rich Presence plugin for KDE Plasma that displays system information.

import psutil
import time
import platform
from pypresence import Presence

# Constants
DISCORD_CLIENT_ID = "your_discord_client_id"  # Replace with your Discord application's client ID
UPDATE_INTERVAL = 15  # Time in seconds between updates

def get_system_info():
    """
    Gather system information to display in Discord Rich Presence.
    Returns a dictionary containing system info.
    """
    try:
        # Get CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Get memory usage
        memory = psutil.virtual_memory()
        memory_usage = f"{memory.used // (1024 ** 2)}MB / {memory.total // (1024 ** 2)}MB"

        # Get operating system info
        os_info = platform.system() + " " + platform.release()

        # Get uptime
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_hours = int(uptime_seconds // 3600)
        uptime_minutes = int((uptime_seconds % 3600) // 60)
        uptime = f"{uptime_hours}h {uptime_minutes}m"

        return {
            "cpu_usage": f"{cpu_usage}%",
            "memory_usage": memory_usage,
            "os_info": os_info,
            "uptime": uptime
        }
    except Exception as e:
        print(f"Error gathering system info: {e}")
        return None

def update_presence(rpc):
    """
    Update the Discord Rich Presence with system information.
    """
    try:
        system_info = get_system_info()
        if system_info:
            rpc.update(
                state=f"Memory: {system_info['memory_usage']}",
                details=f"CPU: {system_info['cpu_usage']}",
                large_image="kde_logo",  # Replace with your asset name in Discord Developer Portal
                large_text=system_info["os_info"],
                small_image="uptime_icon",  # Replace with your asset name in Discord Developer Portal
                small_text=f"Uptime: {system_info['uptime']}"
            )
    except Exception as e:
        print(f"Error updating presence: {e}")

def main():
    """
    Main function to initialize and run the Discord Rich Presence plugin.
    """
    try:
        # Initialize Discord Rich Presence
        rpc = Presence(DISCORD_CLIENT_ID)
        rpc.connect()
        print("Connected to Discord Rich Presence.")

        # Update presence in a loop
        while True:
            update_presence(rpc)
            time.sleep(UPDATE_INTERVAL)
    except Exception as e:
        print(f"Error in main loop: {e}")
    finally:
        print("Shutting down Discord Rich Presence.")
        rpc.close()

if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `your_discord_client_id` with your actual Discord application's client ID.
2. Add appropriate assets (e.g., `kde_logo`, `uptime_icon`) in the Discord Developer Portal for the images used in the presence.
3. Install required dependencies using `pip install psutil pypresence`.
4. Run the script in a Python environment compatible with KDE Plasma.
