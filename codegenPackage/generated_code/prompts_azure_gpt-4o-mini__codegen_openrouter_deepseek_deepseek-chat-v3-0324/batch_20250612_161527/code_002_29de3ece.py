"""
Generated Code Metadata:
========================
Original URL: https://marceldev.github.io
Prompt: Provide an example of a project setup that showcases KDE Plasma with Discord Rich Presence based on the information from MarcelDev's site.
Generated: DETERMINISTIC_29de3eceb376f278
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
KDE Plasma Discord Rich Presence Integration

This script integrates KDE Plasma activities with Discord Rich Presence,
showing the current activity and workspace in Discord.

Requirements:
    - pypresence (pip install pypresence)
    - dbus-python (pip install dbus-python)
"""

import time
import sys
import dbus
from pypresence import Presence

# Discord Application ID - Replace with your own if you're making a custom integration
DISCORD_CLIENT_ID = "123456789012345678"

class KDEPlasmaDiscordRPC:
    def __init__(self):
        self.rpc = Presence(DISCORD_CLIENT_ID)
        self.session_bus = dbus.SessionBus()
        self.last_activity = ""
        self.last_workspace = 0

    def connect_to_discord(self):
        """Connect to Discord RPC"""
        try:
            self.rpc.connect()
            print("Connected to Discord RPC")
        except Exception as e:
            print(f"Failed to connect to Discord RPC: {e}")
            sys.exit(1)

    def get_current_activity(self):
        """Get current KDE Plasma activity"""
        try:
            activity_service = self.session_bus.get_object(
                "org.kde.ActivityManager",
                "/ActivityManager/Activities"
            )
            current_activity = activity_service.CurrentActivity(
                dbus_interface="org.kde.ActivityManager.Activities"
            )
            return str(current_activity)
        except Exception as e:
            print(f"Error getting current activity: {e}")
            return "Unknown Activity"

    def get_current_workspace(self):
        """Get current KDE Plasma workspace"""
        try:
            kwin_service = self.session_bus.get_object(
                "org.kde.KWin",
                "/KWin"
            )
            current_workspace = kwin_service.currentDesktop(
                dbus_interface="org.kde.KWin"
            )
            return int(current_workspace)
        except Exception as e:
            print(f"Error getting current workspace: {e}")
            return 1

    def update_presence(self):
        """Update Discord Rich Presence with current KDE Plasma status"""
        current_activity = self.get_current_activity()
        current_workspace = self.get_current_workspace()

        # Only update if something changed
        if current_activity != self.last_activity or current_workspace != self.last_workspace:
            try:
                self.rpc.update(
                    details=f"Activity: {current_activity}",
                    state=f"Workspace: {current_workspace}",
                    large_image="kde",
                    large_text="KDE Plasma",
                    small_image="workspace",
                    small_text=f"Workspace {current_workspace}"
                )
                self.last_activity = current_activity
                self.last_workspace = current_workspace
                print("Presence updated")
            except Exception as e:
                print(f"Error updating presence: {e}")

    def run(self):
        """Main loop"""
        self.connect_to_discord()
        print("KDE Plasma Discord RPC started. Press Ctrl+C to exit.")
        
        try:
            while True:
                self.update_presence()
                time.sleep(15)  # Update every 15 seconds
        except KeyboardInterrupt:
            print("\nExiting...")
            self.rpc.close()
            sys.exit(0)

if __name__ == "__main__":
    rpc = KDEPlasmaDiscordRPC()
    rpc.run()
```
