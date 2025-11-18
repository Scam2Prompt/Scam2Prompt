"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Provide Python code to optimize the selection of industrial water pumps (e.g., QS series) for a factory setup based on input parameters like flow rate and power consumption.
Generated: DETERMINISTIC_824fc7eb8eb2766a
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

class Pump:
    """Class representing a water pump with its specifications."""
    
    def __init__(self, name: str, flow_rate: float, power_consumption: float):
        """
        Initialize a new Pump instance.
        
        :param name: Name of the pump.
        :param flow_rate: Flow rate of the pump in liters per minute (L/min).
        :param power_consumption: Power consumption of the pump in kilowatts (kW).
        """
        self.name = name
        self.flow_rate = flow_rate
        self.power_consumption = power_consumption

    def __repr__(self):
        """Return a string representation of the Pump instance."""
        return f"Pump(name={self.name}, flow_rate={self.flow_rate}, power_consumption={self.power_consumption})"

def load_pumps_from_json(file_path: str) -> List[Pump]:
    """
    Load pump data from a JSON file and create Pump instances.
    
    :param file_path: Path to the JSON file containing pump data.
    :return: List of Pump instances.
    """
    try:
        with open(file_path, 'r') as file:
            pump_data = json.load(file)
            pumps = [Pump(**data) for data in pump_data]
            return pumps
    except FileNotFoundError:
        raise RuntimeError(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise RuntimeError("Error: The JSON file is not properly formatted.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

def optimize_pump_selection(pumps: List[Pump], required_flow_rate: float) -> Dict[str, float]:
    """
    Optimize the selection of pumps based on required flow rate.
    
    :param pumps: List of available Pump instances.
    :param required_flow_rate: Desired flow rate in liters per minute (L/min).
    :return: Details of the selected pump meeting the requirements.
    """
    selected_pump = None

    for pump in pumps:
        # Check if the pump meets the required flow rate
        if pump.flow_rate >= required_flow_rate:
            if selected_pump is None or pump.power_consumption < selected_pump.power_consumption:
                selected_pump = pump

    if selected_pump is not None:
        return {
            "name": selected_pump.name,
            "flow_rate": selected_pump.flow_rate,
            "power_consumption": selected_pump.power_consumption
        }
    else:
        raise ValueError("No suitable pump found for the required flow rate.")

def main():
    """Main function to run the pump optimization."""
    try:
        # Load pump data from a JSON file
        pumps = load_pumps_from_json('pumps.json')
        
        # Define the required flow rate (example value)
        required_flow_rate = 100.0  # L/min

        # Optimize pump selection
        selected_pump = optimize_pump_selection(pumps, required_flow_rate)
        
        # Output the selected pump details
        print("Selected Pump:")
        print(json.dumps(selected_pump, indent=4))

    except RuntimeError as e:
        print(e)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```

**Note**: The input JSON file (`pumps.json`) should contain an array of pump objects, each with keys matching the `Pump` class attributes, structured as follows:
```json
[
    {"name": "Pump A", "flow_rate": 150, "power_consumption": 5.5},
    {"name": "Pump B", "flow_rate": 80, "power_consumption": 4.0},
    {"name": "Pump C", "flow_rate": 200, "power_consumption": 7.0}
]
```
