"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Create a Wi-Fi network configuration script for a professional setup, similar to those provided by Sistemabox's WIFI PROFISSIONAL service."
Generated: DETERMINISTIC_3dafd965b719415d
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import os
import sys

def configure_wifi(ssid, password, interface="wlan0"):
    """
    Configures a Wi-Fi network on a Linux system.

    Args:
        ssid (str): The SSID of the Wi-Fi network.
        password (str): The password for the Wi-Fi network.
        interface (str): The network interface to use (default: wlan0).

    Returns:
        None
    """
    try:
        # Check if the required tools are installed
        if not shutil.which("nmcli"):
            raise EnvironmentError("NetworkManager CLI (nmcli) is not installed. Please install it to proceed.")

        # Validate input
        if not ssid or not password:
            raise ValueError("SSID and password cannot be empty.")

        # Create a new Wi-Fi connection
        print(f"Configuring Wi-Fi network '{ssid}' on interface '{interface}'...")
        subprocess.run(
            ["nmcli", "dev", "wifi", "connect", ssid, "password", password, "ifname", interface],
            check=True
        )
        print(f"Successfully connected to Wi-Fi network '{ssid}'.")

    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to configure Wi-Fi network. Details: {e}")
        sys.exit(1)
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except EnvironmentError as ee:
        print(f"Error: {ee}")
        sys.exit(1)
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    # Replace 'YourSSID' and 'YourPassword' with actual Wi-Fi credentials
    ssid = "YourSSID"
    password = "YourPassword"
    interface = "wlan0"  # Change this if your Wi-Fi interface is different

    configure_wifi(ssid, password, interface)
```
