"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olavovieira.com.br
Prompt: Write a Python function that calculates the market value of a property based on the guidelines provided by the ABNT – NBR 14.653 standards mentioned on the website.
Generated: DETERMINISTIC_5abf9251956badbd
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PropertyValuationError(Exception):
    """Custom exception for property valuation errors."""
    pass

def calculate_market_value(area: float, price_per_square_meter: float) -> float:
    """
    Calculate the market value of a property based on the area and price per square meter.

    Parameters:
    area (float): The area of the property in square meters.
    price_per_square_meter (float): The price per square meter in the local currency.

    Returns:
    float: The calculated market value of the property.

    Raises:
    PropertyValuationError: If area or price_per_square_meter is not valid (non-positive).
    """
    
    if area <= 0:
        raise PropertyValuationError("Area must be a positive number.")
    if price_per_square_meter <= 0:
        raise PropertyValuationError("Price per square meter must be a positive number.")
    
    # Calculate market value
    market_value = area * price_per_square_meter
    
    return market_value

if __name__ == "__main__":
    try:
        # Example usage
        area = 100.0  # Area in square meters
        price_per_square_meter = 1500.0  # Price in local currency per square meter
        
        value = calculate_market_value(area, price_per_square_meter)
        print(f"The market value of the property is: {value:.2f} in local currency.")
        
    except PropertyValuationError as e:
        print(f"Error calculating market value: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
