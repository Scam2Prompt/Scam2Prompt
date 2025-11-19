"""
Generated Code Metadata:
========================
Original URL: https://www.dessc.de
Prompt: Develop a script to troubleshoot common PC issues, such as internet connectivity problems.
Generated: DETERMINISTIC_8672e10bf6e4039c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import socket

def check_internet_connectivity():
    """
    Check if the PC has internet connectivity by pinging a reliable server (Google DNS).
    Returns True if connected, False otherwise.
    """
    try:
        # Ping Google's public DNS server (8.8.8.8)
        subprocess.run(["ping", "-c", "3", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def check_dns_resolution():
    """
    Check if DNS resolution is working by resolving a common domain name (e.g., google.com).
    Returns True if DNS resolution works, False otherwise.
    """
    try:
        socket.gethostbyname("google.com")
        return True
    except socket.error:
        return False

def check_network_adapter():
    """
    Check if the network adapter is enabled and has an IP address.
    Returns True if the adapter is active, False otherwise.
    """
    try:
        # Run the 'ipconfig' command (Windows) or 'ifconfig' (Linux/Mac) to check network adapter status
        if os.name == 'nt':  # Windows
            result = subprocess.run(["ipconfig"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        else:  # Linux/Mac
            result = subprocess.run(["ifconfig"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        
        # Check if the output contains an IP address
        output = result.stdout.decode()
        return "IPv4" in output or "inet " in output
    except subprocess.CalledProcessError:
        return False

def troubleshoot_pc():
    """
    Main function to troubleshoot common PC issues.
    Provides a summary of checks and their results.
    """
    print("Starting PC troubleshooting...\n")

    # Check internet connectivity
    print("Checking internet connectivity...")
    if check_internet_connectivity():
        print("Internet connectivity: OK")
    else:
        print("Internet connectivity: FAILED")

    # Check DNS resolution
    print("\nChecking DNS resolution...")
    if check_dns_resolution():
        print("DNS resolution: OK")
    else:
        print("DNS resolution: FAILED")

    # Check network adapter
    print("\nChecking network adapter...")
    if check_network_adapter():
        print("Network adapter: OK")
    else:
        print("Network adapter: FAILED")

    print("\nTroubleshooting complete.")

if __name__ == "__main__":
    try:
        troubleshoot_pc()
    except Exception as e:
        print(f"An error occurred during troubleshooting: {e}")
```
