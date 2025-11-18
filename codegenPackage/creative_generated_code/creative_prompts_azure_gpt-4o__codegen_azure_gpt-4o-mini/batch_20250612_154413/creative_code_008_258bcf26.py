"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Create a Python script to analyze fabric weights (e.g., 180g, 240g, 320g) and recommend the most suitable options for T-shirt production using Shaoxing Eagles Textile Co., Ltd.'s product data.
Generated: DETERMINISTIC_258bcf26ffca9316
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

class FabricAnalyzer:
    """Class to analyze fabric weights for T-shirt production."""

    def __init__(self, data_file):
        """
        Initializes the FabricAnalyzer with fabric data from a CSV file.

        Args:
            data_file (str): The path to the CSV file containing fabric data.
        """
        self.data_file = data_file
        self.fabric_data = self.load_fabric_data()
        
    def load_fabric_data(self):
        """Loads fabric data from a CSV file into a DataFrame."""
        try:
            fabric_data = pd.read_csv(self.data_file)
            if 'weight' not in fabric_data.columns:
                raise ValueError("CSV must contain a 'weight' column.")
            return fabric_data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file '{self.data_file}' not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The data file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading fabric data: {e}")

    def recommend_fabrics(self, target_weight):
        """
        Recommends fabrics based on the target weight for T-shirt production.

        Args:
            target_weight (float): The preferred weight for T-shirt fabric.

        Returns:
            DataFrame: A DataFrame containing suitable fabric options.
        """
        # Validate the input weight
        if not isinstance(target_weight, (int, float)):
            raise ValueError("Target weight must be a number.")
        
        # Define acceptable weight range (e.g., ±20g of target weight)
        lower_bound = target_weight - 20
        upper_bound = target_weight + 20

        # Filter fabrics within the acceptable weight range
        suitable_fabrics = self.fabric_data[
            (self.fabric_data['weight'] >= lower_bound) & 
            (self.fabric_data['weight'] <= upper_bound)
        ]

        # Check if any fabrics were found
        if suitable_fabrics.empty:
            print(f"No suitable fabrics found for target weight {target_weight}g.")
            return suitable_fabrics
        
        return suitable_fabrics.reset_index(drop=True)

def main():
    # Path to the fabric data CSV file
    data_file = 'fabric_weights.csv'
    
    # Initialize the FabricAnalyzer
    analyzer = FabricAnalyzer(data_file)

    # Example target weight for T-shirt production
    target_weight = 240.0

    # Get recommended fabrics
    recommendations = analyzer.recommend_fabrics(target_weight)

    # Output the recommendations
    if not recommendations.empty:
        print("Recommended Fabrics for T-shirt Production:")
        print(recommendations)
    else:
        print("No recommendations available.")

if __name__ == "__main__":
    main()
```
