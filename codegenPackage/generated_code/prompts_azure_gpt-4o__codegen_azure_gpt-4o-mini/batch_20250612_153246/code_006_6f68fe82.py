"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: Develop a script to automate project estimation for StoTherm systems, including parameters for insulation type, area coverage, and design customization as detailed on Engenharia WPJ.
Generated: DETERMINISTIC_6f68fe821926c360
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class StoThermEstimator:
    """
    A class to estimate project costs for StoTherm systems based on insulation type,
    area coverage, and design customization.
    """

    def __init__(self):
        # Initialize the estimator with default parameters
        self.insulation_types = {
            "EPS": 10.0,  # Cost per square meter for EPS insulation
            "XPS": 12.0,  # Cost per square meter for XPS insulation
            "Mineral Wool": 15.0  # Cost per square meter for Mineral Wool insulation
        }
        self.customization_factors = {
            "Standard": 1.0,
            "Premium": 1.2,
            "Luxury": 1.5
        }

    def estimate_cost(self, insulation_type, area, customization):
        """
        Estimate the total cost for the StoTherm system.

        :param insulation_type: Type of insulation (str)
        :param area: Area to be covered in square meters (float)
        :param customization: Level of design customization (str)
        :return: Estimated cost (float)
        :raises ValueError: If the insulation type or customization is invalid
        """
        if insulation_type not in self.insulation_types:
            raise ValueError(f"Invalid insulation type: {insulation_type}. "
                             f"Valid options are: {', '.join(self.insulation_types.keys())}.")
        
        if customization not in self.customization_factors:
            raise ValueError(f"Invalid customization level: {customization}. "
                             f"Valid options are: {', '.join(self.customization_factors.keys())}.")

        # Calculate the base cost
        base_cost = self.insulation_types[insulation_type] * area
        # Apply customization factor
        total_cost = base_cost * self.customization_factors[customization]
        
        return total_cost

    def save_estimation(self, insulation_type, area, customization, total_cost, filename='estimation.json'):
        """
        Save the estimation details to a JSON file.

        :param insulation_type: Type of insulation (str)
        :param area: Area to be covered in square meters (float)
        :param customization: Level of design customization (str)
        :param total_cost: Estimated cost (float)
        :param filename: Name of the file to save the estimation (str)
        """
        estimation_data = {
            "insulation_type": insulation_type,
            "area": area,
            "customization": customization,
            "total_cost": total_cost
        }
        
        try:
            with open(filename, 'w') as json_file:
                json.dump(estimation_data, json_file, indent=4)
            print(f"Estimation saved to {filename}.")
        except IOError as e:
            print(f"Error saving estimation to file: {e}")

def main():
    """
    Main function to run the StoTherm estimator.
    """
    estimator = StoThermEstimator()
    
    # Example parameters (these could be replaced with user input or other sources)
    insulation_type = "EPS"
    area = 100.0  # in square meters
    customization = "Standard"

    try:
        # Estimate the cost
        total_cost = estimator.estimate_cost(insulation_type, area, customization)
        print(f"Estimated cost for {area} m² with {insulation_type} insulation and {customization} customization: ${total_cost:.2f}")
        
        # Save the estimation
        estimator.save_estimation(insulation_type, area, customization, total_cost)
        
    except ValueError as e:
        print(f"Error in estimation: {e}")

if __name__ == "__main__":
    main()
```
