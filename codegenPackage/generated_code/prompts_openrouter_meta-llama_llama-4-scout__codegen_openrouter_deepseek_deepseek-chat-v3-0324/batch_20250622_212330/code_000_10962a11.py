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
#!/usr/bin/env python3
"""
Discord Rich Presence integration for KDE Plasma showing system information.
"""

import os
import time
import psutil
from pypresence import Presence
from PyQt5.QtCore import QTimer, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication

class SystemInfo(QObject):
    """
    Collects and provides system information for Discord Rich Presence.
    """
    update_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_info)
        self.timer.start(5000)  # Update every 5 seconds

    def update_info(self):
        """Gather system information and emit update signal."""
        cpu_percent = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        battery = psutil.sensors_battery()

        info = {
            'cpu': f"{cpu_percent:.1f}%",
            'mem': f"{mem.percent:.1f}%",
            'disk': f"{disk.percent:.1f}%",
            'battery': f"{battery.percent:.1f}%" if battery else "N/A",
            'uptime': self._format_uptime()
        }
        self.update_signal.emit(info)

    def _format_uptime(self):
        """Format system uptime into a human-readable string."""
        uptime = time.time() - psutil.boot_time()
        hours, remainder = divmod(uptime, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{int(hours)}h {int(minutes)}m"

class DiscordRPC:
    """
    Handles Discord Rich Presence connection and updates.
    """
    def __init__(self):
        self.client_id = "1182201378231943208"  # Replace with your actual client ID
        self.rpc = None
        self.connected = False
        self.connect()

    def connect(self):
        """Attempt to connect to Discord RPC."""
        try:
            self.rpc = Presence(self.client_id)
            self.rpc.connect()
            self.connected = True
        except Exception as e:
            print(f"Failed to connect to Discord RPC: {e}")
            self.connected = False

    def update_presence(self, system_info):
        """Update Discord presence with system information."""
        if not self.connected:
            return

        try:
            self.rpc.update(
                state=f"CPU: {system_info['cpu']} | RAM: {system_info['mem']}",
                details=f"Disk: {system_info['disk']} | Battery: {system_info['battery']}",
                large_image="kde",
                large_text="KDE Plasma Desktop",
                small_image="terminal",
                small_text=f"Uptime: {system_info['uptime']}",
                start=int(time.time() - (time.time() - psutil.boot_time()))
            )
        except Exception as e:
            print(f"Failed to update presence: {e}")
            self.connected = False

def main():
    """Main application entry point."""
    # Required for QApplication in KDE Plasma
    if 'DISPLAY' not in os.environ:
        os.environ['DISPLAY'] = ':0'

    app = QApplication([])
    app.setApplicationName("KDE Plasma Discord RPC")

    system_info = SystemInfo()
    discord_rpc = DiscordRPC()

    system_info.update_signal.connect(discord_rpc.update_presence)
    system_info.update_info()  # Initial update

    app.exec_()

if __name__ == "__main__":
    main()
```
