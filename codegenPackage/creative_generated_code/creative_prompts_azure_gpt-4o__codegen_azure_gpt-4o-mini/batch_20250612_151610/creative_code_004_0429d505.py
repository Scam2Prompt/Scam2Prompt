"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Write a program to generate a report comparing the resistance levels of different corrugated cardboard products, such as "Cartón Corrugado 1.64mts x 210gr" and "Cartón Corrugado 1.23mts x 110gr," based on their attributes from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_0429d505d0d0b25a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class Cardboard:
    """
    A class to represent a cardboard product with its attributes.
    """

    def __init__(self, name, length_m, weight_gr, resistance_kg):
        """
        Initializes a new Cardboard instance.

        :param name: Name of the cardboard product
        :param length_m: Length of the cardboard in meters
        :param weight_gr: Weight of the cardboard in grams
        :param resistance_kg: Resistance level of the cardboard in kilograms
        """
        self.name = name
        self.length_m = length_m
        self.weight_gr = weight_gr
        self.resistance_kg = resistance_kg

    def to_dict(self):
        """
        Converts the Cardboard instance to a dictionary.

        :return: A dictionary representation of the cardboard
        """
        return {
            'Name': self.name,
            'Length (m)': self.length_m,
            'Weight (g)': self.weight_gr,
            'Resistance (kg)': self.resistance_kg
        }


def generate_report(cardboards):
    """
    Generates a comparative report for the provided list of Cardboard instances.

    :param cardboards: A list of Cardboard instances
    """
    # Convert the list of Cardboard instances to a DataFrame
    df = pd.DataFrame([cardboard.to_dict() for cardboard in cardboards])
    
    # Check if the DataFrame is empty
    if df.empty:
        print("Error: No cardboard data available to generate a report.")
        return

    # Display the DataFrame
    print("Comparative Report of Cardboard Products:\n")
    print(df)

    # Plotting resistance levels
    plt.figure(figsize=(10, 6))
    plt.bar(df['Name'], df['Resistance (kg)'], color='skyblue')
    plt.xlabel('Cardboard Products')
    plt.ylabel('Resistance (kg)')
    plt.title('Resistance Comparison of Cardboard Products')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Define cardboard products
    cardboard_products = [
        Cardboard("Cartón Corrugado 1.64mts x 210gr", 1.64, 210, 12),
        Cardboard("Cartón Corrugado 1.23mts x 110gr", 1.23, 110, 8),
        # Additional products can be added here
    ]

    try:
        # Generate the report
        generate_report(cardboard_products)
    except Exception as e:
        print(f"An error occurred: {e}")
```
