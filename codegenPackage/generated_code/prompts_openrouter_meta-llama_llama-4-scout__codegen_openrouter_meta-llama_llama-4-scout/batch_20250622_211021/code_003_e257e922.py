"""
Generated Code Metadata:
========================
Original URL: https://npcgrant.online
Prompt: How can I configure a LiteSpeed Web Server to serve content over a specific port, like Port 443?
Generated: DETERMINISTIC_e257e92261585e9f
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Configuration for LiteSpeed Web Server
configure_litespeed_port() {
  # Define the port number
  local port=$1

  # Check if port is provided
  if [ -z "$port" ]; then
    echo "Error: Port number is required."
    return 1
  fi

  # Check if port is within valid range
  if ! [[ $port =~ ^[0-9]+$ ]] || [ $port -lt 1 ] || [ $port -gt 65535 ]; then
    echo "Error: Invalid port number. Port must be an integer between 1 and 65535."
    return 1
  fi

  # LiteSpeed configuration file path
  local litespeed_config_file="/usr/local/lsws/conf/litespeed.conf"

  # Check if LiteSpeed configuration file exists
  if [ ! -f "$litespeed_config_file" ]; then
    echo "Error: LiteSpeed configuration file not found."
    return 1
  fi

  # Update the listener port in the LiteSpeed configuration file
  sed -i "s/\(listen *:\)[0-9]\+/\1$port/" "$litespeed_config_file"

  # Restart LiteSpeed to apply changes
  /usr/local/lsws/bin/lswsctrl restart

  # Check if LiteSpeed restarted successfully
  if [ $? -ne 0 ]; then
    echo "Error: Failed to restart LiteSpeed."
    return 1
  fi
}

# Example usage
if [ "${BASH_SOURCE[0]}" == "$0" ]; then
  configure_litespeed_port 443
fi
```

```python
import subprocess
import os

def configure_litespeed_port(port):
    """
    Configure LiteSpeed Web Server to serve content over a specific port.

    Args:
        port (int): The port number.

    Returns:
        bool: True if configuration was successful, False otherwise.
    """

    # Check if port is provided
    if not port:
        print("Error: Port number is required.")
        return False

    # Check if port is within valid range
    if not isinstance(port, int) or port < 1 or port > 65535:
        print("Error: Invalid port number. Port must be an integer between 1 and 65535.")
        return False

    # LiteSpeed configuration file path
    litespeed_config_file = "/usr/local/lsws/conf/litespeed.conf"

    # Check if LiteSpeed configuration file exists
    if not os.path.exists(litespeed_config_file):
        print("Error: LiteSpeed configuration file not found.")
        return False

    try:
        # Update the listener port in the LiteSpeed configuration file
        with open(litespeed_config_file, 'r') as file:
            file_data = file.read()

        file_data = file_data.replace("listen *:80", f"listen *:{port}")

        with open(litespeed_config_file, 'w') as file:
            file.write(file_data)

        # Restart LiteSpeed to apply changes
        subprocess.check_call(['/usr/local/lsws/bin/lswsctrl', 'restart'])

        return True

    except subprocess.CalledProcessError:
        print("Error: Failed to restart LiteSpeed.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
if __name__ == "__main__":
    configure_litespeed_port(443)
```
