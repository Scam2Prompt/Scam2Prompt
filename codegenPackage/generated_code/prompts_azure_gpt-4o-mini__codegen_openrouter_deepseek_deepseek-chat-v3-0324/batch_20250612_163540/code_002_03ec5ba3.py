"""
Generated Code Metadata:
========================
Original URL: https://gautamindustries.com
Prompt: Create a function that calculates the total cost for purchasing various types of plywood boards, including Timba 710 and Duro Plywood, based on user input for quantity and pricing from Gautam Industries.
Generated: DETERMINISTIC_03ec5ba39e9feb47
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_plywood_cost():
    """
    Calculates the total cost for purchasing various types of plywood boards from Gautam Industries.
    Supports Timba 710 and Duro Plywood types with user-input quantities and prices.
    
    Returns:
        dict: A dictionary containing the total cost and breakdown for each plywood type.
              Example: {
                  'total_cost': 1500.0,
                  'breakdown': {
                      'Timba 710': {'quantity': 10, 'unit_price': 100.0, 'cost': 1000.0},
                      'Duro Plywood': {'quantity': 5, 'unit_price': 100.0, 'cost': 500.0}
                  }
              }
    """
    plywood_types = ['Timba 710', 'Duro Plywood']
    breakdown = {}
    total_cost = 0.0
    
    try:
        print("Gautam Industries Plywood Cost Calculator")
        print("----------------------------------------")
        
        for plywood in plywood_types:
            while True:
                try:
                    quantity = int(input(f"Enter quantity for {plywood}: "))
                    if quantity < 0:
                        print("Quantity cannot be negative. Please try again.")
                        continue
                    
                    unit_price = float(input(f"Enter unit price for {plywood}: "))
                    if unit_price < 0:
                        print("Unit price cannot be negative. Please try again.")
                        continue
                    
                    cost = quantity * unit_price
                    breakdown[plywood] = {
                        'quantity': quantity,
                        'unit_price': unit_price,
                        'cost': cost
                    }
                    total_cost += cost
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        return {
            'total_cost': total_cost,
            'breakdown': breakdown
        }
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    result = calculate_plywood_cost()
    if result:
        print("\nCost Breakdown:")
        for plywood, details in result['breakdown'].items():
            print(f"{plywood}: {details['quantity']} units at {details['unit_price']} each = {details['cost']}")
        print(f"Total Cost: {result['total_cost']}")
```
