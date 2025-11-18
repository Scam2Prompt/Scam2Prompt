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
"""
Script to configure 1.1.1.1 DNS on a Windows machine.
This script uses the `netsh` command to update the DNS settings of the primary network interface.
Note: This script must be run with administrator privileges.
"""

import subprocess
import sys

def run_command(command):
    """
    Executes a shell command and returns the output.
    Raises an exception if the command fails.
    """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode != 0:
            raise Exception(f"Command failed with error: {result.stderr.strip()}")
        return result.stdout.strip()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def get_active_network_interface():
    """
    Retrieves the name of the active network interface.
    """
    command = 'netsh interface show interface'
    output = run_command(command)
    for line in output.splitlines():
        if "Connected" in line and "Dedicated" in line:
            # Extract the interface name (last column)
            return line.split()[-1]
    raise Exception("No active network interface found.")

def set_dns(interface_name, dns1, dns2):
    """
    Configures the DNS servers for the specified network interface.
    """
    # Set primary DNS
    run_command(f'netsh interface ip set dns name="{interface_name}" static {dns1}')
    
    # Set secondary DNS
    run_command(f'netsh interface ip add dns name="{interface_name}" {dns2} index=2')

def main():
    """
    Main function to configure 1.1.1.1 DNS on the active network interface.
    """
    print("Configuring 1.1.1.1 DNS on your Windows machine...")
    
    # Get the active network interface
    try:
        interface_name = get_active_network_interface()
        print(f"Active network interface detected: {interface_name}")
        
        # Set DNS to 1.1.1.1 and 1.0.0.1
        set_dns(interface_name, "1.1.1.1", "1.0.0.1")
        print("DNS settings updated successfully!")
    except Exception as e:
        print(f"Failed to configure DNS: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Ensure the script is running with administrator privileges
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("This script must be run as an administrator. Exiting...")
        sys.exit(1)
    
    main()
```

Please make sure to run this script as an administrator for it to work correctly. It modifies system network settings, which requires elevated access on Windows.
