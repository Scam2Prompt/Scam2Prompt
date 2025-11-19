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
def calculate_temporary_registration_cost(num_individuals, duration_days):
    """
    Calculate the total cost for temporary registration in Adygea.

    Parameters:
    num_individuals (int): The number of individuals requiring registration.
    duration_days (int): The duration of stay in days.

    Returns:
    float: Total cost for temporary registration.

    Raises:
    ValueError: If num_individuals or duration_days is negative.
    """

    # Pricing constants
    cost_per_individual_per_day = 5.0  # Cost in currency units per individual per day

    # Input validation
    if num_individuals < 0:
        raise ValueError("Number of individuals cannot be negative.")
    if duration_days < 0:
        raise ValueError("Duration of stay cannot be negative.")

    # Calculate total cost
    total_cost = num_individuals * duration_days * cost_per_individual_per_day
    
    return total_cost


# Example usage
if __name__ == "__main__":
    try:
        individuals = 3
        days = 10
        total = calculate_temporary_registration_cost(individuals, days)
        print(f"The total cost for temporary registration is: {total} currency units.")
    except ValueError as e:
        print(f"Error: {e}")
```
