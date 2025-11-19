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
import pandas as pd

# Define a class to represent a Yanmar mini excavator
class YanmarExcavator:
    def __init__(self, model: str, horsepower: float, excavation_depth: float):
        """
        Initialize a Yanmar excavator with model, horsepower, and excavation depth.

        :param model: The model name of the excavator
        :param horsepower: The horsepower of the excavator
        :param excavation_depth: The maximum excavation depth of the excavator in meters
        """
        self.model = model
        self.horsepower = horsepower
        self.excavation_depth = excavation_depth

    def __repr__(self):
        return f"{self.model}: {self.horsepower} HP, {self.excavation_depth} m depth"


def create_excavator_data():
    """
    Create a list of Yanmar mini excavators with their specifications.

    :return: List of YanmarExcavator objects
    """
    return [
        YanmarExcavator("ViO12", 12.0, 2.4),
        YanmarExcavator("ViO17", 17.0, 2.6),
        YanmarExcavator("ViO25", 25.0, 2.8),
        YanmarExcavator("ViO35", 35.0, 3.2),
        YanmarExcavator("SV100", 100.0, 4.0),
    ]


def display_excavator_comparison(excavators):
    """
    Display the comparison of excavators in a tabular format.

    :param excavators: List of YanmarExcavator objects
    """
    # Create a DataFrame from the excavator data
    data = {
        "Model": [excavator.model for excavator in excavators],
        "Horsepower (HP)": [excavator.horsepower for excavator in excavators],
        "Excavation Depth (m)": [excavator.excavation_depth for excavator in excavators],
    }
    
    df = pd.DataFrame(data)

    # Display the DataFrame
    print(df)


def main():
    """
    Main function to execute the excavator comparison script.
    """
    try:
        # Create excavator data
        excavators = create_excavator_data()
        
        # Display the comparison
        display_excavator_comparison(excavators)
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
