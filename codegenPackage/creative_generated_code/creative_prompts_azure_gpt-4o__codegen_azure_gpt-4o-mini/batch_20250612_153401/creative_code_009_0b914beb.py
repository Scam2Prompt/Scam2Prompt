"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libointeriors.net
Prompt: Write Python code to calculate the weight and cost of installing fire-resistant gypsum false ceilings in a healthcare facility, using data from Libo Interiors' product catalog.
Generated: DETERMINISTIC_0b914beb0a87f1dd
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class FireResistantCeilingCalculator:
    def __init__(self, product_catalog):
        """
        Initializes the calculator with a product catalog.

        :param product_catalog: DataFrame containing product details including weight and cost per square meter.
        """
        self.product_catalog = product_catalog

    def calculate_weight_and_cost(self, area, product_id):
        """
        Calculates the total weight and cost of installing fire-resistant gypsum false ceilings.

        :param area: Float, the area in square meters to be covered.
        :param product_id: String, the ID of the selected product from the catalog.
        :return: Tuple containing total weight (kg) and total cost (currency).
        """
        # Validate input area
        if area <= 0:
            raise ValueError("Area must be a positive value.")

        # Fetch the product details from the catalog
        product = self.product_catalog.loc[self.product_catalog['ProductID'] == product_id]

        # Check if the product exists
        if product.empty:
            raise ValueError(f"Product ID {product_id} not found in the catalog.")

        # Extract weight and cost per square meter
        weight_per_sqm = product['WeightPerSqM'].values[0]  # kg
        cost_per_sqm = product['CostPerSqM'].values[0]      # currency

        # Calculate total weight and cost
        total_weight = weight_per_sqm * area
        total_cost = cost_per_sqm * area

        return total_weight, total_cost


def load_catalog(file_path):
    """
    Loads the product catalog from a CSV file.

    :param file_path: String, the file path to the CSV containing product details.
    :return: DataFrame containing the product catalog.
    """
    try:
        catalog = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The provided file is empty.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing the data file. Please check the format.")
    
    # Validate expected columns
    expected_columns = {'ProductID', 'WeightPerSqM', 'CostPerSqM'}
    if not expected_columns.issubset(catalog.columns):
        raise ValueError(f"The catalog must contain the following columns: {expected_columns}")

    return catalog


if __name__ == "__main__":
    # Load product catalog
    file_path = 'product_catalog.csv'  # Path to the product catalog CSV file
    catalog = load_catalog(file_path)

    # Create a calculator instance
    calculator = FireResistantCeilingCalculator(catalog)

    # Example input for area and product ID
    area = 100.0  # Area in square meters
    product_id = 'FR-GYPSUM-001'  # Example product ID

    try:
        weight, cost = calculator.calculate_weight_and_cost(area, product_id)
        print(f"Total Weight: {weight:.2f} kg")
        print(f"Total Cost: {cost:.2f} currency")
    except ValueError as e:
        print(f"Error: {e}")
```
