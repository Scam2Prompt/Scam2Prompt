"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: Create a Python script that retrieves and displays kernel version information for use in a Discord Rich Presence integration, inspired by MarcelDev's project.
Generated: DETERMINISTIC_eab7580e31569cad
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import platform
import pypresence
import time

def get_kernel_version():
    """
    Retrieves the kernel version information using Python's platform module.
    Returns:
        str: A string representing the kernel version.
    """
    try:
        return platform.uname().release
    except Exception as e:
        # Log the error (if needed) and return a fallback message
        print(f"Error retrieving kernel version: {e}")
        return "Unknown Kernel Version"

def discord_rich_presence(kernel_version):
    """
    Sets up Discord Rich Presence using the pypresence module.
    Args:
        kernel_version (str): The kernel version to display in Discord.
    """
    try:
        # Replace 'your_client_id' with your application's Discord client ID
        client_id = 'your_client_id'
        rpc = pypresence.Presence(client_id)
        rpc.connect()

        # Update Rich Presence with kernel version information
        rpc.update(
            state=f"Kernel Version: {kernel_version}",
            details="Monitoring system configuration",
            large_image="linux",  # Replace with your asset key from Discord Developer Portal
            large_text="Linux Kernel Info",
            start=time.time()  # Start time for activity tracking
        )
        print("Discord Rich Presence updated successfully.")
        
        while True:
            # Keep the presence alive
            time.sleep(15)
    except pypresence.exceptions.InvalidID:
        print("Invalid Discord client ID. Please check your configuration.")
    except Exception as e:
        print(f"Error setting up Discord Rich Presence: {e}")
    finally:
        try:
            rpc.close()
        except NameError:
            pass

if __name__ == "__main__":
    # Main entry point for the script
    kernel_version = get_kernel_version()
    discord_rich_presence(kernel_version)
```

**Requirements:**
- Install `pypresence` using pip: `pip install pypresence`
- Replace `'your_client_id'` with your Discord application's client ID from the Discord Developer Portal.
