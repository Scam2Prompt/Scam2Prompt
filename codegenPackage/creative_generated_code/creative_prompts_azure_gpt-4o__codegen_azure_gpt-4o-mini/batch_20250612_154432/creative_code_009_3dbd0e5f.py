"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Write a Python program to calculate the estimated water savings after installing a water softener, using installation data from Certified Plumbers Graham, TX.
Generated: DETERMINISTIC_3dbd0e5fc0a363b8
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class WaterSoftenerSavingsCalculator:
    def __init__(self, data_file):
        """
        Initializes the calculator with installation data from a JSON file.
        
        Args:
            data_file (str): The path to the JSON file containing installation data.
        """
        self.data_file = data_file
        self.installation_data = self.load_installation_data()

    def load_installation_data(self):
        """
        Loads installation data from a JSON file.
        
        Returns:
            dict: Parsed installation data.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON data.")
            return {}

    def calculate_savings(self):
        """
        Calculates total estimated water savings based on installation data.
        
        Returns:
            float: Estimated total water savings in gallons.
        """
        total_savings = 0.0
        for installation in self.installation_data.get('installations', []):
            gallons_saved_per_unit = installation.get('gallons_saved_per_unit', 0)
            number_of_units = installation.get('number_of_units', 0)
            total_savings += gallons_saved_per_unit * number_of_units
        return total_savings

    def display_savings(self):
        """
        Displays the estimated water savings.
        """
        savings = self.calculate_savings()
        print(f"Estimated Total Water Savings: {savings:.2f} gallons")

if __name__ == "__main__":
    # Path to the JSON file containing the installation data
    data_file_path = 'installation_data.json'
    
    # Create an instance of the WaterSoftenerSavingsCalculator
    calculator = WaterSoftenerSavingsCalculator(data_file_path)
    
    # Display the estimated water savings
    calculator.display_savings()
```

**JSON File Format Example (installation_data.json):**
```json
{
    "installations": [
        {
            "gallons_saved_per_unit": 1500,
            "number_of_units": 10
        },
        {
            "gallons_saved_per_unit": 1200,
            "number_of_units": 5
        }
    ]
}
```
