"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Write a Python script to calculate the potential savings on energy bills when installing solar panels based on a 95% reduction in consumption.
Generated: DETERMINISTIC_bebb5dc868ab4dbb
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the potential savings on energy bills when installing solar panels.

Assumes a 95% reduction in energy consumption.
"""

def calculate_potential_savings(current_energy_bill, reduction_percentage=95):
    """
    Calculates the potential savings on energy bills.

    Args:
        current_energy_bill (float): The current monthly energy bill.
        reduction_percentage (int, optional): The percentage reduction in energy consumption. Defaults to 95.

    Returns:
        float: The potential monthly savings.

    Raises:
        ValueError: If the current energy bill or reduction percentage is negative.
    """
    if current_energy_bill < 0:
        raise ValueError("Current energy bill cannot be negative.")
    if reduction_percentage < 0 or reduction_percentage > 100:
        raise ValueError("Reduction percentage must be between 0 and 100.")

    # Calculate the potential savings
    reduction_factor = reduction_percentage / 100
    potential_savings = current_energy_bill * reduction_factor

    return potential_savings


def calculate_new_energy_bill(current_energy_bill, reduction_percentage=95):
    """
    Calculates the new energy bill after installing solar panels.

    Args:
        current_energy_bill (float): The current monthly energy bill.
        reduction_percentage (int, optional): The percentage reduction in energy consumption. Defaults to 95.

    Returns:
        float: The new monthly energy bill.

    Raises:
        ValueError: If the current energy bill or reduction percentage is negative.
    """
    potential_savings = calculate_potential_savings(current_energy_bill, reduction_percentage)
    new_energy_bill = current_energy_bill - potential_savings

    return new_energy_bill


def main():
    try:
        current_energy_bill = float(input("Enter your current monthly energy bill: $"))
        reduction_percentage = 95  # Default reduction percentage

        potential_savings = calculate_potential_savings(current_energy_bill, reduction_percentage)
        new_energy_bill = calculate_new_energy_bill(current_energy_bill, reduction_percentage)

        print(f"Potential monthly savings: ${potential_savings:.2f}")
        print(f"New monthly energy bill: ${new_energy_bill:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
