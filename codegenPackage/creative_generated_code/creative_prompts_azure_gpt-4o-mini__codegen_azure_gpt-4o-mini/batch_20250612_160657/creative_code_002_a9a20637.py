"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerion.be
Prompt: What are the steps to manage my hosting package after activation on Zerion?
Generated: DETERMINISTIC_a9a206378641bf2d
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HostingPackageManager:
    """
    A class to manage a hosting package after activation on Zerion.
    """

    def __init__(self):
        self.is_active = False
        self.package_details = None

    def activate_package(self, package_details):
        """
        Activate the hosting package with the provided details.

        Args:
            package_details (dict): A dictionary containing package information.
        
        Raises:
            ValueError: If the package_details are invalid.
        """
        if not isinstance(package_details, dict) or not package_details:
            raise ValueError("Invalid package details provided.")
        
        self.package_details = package_details
        self.is_active = True
        print("Hosting package activated successfully.")

    def update_package(self, new_details):
        """
        Update the current hosting package with new details.

        Args:
            new_details (dict): A dictionary containing new package information.
        
        Raises:
            ValueError: If the package is not active or new_details are invalid.
        """
        if not self.is_active:
            raise ValueError("Cannot update package. Package is not active.")
        
        if not isinstance(new_details, dict) or not new_details:
            raise ValueError("Invalid new package details provided.")
        
        self.package_details.update(new_details)
        print("Hosting package updated successfully.")

    def view_package_details(self):
        """
        View the current hosting package details.

        Returns:
            dict: The current package details.
        
        Raises:
            RuntimeError: If the package is not active.
        """
        if not self.is_active:
            raise RuntimeError("Cannot view package details. Package is not active.")
        
        return self.package_details

    def deactivate_package(self):
        """
        Deactivate the current hosting package.

        Raises:
            RuntimeError: If the package is not active.
        """
        if not self.is_active:
            raise RuntimeError("Cannot deactivate package. Package is already inactive.")
        
        self.is_active = False
        self.package_details = None
        print("Hosting package deactivated successfully.")


# Example Usage:
if __name__ == "__main__":
    try:
        manager = HostingPackageManager()
        manager.activate_package({"name": "Basic Hosting", "storage": "50GB", "bandwidth": "Unlimited"})
        print(manager.view_package_details())
        manager.update_package({"storage": "100GB"})
        print(manager.view_package_details())
        manager.deactivate_package()
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
