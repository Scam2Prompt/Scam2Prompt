"""
Generated Code Metadata:
========================
Original URL: https://marceldev.github.io
Prompt: Generate a code snippet for integrating Discord Rich Presence to display KDE, distro, and kernel versions as described on MarcelDev's website.
Generated: DETERMINISTIC_df3946c410db1736
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pypresence
import subprocess
import time

# Function to get the KDE version
def get_kde_version():
    try:
        result = subprocess.run(["plasmashell", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip().split(" ")[-1]  # Extract version number
        else:
            return "Unknown KDE Version"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to get the Linux distribution name and version
def get_distro_info():
    try:
        result = subprocess.run(["lsb_release", "-d"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip().split(":")[1].strip()  # Extract distro info
        else:
            return "Unknown Distro"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to get the kernel version
def get_kernel_version():
    try:
        result = subprocess.run(["uname", "-r"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()  # Extract kernel version
        else:
            return "Unknown Kernel Version"
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize Discord Rich Presence
def initialize_discord_presence(client_id):
    try:
        rpc = pypresence.Presence(client_id)  # Create a Presence object
        rpc.connect()  # Connect to Discord
        return rpc
    except Exception as e:
        print(f"Failed to initialize Discord Rich Presence: {str(e)}")
        return None

# Update Discord Rich Presence
def update_discord_presence(rpc):
    try:
        kde_version = get_kde_version()
        distro_info = get_distro_info()
        kernel_version = get_kernel_version()

        rpc.update(
            state=f"Distro: {distro_info}",
            details=f"Kernel: {kernel_version}",
            large_image="kde_logo",  # Replace with your asset name in Discord Developer Portal
            large_text=f"KDE Version: {kde_version}",
            start=time.time()  # Start time for the session
        )
    except Exception as e:
        print(f"Failed to update Discord Rich Presence: {str(e)}")

# Main function
def main():
    CLIENT_ID = "your_client_id_here"  # Replace with your Discord application's client ID
    rpc = initialize_discord_presence(CLIENT_ID)
    if rpc is None:
        return

    try:
        while True:
            update_discord_presence(rpc)
            time.sleep(15)  # Update every 15 seconds
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        rpc.close()  # Ensure the connection is closed properly

if __name__ == "__main__":
    main()
```
