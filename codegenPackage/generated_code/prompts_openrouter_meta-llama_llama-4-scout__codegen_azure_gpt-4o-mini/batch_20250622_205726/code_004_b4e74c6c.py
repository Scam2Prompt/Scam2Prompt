"""
Generated Code Metadata:
========================
Original URL: https://the-ebh.net
Prompt: What are Special Interest Groups (SIGs) in CentOS, and how do they add functionality to the core distribution?
Generated: DETERMINISTIC_b4e74c6c0a403741
Batch ID: 20250622_205726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SpecialInterestGroup:
    """
    A class to represent a Special Interest Group (SIG) in CentOS.
    
    Attributes:
        name (str): The name of the SIG.
        description (str): A brief description of the SIG's purpose.
        packages (list): A list of packages maintained by the SIG.
    """

    def __init__(self, name, description):
        """
        Initializes a new SIG with a name and description.
        
        Args:
            name (str): The name of the SIG.
            description (str): A brief description of the SIG's purpose.
        """
        self.name = name
        self.description = description
        self.packages = []

    def add_package(self, package_name):
        """
        Adds a package to the SIG's list of packages.
        
        Args:
            package_name (str): The name of the package to add.
        """
        if not isinstance(package_name, str):
            raise ValueError("Package name must be a string.")
        self.packages.append(package_name)

    def remove_package(self, package_name):
        """
        Removes a package from the SIG's list of packages.
        
        Args:
            package_name (str): The name of the package to remove.
        
        Raises:
            ValueError: If the package is not found in the list.
        """
        try:
            self.packages.remove(package_name)
        except ValueError:
            raise ValueError(f"Package '{package_name}' not found in the SIG.")

    def list_packages(self):
        """
        Returns a list of packages maintained by the SIG.
        
        Returns:
            list: A list of package names.
        """
        return self.packages

    def __str__(self):
        """
        Returns a string representation of the SIG.
        
        Returns:
            str: A description of the SIG including its name and packages.
        """
        return f"SIG Name: {self.name}\nDescription: {self.description}\nPackages: {', '.join(self.packages) if self.packages else 'None'}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a new SIG for a web server
        web_server_sig = SpecialInterestGroup("Web Server SIG", "Focuses on web server technologies and packages.")
        
        # Add packages to the SIG
        web_server_sig.add_package("httpd")
        web_server_sig.add_package("nginx")
        
        # List packages in the SIG
        print(web_server_sig)
        
        # Remove a package
        web_server_sig.remove_package("nginx")
        
        # List packages after removal
        print(web_server_sig)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
