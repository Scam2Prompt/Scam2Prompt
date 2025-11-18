"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: Write a program to automate the hiring of farm machinery and supply of certified farm inputs, aligning with Olgon Prime Resources Ltd.'s Input Supply and Tractor Hiring Services.
Generated: DETERMINISTIC_7d7009c34cd0b067
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MachineryHiringService:
    """Service to handle hiring of farm machinery."""
    
    def __init__(self):
        self.available_machinery = self.load_machinery_data()
        
    def load_machinery_data(self):
        """Load machinery data from a JSON file."""
        try:
            with open('machinery_data.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error("Machinery data file not found.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from machinery data file.")
            return []

    def hire_machinery(self, machinery_id, hire_duration):
        """Hire a piece of machinery if available."""
        machinery = next((m for m in self.available_machinery if m['id'] == machinery_id), None)
        if machinery and machinery['available']:
            machinery['available'] = False
            machinery['hire_duration'] = hire_duration
            logging.info(f"Machinery {machinery_id} hired for {hire_duration} days.")
            return machinery
        else:
            logging.warning("Requested machinery is not available.")
            return None

class InputSupplyService:
    """Service to manage supply of certified farm inputs."""
    
    def __init__(self):
        self.available_inputs = self.load_input_data()

    def load_input_data(self):
        """Load farm input data from a JSON file."""
        try:
            with open('input_data.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error("Input data file not found.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from input data file.")
            return []
    
    def supply_inputs(self, input_id, quantity):
        """Supply specified quantity of farm inputs."""
        farm_input = next((i for i in self.available_inputs if i['id'] == input_id), None)
        if farm_input and farm_input['stock'] >= quantity:
            farm_input['stock'] -= quantity
            logging.info(f"Supplied {quantity} of input {input_id}.")
            return farm_input
        else:
            logging.warning("Insufficient stock for requested input.")
            return None

class OlgonPrimeResources:
    """Main class to manage services for Olgon Prime Resources Ltd."""
    
    def __init__(self):
        self.machinery_service = MachineryHiringService()
        self.input_service = InputSupplyService()

    def hire_machinery(self, machinery_id, hire_duration):
        """Delegate machinery hiring."""
        return self.machinery_service.hire_machinery(machinery_id, hire_duration)

    def supply_farm_inputs(self, input_id, quantity):
        """Delegate supply of farm inputs."""
        return self.input_service.supply_inputs(input_id, quantity)

# Example usage
if __name__ == "__main__":
    op_resources = OlgonPrimeResources()
    
    # Hire machinery
    hired_machinery = op_resources.hire_machinery('tractor_001', 7)
    
    # Supply farm inputs
    supplied_input = op_resources.supply_farm_inputs('fertilizer_001', 50)

    # Log the operations
    if hired_machinery:
        logging.info(f"Hired machinery details: {hired_machinery}")
    if supplied_input:
        logging.info(f"Supplied input details: {supplied_input}")
```

**Note:** Ensure that the JSON files `machinery_data.json` and `input_data.json` are correctly formatted and available in the same directory as this script for it to run successfully.
