"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iplis.ru
Prompt: Create a function that generates random IP addresses for testing purposes, similar to the Random IP generator feature on IP Logger.
Generated: DETERMINISTIC_3220c2ff9c4f6344
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import ipaddress

def generate_random_ip() -> str:
    """
    Generates a random valid IPv4 address.
    
    Returns:
        str: A randomly generated IPv4 address in string format.
    
    Raises:
        ValueError: If the generated IP address is not valid (should not occur).
    """
    try:
        # Generate four random octets between 0 and 255
        octets = [random.randint(0, 255) for _ in range(4)]
        
        # Form the IP address
        ip_address = '.'.join(map(str, octets))
        
        # Validate the IP address
        ipaddress.IPv4Address(ip_address)  # This will raise an error if the IP is invalid
        
        return ip_address
    except Exception as e:
        # Log the error and raise a ValueError
        raise ValueError(f"Error generating IP address: {e}")

# Example usage
if __name__ == "__main__":
    try:
        random_ip = generate_random_ip()
        print(f"Generated random IP address: {random_ip}")
    except ValueError as e:
        print(e)
```
