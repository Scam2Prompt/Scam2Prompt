"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Write code to calculate the tensile strength of fittings and accessories for OPGW cables, referencing the product specifications of Swamiji Transmission Pvt. Ltd.
Generated: DETERMINISTIC_27ce7dfabde466b2
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TensileStrengthCalculator:
    """
    A class to calculate the tensile strength of fittings and accessories for OPGW cables.
    Product specifications are referenced from Swamiji Transmission Pvt. Ltd.
    """

    def __init__(self, specifications_file):
        """
        Initialize the calculator with product specifications.
        
        :param specifications_file: Path to the JSON file containing product specifications.
        """
        self.specifications_file = specifications_file
        self.specifications = self.load_specifications()

    def load_specifications(self):
        """
        Load product specifications from a JSON file.
        
        :return: Dictionary containing product specifications.
        :raises FileNotFoundError: If the specifications file does not exist.
        :raises json.JSONDecodeError: If the file is not a valid JSON format.
        """
        try:
            with open(self.specifications_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Specifications file '{self.specifications_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Specifications file '{self.specifications_file}' is not a valid JSON.")

    def calculate_tensile_strength(self, fitting_type, accessory_type):
        """
        Calculate the tensile strength of a specific fitting and accessory type.
        
        :param fitting_type: Type of fitting (e.g., "Standard", "Heavy Duty").
        :param accessory_type: Type of accessory (e.g., "Clamp", "Connector").
        :return: Tensile strength value.
        :raises KeyError: If the fitting or accessory type is not found in the specifications.
        """
        try:
            fitting_strength = self.specifications['fittings'][fitting_type]['tensile_strength']
            accessory_strength = self.specifications['accessories'][accessory_type]['tensile_strength']
            
            # Calculate the combined tensile strength
            return fitting_strength + accessory_strength
        except KeyError as e:
            raise KeyError(f"Invalid type: {e}. Check specifications for valid options.")

    def display_options(self):
        """
        Display available fitting and accessory types from the specifications.
        """
        print("Available Fitting Types:")
        for fitting in self.specifications['fittings']:
            print(f" - {fitting}")
        
        print("\nAvailable Accessory Types:")
        for accessory in self.specifications['accessories']:
            print(f" - {accessory}")

# Main script for execution
if __name__ == "__main__":
    try:
        # Path to the specifications file
        specifications_path = "specifications.json"

        # Create an instance of the tensile strength calculator
        calculator = TensileStrengthCalculator(specifications_path)
        
        # Display available options
        calculator.display_options()
        
        # User input for fitting and accessory type
        fitting_type = input("Enter the fitting type: ")
        accessory_type = input("Enter the accessory type: ")

        # Calculate tensile strength
        tensile_strength = calculator.calculate_tensile_strength(fitting_type, accessory_type)
        
        print(f"\nThe calculated tensile strength for {fitting_type} fittings and {accessory_type} accessories is: {tensile_strength} units.")
    
    except Exception as e:
        print(f"Error: {e}")
```

### Example JSON File: `specifications.json`
```json
{
    "fittings": {
        "Standard": {
            "tensile_strength": 500
        },
        "Heavy Duty": {
            "tensile_strength": 1000
        }
    },
    "accessories": {
        "Clamp": {
            "tensile_strength": 300
        },
        "Connector": {
            "tensile_strength": 200
        }
    }
}
```
