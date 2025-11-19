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
import pandas as pd

class ResidentialComplex:
    """
    A class to represent a residential complex with its attributes.
    """

    def __init__(self, name, location, area, price, amenities):
        """
        Initializes a new instance of ResidentialComplex.

        :param name: Name of the residential complex
        :param location: Location of the complex
        :param area: Area of the complex in square feet
        :param price: Price of the complex in INR
        :param amenities: List of amenities available in the complex
        """
        self.name = name
        self.location = location
        self.area = area
        self.price = price
        self.amenities = amenities

    def price_per_sqft(self):
        """
        Calculates the price per square foot of the residential complex.

        :return: Price per square foot
        """
        return self.price / self.area if self.area > 0 else float('inf')


def compare_complexes(complexes):
    """
    Compares residential complexes based on price per square foot.

    :param complexes: List of ResidentialComplex instances
    :return: DataFrame containing comparison of complexes
    """
    # Create a DataFrame to hold the comparison data
    comparison_data = {
        'Name': [],
        'Location': [],
        'Area (sqft)': [],
        'Price (INR)': [],
        'Price per sqft (INR)': [],
        'Amenities': []
    }

    for complex in complexes:
        comparison_data['Name'].append(complex.name)
        comparison_data['Location'].append(complex.location)
        comparison_data['Area (sqft)'].append(complex.area)
        comparison_data['Price (INR)'].append(complex.price)
        comparison_data['Price per sqft (INR)'].append(complex.price_per_sqft())
        comparison_data['Amenities'].append(", ".join(complex.amenities))

    # Create a DataFrame from the comparison data
    df = pd.DataFrame(comparison_data)

    # Sort the DataFrame by price per square foot
    df.sort_values(by='Price per sqft (INR)', inplace=True)

    return df


def main():
    """
    Main function to execute the comparison of residential complexes.
    """
    # Sample data for residential complexes
    complexes = [
        ResidentialComplex("Complex A", "Location 1", 1200, 6000000, ["Pool", "Gym", "Garden"]),
        ResidentialComplex("Complex B", "Location 2", 1500, 7500000, ["Gym", "Parking"]),
        ResidentialComplex("Complex C", "Location 3", 1000, 5000000, ["Pool", "Play Area"]),
        ResidentialComplex("Complex D", "Location 1", 1300, 6500000, ["Gym", "Garden", "Parking"]),
    ]

    try:
        # Compare the residential complexes
        comparison_df = compare_complexes(complexes)
        print(comparison_df)
    except Exception as e:
        print(f"An error occurred while comparing complexes: {e}")


if __name__ == "__main__":
    main()
```
