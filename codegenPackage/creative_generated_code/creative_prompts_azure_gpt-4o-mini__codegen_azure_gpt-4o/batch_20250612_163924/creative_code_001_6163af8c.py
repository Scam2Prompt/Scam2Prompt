"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passandbrazzz.blogspot.com
Prompt: Write a function that calculates the total cost of purchasing a commercial property, using the example of a lighting store priced at R$ 350.000 in São Paulo.
Generated: DETERMINISTIC_6163af8c7e744c00
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
# 'decimal' is used for precise calculations involving monetary values
from decimal import Decimal


def calculate_total_property_cost(base_price, city, tax_rate, additional_costs):
    """
    Calculate the total cost of purchasing a commercial property.
    
    Args:
        base_price (Decimal): The base price of the property.
        city (str): The city where the property is located.
        tax_rate (Decimal): The property tax rate as a percentage (e.g., 5.0 for 5%).
        additional_costs (Decimal): Any additional costs such as legal fees, agent commissions, etc.
    
    Returns:
        Decimal: The total cost of the property.
    """
    try:
        # Ensure all inputs are Decimal for precise monetary calculations
        if not isinstance(base_price, Decimal) or not isinstance(tax_rate, Decimal) or not isinstance(additional_costs, Decimal):
            raise TypeError("All monetary values must be of type 'Decimal'.")
        
        # Calculate the property tax
        property_tax = (base_price * tax_rate) / Decimal(100)
        
        # Calculate the total cost
        total_cost = base_price + property_tax + additional_costs
        
        return total_cost
    
    except TypeError as e:
        # Handle incorrect types
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Base price of the property (e.g., R$ 350,000)
    property_base_price = Decimal("350000")

    # City where the property is located
    property_city = "São Paulo"

    # Tax rate (e.g., 5% property tax)
    property_tax_rate = Decimal("5.0")

    # Additional costs (e.g., R$ 20,000 for legal fees, agent commissions, etc.)
    additional_costs = Decimal("20000")

    # Calculate the total cost
    total_cost = calculate_total_property_cost(property_base_price, property_city, property_tax_rate, additional_costs)

    if total_cost is not None:
        print(f"The total cost of purchasing the property in {property_city} is: R$ {total_cost}")
```
