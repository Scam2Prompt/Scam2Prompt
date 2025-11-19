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
import subprocess
import platform
import socket

def check_internet_connection():
    """Check if the computer can connect to the internet by pinging a reliable server."""
    try:
        # Ping Google's public DNS server
        subprocess.check_output("ping -c 1 8.8.8.8", shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def get_local_ip():
    """Retrieve the local IP address of the machine."""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except socket.error as e:
        print(f"Error retrieving local IP: {e}")
        return None

def check_dns_resolution(domain):
    """Check if the DNS resolution is working for a given domain."""
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror as e:
        print(f"DNS resolution error for {domain}: {e}")
        return None

def troubleshoot_internet():
    """Run a series of checks to troubleshoot internet connectivity issues."""
    print("Starting internet connectivity troubleshooting...")

    # Check internet connection
    if check_internet_connection():
        print("Internet connection is active.")
    else:
        print("No internet connection detected.")
        print("Checking local IP address...")
        local_ip = get_local_ip()
        if local_ip:
            print(f"Local IP Address: {local_ip}")
        else:
            print("Could not retrieve local IP address.")

        print("Checking DNS resolution for google.com...")
        dns_ip = check_dns_resolution("google.com")
        if dns_ip:
            print(f"DNS resolution successful. IP for google.com: {dns_ip}")
        else:
            print("DNS resolution failed. Please check your DNS settings.")

if __name__ == "__main__":
    # Run the troubleshooting script
    troubleshoot_internet()
```
