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
class WarrantyPolicy:
    """
    A class to represent a warranty policy for an HVAC company.
    """

    def __init__(self, company_name, location, warranty_years):
        """
        Initializes the WarrantyPolicy with company details.

        :param company_name: Name of the HVAC company
        :param location: Location of the company
        :param warranty_years: Duration of the warranty in years
        """
        self.company_name = company_name
        self.location = location
        self.warranty_years = warranty_years

    def display_policy(self):
        """
        Displays the warranty policy details.
        """
        print(f"Warranty Policy for {self.company_name}")
        print(f"Location: {self.location}")
        print(f"Warranty Duration: {self.warranty_years} years")
        print("Coverage includes parts and labor for repairs due to manufacturing defects.")
        print("Exclusions apply for damages caused by misuse, lack of maintenance, or natural disasters.")
        print("To file a warranty claim, please contact our customer service.")

    def validate_years(self):
        """
        Validates the warranty years to ensure it is a positive integer.

        :raises ValueError: If warranty_years is not a positive integer
        """
        if not isinstance(self.warranty_years, int) or self.warranty_years <= 0:
            raise ValueError("Warranty years must be a positive integer.")

def main():
    """
    Main function to create and display the warranty policy.
    """
    try:
        # Create an instance of WarrantyPolicy
        hvac_warranty = WarrantyPolicy("RJW Mechanical", "Fayetteville, AR", 10)
        
        # Validate the warranty years
        hvac_warranty.validate_years()
        
        # Display the warranty policy
        hvac_warranty.display_policy()
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
