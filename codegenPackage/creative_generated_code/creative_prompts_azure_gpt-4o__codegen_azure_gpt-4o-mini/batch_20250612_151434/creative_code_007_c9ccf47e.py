"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tromba-sa.com.ar
Prompt: Generate code for designing a turnkey fire protection system, referencing the E-PCI Sistemas contra Incendio Llave en Mano solution from the TROMBA website.
Generated: DETERMINISTIC_c9ccf47ed6ae7ab2
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FireProtectionSystem:
    """
    Class representing a turnkey fire protection system.

    Attributes:
        system_type (str): Type of fire protection system.
        location (str): Location of the installation.
        capacity (float): Capacity of the system in gallons per minute.
        installation_date (str): Date of installation in YYYY-MM-DD format.
    """

    def __init__(self, system_type, location, capacity):
        """
        Initializes a FireProtectionSystem instance.

        Args:
            system_type (str): Type of fire protection system.
            location (str): Location of the installation.
            capacity (float): Capacity of the system in gallons per minute.

        Raises:
            ValueError: If capacity is less than or equal to zero.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        
        self.system_type = system_type
        self.location = location
        self.capacity = capacity
        self.installation_date = None

    def install_system(self, installation_date):
        """
        Marks the system as installed.

        Args:
            installation_date (str): Date of installation in YYYY-MM-DD format.

        Raises:
            ValueError: If installation_date is not in the correct format.
        """
        if not self._is_valid_date(installation_date):
            raise ValueError("Installation date must be in YYYY-MM-DD format.")
        
        self.installation_date = installation_date
        print(f"Fire protection system installed on {self.installation_date}.")

    @staticmethod
    def _is_valid_date(date_string):
        """
        Validates if the given date string is in YYYY-MM-DD format.

        Args:
            date_string (str): Date string to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        import re
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        return bool(re.match(pattern, date_string))

    def get_system_info(self):
        """
        Retrieves information about the fire protection system.

        Returns:
            dict: Information about the system.
        """
        return {
            "System Type": self.system_type,
            "Location": self.location,
            "Capacity (GPM)": self.capacity,
            "Installation Date": self.installation_date or "Not installed yet"
        }

    def perform_maintenance(self):
        """
        Performs maintenance on the fire protection system.
        This method can include tasks such as inspections or system tests.

        Raises:
            RuntimeError: If the system has not been installed yet.
        """
        if self.installation_date is None:
            raise RuntimeError("Maintenance cannot be performed. System is not installed.")
        
        print("Performing maintenance on the fire protection system...")
        # Simulate maintenance logic here
        print("Maintenance completed successfully.")

# Example usage of the FireProtectionSystem class
if __name__ == "__main__":
    try:
        fire_system = FireProtectionSystem("Sprinkler System", "Warehouse A", 500.0)
        fire_system.install_system("2023-10-15")
        print(fire_system.get_system_info())
        fire_system.perform_maintenance()
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
