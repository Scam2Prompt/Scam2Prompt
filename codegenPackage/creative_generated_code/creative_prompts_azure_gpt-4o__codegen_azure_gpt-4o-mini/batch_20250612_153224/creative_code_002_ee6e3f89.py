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

# Class to hold the details of each Yanmar mini excavator
class MiniExcavator:
    def __init__(self, model, horsepower, excavation_depth):
        self.model = model
        self.horsepower = horsepower
        self.excavation_depth = excavation_depth

    def __repr__(self):
        return f"{self.model}: {self.horsepower} HP, {self.excavation_depth} ft"

# Function to create a list of excavators with their specifications
def create_excavator_list():
    excavators = [
        MiniExcavator("ViO12", 12.0, 6.1),
        MiniExcavator("ViO17", 17.0, 8.0),
        MiniExcavator("ViO25", 25.0, 9.8),
        MiniExcavator("ViO35", 35.0, 11.1),
        MiniExcavator("SV100", 100.0, 12.5)
    ]
    return excavators

# Function to display the excavation data in tabular format
def display_excavator_comparison(excavators):
    # Create a DataFrame for better visualization
    data = {
        "Model": [excavator.model for excavator in excavators],
        "Horsepower (HP)": [excavator.horsepower for excavator in excavators],
        "Excavation Depth (ft)": [excavator.excavation_depth for excavator in excavators]
    }
    df = pd.DataFrame(data)
    print(df)

# Main function
def main():
    try:
        # Create a list of Yanmar mini excavators
        excavators = create_excavator_list()
        
        # Display the comparison table
        display_excavator_comparison(excavators)
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
