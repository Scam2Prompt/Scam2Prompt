"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: Provide an example of a project setup that showcases KDE Plasma with Discord Rich Presence based on the information from MarcelDev's site.
Generated: DETERMINISTIC_29de3eceb376f278
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pypresence  # Discord Rich Presence library
import subprocess
import time
import os

# Constants for Discord Application ID and update interval
DISCORD_CLIENT_ID = "YOUR_DISCORD_CLIENT_ID"  # Replace with your Discord application's ID
UPDATE_INTERVAL = 15  # Time (in seconds) between Rich Presence updates

# Helper function to get the current active window's title in KDE Plasma
def get_active_window_title():
    try:
        # Use the `xdotool` command to fetch the active window title
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode != 0:
            # Handle errors gracefully
            return "Unknown Application"
        return result.stdout.strip()
    except FileNotFoundError:
        # `xdotool` might not be installed
        return "Error: xdotool not found"

# Set up the Discord Rich Presence client
def setup_rpc():
    try:
        rpc = pypresence.Presence(DISCORD_CLIENT_ID)
        rpc.connect()
        return rpc
    except Exception as e:
        print(f"Error setting up Discord RPC: {e}")
        return None

# Main function to update Rich Presence data
def update_presence(rpc):
    while True:
        try:
            # Fetch active window title
            active_window = get_active_window_title()
            
            # Format the Rich Presence update
            rpc.update(
                state=f"Using {active_window}",  # Dynamic application name
                details="On KDE Plasma Desktop",  # Static environment name
                large_image="kde",  # Use your application's image assets
                large_text="KDE Plasma",  # Hover text for large_image
            )
        except Exception as e:
            print(f"Error updating presence: {e}")

        # Wait before updating again
        time.sleep(UPDATE_INTERVAL)

# Script entry point
if __name__ == "__main__":
    rpc = setup_rpc()
    if rpc:
        print("Discord Rich Presence started successfully.")
        try:
            update_presence(rpc)
        except KeyboardInterrupt:
            print("\nGracefully shutting down...")  # Handle Ctrl+C
            rpc.clear()
            rpc.close()
        except Exception as e:
            print(f"Unexpected error: {e}")
    else:
        print("Failed to initialize Discord RPC.")
```

### Notes:
1. Replace `YOUR_DISCORD_CLIENT_ID` with the Discord Rich Presence application's client ID obtained from the Discord Developer Portal.
2. Ensure you have `pypresence` installed via `pip install pypresence` and `xdotool` available on your system.
3. You need to configure Discord images (e.g., "kde") in the Rich Presence assets section of your Discord application settings.
