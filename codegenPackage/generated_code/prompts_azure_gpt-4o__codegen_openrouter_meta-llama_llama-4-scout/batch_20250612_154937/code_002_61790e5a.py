"""
Generated Code Metadata:
========================
Original URL: https://marceldev.github.io
Prompt: Generate code for integrating Discord Rich Presence with KDE Plasma to show system information, referencing MarcelDev's implementation.
Generated: DETERMINISTIC_61790e5af69ce54a
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import platform
import psutil
import requests
import time
from datetime import datetime

# Discord Rich Presence
import pypresence

# KDE Plasma Integration
from dbus import BusType, Interface

class DiscordRichPresence:
    def __init__(self, client_id):
        self.client_id = client_id
        self.rpc = pypresence.Presence(client_id=client_id)
        self.rpc.connect()

    def update_presence(self, details, state, large_image, large_text, small_image=None, small_text=None):
        self.rpc.update(
            details=details,
            state=state,
            large_image=large_image,
            large_text=large_text,
            small_image=small_image,
            small_text=small_text
        )

class KDEPlasmaIntegration:
    def __init__(self):
        self.bus = Interface("org.freedesktop.DBus", "/org/freedesktop/sample/DBus", BusType.SESSION)

    def get_system_info(self):
        try:
            # Get CPU usage
            cpu_usage = psutil.cpu_percent()

            # Get memory usage
            memory = psutil.virtual_memory()
            memory_usage = memory.percent

            # Get current time
            current_time = datetime.now().strftime("%H:%M:%S")

            return {
                "cpu_usage": cpu_usage,
                "memory_usage": memory_usage,
                "current_time": current_time
            }
        except Exception as e:
            print(f"Error getting system info: {e}")
            return None

def main():
    client_id = "YOUR_CLIENT_ID"  # Replace with your Discord client ID
    rpc = DiscordRichPresence(client_id)

    kde_integration = KDEPlasmaIntegration()

    try:
        while True:
            system_info = kde_integration.get_system_info()
            if system_info:
                cpu_usage = system_info["cpu_usage"]
                memory_usage = system_info["memory_usage"]
                current_time = system_info["current_time"]

                details = f"CPU: {cpu_usage}% | Memory: {memory_usage}%"
                state = f"Current Time: {current_time}"
                large_image = "system_info"
                large_text = "System Information"

                rpc.update_presence(details, state, large_image, large_text)
            time.sleep(15)  # Update every 15 seconds
    except KeyboardInterrupt:
        print("Stopping Discord Rich Presence...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
