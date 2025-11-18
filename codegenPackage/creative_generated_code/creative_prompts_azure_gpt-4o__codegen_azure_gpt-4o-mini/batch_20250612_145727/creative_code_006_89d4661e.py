"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nosupertela.com
Prompt: Develop a script to automate the process of switching DNS to 1.1.1.1 when accessing streaming platforms like SuperTela, ensuring stable and unrestricted connectivity.
Generated: DETERMINISTIC_89d4661e61b2d2ba
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import platform
import subprocess
import requests

# Constants for DNS settings
DNS_SERVER = "1.1.1.1"
STREAMING_PLATFORMS = ["supertela.com"]  # Add more platforms as needed

def is_streaming_platform(url):
    """Check if the provided URL is one of the streaming platforms."""
    return any(platform in url for platform in STREAMING_PLATFORMS)

def set_dns(dns_server):
    """Set the system DNS to the specified DNS server."""
    try:
        if platform.system() == "Linux":
            # For Linux systems using NetworkManager
            subprocess.run(["nmcli", "connection", "modify", "System eth0", "ipv4.dns", dns_server], check=True)
            subprocess.run(["nmcli", "connection", "up", "System eth0"], check=True)
        
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["networksetup", "-setdnsservers", "Wi-Fi", dns_server], check=True)

        elif platform.system() == "Windows":
            subprocess.run(["netsh", "interface", "ip", "set", "dns", "Wi-Fi", "static", dns_server], check=True)

        else:
            raise Exception("Unsupported OS!")
        
        print(f"Successfully set DNS to {dns_server}")

    except subprocess.CalledProcessError as e:
        print(f"Error setting DNS: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to handle the DNS switching logic."""
    try:
        current_url = input("Enter the streaming URL you want to access: ")
        
        if is_streaming_platform(current_url):
            print(f"Detected streaming platform: {current_url}")
            set_dns(DNS_SERVER)
            print("You should now have stable and unrestricted connectivity.")
        else:
            print(f"{current_url} is not a recognized streaming platform.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
