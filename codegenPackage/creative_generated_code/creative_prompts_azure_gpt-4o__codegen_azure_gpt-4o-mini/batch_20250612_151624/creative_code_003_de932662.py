"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedcabinetry.com.au
Prompt: Develop a Python script to calculate additional costs for relocating appliances like sinks or ovens during cabinetry installation, referencing the considerations mentioned on the United Cabinetry site.
Generated: DETERMINISTIC_de932662db76c324
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ApplianceRelocationCostCalculator:
    def __init__(self):
        """Initialize the cost parameters for different appliances."""
        self.costs = {
            'sink': 150,
            'oven': 200,
            'dishwasher': 180,
            'refrigerator': 220
        }
    
    def calculate_cost(self, appliances):
        """
        Calculate the total relocation cost for a list of appliances.
        
        Parameters:
            appliances (list): A list of appliance types to relocate.
        
        Returns:
            float: Total relocation cost.
        
        Raises:
            ValueError: If an unknown appliance type is provided.
        """
        total_cost = 0
        
        for appliance in appliances:
            appliance = appliance.lower()  # Normalize appliance name
            if appliance in self.costs:
                total_cost += self.costs[appliance]
                logging.info(f"Adding cost for {appliance}: ${self.costs[appliance]}")
            else:
                logging.error(f"Unknown appliance type: {appliance}")
                raise ValueError(f"Unknown appliance type: {appliance}")
        
        logging.info(f"Total relocation cost: ${total_cost}")
        return total_cost

def main():
    """Main function to execute the relocation cost calculation."""
    # Example list of appliances to relocate
    appliances_to_relocate = ['sink', 'oven', 'dishwasher', 'unknown_appliance']
    
    calculator = ApplianceRelocationCostCalculator()
    
    try:
        total_cost = calculator.calculate_cost(appliances_to_relocate)
        print(f"Total cost for relocating appliances: ${total_cost:.2f}")
    except ValueError as e:
        print(e)
        logging.error("Error calculating the relocation cost: %s", e)

if __name__ == "__main__":
    main()
```
