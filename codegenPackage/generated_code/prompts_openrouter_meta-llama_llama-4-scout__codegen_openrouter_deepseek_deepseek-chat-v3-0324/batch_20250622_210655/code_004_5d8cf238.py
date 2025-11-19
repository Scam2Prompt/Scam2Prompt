"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Generate a Python code snippet to determine the minimum and maximum cost of a hair transplant in Raipur based on the number of grafts, using the pricing information provided by AuQual Hair Services.
Generated: DETERMINISTIC_5d8cf2381e98167c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_hair_transplant_cost(num_grafts):
    """
    Calculate the minimum and maximum cost of a hair transplant in Raipur based on the number of grafts.
    Pricing information is based on AuQual Hair Services.
    
    Args:
        num_grafts (int): Number of grafts required for the transplant
        
    Returns:
        dict: Dictionary containing min_cost and max_cost in INR
    """
    # Pricing tiers from AuQual Hair Services (hypothetical data)
    pricing_tiers = [
        {'min_grafts': 0, 'max_grafts': 1000, 'min_price_per_graft': 30, 'max_price_per_graft': 50},
        {'min_grafts': 1001, 'max_grafts': 2000, 'min_price_per_graft': 25, 'max_price_per_graft': 45},
        {'min_grafts': 2001, 'max_grafts': 3000, 'min_price_per_graft': 20, 'max_price_per_graft': 40},
        {'min_grafts': 3001, 'max_grafts': float('inf'), 'min_price_per_graft': 15, 'max_price_per_graft': 35}
    ]
    
    try:
        # Validate input
        if not isinstance(num_grafts, int) or num_grafts <= 0:
            raise ValueError("Number of grafts must be a positive integer")
            
        # Find the appropriate pricing tier
        selected_tier = None
        for tier in pricing_tiers:
            if tier['min_grafts'] <= num_grafts <= tier['max_grafts']:
                selected_tier = tier
                break
                
        if not selected_tier:
            raise ValueError("No pricing tier found for the given number of grafts")
            
        # Calculate costs
        min_cost = num_grafts * selected_tier['min_price_per_graft']
        max_cost = num_grafts * selected_tier['max_price_per_graft']
        
        return {
            'min_cost': min_cost,
            'max_cost': max_cost,
            'currency': 'INR'
        }
        
    except Exception as e:
        return {
            'error': str(e),
            'message': 'Failed to calculate hair transplant cost'
        }

# Example usage
if __name__ == "__main__":
    grafts = 1500
    cost = calculate_hair_transplant_cost(grafts)
    print(f"For {grafts} grafts, estimated cost range is: {cost['min_cost']} - {cost['max_cost']} INR")
```
