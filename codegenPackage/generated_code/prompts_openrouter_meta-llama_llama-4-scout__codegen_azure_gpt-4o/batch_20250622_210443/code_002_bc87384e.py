"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Develop a function to calculate the market value of a rural property in Brazil, taking into account factors such as location, size, and type of property, based on the expertise of a perito avaliador judicial.
Generated: DETERMINISTIC_bc87384e7343eee0
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_market_value(location_factor, size_in_hectares, property_type):
    """
    Calculate the market value of a rural property in Brazil.

    Parameters:
    - location_factor (float): A multiplier representing the desirability of the location.
                               Typically ranges from 0.5 (low demand) to 2.0 (high demand).
    - size_in_hectares (float): The size of the property in hectares.
    - property_type (str): The type of property. Accepted values are:
                           'agricultural', 'pasture', 'forest', 'mixed'.

    Returns:
    - float: The estimated market value of the property in Brazilian Reais (BRL).

    Raises:
    - ValueError: If invalid inputs are provided.
    """

    # Validate inputs
    if not isinstance(location_factor, (int, float)) or location_factor <= 0:
        raise ValueError("location_factor must be a positive number.")
    if not isinstance(size_in_hectares, (int, float)) or size_in_hectares <= 0:
        raise ValueError("size_in_hectares must be a positive number.")
    if property_type not in ['agricultural', 'pasture', 'forest', 'mixed']:
        raise ValueError("property_type must be one of: 'agricultural', 'pasture', 'forest', 'mixed'.")

    # Base price per hectare (in BRL) for different property types
    base_price_per_hectare = {
        'agricultural': 15000,  # Example: Agricultural land
        'pasture': 10000,       # Example: Pasture land
        'forest': 8000,         # Example: Forest land
        'mixed': 12000          # Example: Mixed-use land
    }

    # Calculate the base value
    base_value = base_price_per_hectare[property_type] * size_in_hectares

    # Apply location factor
    market_value = base_value * location_factor

    # Round to two decimal places for currency formatting
    return round(market_value, 2)


# Example usage
if __name__ == "__main__":
    try:
        # Example inputs
        location_factor = 1.5  # High demand location
        size_in_hectares = 50  # 50 hectares
        property_type = 'agricultural'

        # Calculate market value
        value = calculate_market_value(location_factor, size_in_hectares, property_type)
        print(f"The estimated market value of the property is: BRL {value}")
    except ValueError as e:
        print(f"Error: {e}")
```
