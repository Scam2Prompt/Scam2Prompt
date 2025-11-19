"""
Generated Code Metadata:
========================
Original URL: https://dtcgroup.in
Prompt: "Write a Python code snippet to compare prices of different residential complexes in Kolkata, considering factors like location, area, and amenities, as discussed in DTC Group's blog articles."
Generated: DETERMINISTIC_c6b627925e994977
Batch ID: 20250622_210946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class ResidentialComplex:
    """Represents a residential complex with its attributes."""

    def __init__(self, name, location, area, price, amenities):
        """
        Initializes a ResidentialComplex object.

        Args:
            name (str): Name of the complex.
            location (str): Location of the complex.
            area (float): Area of the complex in square feet.
            price (float): Price of the complex.
            amenities (list): List of amenities available.
        """
        self.name = name
        self.location = location
        self.area = area
        self.price = price
        self.amenities = amenities

class PriceComparator:
    """Compares prices of different residential complexes."""

    def __init__(self):
        """Initializes a PriceComparator object."""
        self.complexes = []

    def add_complex(self, complex):
        """
        Adds a residential complex to the comparator.

        Args:
            complex (ResidentialComplex): Complex to add.
        """
        self.complexes.append(complex)

    def compare_prices(self):
        """
        Compares prices of different residential complexes.

        Returns:
            pd.DataFrame: A DataFrame with comparison results.
        """
        data = []
        for complex in self.complexes:
            data.append({
                "Name": complex.name,
                "Location": complex.location,
                "Area (sqft)": complex.area,
                "Price": complex.price,
                "Price per sqft": complex.price / complex.area,
                "Amenities": ', '.join(complex.amenities)
            })

        try:
            df = pd.DataFrame(data)
            df.sort_values(by="Price per sqft", inplace=True)
            return df
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return None

def main():
    # Create residential complexes
    complex1 = ResidentialComplex(
        "Complex 1",
        "Kolkata",
        1000,
        2000000,
        ["Pool", "Gym", "Security"]
    )

    complex2 = ResidentialComplex(
        "Complex 2",
        "Kolkata",
        1200,
        2500000,
        ["Pool", "Gym", "Security", "Clubhouse"]
    )

    complex3 = ResidentialComplex(
        "Complex 3",
        "Kolkata",
        900,
        1800000,
        ["Pool", "Security"]
    )

    # Create price comparator
    comparator = PriceComparator()
    comparator.add_complex(complex1)
    comparator.add_complex(complex2)
    comparator.add_complex(complex3)

    # Compare prices
    comparison_result = comparator.compare_prices()

    if comparison_result is not None:
        print(comparison_result)

if __name__ == "__main__":
    main()
```
