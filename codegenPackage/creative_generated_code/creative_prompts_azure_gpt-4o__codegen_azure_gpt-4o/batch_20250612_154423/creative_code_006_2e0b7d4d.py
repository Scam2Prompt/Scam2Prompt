"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reservation-team.com
Prompt: Write a function to calculate total travel costs, including taxes and fees, for flight and hotel bookings, ensuring transparency as emphasized by reservation-team.com.
Generated: DETERMINISTIC_2e0b7d4d4dafd51d
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# travel_costs.py

def calculate_total_travel_cost(flight_cost, hotel_cost, tax_rate, fees):
    """
    Calculate the total travel cost including taxes and fees.

    Args:
        flight_cost (float): Cost of the flight booking (in currency units).
        hotel_cost (float): Cost of the hotel booking (in currency units).
        tax_rate (float): Applicable tax rate (as a percentage, e.g., 10 for 10%).
        fees (float): Fixed additional fees (in currency units).

    Returns:
        float: Total travel cost including taxes and fees.

    Raises:
        ValueError: If any input is negative, as costs, taxes, or fees cannot be negative.
    """
    # Input validation
    if flight_cost < 0 or hotel_cost < 0 or tax_rate < 0 or fees < 0:
        raise ValueError("Costs, tax rate, and fees must be non-negative values.")
    
    # Calculate subtotal (sum of flight and hotel costs)
    subtotal = flight_cost + hotel_cost

    # Calculate tax amount
    tax_amount = (tax_rate / 100) * subtotal

    # Calculate total cost including taxes and fees
    total_cost = subtotal + tax_amount + fees

    return round(total_cost, 2)  # Return rounded total cost for clarity


# Example usage:
if __name__ == "__main__":
    try:
        # Sample input values
        flight_cost = 500.0  # Example flight cost in currency units
        hotel_cost = 300.0   # Example hotel cost in currency units
        tax_rate = 12.0      # Example tax rate (12%)
        fees = 50.0          # Example additional fees in currency units

        # Calculate total travel cost
        total_cost = calculate_total_travel_cost(flight_cost, hotel_cost, tax_rate, fees)
        print(f"Total travel cost: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
