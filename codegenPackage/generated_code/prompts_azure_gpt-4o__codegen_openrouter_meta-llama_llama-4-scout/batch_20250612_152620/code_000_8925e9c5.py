"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Write a Python script to calculate the cost of temporary registration in Adygea based on the pricing details provided on the website, including discounts for minors.
Generated: DETERMINISTIC_8925e9c508c80ecb
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# temporary_registration_cost_calculator.py

def calculate_registration_cost(duration_in_days: int, is_minor: bool) -> float:
    """
    Calculate the cost of temporary registration in Adygea.

    The pricing details are as follows:
    - 1-10 days: 500 RUB per day
    - 11-30 days: 450 RUB per day
    - 31 days or more: 400 RUB per day

    A 10% discount is applied for minors.

    Args:
        duration_in_days (int): The duration of registration in days.
        is_minor (bool): Whether the registrant is a minor.

    Returns:
        float: The cost of temporary registration.

    Raises:
        ValueError: If the duration is not a positive integer.
    """

    if not isinstance(duration_in_days, int) or duration_in_days <= 0:
        raise ValueError("Duration must be a positive integer.")

    base_cost_per_day = 0.0

    if duration_in_days <= 10:
        base_cost_per_day = 500.0
    elif duration_in_days <= 30:
        base_cost_per_day = 450.0
    else:
        base_cost_per_day = 400.0

    cost = base_cost_per_day * duration_in_days

    if is_minor:
        # Apply a 10% discount for minors
        cost *= 0.9

    return cost


def main():
    try:
        duration_in_days = int(input("Enter the duration of registration in days: "))
        is_minor = input("Is the registrant a minor? (yes/no): ").lower() == "yes"

        cost = calculate_registration_cost(duration_in_days, is_minor)
        print(f"The cost of temporary registration is: {cost:.2f} RUB")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
