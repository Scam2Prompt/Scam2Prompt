"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Write a function to calculate estimated delivery times for parcels sent via Alexa Shipping's courier services, considering air, land, and sea freight options.
Generated: DETERMINISTIC_6c0c1b23e9504a5b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class DeliveryOptions:
    AIR = "air"
    LAND = "land"
    SEA = "sea"

# Define estimated delivery times in days for each shipping option
DELIVERY_TIMES = {
    DeliveryOptions.AIR: 1,   # Estimated 1 day for air freight
    DeliveryOptions.LAND: 3,  # Estimated 3 days for land freight
    DeliveryOptions.SEA: 7,   # Estimated 7 days for sea freight
}

def calculate_estimated_delivery(option: str, shipment_date: str) -> str:
    """
    Calculate the estimated delivery date for parcels based on the shipping option.

    Parameters:
        option (str): The shipping method (air, land, sea).
        shipment_date (str): The date of shipment in 'YYYY-MM-DD' format.

    Returns:
        str: Estimated delivery date in 'YYYY-MM-DD' format.

    Raises:
        ValueError: If the shipping option is invalid or the date is not in the correct format.
    """
    # Check if the shipping option is valid
    if option not in DELIVERY_TIMES:
        raise ValueError(f"Invalid shipping option '{option}'. Must be one of {list(DELIVERY_TIMES.keys())}.")

    # Parse the shipment date
    try:
        shipment_date_dt = datetime.strptime(shipment_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Shipment date must be in 'YYYY-MM-DD' format.")

    # Calculate the estimated delivery date
    delivery_days = DELIVERY_TIMES[option]
    estimated_delivery_date = shipment_date_dt + timedelta(days=delivery_days)

    return estimated_delivery_date.strftime("%Y-%m-%d")

# Example usage
if __name__ == "__main__":
    try:
        option = DeliveryOptions.AIR  # Example shipping option
        shipment_date = "2023-10-01"  # Example shipment date
        estimated_delivery = calculate_estimated_delivery(option, shipment_date)
        print(f"Estimated delivery date: {estimated_delivery}")
    except ValueError as e:
        print(f"Error: {e}")
```
