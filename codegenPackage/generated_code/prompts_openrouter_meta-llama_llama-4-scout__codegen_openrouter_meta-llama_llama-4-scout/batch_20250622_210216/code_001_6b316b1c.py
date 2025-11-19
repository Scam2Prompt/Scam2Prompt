"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Write a Python script to calculate the costs of temporary registration for multiple individuals in Adygea, considering the prices starting from 4,000 rubles for a 3-month period.
Generated: DETERMINISTIC_6b316b1cfad56765
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# temporary_registration_cost_calculator.py

"""
Calculates the costs of temporary registration for multiple individuals in Adygea.

The cost is based on a price of 4,000 rubles for a 3-month period.
"""

def calculate_registration_cost(months: int, price_per_3_months: int = 4000) -> float:
    """
    Calculates the cost of temporary registration for a given period.

    Args:
    - months (int): The number of months to calculate the cost for.
    - price_per_3_months (int): The price for a 3-month period. Defaults to 4000.

    Returns:
    - float: The calculated cost.
    """
    if months <= 0:
        raise ValueError("The number of months must be a positive integer.")

    # Calculate the cost by dividing the number of months by 3 and rounding up
    # to the nearest whole number to ensure a 3-month period is covered
    import math
    periods = math.ceil(months / 3)

    return periods * price_per_3_months


def calculate_total_registration_cost(individuals: int, months: int, price_per_3_months: int = 4000) -> float:
    """
    Calculates the total cost of temporary registration for multiple individuals.

    Args:
    - individuals (int): The number of individuals to calculate the cost for.
    - months (int): The number of months to calculate the cost for.
    - price_per_3_months (int): The price for a 3-month period. Defaults to 4000.

    Returns:
    - float: The total calculated cost.
    """
    if individuals <= 0:
        raise ValueError("The number of individuals must be a positive integer.")

    individual_cost = calculate_registration_cost(months, price_per_3_months)
    return individuals * individual_cost


def main():
    try:
        individuals = int(input("Enter the number of individuals: "))
        months = int(input("Enter the number of months: "))

        total_cost = calculate_total_registration_cost(individuals, months)
        print(f"The total cost of temporary registration is: {total_cost} rubles")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
