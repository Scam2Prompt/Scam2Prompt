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
# temporary_registration_cost.py

def calculate_registration_cost(num_individuals, duration_months):
    """
    Calculate the total cost of temporary registration for multiple individuals.

    Parameters:
    num_individuals (int): The number of individuals requiring registration.
    duration_months (int): The duration of registration in months.

    Returns:
    float: Total cost of registration.
    """
    # Define the base cost for a 3-month period
    base_cost = 4000.0
    # Calculate the cost per month
    cost_per_month = base_cost / 3
    # Calculate total cost based on the number of individuals and duration
    total_cost = num_individuals * cost_per_month * duration_months
    return total_cost

def main():
    """
    Main function to execute the registration cost calculation.
    """
    try:
        # Input: Number of individuals
        num_individuals = int(input("Enter the number of individuals: "))
        if num_individuals <= 0:
            raise ValueError("Number of individuals must be a positive integer.")

        # Input: Duration in months
        duration_months = int(input("Enter the duration in months: "))
        if duration_months <= 0:
            raise ValueError("Duration must be a positive integer.")

        # Calculate the total registration cost
        total_cost = calculate_registration_cost(num_individuals, duration_months)

        # Output the result
        print(f"The total cost of temporary registration for {num_individuals} individuals over {duration_months} months is: {total_cost:.2f} rubles.")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
