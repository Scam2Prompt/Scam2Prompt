"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: Develop a Discord bot that uses Rich Presence to display system details specific to KDE Plasma, following the concept described on MarcelDev's site.
Generated: DETERMINISTIC_fbc0be6ad318c259
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import time
import psutil
from pypresence import Presence

# Discord Application ID from your application's settings
DISCORD_CLIENT_ID = 'your_client_id_here'

# Check if running on KDE Plasma
try:
    desktop_env = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()
    if 'kde' not in desktop_env:
        raise EnvironmentError("This script is intended to run on KDE Plasma only.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

# Initialize Discord Rich Presence
try:
    rpc = Presence(DISCORD_CLIENT_ID)
    rpc.connect()
except Exception as e:
    print(f"Failed to connect to Discord RPC: {e}")
    sys.exit(1)

# Function to retrieve KDE Plasma version
def get_kde_version():
    try:
        kde_version = os.popen('plasmashell --version').read().strip()
        return kde_version.split(' ')[-1] if kde_version else "Unknown"
    except Exception as e:
        print(f"Error retrieving KDE version: {e}")
        return "Unknown"

# Function to retrieve CPU and RAM usage
def get_system_details():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        return cpu_usage, ram_usage
    except Exception as e:
        print(f"Error retrieving system details: {e}")
        return None, None

# Function to update Rich Presence details
def update_presence():
    try:
        kde_version = get_kde_version()
        cpu_usage, ram_usage = get_system_details()

        if cpu_usage is not None and ram_usage is not None:
            rpc.update(
                state=f"RAM Usage: {ram_usage}%",
                details=f"CPU Usage: {cpu_usage}%",
                large_image="kde_logo",  # Replace with your image asset name from Discord Dev Portal
                large_text=f"KDE Plasma {kde_version}",
                small_image="system_icon",  # Replace with your image asset name from Discord Dev Portal
                small_text="System Monitoring",
                start=time.time()
            )
    except Exception as e:
        print(f"Error updating Discord Presence: {e}")

# Main loop
print("Starting KDE Plasma Discord Rich Presence...")
try:
    while True:
        update_presence()
        time.sleep(15)  # Update presence every 15 seconds
except KeyboardInterrupt:
    print("\nExiting Discord Rich Presence...")
    rpc.close()
except Exception as e:
    print(f"Unexpected error: {e}")
    rpc.close()
```

### Notes:
1. Replace `your_client_id_here` with the Client ID of your Discord application.
2. Ensure you have the image assets (`kde_logo` and `system_icon`) uploaded in your Discord Developer Portal application settings.
3. Install dependencies using `pip install psutil pypresence`.
4. Run this script in a KDE Plasma environment; otherwise, it will exit gracefully with an error message.
