"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Generate a script to compare the horsepower and excavation depth of Yanmar mini excavators (e.g., ViO12, ViO17, ViO25, ViO35, SV100) and display the results in a tabular format.
Generated: DETERMINISTIC_ee6e3f89f077454c
Batch ID: 20250612_153224
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
from tabulate import tabulate

# Define a class for Yanmar mini excavators
class YanmarExcavator:
    def __init__(self, model, horsepower, excavation_depth):
        """
        Initialize a Yanmar excavator object.

        Args:
            model (str): Model of the excavator (e.g., ViO12, ViO17, ViO25, ViO35, SV100)
            horsepower (float): Horsepower of the excavator
            excavation_depth (float): Excavation depth of the excavator in meters
        """
        self.model = model
        self.horsepower = horsepower
        self.excavation_depth = excavation_depth

# Define a function to compare excavators
def compare_excavators(excavators):
    """
    Compare the horsepower and excavation depth of Yanmar mini excavators.

    Args:
        excavators (list[YanmarExcavator]): List of Yanmar excavator objects

    Returns:
        pd.DataFrame: DataFrame containing the comparison results
    """
    try:
        # Create a dictionary to store the comparison results
        data = {
            "Model": [excavator.model for excavator in excavators],
            "Horsepower": [excavator.horsepower for excavator in excavators],
            "Excavation Depth (m)": [excavator.excavation_depth for excavator in excavators]
        }

        # Create a DataFrame from the dictionary
        df = pd.DataFrame(data)

        # Return the DataFrame
        return df

    except Exception as e:
        # Handle any exceptions that occur during the comparison
        print(f"An error occurred: {e}")
        return None

# Define a main function
def main():
    try:
        # Create a list of Yanmar excavator objects
        excavators = [
            YanmarExcavator("ViO12", 9.4, 3.6),
            YanmarExcavator("ViO17", 14.2, 4.1),
            YanmarExcavator("ViO25", 22.1, 4.7),
            YanmarExcavator("ViO35", 33.5, 5.3),
            YanmarExcavator("SV100", 74.3, 6.1)
        ]

        # Compare the excavators
        df = compare_excavators(excavators)

        # Display the results in a tabular format
        if df is not None:
            print(tabulate(df, headers="keys", tablefmt="psql"))

    except Exception as e:
        # Handle any exceptions that occur during the main function
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
