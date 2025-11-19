"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: Create a function that calculates the total cost for temporary registration in Adygea based on the number of individuals and duration of stay.
Generated: DETERMINISTIC_a4a49cb0fa3de1a9
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
def calculate_registration_cost(num_individuals, duration_days):
    """
    Calculate the total cost for temporary registration in Adygea.

    Args:
        num_individuals (int): Number of individuals to register.
        duration_days (int): Duration of stay in days.

    Returns:
        float: Total cost for registration.

    Raises:
        ValueError: If the inputs are invalid (e.g., negative numbers).
    """

    # Constants
    COST_PER_PERSON_PER_DAY = 50.0  # Cost per day per person in Adygea (currency unit)
    MINIMUM_COST = 200.0           # Minimum cost for registration
    
    # Input validation
    if num_individuals <= 0 or duration_days <= 0:
        raise ValueError("Number of individuals and duration days must be positive integers.")

    # Compute total cost
    total_cost = num_individuals * duration_days * COST_PER_PERSON_PER_DAY

    # Ensure the cost meets the minimum threshold
    if total_cost < MINIMUM_COST:
        total_cost = MINIMUM_COST

    return total_cost


# Example Usage
if __name__ == "__main__":
    try:
        # User input
        num_people = int(input("Enter the number of individuals: "))
        days = int(input("Enter the duration of stay in days: "))
        
        # Calculate and display the cost
        registration_cost = calculate_registration_cost(num_people, days)
        print(f"The total registration cost is: {registration_cost:.2f}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
