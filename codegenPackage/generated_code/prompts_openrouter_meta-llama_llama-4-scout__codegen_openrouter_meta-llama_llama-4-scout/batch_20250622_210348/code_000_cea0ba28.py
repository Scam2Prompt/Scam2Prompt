"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: What is Plesk and how does it help IT specialists manage web services?
Generated: DETERMINISTIC_cea0ba28f8e0a8cd
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Plesk Information and Web Service Management Simulator

class Plesk:
    """
    A class representing Plesk, a web management tool.
    
    Attributes:
    ----------
    web_services : list
        A list of web services managed by Plesk.
        
    Methods:
    -------
    add_service(service_name)
        Adds a new web service to Plesk.
    remove_service(service_name)
        Removes a web service from Plesk.
    display_services()
        Displays all web services managed by Plesk.
    """

    def __init__(self):
        """
        Initializes Plesk with an empty list of web services.
        """
        self.web_services = []

    def add_service(self, service_name):
        """
        Adds a new web service to Plesk.

        Parameters:
        ----------
        service_name : str
            The name of the web service to add.

        Raises:
        ------
        ValueError
            If the service name is empty or already exists.
        """
        if not service_name:
            raise ValueError("Service name cannot be empty.")
        if service_name in self.web_services:
            raise ValueError("Service already exists.")
        self.web_services.append(service_name)

    def remove_service(self, service_name):
        """
        Removes a web service from Plesk.

        Parameters:
        ----------
        service_name : str
            The name of the web service to remove.

        Raises:
        ------
        ValueError
            If the service name does not exist.
        """
        if service_name not in self.web_services:
            raise ValueError("Service does not exist.")
        self.web_services.remove(service_name)

    def display_services(self):
        """
        Displays all web services managed by Plesk.
        """
        return self.web_services


def main():
    try:
        plesk = Plesk()

        # Adding web services
        plesk.add_service("Webmail")
        plesk.add_service("FTP")
        plesk.add_service("SSH")

        # Displaying web services
        print("Managed Web Services:")
        for service in plesk.display_services():
            print(service)

        # Removing a web service
        plesk.remove_service("FTP")

        # Displaying updated web services
        print("\nUpdated Managed Web Services:")
        for service in plesk.display_services():
            print(service)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
