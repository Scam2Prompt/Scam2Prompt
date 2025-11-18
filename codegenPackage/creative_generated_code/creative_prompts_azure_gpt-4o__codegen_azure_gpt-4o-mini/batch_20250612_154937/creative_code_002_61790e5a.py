"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: Generate code for integrating Discord Rich Presence with KDE Plasma to show system information, referencing MarcelDev's implementation.
Generated: DETERMINISTIC_61790e5af69ce54a
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
import discord
from discord import RichPresence
from dbus import SystemBus, Interface
from threading import Thread

# Constants for DBus paths and service names
KDE_SERVICE = 'org.kde.plasmashell'
KDE_PATH = '/PlasmaShell'
KDE_INTERFACE = 'org.kde.PlasmaShell'

# Discord Rich Presence client
rpc = RichPresence()

def initialize_discord_rpc(client_id):
    """Initialize Discord Rich Presence with the given client ID."""
    try:
        rpc.start(client_id)
    except Exception as e:
        print(f"Error initializing Discord Rich Presence: {e}")
        sys.exit(1)

def update_rich_presence(state, details):
    """Update the Discord Rich Presence with the provided state and details."""
    try:
        rpc.update(state=state, details=details)
    except Exception as e:
        print(f"Error updating Discord Rich Presence: {e}")

def get_system_info():
    """Fetch system information from KDE Plasma using DBus."""
    try:
        bus = SystemBus()
        plasma_interface = Interface(bus.get_object(KDE_SERVICE, KDE_PATH), KDE_INTERFACE)
        current_desktop = plasma_interface.currentActivity()
        return f"Activity: {current_desktop}"
    except Exception as e:
        print(f"Error fetching system info from KDE Plasma: {e}")
        return "Error fetching info"

def update_presence_periodically(interval):
    """Periodically update Discord Rich Presence every `interval` seconds."""
    while True:
        system_info = get_system_info()
        update_rich_presence("Using KDE Plasma", system_info)
        time.sleep(interval)

def main():
    """Main function to run the Discord Rich Presence integration."""
    client_id = 'YOUR_DISCORD_APPLICATION_CLIENT_ID'  # Replace with your Discord application client ID
    initialize_discord_rpc(client_id)

    # Start the thread to update presence every 15 seconds
    update_thread = Thread(target=update_presence_periodically, args=(15,))
    update_thread.daemon = True
    update_thread.start()

    # Keep the program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting the application.")
        rpc.close()

if __name__ == "__main__":
    main()
```

Ensure to replace `'YOUR_DISCORD_APPLICATION_CLIENT_ID'` with your actual Discord application client ID before running the code.
