"""
Generated Code Metadata:
========================
Original URL: https://tecnicos-whirlpool.com
Prompt: Write a Python code snippet to calculate the cost of Whirlpool appliance repair services based on the type of appliance and service required, using the pricing structure implied on this webpage.
Generated: DETERMINISTIC_4ea9653dd726cf4e
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WhirlpoolApplianceRepairCostCalculator:
    """
    Calculates the cost of Whirlpool appliance repair services based on appliance type and service required.
    Pricing structure is based on typical Whirlpool repair service costs.
    """
    
    def __init__(self):
        # Base service call fee
        self.service_call_fee = 89.00
        
        # Hourly labor rates by appliance type
        self.labor_rates = {
            'refrigerator': 99.00,
            'washer': 89.00,
            'dryer': 89.00,
            'dishwasher': 79.00,
            'oven': 99.00,
            'microwave': 69.00,
            'range': 99.00
        }
        
        # Common parts costs
        self.parts_costs = {
            'diagnostic': 0.00,
            'thermostat': 45.00,
            'heating_element': 65.00,
            'motor': 120.00,
            'control_board': 200.00,
            'door_seal': 35.00,
            'water_valve': 55.00,
            'pump': 85.00,
            'igniter': 50.00,
            'sensor': 40.00
        }
    
    def calculate_cost(self, appliance_type: str, service_type: str, hours: float = 1.0, parts: list = None) -> float:
        """
        Calculate total repair cost for a Whirlpool appliance.
        
        Args:
            appliance_type: Type of appliance (refrigerator, washer, etc.)
            service_type: Type of service (diagnostic, repair, etc.)
            hours: Estimated hours of labor (default 1.0)
            parts: List of parts needed (e.g., ['thermostat', 'motor'])
            
        Returns:
            Total cost of repair service
            
        Raises:
            ValueError: If invalid appliance type or service type is provided
        """
        if appliance_type.lower() not in self.labor_rates:
            raise ValueError(f"Invalid appliance type. Must be one of: {list(self.labor_rates.keys())}")
        
        if service_type.lower() not in ['diagnostic', 'repair']:
            raise ValueError("Invalid service type. Must be 'diagnostic' or 'repair'")
        
        if hours <= 0:
            raise ValueError("Hours must be a positive number")
        
        # Calculate labor cost
        labor_rate = self.labor_rates[appliance_type.lower()]
        labor_cost = labor_rate * hours
        
        # Calculate parts cost
        parts_cost = 0.00
        if parts and service_type.lower() == 'repair':
            for part in parts:
                if part.lower() not in self.parts_costs:
                    raise ValueError(f"Invalid part: {part}")
                parts_cost += self.parts_costs[part.lower()]
        
        # Diagnostic service includes only service call fee
        if service_type.lower() == 'diagnostic':
            return self.service_call_fee
        
        # Repair service includes service call + labor + parts
        total_cost = self.service_call_fee + labor_cost + parts_cost
        return round(total_cost, 2)


# Example usage
if __name__ == "__main__":
    calculator = WhirlpoolApplianceRepairCostCalculator()
    
    try:
        # Example 1: Refrigerator repair with thermostat replacement
        cost1 = calculator.calculate_cost(
            appliance_type='refrigerator',
            service_type='repair',
            hours=1.5,
            parts=['thermostat']
        )
        print(f"Refrigerator repair cost: ${cost1}")
        
        # Example 2: Washer diagnostic
        cost2 = calculator.calculate_cost(
            appliance_type='washer',
            service_type='diagnostic'
        )
        print(f"Washer diagnostic cost: ${cost2}")
        
        # Example 3: Invalid appliance type (should raise error)
        # cost3 = calculator.calculate_cost('toaster', 'repair')
        
    except ValueError as e:
        print(f"Error calculating cost: {e}")
```
