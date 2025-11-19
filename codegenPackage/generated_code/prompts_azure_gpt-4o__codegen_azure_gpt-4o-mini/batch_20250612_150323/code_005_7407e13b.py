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
class WarrantyCoverage:
    """
    A class to represent the warranty coverage for HVAC systems.
    """

    def __init__(self, parts_years=10, heat_exchanger_years=20, compressor_years=float('inf')):
        """
        Initializes the warranty coverage with specified years for parts, heat exchanger, and compressor.

        :param parts_years: Number of years for parts warranty (default is 10)
        :param heat_exchanger_years: Number of years for heat exchanger warranty (default is 20)
        :param compressor_years: Number of years for compressor warranty (default is lifetime)
        """
        self.parts_years = parts_years
        self.heat_exchanger_years = heat_exchanger_years
        self.compressor_years = compressor_years

    def is_covered(self, warranty_type, years):
        """
        Checks if the specified warranty type is covered for the given number of years.

        :param warranty_type: Type of warranty ('parts', 'heat_exchanger', 'compressor')
        :param years: Number of years to check coverage for
        :return: True if covered, False otherwise
        """
        try:
            if warranty_type == 'parts':
                return years <= self.parts_years
            elif warranty_type == 'heat_exchanger':
                return years <= self.heat_exchanger_years
            elif warranty_type == 'compressor':
                return years <= self.compressor_years
            else:
                raise ValueError("Invalid warranty type. Choose from 'parts', 'heat_exchanger', or 'compressor'.")
        except Exception as e:
            print(f"Error checking warranty coverage: {e}")
            return False

    def warranty_details(self):
        """
        Returns a summary of the warranty coverage details.

        :return: A string summarizing the warranty coverage
        """
        return (f"Warranty Coverage:\n"
                f" - Parts: {self.parts_years} years\n"
                f" - Heat Exchanger: {self.heat_exchanger_years} years\n"
                f" - Compressor: {'Lifetime' if self.compressor_years == float('inf') else self.compressor_years} years\n")


def main():
    """
    Main function to demonstrate the warranty coverage calculation.
    """
    # Create an instance of WarrantyCoverage
    hvac_warranty = WarrantyCoverage()

    # Display warranty details
    print(hvac_warranty.warranty_details())

    # Check coverage for different warranty types
    warranty_checks = {
        'parts': 5,
        'heat_exchanger': 15,
        'compressor': 25
    }

    for warranty_type, years in warranty_checks.items():
        covered = hvac_warranty.is_covered(warranty_type, years)
        print(f"{warranty_type.capitalize()} warranty for {years} years: {'Covered' if covered else 'Not Covered'}")


if __name__ == "__main__":
    main()
```
