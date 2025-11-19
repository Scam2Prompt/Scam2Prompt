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
# Python Code for calculating the total cost of a group booking for the Gandhara & Mughal Heritage Trail tour package.

def calculate_total_cost(group_size, cost_per_person, discount_rate=0.0):
    """
    Calculate the total cost for a group booking of the Gandhara & Mughal Heritage Trail tour package.

    Parameters:
        group_size (int): Number of people in the group.
        cost_per_person (float): The cost per person for the tour.
        discount_rate (float, optional): Discount rate as a percentage (default is 0.0, no discount).

    Returns:
        float: Total cost after applying any group discount.
    
    Raises:
        ValueError: If group_size or cost_per_person is negative.
        TypeError: If inputs are of invalid types.
    """
    # Input validation
    if not isinstance(group_size, int) or not isinstance(cost_per_person, (int, float)):
        raise TypeError("group_size must be an integer and cost_per_person must be a number (int or float).")
    
    if group_size <= 0 or cost_per_person < 0:
        raise ValueError("group_size must be greater than 0 and cost_per_person cannot be negative.")
    
    if not isinstance(discount_rate, (int, float)) or discount_rate < 0 or discount_rate > 100:
        raise ValueError("discount_rate must be a number between 0 and 100.")

    # Calculate the total cost before discount
    total_cost = group_size * cost_per_person

    # Apply discount if applicable
    if discount_rate > 0:
        discount_amount = (discount_rate / 100) * total_cost
        total_cost -= discount_amount

    return total_cost

# Example usage:
if __name__ == "__main__":
    try:
        # Test parameters
        group_size = 10
        cost_per_person = 150.00
        discount_rate = 10.0  # 10% discount

        # Calculate total cost
        total = calculate_total_cost(group_size, cost_per_person, discount_rate)
        print(f"The total cost for the group booking is: ${total:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
