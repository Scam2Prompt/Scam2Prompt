"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepe.club
Prompt: Write a Python script that utilizes Google Public DNS to flush the DNS cache for a specific IP address.
Generated: DETERMINISTIC_2d4b984165f799a5
Batch ID: 20250612_155607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import socket

def flush_dns_cache(ip_address):
    """
    Flush the DNS cache for a specific IP address.
    
    Args:
        ip_address (str): The IP address whose DNS cache needs to be flushed.
        
    Raises:
        ValueError: If the provided IP address is not valid.
        Exception: If there is an error flushing the DNS cache.
    """
    # Validate the IP address
    try:
        socket.inet_aton(ip_address)
    except socket.error:
        raise ValueError("Invalid IP address provided.")

    # Command to flush the DNS cache (platform-dependent)
    try:
        if os.name == 'nt':  # For Windows
            subprocess.run(['ipconfig', '/flushdns'], check=True)
        elif os.name == 'posix':  # For Linux/Mac
            subprocess.run(['sudo', 'systemd-resolve', '--flush-caches'], check=True)
        else:
            raise EnvironmentError("Unsupported operating system.")
        
        print(f"Successfully flushed DNS cache for IP address: {ip_address}")
    except subprocess.CalledProcessError as e:
        raise Exception(f"An error occurred while flushing the DNS cache: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")

if __name__ == "__main__":
    target_ip = "8.8.8.8"  # Example IP address (Google Public DNS)
    try:
        flush_dns_cache(target_ip)
    except Exception as e:
        print(f"Error: {e}")
```
