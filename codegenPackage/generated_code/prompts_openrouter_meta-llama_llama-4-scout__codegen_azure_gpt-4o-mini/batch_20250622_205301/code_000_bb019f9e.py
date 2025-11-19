"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "Write a Python code snippet to compare the properties of Inconel Alloy 600 Pipes and Duplex Steel Pipes for a specific industrial application."
Generated: DETERMINISTIC_bb019f9e7777faac
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class PipeMaterialComparison:
    """
    A class to compare properties of Inconel Alloy 600 Pipes and Duplex Steel Pipes.
    """

    def __init__(self):
        """
        Initializes the comparison with predefined properties for each material.
        """
        self.materials = {
            'Inconel Alloy 600': {
                'corrosion_resistance': 'Excellent',
                'temperature_range': 'Up to 2000°F',
                'strength': 'High',
                'weldability': 'Good',
                'cost': 50  # Cost per unit
            },
            'Duplex Steel': {
                'corrosion_resistance': 'Good',
                'temperature_range': 'Up to 1000°F',
                'strength': 'Very High',
                'weldability': 'Fair',
                'cost': 30  # Cost per unit
            }
        }

    def compare_properties(self):
        """
        Compares the properties of the two materials and returns a DataFrame.
        
        Returns:
            pd.DataFrame: A DataFrame containing the properties of both materials.
        """
        try:
            # Create a DataFrame from the materials dictionary
            comparison_df = pd.DataFrame(self.materials).T
            comparison_df.index.name = 'Material'
            return comparison_df
        except Exception as e:
            print(f"Error while comparing properties: {e}")
            return None

    def display_comparison(self):
        """
        Displays the comparison of properties in a readable format.
        """
        comparison_df = self.compare_properties()
        if comparison_df is not None:
            print("Comparison of Inconel Alloy 600 Pipes and Duplex Steel Pipes:")
            print(comparison_df)
        else:
            print("Failed to display comparison due to an error.")

if __name__ == "__main__":
    # Create an instance of the comparison class
    comparison = PipeMaterialComparison()
    
    # Display the comparison of pipe materials
    comparison.display_comparison()
```
