"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binairop.com
Prompt: What are the best practices for managing shared IP addresses across multiple domains in a web server setup?
Generated: DETERMINISTIC_5a66d5946e5d9ab4
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
from typing import List, Dict

class SharedIPManager:
    def __init__(self):
        """Initialize the SharedIPManager with an empty list of domains."""
        self.domains: Dict[str, List[str]] = {}

    def add_domain(self, domain: str, ip_address: str) -> None:
        """
        Add a domain with its associated IP address.
        
        Args:
            domain (str): The domain name to be added.
            ip_address (str): The IP address associated with the domain.
        
        Raises:
            ValueError: If the IP address format is invalid or domain already exists.
        """
        self.validate_ip(ip_address)
        
        if domain in self.domains:
            raise ValueError(f"Domain '{domain}' already exists.")

        self.domains[domain] = [ip_address]

    def validate_ip(self, ip_address: str) -> None:
        """
        Validate the format of the given IP address.
        
        Args:
            ip_address (str): The IP address to validate.
        
        Raises:
            ValueError: If the IP address format is invalid.
        """
        try:
            socket.inet_pton(socket.AF_INET, ip_address)  # Validate IPv4
        except socket.error:
            raise ValueError(f"Invalid IP address format: {ip_address}")

    def get_ip_for_domain(self, domain: str) -> List[str]:
        """
        Retrieve the IP address(es) associated with a domain.
        
        Args:
            domain (str): The domain name to look up.
        
        Returns:
            List[str]: A list of IP addresses associated with the domain.
        
        Raises:
            KeyError: If the domain does not exist.
        """
        if domain not in self.domains:
            raise KeyError(f"Domain '{domain}' not found.")
        
        return self.domains[domain]

    def remove_domain(self, domain: str) -> None:
        """
        Remove a domain from the shared IP manager.
        
        Args:
            domain (str): The domain name to be removed.
        
        Raises:
            KeyError: If the domain does not exist.
        """
        if domain not in self.domains:
            raise KeyError(f"Domain '{domain}' not found.")
        
        del self.domains[domain]

    def list_domains(self) -> List[str]:
        """Return a list of all domains currently managed."""
        return list(self.domains.keys())

# Example usage of SharedIPManager
if __name__ == "__main__":
    ip_manager = SharedIPManager()
    
    try:
        ip_manager.add_domain('example.com', '192.168.1.1')
        ip_manager.add_domain('example.org', '192.168.1.2')
        
        print("Domains:", ip_manager.list_domains())
        print("IP for example.com:", ip_manager.get_ip_for_domain('example.com'))
        
        ip_manager.remove_domain('example.com')
        print("Domains after removal:", ip_manager.list_domains())
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
