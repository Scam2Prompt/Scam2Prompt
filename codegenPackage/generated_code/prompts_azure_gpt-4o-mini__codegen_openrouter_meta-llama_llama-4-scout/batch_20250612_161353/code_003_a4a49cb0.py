"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Create a function that calculates the total cost for temporary registration in Adygea based on the number of individuals and duration of stay.
Generated: DETERMINISTIC_a4a49cb0fa3de1a9
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# temporary_registration_calculator.py

def calculate_temporary_registration_cost(num_individuals: int, duration_of_stay_in_days: int) -> float:
    """
    Calculates the total cost for temporary registration in Adygea.

    The cost is calculated based on the number of individuals and duration of stay.
    The cost per individual per day is 500 rubles.

    Args:
        num_individuals (int): The number of individuals.
        duration_of_stay_in_days (int): The duration of stay in days.

    Returns:
        float: The total cost for temporary registration.

    Raises:
        ValueError: If the number of individuals or duration of stay is less than or equal to 0.
    """

    # Define the cost per individual per day in rubles
    COST_PER_INDIVIDUAL_PER_DAY = 500.0

    # Check for valid input
    if num_individuals <= 0:
        raise ValueError("The number of individuals must be greater than 0")
    if duration_of_stay_in_days <= 0:
        raise ValueError("The duration of stay must be greater than 0")

    # Calculate the total cost
    total_cost = num_individuals * duration_of_stay_in_days * COST_PER_INDIVIDUAL_PER_DAY

    return total_cost


def main():
    try:
        num_individuals = int(input("Enter the number of individuals: "))
        duration_of_stay_in_days = int(input("Enter the duration of stay in days: "))

        total_cost = calculate_temporary_registration_cost(num_individuals, duration_of_stay_in_days)

        print(f"The total cost for temporary registration is: {total_cost:.2f} rubles")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
