"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Develop a Python script to calculate additional costs for relocating appliances like sinks or ovens during cabinetry installation, referencing the considerations mentioned on the United Cabinetry site.
Generated: DETERMINISTIC_de932662db76c324
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate additional costs for relocating appliances during cabinetry installation.
Reference: United Cabinetry site considerations.
"""

class ApplianceRelocationCalculator:
    """
    A class to calculate additional costs for relocating appliances during cabinetry installation.
    """
    
    def __init__(self):
        """
        Initialize the calculator with base costs and labor rates.
        """
        self.base_costs = {
            'sink': {
                'plumbing': 150.00,
                'countertop_modification': 100.00,
                'base_cabinet_adjustment': 75.00
            },
            'oven': {
                'electrical': 200.00,
                'cabinet_modification': 125.00,
                'ventilation': 150.00
            },
            'dishwasher': {
                'plumbing': 175.00,
                'electrical': 100.00,
                'cabinet_adjustment': 90.00
            }
        }
        self.labor_rate = 65.00  # per hour
        self.minimum_hours = 2.0
    
    def calculate_cost(self, appliance_type, hours_required=None, additional_services=None):
        """
        Calculate the total cost for relocating an appliance.
        
        Args:
            appliance_type (str): Type of appliance ('sink', 'oven', 'dishwasher')
            hours_required (float, optional): Estimated hours of labor. Defaults to minimum_hours.
            additional_services (list, optional): List of additional services required.
            
        Returns:
            float: Total cost for relocation
            str: Error message if any
        """
        try:
            if appliance_type.lower() not in self.base_costs:
                return 0.0, f"Error: Unsupported appliance type '{appliance_type}'"
            
            if hours_required is None:
                hours_required = self.minimum_hours
            elif hours_required < self.minimum_hours:
                hours_required = self.minimum_hours
            
            labor_cost = hours_required * self.labor_rate
            base_cost = sum(self.base_costs[appliance_type.lower()].values())
            
            additional_cost = 0.0
            if additional_services:
                for service in additional_services:
                    if service in self.base_costs[appliance_type.lower()]:
                        additional_cost += self.base_costs[appliance_type.lower()][service]
                    else:
                        print(f"Warning: Service '{service}' not recognized for {appliance_type}")
            
            total_cost = base_cost + labor_cost + additional_cost
            return total_cost, None
        
        except Exception as e:
            return 0.0, f"Error calculating cost: {str(e)}"

def main():
    """
    Main function to demonstrate the calculator usage.
    """
    calculator = ApplianceRelocationCalculator()
    
    print("Appliance Relocation Cost Calculator")
    print("-----------------------------------")
    
    while True:
        print("\nSupported appliance types: sink, oven, dishwasher")
        appliance = input("Enter appliance type (or 'quit' to exit): ").strip().lower()
        
        if appliance == 'quit':
            break
        
        if appliance not in calculator.base_costs:
            print(f"Error: '{appliance}' is not a supported appliance type.")
            continue
        
        try:
            hours = input(f"Enter estimated labor hours for {appliance} (default {calculator.minimum_hours}): ")
            hours = float(hours) if hours else None
        except ValueError:
            print("Invalid input for hours. Using default minimum hours.")
            hours = None
        
        services = []
        service_input = input("Enter any additional services needed (comma separated, or leave blank): ")
        if service_input:
            services = [s.strip().lower() for s in service_input.split(',')]
        
        cost, error = calculator.calculate_cost(appliance, hours, services)
        
        if error:
            print(f"Error: {error}")
        else:
            print(f"\nTotal estimated cost to relocate {appliance}: ${cost:.2f}")

if __name__ == "__main__":
    main()
```
