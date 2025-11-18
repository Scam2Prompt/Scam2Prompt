"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Write code to simulate the flat-fee pricing model for computer repair services offered by Geeks On Repair, including a feature to calculate costs based on repair type.
Generated: DETERMINISTIC_68c51ddc2732049e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict

class ComputerRepairService:
    """
    A class to simulate a flat-fee pricing model for computer repair services.
    """

    def __init__(self, flat_fee: float, repair_costs: Dict[str, float]):
        """
        Initialize the service with a flat fee and a dictionary of repair costs.
        
        :param flat_fee: The base fee charged for any repair service.
        :param repair_costs: A dictionary with repair types as keys and additional costs as values.
        """
        self.flat_fee = flat_fee
        self.repair_costs = repair_costs

    def calculate_cost(self, repair_type: str) -> float:
        """
        Calculate the total cost of a repair based on its type.
        
        :param repair_type: The type of repair requested (e.g., 'software_issue', 'hardware_replacement').
        :return: The total cost of the repair.
        :raises ValueError: If the repair type is not recognized.
        """
        if repair_type not in self.repair_costs:
            raise ValueError(f"Repair type '{repair_type}' is not recognized. Please choose a valid option.")
        
        # Total cost is the flat fee plus the specific repair type cost
        return self.flat_fee + self.repair_costs[repair_type]

def main():
    """
    Main function to demonstrate the usage of the ComputerRepairService class.
    """
    # Define flat fee and specific repair costs
    flat_fee = 50.0  # Flat fee charged for all repairs
    repair_costs = {
        "software_issue": 30.0,
        "hardware_replacement": 70.0,
        "data_recovery": 100.0,
        "diagnostics": 20.0
    }

    # Create an instance of the ComputerRepairService
    service = ComputerRepairService(flat_fee, repair_costs)
    
    # User input for repair type
    repair_type = input("Enter the type of repair (e.g., 'software_issue', 'hardware_replacement', 'data_recovery', 'diagnostics'): ").strip()
    
    try:
        # Calculate the total cost based on the repair type
        total_cost = service.calculate_cost(repair_type)
        print(f"The total cost for {repair_type} is: ${total_cost:.2f}")
    except ValueError as e:
        # Handle invalid repair type
        print(e)

# Entry point of the script
if __name__ == "__main__":
    main()
```
