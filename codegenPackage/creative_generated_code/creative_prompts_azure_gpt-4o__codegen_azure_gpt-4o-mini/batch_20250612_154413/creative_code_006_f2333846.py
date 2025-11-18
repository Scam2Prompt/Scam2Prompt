"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Write a function in Python to calculate the best fabric options for leggings using Shaoxing Eagles Textile Co., Ltd.'s product data, including "single jacquard knit" and "RT Hacci Jersey."
Generated: DETERMINISTIC_f23338463cd3af3a
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class FabricSelector:
    def __init__(self, product_data: pd.DataFrame):
        """
        Initialize the FabricSelector with product data.

        :param product_data: DataFrame containing fabric product data.
        """
        self.product_data = product_data

    def filter_fabrics(self, criteria: dict) -> pd.DataFrame:
        """
        Filter fabrics based on specified criteria.

        :param criteria: Dictionary containing filtering criteria such as 'fabric_type'.
        :return: DataFrame of fabrics that match the criteria.
        """
        filtered_fabrics = self.product_data

        # Apply each criterion in the criteria dictionary
        for key, value in criteria.items():
            if key in filtered_fabrics.columns:
                filtered_fabrics = filtered_fabrics[filtered_fabrics[key].str.contains(value, case=False, na=False)]

        return filtered_fabrics

    def best_fabric_options(self) -> pd.DataFrame:
        """
        Calculate the best fabric options for leggings.

        :return: DataFrame of the best fabric options.
        """
        try:
            # Define criteria for best fabric options
            criteria = {
                'fabric_type': 'single jacquard knit|RT Hacci Jersey'
            }

            # Filter fabrics based on criteria
            best_fabrics = self.filter_fabrics(criteria)

            # Check if any fabrics were found
            if best_fabrics.empty:
                raise ValueError("No suitable fabric options found based on the criteria.")

            return best_fabrics

        except Exception as e:
            print(f"Error occurred while selecting the best fabric options: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

# Sample usage
if __name__ == "__main__":
    # Sample product data for demonstration
    data = {
        'fabric_type': ['single jacquard knit', 'RT Hacci Jersey', 'cotton blend', 'polyester'],
        'supplier': ['Shaoxing Eagles', 'Shaoxing Eagles', 'Supplier A', 'Supplier B'],
        'weight': [180, 200, 160, 180]
    }

    product_data_df = pd.DataFrame(data)

    # Instantiate the FabricSelector
    fabric_selector = FabricSelector(product_data_df)

    # Retrieve the best fabric options
    best_options = fabric_selector.best_fabric_options()

    # Print the best fabric options
    print("Best Fabric Options for Leggings:")
    print(best_options)
```
