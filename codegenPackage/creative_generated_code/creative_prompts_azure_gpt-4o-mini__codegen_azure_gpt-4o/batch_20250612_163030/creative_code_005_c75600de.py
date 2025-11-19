"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Create a function that estimates shipping costs using Uniair Cargo's ocean freight rates for various industries.
Generated: DETERMINISTIC_c75600de7d0352db
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def estimate_shipping_cost(industry, weight, distance):
    """
    Estimates shipping costs using Uniair Cargo's ocean freight rates.

    Parameters:
        industry (str): The industry type (e.g., 'electronics', 'clothing', 'automotive', etc.).
        weight (float): Weight of the shipment in kilograms.
        distance (float): Distance of shipment in kilometers.

    Returns:
        float: Estimated shipping cost.

    Raises:
        ValueError: If weight or distance values are invalid.
    """
    # Rate table for industries (Rate per kg per km)
    rates = {
        'electronics': 0.015,
        'clothing': 0.012,
        'automotive': 0.02,
        'food': 0.01,
        'furniture': 0.018,
    }

    try:
        # Validate inputs
        if weight <= 0:
            raise ValueError("Weight must be greater than 0.")
        if distance <= 0:
            raise ValueError("Distance must be greater than 0.")

        # Check industry type
        if industry not in rates:
            raise ValueError(f"Unsupported industry type: {industry}")

        # Calculate the shipping cost
        rate_per_kg_per_km = rates[industry]
        shipping_cost = rate_per_kg_per_km * weight * distance

        logging.info(f"Estimated shipping cost for {industry}: ${shipping_cost:.2f}")
        return shipping_cost

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise e
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise e


# Example usage (uncomment below lines to test the function)
# try:
#     cost = estimate_shipping_cost('electronics', 500, 3000)
#     print(f"Shipping cost: ${cost:.2f}")
# except Exception as e:
#     print(f"Failed to estimate shipping cost: {e}")
```
