"""
Generated Code Metadata:
========================
Original URL: https://nosupertela.com
Prompt: Create a step-by-step guide in code for setting up 1.1.1.1 DNS on Windows to optimize internet connection and bypass domain blocks, as explained on the SuperTela website.
Generated: DETERMINISTIC_eef7c88a36180b4c
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import sys

def set_dns(dns_servers):
    """
    Set the DNS servers for the network adapter to the specified DNS servers.

    Args:
        dns_servers (list): A list of DNS server IP addresses to set.
    """
    try:
        # Get the name of the active network adapter
        adapter_name = subprocess.check_output("netsh interface show interface", shell=True).decode()
        adapter_name = [line.split()[3] for line in adapter_name.splitlines() if "Connected" in line][0]

        # Construct the command to set the DNS servers
        command = f"netsh interface ip set dns name=\"{adapter_name}\" static {dns_servers[0]}"
        subprocess.run(command, shell=True, check=True)

        # Set the secondary DNS server if provided
        if len(dns_servers) > 1:
            command = f"netsh interface ip add dns name=\"{adapter_name}\" {dns_servers[1]} index=2"
            subprocess.run(command, shell=True, check=True)

        print(f"Successfully set DNS servers to: {', '.join(dns_servers)}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while setting DNS: {e}")
        sys.exit(1)
    except IndexError:
        print("No active network adapter found.")
        sys.exit(1)

def main():
    """
    Main function to execute the DNS setup.
    """
    # Define the DNS servers to be set (1.1.1.1 and 1.0.0.1)
    dns_servers = ["1.1.1.1", "1.0.0.1"]

    print("Setting up DNS servers to optimize internet connection and bypass domain blocks...")
    set_dns(dns_servers)

if __name__ == "__main__":
    main()
```

### Note:
- This script should be run with administrative privileges to modify network settings.
- Ensure that Python is installed on the Windows machine where this script will be executed.
