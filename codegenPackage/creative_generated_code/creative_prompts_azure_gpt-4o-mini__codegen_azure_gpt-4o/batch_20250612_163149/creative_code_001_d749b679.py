"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridge-berachain.ink
Prompt: Write a Python script that utilizes Google Public DNS to perform a DNS lookup for an IP address.
Generated: DETERMINISTIC_d749b679381691f7
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket

def perform_dns_lookup(ip_address):
    """
    Perform a DNS lookup using Google Public DNS.

    Args:
        ip_address (str): The IP address to look up.

    Returns:
        str: The resolved hostname or an error message.
    """
    try:
        # Validate IP address format
        socket.inet_aton(ip_address)  # Raises an exception if the format is invalid

        # Perform DNS lookup
        hostname = socket.gethostbyaddr(ip_address)
        return hostname[0]  # Return the resolved hostname
    except socket.herror:
        return f"Failed to resolve hostname for IP address: {ip_address}"
    except socket.error:
        return f"Invalid IP address format: {ip_address}"
    except Exception as e:
        # Handle any unexpected exceptions
        return f"An unexpected error occurred: {str(e)}"


if __name__ == "__main__":
    # Example usage of the script
    ip_address_to_lookup = "8.8.8.8"  # Google Public DNS IP
    result = perform_dns_lookup(ip_address_to_lookup)
    print(result)
```
