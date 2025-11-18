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
import subprocess
import sys


def set_dns_servers(servers):
    """
    Set the DNS servers for the system.

    Args:
        servers (list): A list of DNS server IP addresses.

    Raises:
        subprocess.CalledProcessError: If the command fails.
    """
    try:
        # Configure the system DNS settings using the specified servers
        dns_config_command = f"networksetup -setdnsservers Wi-Fi {' '.join(servers)}"
        subprocess.run(dns_config_command, check=True, shell=True)
        print(f"Successfully set DNS servers to: {', '.join(servers)}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting DNS servers: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to configure OpenDNS for enhanced security and phishing protection.
    """
    # List of OpenDNS servers
    opendns_servers = [
        "208.67.222.222",  # OpenDNS Home
        "208.67.220.220"   # OpenDNS Home
    ]

    # Confirm with the user before making changes
    confirm = input("This will set your DNS servers to OpenDNS. Proceed? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Operation canceled by user.")
        sys.exit(0)

    # Set the DNS servers
    set_dns_servers(opendns_servers)


if __name__ == "__main__":
    main()
```

**Important Note:** This script is meant to be run on macOS due to the use of the `networksetup` command. Adjust the DNS configuration method based on your operating system as necessary. Always ensure you have the proper permissions to change network settings.
