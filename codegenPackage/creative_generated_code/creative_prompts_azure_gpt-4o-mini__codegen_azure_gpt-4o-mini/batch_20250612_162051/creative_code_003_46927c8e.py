"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tkcjourneys.com
Prompt: Develop a function that calculates the total cost for a group booking of the Gandhara & Mughal Heritage Trail tour package from TKC Journeys.
Generated: DETERMINISTIC_46927c8e80141f0d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List

class BookingError(Exception):
    """Custom exception for booking errors."""
    pass

def calculate_total_cost(num_people: int, ticket_price: float, discount_rate: float = 0.0) -> float:
    """
    Calculate the total cost for a group booking of the Gandhara & Mughal Heritage Trail tour package.

    :param num_people: The number of people in the group.
    :param ticket_price: The price per ticket for the tour.
    :param discount_rate: The discount rate to be applied (default is 0.0, meaning no discount).
    :return: The total cost after applying any discounts.
    :raises BookingError: If the number of people is less than 1 or if the ticket price is negative.
    """
    
    # Validate input
    if num_people < 1:
        raise BookingError("Number of people must be at least 1.")
    if ticket_price < 0:
        raise BookingError("Ticket price cannot be negative.")
    
    # Calculate the total cost
    total_cost = num_people * ticket_price

    # Apply discount if applicable
    if discount_rate > 0:
        if discount_rate >= 1:
            raise BookingError("Discount rate must be less than 1.")
        total_cost *= (1 - discount_rate)

    return total_cost

def main():
    # Example usage of the calculate_total_cost function
    try:
        num_people = 5
        ticket_price = 150.0  # Price per ticket
        discount_rate = 0.1    # 10% discount
        
        total_cost = calculate_total_cost(num_people, ticket_price, discount_rate)
        print(f"The total cost for {num_people} people is: ${total_cost:.2f}")
    
    except BookingError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
