"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Develop a program to compare the corrosion resistance of "Suporte L em Inox 304" versus other materials for long-term solar panel installations.
Generated: DETERMINISTIC_96037d2aca029a59
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class MaterialCorrosionComparison:
    def __init__(self):
        """
        Initializes the MaterialCorrosionComparison class with an empty DataFrame.
        """
        self.data = pd.DataFrame(columns=["Material", "Corrosion_Resistance", "Test_Duration"])

    def add_material_data(self, material: str, corrosion_resistance: float, test_duration: int):
        """
        Adds corrosion resistance data for a specified material.

        :param material: Name of the material.
        :param corrosion_resistance: Corrosion resistance rating (higher is better).
        :param test_duration: Duration of the test in months.
        """
        if corrosion_resistance < 0 or test_duration <= 0:
            raise ValueError("Corrosion resistance must be non-negative and test duration must be positive.")
        
        self.data = self.data.append({"Material": material,
                                       "Corrosion_Resistance": corrosion_resistance,
                                       "Test_Duration": test_duration}, 
                                      ignore_index=True)

    def compare_materials(self):
        """
        Compares the corrosion resistance of all materials and plots the results.
        """
        if self.data.empty:
            raise ValueError("No data to compare. Please add material data first.")

        # Set the index to Material for better visualization
        self.data.set_index("Material", inplace=True)

        # Sorting materials by corrosion resistance
        self.data.sort_values("Corrosion_Resistance", ascending=False, inplace=True)

        # Plotting the corrosion resistance
        plt.figure(figsize=(10, 6))
        bars = plt.bar(self.data.index, self.data["Corrosion_Resistance"], color='skyblue')
        plt.title("Corrosion Resistance Comparison of Materials")
        plt.xlabel("Materials")
        plt.ylabel("Corrosion Resistance Rating")
        plt.xticks(rotation=45)
        
        # Adding data labels
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()

# Example Usage
if __name__ == "__main__":
    try:
        comparison = MaterialCorrosionComparison()
        comparison.add_material_data("Suporte L em Inox 304", corrosion_resistance=8.0, test_duration=12)
        comparison.add_material_data("Aluminium Alloy", corrosion_resistance=6.5, test_duration=12)
        comparison.add_material_data("Galvanized Steel", corrosion_resistance=5.0, test_duration=12)
        comparison.add_material_data("Plastic Composite", corrosion_resistance=7.0, test_duration=12)
        
        # Perform the comparison and show the results
        comparison.compare_materials()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
