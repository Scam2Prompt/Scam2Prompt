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
import time
import psutil
from pypresence import Presence
from subprocess import check_output, CalledProcessError

# Constants
DISCORD_CLIENT_ID = "your_discord_client_id_here"  # Replace with your Discord Application Client ID
UPDATE_INTERVAL = 15  # Time in seconds between updates

def get_system_info():
    """
    Gather system information for Rich Presence display.
    Returns a dictionary with CPU usage, RAM usage, and KDE Plasma version.
    """
    try:
        # CPU usage
        cpu_usage = psutil.cpu_percent()

        # RAM usage
        memory_info = psutil.virtual_memory()
        ram_usage = f"{memory_info.used // (1024 * 1024)}MB / {memory_info.total // (1024 * 1024)}MB"

        # KDE Plasma version
        try:
            plasma_version_output = check_output(["plasmashell", "--version"], universal_newlines=True)
            plasma_version = plasma_version_output.strip().split(" ")[-1]
        except CalledProcessError:
            plasma_version = "Unknown"

        return {
            "cpu_usage": f"{cpu_usage}%",
            "ram_usage": ram_usage,
            "plasma_version": plasma_version,
        }
    except Exception as e:
        print(f"Error retrieving system information: {e}")
        return {
            "cpu_usage": "Error",
            "ram_usage": "Error",
            "plasma_version": "Error",
        }

def main():
    """
    Main function to integrate Discord Rich Presence with KDE Plasma system information.
    """
    try:
        # Initialize Discord Rich Presence
        rpc = Presence(DISCORD_CLIENT_ID)
        rpc.connect()

        while True:
            # Fetch system information
            system_info = get_system_info()

            # Update Rich Presence details
            rpc.update(
                state=f"RAM: {system_info['ram_usage']}",
                details=f"CPU Usage: {system_info['cpu_usage']}",
                large_image="kde_icon",  # Replace with uploaded image key in Discord developer portal
                large_text=f"KDE Plasma {system_info['plasma_version']}",
                small_image="cpu_icon",  # Replace with uploaded image key in Discord developer portal
                small_text="System Monitoring",
            )

            # Wait for the next update
            time.sleep(UPDATE_INTERVAL)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up resources
        try:
            rpc.close()
        except Exception as e:
            print(f"Error closing Discord RPC connection: {e}")

if __name__ == "__main__":
    main()
```
