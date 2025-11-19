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

def dns_lookup(ip_address):
    """
    Perform a DNS lookup for a given IP address using Google Public DNS.
    
    Args:
        ip_address (str): The IP address to look up.
        
    Returns:
        str: The hostname corresponding to the IP address, or an error message.
    """
    try:
        # Use the gethostbyaddr function to perform a reverse DNS lookup
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        # Handle the case where the IP address cannot be resolved
        return f"Error: No host found for IP address '{ip_address}'."
    except socket.gaierror:
        # Handle the case where the input is not a valid IP address
        return f"Error: Invalid IP address '{ip_address}'."
    except Exception as e:
        # Handle any other unexpected exceptions
        return f"Unexpected error: {str(e)}"

def main():
    """
    Main function to execute the DNS lookup script.
    Prompts the user for an IP address and prints the corresponding hostname.
    """
    ip_address = input("Enter the IP address to lookup: ").strip()
    
    # Perform DNS lookup
    result = dns_lookup(ip_address)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
```
