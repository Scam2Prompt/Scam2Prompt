"""
Generated Code Metadata:
========================
Original URL: https://zetachain.id
Prompt: "What are the implications of shared IP addresses for website hosting and how can it be managed?"
Generated: DETERMINISTIC_68dd6545e0e419c7
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Shared IP Address Manager for Website Hosting

import ipaddress

class SharedIPManager:
    """
    Manages shared IP addresses for website hosting.

    Attributes:
    -----------
    ip_addresses (list): List of shared IP addresses.
    websites (dict): Dictionary of websites mapped to their respective IP addresses.

    Methods:
    --------
    add_ip_address(ip): Adds a new shared IP address.
    remove_ip_address(ip): Removes a shared IP address.
    add_website(ip, website): Maps a website to a shared IP address.
    remove_website(ip, website): Unmaps a website from a shared IP address.
    get_websites(ip): Retrieves a list of websites mapped to a shared IP address.
    """

    def __init__(self):
        self.ip_addresses = []
        self.websites = {}

    def add_ip_address(self, ip):
        """
        Adds a new shared IP address.

        Args:
        -----
        ip (str): IP address to add.

        Raises:
        ------
        ValueError: If the IP address is invalid or already exists.
        """
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            raise ValueError("Invalid IP address")

        if ip in self.ip_addresses:
            raise ValueError("IP address already exists")

        self.ip_addresses.append(ip)
        self.websites.setdefault(ip, [])

    def remove_ip_address(self, ip):
        """
        Removes a shared IP address.

        Args:
        -----
        ip (str): IP address to remove.

        Raises:
        ------
        ValueError: If the IP address does not exist.
        """
        if ip not in self.ip_addresses:
            raise ValueError("IP address does not exist")

        self.ip_addresses.remove(ip)
        del self.websites[ip]

    def add_website(self, ip, website):
        """
        Maps a website to a shared IP address.

        Args:
        -----
        ip (str): Shared IP address.
        website (str): Website to map.

        Raises:
        ------
        ValueError: If the IP address does not exist or the website is already mapped.
        """
        if ip not in self.ip_addresses:
            raise ValueError("IP address does not exist")

        if website in self.websites[ip]:
            raise ValueError("Website already mapped to this IP address")

        self.websites[ip].append(website)

    def remove_website(self, ip, website):
        """
        Unmaps a website from a shared IP address.

        Args:
        -----
        ip (str): Shared IP address.
        website (str): Website to unmap.

        Raises:
        ------
        ValueError: If the IP address does not exist or the website is not mapped.
        """
        if ip not in self.ip_addresses:
            raise ValueError("IP address does not exist")

        if website not in self.websites[ip]:
            raise ValueError("Website is not mapped to this IP address")

        self.websites[ip].remove(website)

    def get_websites(self, ip):
        """
        Retrieves a list of websites mapped to a shared IP address.

        Args:
        -----
        ip (str): Shared IP address.

        Returns:
        -------
        list: List of websites mapped to the IP address.

        Raises:
        ------
        ValueError: If the IP address does not exist.
        """
        if ip not in self.ip_addresses:
            raise ValueError("IP address does not exist")

        return self.websites[ip]


def main():
    # Example usage
    manager = SharedIPManager()

    try:
        manager.add_ip_address("192.168.1.1")
        manager.add_website("192.168.1.1", "example.com")
        manager.add_website("192.168.1.1", "sub.example.com")

        print(manager.get_websites("192.168.1.1"))  # Output: ['example.com', 'sub.example.com']

        manager.remove_website("192.168.1.1", "example.com")

        print(manager.get_websites("192.168.1.1"))  # Output: ['sub.example.com']

        manager.remove_ip_address("192.168.1.1")

        print(manager.ip_addresses)  # Output: []

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
