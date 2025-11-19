"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Create a sample warranty policy for an HVAC company based in Fayetteville, AR, inspired by RJW Mechanical's 10-year warranty offer.
Generated: DETERMINISTIC_9ffc71b23ac43910
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class WarrantyPolicy:
    """
    A class representing a warranty policy for an HVAC company.

    Attributes:
    company_name (str): The name of the HVAC company.
    location (str): The location of the HVAC company.
    warranty_duration (int): The duration of the warranty in years.
    """

    def __init__(self, company_name, location, warranty_duration):
        """
        Initializes a WarrantyPolicy object.

        Args:
        company_name (str): The name of the HVAC company.
        location (str): The location of the HVAC company.
        warranty_duration (int): The duration of the warranty in years.
        """
        self.company_name = company_name
        self.location = location
        self.warranty_duration = warranty_duration

    def get_warranty_details(self):
        """
        Returns a string containing the warranty details.

        Returns:
        str: A string containing the warranty details.
        """
        return f"{self.company_name} in {self.location} offers a {self.warranty_duration}-year warranty."

    def calculate_warranty_expiration(self, installation_date):
        """
        Calculates the warranty expiration date.

        Args:
        installation_date (datetime): The date of installation.

        Returns:
        datetime: The warranty expiration date.
        """
        try:
            if not isinstance(installation_date, datetime):
                raise TypeError("Installation date must be a datetime object.")
            warranty_expiration = installation_date + timedelta(days=self.warranty_duration * 365)
            return warranty_expiration
        except Exception as e:
            print(f"An error occurred: {e}")

    def print_warranty_policy(self, installation_date):
        """
        Prints the warranty policy details.

        Args:
        installation_date (datetime): The date of installation.
        """
        warranty_details = self.get_warranty_details()
        warranty_expiration = self.calculate_warranty_expiration(installation_date)

        if warranty_expiration:
            print("Warranty Policy:")
            print(warranty_details)
            print(f"Warranty Expiration Date: {warranty_expiration.strftime('%Y-%m-%d')}")
        else:
            print("Failed to calculate warranty expiration date.")


def main():
    company_name = "RJW Mechanical"
    location = "Fayetteville, AR"
    warranty_duration = 10

    warranty_policy = WarrantyPolicy(company_name, location, warranty_duration)

    installation_date = datetime.now()
    print(f"Installation Date: {installation_date.strftime('%Y-%m-%d')}")
    warranty_policy.print_warranty_policy(installation_date)


if __name__ == "__main__":
    main()
```
