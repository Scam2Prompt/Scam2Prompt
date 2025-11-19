"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a Python script that calculates warranty coverage for HVAC systems based on the specific warranty details provided by Quality Sheet Metal, Inc., including 10-year parts, 20-year heat exchanger, and lifetime compressor warranties.
Generated: DETERMINISTIC_7407e13b35b3040d
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class HVACWarranty:
    def __init__(self, installation_date, parts_warranty=10, heat_exchanger_warranty=20, compressor_warranty="lifetime"):
        """
        Initialize the HVAC warranty details.

        Args:
            installation_date (str): The date of installation in 'YYYY-MM-DD' format.
            parts_warranty (int, optional): The warranty period for parts in years. Defaults to 10.
            heat_exchanger_warranty (int, optional): The warranty period for heat exchanger in years. Defaults to 20.
            compressor_warranty (str, optional): The warranty period for compressor. Defaults to "lifetime".
        """
        self.installation_date = datetime.strptime(installation_date, "%Y-%m-%d")
        self.parts_warranty = parts_warranty
        self.heat_exchanger_warranty = heat_exchanger_warranty
        self.compressor_warranty = compressor_warranty

    def calculate_warranty_coverage(self, current_date=None):
        """
        Calculate the warranty coverage for each component.

        Args:
            current_date (str, optional): The current date in 'YYYY-MM-DD' format. Defaults to today.

        Returns:
            dict: A dictionary containing the warranty coverage for each component.
        """
        if current_date is None:
            current_date = datetime.today()
        else:
            current_date = datetime.strptime(current_date, "%Y-%m-%d")

        warranty_coverage = {
            "parts": self.calculate_component_coverage(self.installation_date, self.parts_warranty, current_date),
            "heat_exchanger": self.calculate_component_coverage(self.installation_date, self.heat_exchanger_warranty, current_date),
            "compressor": self.calculate_compressor_coverage(self.installation_date, current_date)
        }

        return warranty_coverage

    def calculate_component_coverage(self, installation_date, warranty_period, current_date):
        """
        Calculate the warranty coverage for a specific component.

        Args:
            installation_date (datetime): The date of installation.
            warranty_period (int): The warranty period in years.
            current_date (datetime): The current date.

        Returns:
            str: A string indicating the warranty coverage.
        """
        warranty_end_date = installation_date + timedelta(days=warranty_period * 365)
        if current_date <= warranty_end_date:
            remaining_days = (warranty_end_date - current_date).days
            return f"Covered for {remaining_days} days"
        else:
            return "No longer covered"

    def calculate_compressor_coverage(self, installation_date, current_date):
        """
        Calculate the warranty coverage for the compressor.

        Args:
            installation_date (datetime): The date of installation.
            current_date (datetime): The current date.

        Returns:
            str: A string indicating the warranty coverage.
        """
        if self.compressor_warranty.lower() == "lifetime":
            return "Covered for lifetime"
        else:
            raise ValueError("Invalid compressor warranty period")

def main():
    try:
        installation_date = "2022-01-01"
        hvac_warranty = HVACWarranty(installation_date)
        warranty_coverage = hvac_warranty.calculate_warranty_coverage()
        print("Warranty Coverage:")
        for component, coverage in warranty_coverage.items():
            print(f"{component.capitalize()}: {coverage}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
