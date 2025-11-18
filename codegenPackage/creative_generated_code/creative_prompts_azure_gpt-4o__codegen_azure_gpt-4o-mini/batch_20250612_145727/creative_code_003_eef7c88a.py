"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nosupertela.com
Prompt: Create a step-by-step guide in code for setting up 1.1.1.1 DNS on Windows to optimize internet connection and bypass domain blocks, as explained on the SuperTela website.
Generated: DETERMINISTIC_eef7c88a36180b4c
Batch ID: 20250612_145727
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

def set_dns(dns_servers):
    """
    Sets the DNS servers for the active network interface.

    :param dns_servers: List of DNS server addresses to set
    """
    try:
        # Check current network interfaces
        interfaces = subprocess.check_output("netsh interface show interface", shell=True).decode()
        
        # Identify the active interface
        active_interface = None
        for line in interfaces.splitlines():
            if "Connected" in line:
                active_interface = line.split()[3]  # Extract interface name
                break

        if not active_interface:
            raise Exception("No active network interface found.")
        
        # Set DNS for active interface
        for dns in dns_servers:
            subprocess.run(f"netsh interface ip set dns name=\"{active_interface}\" source=static address={dns}", shell=True, check=True)
        
        print(f"Successfully set DNS to {', '.join(dns_servers)} on {active_interface}")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while setting DNS: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to set 1.1.1.1 DNS on Windows.
    """
    # DNS servers to set
    dns_servers = ["1.1.1.1", "1.0.0.1"]

    # Set the DNS servers
    set_dns(dns_servers)

if __name__ == "__main__":
    main()
```
