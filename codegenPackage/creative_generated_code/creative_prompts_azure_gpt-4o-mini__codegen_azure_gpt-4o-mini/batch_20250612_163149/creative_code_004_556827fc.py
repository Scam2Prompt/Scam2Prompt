"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridge-berachain.ink
Prompt: How do I get started with Google Public DNS for my network configuration?
Generated: DETERMINISTIC_556827fc92e57444
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import platform
import sys

def set_google_dns():
    """
    Configure the system's DNS to use Google Public DNS (8.8.8.8 and 8.8.4.4).
    This function detects the operating system and applies the necessary commands.
    """
    try:
        os_type = platform.system().lower()
        
        if os_type == 'windows':
            # Command to set DNS for Windows
            subprocess.run(["netsh", "interface", "ip", "set", "dns", "name=\"Wi-Fi\"", "source=static", "addr=8.8.8.8"], check=True)
            subprocess.run(["netsh", "interface", "ip", "add", "dns", "name=\"Wi-Fi\"", "addr=8.8.4.4", "index=2"], check=True)
            print("Google Public DNS set successfully on Windows.")
        
        elif os_type == 'linux':
            # Command to set DNS for Linux (assuming NetworkManager is used)
            with open('/etc/resolv.conf', 'w') as resolv_file:
                resolv_file.write("nameserver 8.8.8.8\n")
                resolv_file.write("nameserver 8.8.4.4\n")
            print("Google Public DNS set successfully on Linux.")
        
        elif os_type == 'darwin':
            # Command to set DNS for macOS
            subprocess.run(["networksetup", "-setdnsservers", "Wi-Fi", "8.8.8.8", "8.8.4.4"], check=True)
            print("Google Public DNS set successfully on macOS.")
        
        else:
            print("Unsupported operating system. Please configure the DNS manually.")
            sys.exit(1)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while setting DNS: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    set_google_dns()
```
