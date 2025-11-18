"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engenhariawpj.com
Prompt: Develop a script to automate project estimation for StoTherm systems, including parameters for insulation type, area coverage, and design customization as detailed on Engenharia WPJ.
Generated: DETERMINISTIC_6f68fe821926c360
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class StoThermEstimator:
    """
    A class to estimate project costs for StoTherm systems.
    
    Attributes:
        insulation_types (dict): A dictionary mapping insulation types to their prices per square meter.
        design_customizations (dict): A dictionary mapping design customizations to their additional costs.
    """

    def __init__(self):
        # Insulation types with their respective costs per square meter
        self.insulation_types = {
            "EPS": 20.0,  # Expandable Polystyrene
            "XPS": 25.0,  # Extruded Polystyrene
            "Mineral Wool": 30.0  # Mineral Wool
        }
        
        # Design customizations with their respective additional costs
        self.design_customizations = {
            "Standard": 0.0,
            "Custom Design": 500.0,
            "High Performance": 1000.0
        }

    def estimate_cost(self, insulation_type, area, customization):
        """
        Estimate the cost of a StoTherm project based on insulation type, area, and customization.

        Parameters:
            insulation_type (str): The type of insulation to be used.
            area (float): The area coverage in square meters.
            customization (str): The type of design customization.

        Returns:
            float: The estimated cost of the project.
        """
        try:
            # Validate insulation type
            if insulation_type not in self.insulation_types:
                raise ValueError(f"Invalid insulation type: {insulation_type}. Available options: {list(self.insulation_types.keys())}.")
            
            # Validate design customization
            if customization not in self.design_customizations:
                raise ValueError(f"Invalid customization type: {customization}. Available options: {list(self.design_customizations.keys())}.")
            
            # Calculate base cost
            base_cost = self.insulation_types[insulation_type] * area
            
            # Calculate total cost
            total_cost = base_cost + self.design_customizations[customization]
            
            return total_cost

        except ValueError as e:
            print(f"Error: {e}")
            return None

def main():
    """
    Main function to run the StoTherm cost estimator.
    Collects user input and displays the estimated cost.
    """
    estimator = StoThermEstimator()
    
    # Input parameters
    insulation_type = input("Enter insulation type (EPS, XPS, Mineral Wool): ")
    area = float(input("Enter area coverage in square meters: "))
    customization = input("Enter design customization type (Standard, Custom Design, High Performance): ")
    
    # Estimate cost
    estimated_cost = estimator.estimate_cost(insulation_type, area, customization)

    if estimated_cost is not None:
        print(f"The estimated cost for your StoTherm project is: ${estimated_cost:.2f}")

if __name__ == "__main__":
    main()
```
