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

def set_dns_to_1_1_1_1(interface_name: str):
    """
    Sets the DNS server for the specified network interface to 1.1.1.1.

    Args:
        interface_name (str): The name of the network interface to configure.

    Returns:
        bool: True if the DNS was successfully set, False otherwise.
    """
    try:
        # Command to set primary DNS to 1.1.1.1
        command_primary_dns = ["netsh", "interface", "ip", "set", "dns", interface_name, "static", "1.1.1.1"]
        
        # Command to set alternate DNS to 1.0.0.1
        command_alternate_dns = ["netsh", "interface", "ip", "add", "dns", interface_name, "1.0.0.1", "index=2"]
        
        # Execute the primary DNS command
        subprocess.run(command_primary_dns, check=True)
        
        # Execute the alternate DNS command
        subprocess.run(command_alternate_dns, check=True)
        
        print(f"DNS successfully set to 1.1.1.1 (primary) and 1.0.0.1 (alternate) for interface '{interface_name}'.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error setting DNS: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def main():
    """
    Main function to handle user input and configure the DNS.
    """
    print("Automated 1.1.1.1 DNS Setup for SuperTela")
    
    # Prompt user for the network interface name
    interface_name = input("Enter the name of the network interface to configure: ").strip()
    
    if not interface_name:
        print("Error: Interface name cannot be empty.")
        sys.exit(1)
    
    # Attempt to set the DNS
    success = set_dns_to_1_1_1_1(interface_name)
    
    if success:
        print("DNS setup completed successfully!")
    else:
        print("DNS setup failed. Please verify the network interface name and try again.")


if __name__ == "__main__":
    main()
```
