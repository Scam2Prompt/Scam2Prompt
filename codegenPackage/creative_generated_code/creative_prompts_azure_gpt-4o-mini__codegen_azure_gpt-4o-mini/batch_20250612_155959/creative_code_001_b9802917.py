"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nosupertela.com
Prompt: Write a script that automates the setup of 1.1.1.1 DNS on a Windows machine to ensure access to SuperTela.
Generated: DETERMINISTIC_b980291718343b61
Batch ID: 20250612_155959
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

def set_dns_server(dns_server="1.1.1.1"):
    """
    Set the DNS server for all network interfaces on a Windows machine.
    
    Args:
        dns_server (str): The DNS server IP address to be set. Default is "1.1.1.1".
    
    Raises:
        RuntimeError: If the DNS server configuration fails.
    """
    try:
        # Get the list of all network interfaces
        interfaces = subprocess.check_output("netsh interface show interface", shell=True, text=True)
        
        # Extract interface names
        interface_lines = [line for line in interfaces.splitlines() if "Connected" in line]
        interface_names = [line.split()[3] for line in interface_lines]

        for interface in interface_names:
            # Set the DNS server for each interface
            command = f"netsh interface ip set dns name=\"{interface}\" source=static addr={dns_server}"
            subprocess.run(command, shell=True, check=True)
            print(f"Successfully set DNS server for {interface} to {dns_server}")

    except subprocess.CalledProcessError as e:
        print(f"Failed to set DNS server: {e}", file=sys.stderr)
        raise RuntimeError("DNS server configuration failed") from e

if __name__ == "__main__":
    # Run the DNS setup
    set_dns_server()
```

Make sure to run this script with administrative privileges for it to successfully modify the DNS settings on the Windows machine.
