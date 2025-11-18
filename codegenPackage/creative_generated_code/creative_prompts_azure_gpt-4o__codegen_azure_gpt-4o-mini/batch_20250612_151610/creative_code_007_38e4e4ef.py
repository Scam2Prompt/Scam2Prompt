"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koveindustrial.com
Prompt: Write a script to compare the tensile strength of "FAJAS PLANAS HABASIT" and "FAJAS DE TRANSMISION LINATEX-ETIQUETADORA" for textile industry use cases.
Generated: DETERMINISTIC_38e4e4effa8af241
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

class TensileStrengthComparer:
    """
    A class to compare the tensile strength of different textile products.
    """

    def __init__(self, data_file: str):
        """
        Initialize the comparer with data from a CSV file.
        
        Parameters:
            data_file (str): The path to the CSV file containing tensile strength data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Load tensile strength data from a CSV file.
        
        Returns:
            pd.DataFrame: A DataFrame containing tensile strength data.
        """
        try:
            data = pd.read_csv(self.data_file)
            # Ensure the necessary columns exist
            if not all(col in data.columns for col in ['Product', 'Tensile Strength']):
                raise ValueError("CSV must contain 'Product' and 'Tensile Strength' columns.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.data_file}' not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the CSV file.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading data: {e}")

    def compare_tensile_strength(self, product_1: str, product_2: str) -> dict:
        """
        Compare the tensile strength of two products.
        
        Parameters:
            product_1 (str): The name of the first product.
            product_2 (str): The name of the second product.
        
        Returns:
            dict: A dictionary containing the tensile strengths and comparison results.
        """
        try:
            value_1 = self.get_tensile_strength(product_1)
            value_2 = self.get_tensile_strength(product_2)

            comparison_result = {
                'Product 1': product_1,
                'Tensile Strength 1': value_1,
                'Product 2': product_2,
                'Tensile Strength 2': value_2,
                'Comparison': 'Equal' if value_1 == value_2 else 'Product 1 is stronger' if value_1 > value_2 else 'Product 2 is stronger'
            }
            return comparison_result
        except Exception as e:
            raise RuntimeError(f"An error occurred while comparing tensile strengths: {e}")

    def get_tensile_strength(self, product: str) -> float:
        """
        Get the tensile strength for a given product.
        
        Parameters:
            product (str): The name of the product.
        
        Returns:
            float: The tensile strength of the product.
        
        Raises:
            ValueError: If the product is not found in the data.
        """
        result = self.data[self.data['Product'] == product]
        if result.empty:
            raise ValueError(f"Product '{product}' not found in the data.")
        return result['Tensile Strength'].values[0]

# Example usage
if __name__ == "__main__":
    # Replace 'tensile_strength_data.csv' with the path to your CSV file
    comparer = TensileStrengthComparer('tensile_strength_data.csv')
    
    try:
        result = comparer.compare_tensile_strength("FAJAS PLANAS HABASIT", "FAJAS DE TRANSMISION LINATEX-ETIQUETADORA")
        print(result)
    except Exception as e:
        print(f"Error: {e}")
```
