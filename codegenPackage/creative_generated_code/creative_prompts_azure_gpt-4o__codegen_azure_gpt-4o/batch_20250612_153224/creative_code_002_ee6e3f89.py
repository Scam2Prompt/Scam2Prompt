"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Generate a script to compare the horsepower and excavation depth of Yanmar mini excavators (e.g., ViO12, ViO17, ViO25, ViO35, SV100) and display the results in a tabular format.
Generated: DETERMINISTIC_ee6e3f89f077454c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Define a class for Mini Excavator
class MiniExcavator:
    def __init__(self, model, horsepower, excavation_depth):
        """
        Initialize a Mini Excavator object.

        :param model: Excavator model name (e.g., ViO12, ViO17)
        :param horsepower: Excavator horsepower
        :param excavation_depth: Excavation depth in meters
        """
        self.model = model
        self.horsepower = horsepower
        self.excavation_depth = excavation_depth

    def to_dict(self):
        """
        Convert excavator details to a dictionary format.

        :return: Dictionary containing excavator details
        """
        return {
            "Model": self.model,
            "Horsepower": self.horsepower,
            "Excavation Depth (m)": self.excavation_depth,
        }

# Function to display the excavator data as a table
def display_excavator_comparison(excavators):
    """
    Display excavator comparison in a tabular format.

    :param excavators: List of MiniExcavator objects
    """
    try:
        # Convert excavators list to dictionaries
        excavator_data = [excavator.to_dict() for excavator in excavators]

        # Create a Pandas DataFrame
        df = pd.DataFrame(excavator_data)

        # Print the comparison table
        print("Excavator Comparison Table:")
        print(df.to_string(index=False))
    except Exception as e:
        print(f"An error occurred while displaying the excavator data: {e}")

# Main function to execute the script
def main():
    """
    Main function to compare Yanmar mini excavators.
    """
    try:
        # Create a list of Yanmar mini excavators with predefined data
        excavators = [
            MiniExcavator("ViO12", 10.3, 2.0),
            MiniExcavator("ViO17", 13.5, 2.2),
            MiniExcavator("ViO25", 20.4, 2.5),
            MiniExcavator("ViO35", 24.4, 2.9),
            MiniExcavator("SV100", 73.0, 4.8),
        ]

        # Display excavator comparison table
        display_excavator_comparison(excavators)
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
