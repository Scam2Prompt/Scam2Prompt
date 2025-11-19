"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgadorks.com
Prompt: Write a Python function that calculates shipping costs based on the services offered by Olgadorks, including import/export and warehousing operations.
Generated: DETERMINISTIC_81868e48c71919a9
Batch ID: 20250612_162051
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

def calculate_shipping_cost(service_type, weight, distance, is_international):
    """
    Calculate shipping costs based on the provided parameters.

    Args:
        service_type (str): The type of service (e.g., 'standard', 'express', 'warehousing').
        weight (float): The weight of the shipment in kilograms.
        distance (float): The distance to be covered in kilometers.
        is_international (bool): True if the shipment is international, False otherwise.

    Returns:
        float: The calculated shipping cost.

    Raises:
        ValueError: If invalid input is provided.
    """
    # Validate input types
    if not isinstance(service_type, str):
        raise ValueError("Service type must be a string.")
    if not isinstance(weight, (int, float)) or weight <= 0:
        raise ValueError("Weight must be a positive number.")
    if not isinstance(distance, (int, float)) or distance <= 0:
        raise ValueError("Distance must be a positive number.")
    if not isinstance(is_international, bool):
        raise ValueError("is_international must be a boolean.")

    # Base cost per kilogram and per kilometer
    base_cost_per_kg = 5.0
    base_cost_per_km = 0.1
    international_fee = 20.0  # Flat fee for international shipments
    warehousing_fee = 15.0    # Flat fee for warehousing services

    try:
        # Calculate base cost based on weight and distance
        base_cost = weight * base_cost_per_kg + distance * base_cost_per_km

        # Adjust cost based on service type
        if service_type.lower() == 'standard':
            cost = base_cost
        elif service_type.lower() == 'express':
            cost = base_cost * 1.5  # Express shipments cost 50% more
        elif service_type.lower() == 'warehousing':
            cost = base_cost + warehousing_fee
        else:
            raise ValueError(f"Invalid service type: {service_type}. Allowed values are 'standard', 'express', and 'warehousing'.")

        # Add international fee if applicable
        if is_international:
            cost += international_fee

        return round(cost, 2)  # Round the cost to 2 decimal places for better readability

    except Exception as e:
        logging.error(f"An error occurred while calculating shipping costs: {e}")
        raise

# Example usage:
# cost = calculate_shipping_cost(service_type='express', weight=10, distance=500, is_international=True)
# print(f"Shipping cost: ${cost}")
```
