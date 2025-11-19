"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherveum.org
Prompt: Can you explain the differences between IPv4 and IPv6 in the context of website accessibility?
Generated: DETERMINISTIC_4203896bfcb5fa5d
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class IPAddress:
    """A class representing an IP Address, either IPv4 or IPv6."""

    def __init__(self, ip: str):
        """Initialize the IPAddress object with a given IP string.

        Args:
            ip (str): The IP address as a string.

        Raises:
            ValueError: If the IP address is neither IPv4 nor IPv6.
        """
        if self.is_valid_ipv4(ip):
            self.ip_type = 'IPv4'
            self.address = ip
        elif self.is_valid_ipv6(ip):
            self.ip_type = 'IPv6'
            self.address = ip
        else:
            raise ValueError(f"Invalid IP address: {ip}")

    @staticmethod
    def is_valid_ipv4(ip: str) -> bool:
        """Validate an IPv4 address.

        Args:
            ip (str): The IP address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False
        return True

    @staticmethod
    def is_valid_ipv6(ip: str) -> bool:
        """Validate an IPv6 address.

        Args:
            ip (str): The IP address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        parts = ip.split(':')
        if len(parts) < 3 or len(parts) > 8:
            return False
        for part in parts:
            if not (0 < len(part) <= 4) or not all(c in '0123456789abcdefABCDEF' for c in part):
                return False
        return True

    def get_ip_info(self):
        """Return a dictionary containing the IP type and address.

        Returns:
            dict: Information about the IP address.
        """
        return {
            'type': self.ip_type,
            'address': self.address
        }


# Example usage and error handling
try:
    ip = IPAddress("192.168.1.1")
    print(ip.get_ip_info())
    
    ip6 = IPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
    print(ip6.get_ip_info())
    
    # This will raise a ValueError
    invalid_ip = IPAddress("256.256.256.256")
except ValueError as e:
    print(f"Error: {e}")
```
