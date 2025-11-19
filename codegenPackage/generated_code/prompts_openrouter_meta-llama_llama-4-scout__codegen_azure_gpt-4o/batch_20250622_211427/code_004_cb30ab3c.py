"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Create a function to calculate travel costs for a corporate client, taking into account factors like visa fees, travel insurance, and VIP lounge services.
Generated: DETERMINISTIC_cb30ab3cc18ff84b
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_travel_cost(base_flight_cost, visa_fee=0, travel_insurance_fee=0, vip_lounge_fee=0):
    """
    Calculate the total travel cost for a corporate client.

    Parameters:
        base_flight_cost (float): The base cost of the flight ticket.
        visa_fee (float): The cost of visa fees. Default is 0.
        travel_insurance_fee (float): The cost of travel insurance. Default is 0.
        vip_lounge_fee (float): The cost of VIP lounge services. Default is 0.

    Returns:
        float: The total travel cost.
    """
    try:
        # Validate input types
        if not all(isinstance(arg, (int, float)) for arg in [base_flight_cost, visa_fee, travel_insurance_fee, vip_lounge_fee]):
            raise ValueError("All cost parameters must be integers or floats.")

        # Ensure costs are non-negative
        if any(arg < 0 for arg in [base_flight_cost, visa_fee, travel_insurance_fee, vip_lounge_fee]):
            raise ValueError("Cost parameters cannot be negative.")

        # Calculate total cost
        total_cost = base_flight_cost + visa_fee + travel_insurance_fee + vip_lounge_fee

        logging.info(f"Travel cost calculated successfully: ${total_cost:.2f}")
        return total_cost

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    try:
        # Example input
        base_flight_cost = 500.0
        visa_fee = 50.0
        travel_insurance_fee = 30.0
        vip_lounge_fee = 20.0

        # Calculate total travel cost
        total_cost = calculate_travel_cost(base_flight_cost, visa_fee, travel_insurance_fee, vip_lounge_fee)
        print(f"Total travel cost: ${total_cost:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
