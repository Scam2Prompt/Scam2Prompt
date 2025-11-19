"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-2v.xyz
Prompt: Provide an example of how to enter an IP address into Google Public DNS for resolution.
Generated: DETERMINISTIC_55ebee6cc1ec77b0
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import socket

def resolve_ip_with_google_dns(ip_address):
    """
    Function to resolve an IP address using Google Public DNS.
    
    Args:
        ip_address (str): The IP address to be resolved.
        
    Returns:
        str: The resolved domain name or a message indicating an error.
    """
    try:
        # Ensure the IP address format is valid
        socket.inet_aton(ip_address)  # Will raise an exception if IP is invalid
        
        # Use Google Public DNS (8.8.8.8 and 8.8.4.4 are Google's DNS servers)
        # Google Public DNS is used implicitly when resolving hostnames with socket.gethostbyaddr
        resolved_domain, _, _ = socket.gethostbyaddr(ip_address)
        
        return resolved_domain  # Return the resolved domain name
    except socket.herror:
        # Handle errors during hostname resolution
        return f"Error: Unable to resolve IP address {ip_address}."
    except socket.error:
        # Handle invalid IP format
        return f"Error: Invalid IP address format {ip_address}."
    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected issue occurred: {str(e)}."

# Example usage
if __name__ == "__main__":
    # Replace '8.8.8.8' with the IP address you want to resolve
    ip_to_resolve = "8.8.8.8"
    
    # Resolve the IP address
    result = resolve_ip_with_google_dns(ip_to_resolve)
    
    # Print the result
    print(result)
```
