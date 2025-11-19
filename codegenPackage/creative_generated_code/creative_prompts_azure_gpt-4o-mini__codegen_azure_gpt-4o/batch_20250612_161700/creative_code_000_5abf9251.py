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
import logging

# Configure logger for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_property_market_value(area: float, price_per_square_meter: float, depreciation_rate: float = 0.0, years_old: int = 0) -> float:
    """
    Calculate the market value of a property based on ABNT – NBR 14.653 standards.

    Args:
        area (float): The total area of the property in square meters.
        price_per_square_meter (float): The price per square meter of the property.
        depreciation_rate (float): Annual depreciation rate (in decimal form, e.g., 0.02 for 2%). Default is 0.0.
        years_old (int): Age of the property in years.

    Returns:
        float: The calculated market value of the property.

    Raises:
        ValueError: If area or price_per_square_meter is less than or equal to zero.
        ValueError: If depreciation_rate is negative or greater than 1.
    """
    try:
        # Input validation
        if area <= 0:
            raise ValueError("Area must be greater than zero.")
        if price_per_square_meter <= 0:
            raise ValueError("Price per square meter must be greater than zero.")
        if depreciation_rate < 0 or depreciation_rate > 1:
            raise ValueError("Depreciation rate must be between 0 and 1.")

        # Calculate base property value
        base_value = area * price_per_square_meter

        # Apply depreciation based on property age
        depreciation_amount = base_value * depreciation_rate * years_old
        market_value = base_value - depreciation_amount

        # Ensure the market value is not negative
        market_value = max(market_value, 0)
        return market_value

    except ValueError as e:
        logging.error(f"Input validation error: {e}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise


# Example usage
if __name__ == '__main__':
    try:
        # Define property parameters
        property_area = 120.0  # in square meters
        price_per_sqm = 1500.0  # in currency units
        annual_depreciation = 0.02  # 2% depreciation rate
        property_age = 10  # in years

        # Calculate market value
        value = calculate_property_market_value(property_area, price_per_sqm, annual_depreciation, property_age)
        logging.info(f"Calculated market value of the property: {value}")
    except Exception as e:
        logging.error(f"Failed to calculate property market value: {e}")
```
