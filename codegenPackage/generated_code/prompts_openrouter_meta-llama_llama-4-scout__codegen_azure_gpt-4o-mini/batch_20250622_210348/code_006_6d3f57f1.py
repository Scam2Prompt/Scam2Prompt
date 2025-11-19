"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: How does Plesk's comprehensive GUI simplify web server and website management for IT specialists?
Generated: DETERMINISTIC_6d3f57f152a34519
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Plesk GUI Management Simulation

This script simulates a simplified version of Plesk's GUI for managing web servers and websites.
It provides functionalities to add, remove, and list websites, as well as manage server settings.
"""

class Website:
    """Class representing a website hosted on the server."""
    
    def __init__(self, domain: str):
        """
        Initialize a new website with a domain name.

        Args:
            domain (str): The domain name of the website.
        """
        self.domain = domain

    def __str__(self):
        """Return a string representation of the website."""
        return f"Website: {self.domain}"


class Server:
    """Class representing a web server with multiple websites."""
    
    def __init__(self):
        """Initialize the server with an empty list of websites."""
        self.websites = []

    def add_website(self, domain: str):
        """
        Add a new website to the server.

        Args:
            domain (str): The domain name of the website to add.

        Raises:
            ValueError: If the domain is already in use.
        """
        if any(website.domain == domain for website in self.websites):
            raise ValueError(f"Website with domain '{domain}' already exists.")
        self.websites.append(Website(domain))
        print(f"Website '{domain}' added successfully.")

    def remove_website(self, domain: str):
        """
        Remove a website from the server.

        Args:
            domain (str): The domain name of the website to remove.

        Raises:
            ValueError: If the domain does not exist.
        """
        for website in self.websites:
            if website.domain == domain:
                self.websites.remove(website)
                print(f"Website '{domain}' removed successfully.")
                return
        raise ValueError(f"Website with domain '{domain}' does not exist.")

    def list_websites(self):
        """List all websites hosted on the server."""
        if not self.websites:
            print("No websites hosted on this server.")
        else:
            print("Websites hosted on this server:")
            for website in self.websites:
                print(f"- {website}")

    def manage_server_settings(self):
        """Simulate managing server settings."""
        print("Managing server settings... (This is a placeholder for actual settings management.)")


def main():
    """Main function to simulate Plesk GUI operations."""
    server = Server()

    try:
        # Adding websites
        server.add_website("example.com")
        server.add_website("test.com")
        
        # Listing websites
        server.list_websites()

        # Removing a website
        server.remove_website("example.com")
        
        # Listing websites again
        server.list_websites()

        # Managing server settings
        server.manage_server_settings()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
