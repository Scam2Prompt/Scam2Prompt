"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://internetbadguys.com
Prompt: Write code to integrate OpenDNS into a network configuration for enhanced security and phishing site blocking, inspired by InternetBadGuys.com.
Generated: DETERMINISTIC_c0f5352baa50d497
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import subprocess


def configure_opendns(primary_dns="208.67.222.222", secondary_dns="208.67.220.220"):
    """
    Configures the system to use OpenDNS servers for enhanced security.
    
    Args:
        primary_dns (str): OpenDNS Primary DNS IP.
        secondary_dns (str): OpenDNS Secondary DNS IP.
    """
    try:
        # Confirm root privileges
        if os.geteuid() != 0:
            print("This script requires root privileges. Please run as root or use sudo.")
            sys.exit(1)
        
        # Update resolv.conf file with OpenDNS IPs
        resolv_conf_path = "/etc/resolv.conf"
        with open(resolv_conf_path, "w") as resolv_conf:
            resolv_conf.write(f"# Updated by OpenDNS Integration Script\n")
            resolv_conf.write(f"nameserver {primary_dns}\n")
            resolv_conf.write(f"nameserver {secondary_dns}\n")
        
        print("OpenDNS servers have been successfully configured.")
        
    except PermissionError:
        print("Permission denied. Ensure you have the necessary privileges to modify network settings.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def restart_network_service():
    """
    Restarts the network service to apply DNS changes.
    """
    try:
        # Detect the operating system and restart the network service accordingly
        if sys.platform.startswith("linux"):
            subprocess.run(["systemctl", "restart", "networking"], check=True)
            print("Network service restarted successfully.")
        else:
            print("Unsupported operating system. Please restart your network service manually.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to restart the network service: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point for the script
    print("Integrating OpenDNS into network configuration...")
    configure_opendns()
    restart_network_service()
    print("Integration complete. Your system is now using OpenDNS.")
```
