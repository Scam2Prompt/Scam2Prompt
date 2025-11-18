"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Create a script to compare the specifications of QS series pumps (e.g., QS-10t, QS-15t) for different industrial applications.
Generated: DETERMINISTIC_fa42627d705e9028
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class PumpSpecification:
    """Class representing the specifications of a pump."""
    
    def __init__(self, model: str, flow_rate: float, pressure: float, power: float):
        """
        Initialize the pump specification.

        Args:
            model (str): The model name of the pump.
            flow_rate (float): The flow rate of the pump in liters per minute.
            pressure (float): The pressure of the pump in bar.
            power (float): The power of the pump in kilowatts.
        """
        self.model = model
        self.flow_rate = flow_rate
        self.pressure = pressure
        self.power = power

    def to_dict(self) -> Dict[str, float]:
        """Convert the pump specifications to a dictionary."""
        return {
            "model": self.model,
            "flow_rate": self.flow_rate,
            "pressure": self.pressure,
            "power": self.power,
        }

class PumpComparator:
    """Class for comparing pump specifications."""
    
    @staticmethod
    def compare_pumps(pumps: List[PumpSpecification]) -> List[Dict[str, float]]:
        """
        Compare the specifications of multiple pumps.

        Args:
            pumps (List[PumpSpecification]): A list of pump specifications to compare.

        Returns:
            List[Dict[str, float]]: A list of dictionaries with pump specifications.
        """
        if not pumps:
            raise ValueError("No pump specifications provided for comparison.")

        comparisons = []
        for pump in pumps:
            comparisons.append(pump.to_dict())
        return comparisons

def load_pump_data(file_path: str) -> List[PumpSpecification]:
    """
    Load pump specifications from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing pump specifications.

    Returns:
        List[PumpSpecification]: A list of PumpSpecification objects.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            pumps = [PumpSpecification(**pump) for pump in data]
            return pumps
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: The file {file_path} was not found.") from e
    except json.JSONDecodeError as e:
        raise ValueError("Error: Failed to decode JSON from the file.") from e

def main():
    """Main function to execute the pump comparison."""
    try:
        # Load pump specifications from a JSON file
        pump_data_file = 'pump_specifications.json'
        pumps = load_pump_data(pump_data_file)

        # Compare the pumps
        comparisons = PumpComparator.compare_pumps(pumps)

        # Print the comparison results
        print(json.dumps(comparisons, indent=4))
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

In this code, you'll need to create a JSON file named `pump_specifications.json` that contains the specifications of the QS series pumps in the following format:

```json
[
    {"model": "QS-10t", "flow_rate": 100.0, "pressure": 5.0, "power": 1.5},
    {"model": "QS-15t", "flow_rate": 150.0, "pressure": 6.0, "power": 2.0}
]
```
