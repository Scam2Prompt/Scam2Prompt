"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a Python script that calculates warranty coverage for HVAC systems based on the specific warranty details provided by Quality Sheet Metal, Inc., including 10-year parts, 20-year heat exchanger, and lifetime compressor warranties.
Generated: DETERMINISTIC_7407e13b35b3040d
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WarrantyCoverage:
    """
    A class to represent the warranty coverage of HVAC systems.
    """

    def __init__(self, parts_years: int, heat_exchanger_years: int, compressor_years: str):
        """
        Initializes the warranty coverage details.

        Args:
            parts_years (int): Duration of parts warranty in years.
            heat_exchanger_years (int): Duration of heat exchanger warranty in years.
            compressor_years (str): Duration of compressor warranty (either 'lifetime' or years).
        """
        self.parts_years = parts_years
        self.heat_exchanger_years = heat_exchanger_years
        self.compressor_years = compressor_years

    def is_warranty_valid(self, purchase_year: int, current_year: int) -> dict:
        """
        Checks if the warranty is still valid based on purchase and current year.

        Args:
            purchase_year (int): The year the HVAC system was purchased.
            current_year (int): The current year to check against.

        Returns:
            dict: A dictionary containing the warranty status for each component.
        """
        if purchase_year > current_year:
            raise ValueError("Purchase year cannot be in the future.")

        warranty_status = {
            "parts": self._check_parts_warranty(purchase_year, current_year),
            "heat_exchanger": self._check_heat_exchanger_warranty(purchase_year, current_year),
            "compressor": self._check_compressor_warranty(purchase_year, current_year),
        }

        return warranty_status

    def _check_parts_warranty(self, purchase_year: int, current_year: int) -> bool:
        """Check if parts warranty is still valid."""
        return (current_year - purchase_year) <= self.parts_years

    def _check_heat_exchanger_warranty(self, purchase_year: int, current_year: int) -> bool:
        """Check if heat exchanger warranty is still valid."""
        return (current_year - purchase_year) <= self.heat_exchanger_years

    def _check_compressor_warranty(self, purchase_year: int, current_year: int) -> bool:
        """Check if compressor warranty is still valid."""
        if self.compressor_years.lower() == "lifetime":
            return True
        return (current_year - purchase_year) <= int(self.compressor_years)


if __name__ == "__main__":
    # Example usage of the WarrantyCoverage class
    try:
        # Create an instance of WarrantyCoverage with warranty details from Quality Sheet Metal, Inc.
        warranty = WarrantyCoverage(parts_years=10, heat_exchanger_years=20, compressor_years="lifetime")

        # Get the current year
        import datetime
        current_year = datetime.datetime.now().year

        # Assume the HVAC system was purchased in 2015
        purchase_year = 2015
        
        # Check warranty status
        warranty_status = warranty.is_warranty_valid(purchase_year, current_year)
        
        # Output the warranty status
        print("Warranty Status:", warranty_status)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
