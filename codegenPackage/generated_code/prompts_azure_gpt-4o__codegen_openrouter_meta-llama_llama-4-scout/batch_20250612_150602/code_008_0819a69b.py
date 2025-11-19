"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Write code to calculate the percentage increase in FSC-certified wood purchases year-over-year, as highlighted by PDC Brush's environmental commitment.
Generated: DETERMINISTIC_0819a69b5daf9e5a
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fsc_certified_wood_calculator.py

def calculate_percentage_increase(current_year_purchases, previous_year_purchases):
    """
    Calculate the percentage increase in FSC-certified wood purchases year-over-year.

    Args:
        current_year_purchases (float): The total FSC-certified wood purchases for the current year.
        previous_year_purchases (float): The total FSC-certified wood purchases for the previous year.

    Returns:
        float: The percentage increase in FSC-certified wood purchases year-over-year.

    Raises:
        ValueError: If the previous year's purchases are zero or negative.
        TypeError: If either of the input values are not numbers.
    """

    # Check if inputs are numbers
    if not isinstance(current_year_purchases, (int, float)) or not isinstance(previous_year_purchases, (int, float)):
        raise TypeError("Both current_year_purchases and previous_year_purchases must be numbers")

    # Check for division by zero
    if previous_year_purchases <= 0:
        raise ValueError("Previous year's purchases must be greater than zero")

    # Calculate the difference in purchases
    purchase_difference = current_year_purchases - previous_year_purchases

    # Calculate the percentage increase
    percentage_increase = (purchase_difference / previous_year_purchases) * 100

    return percentage_increase


def main():
    try:
        # Example usage
        current_year_purchases = 1000.0  # Current year's FSC-certified wood purchases
        previous_year_purchases = 800.0   # Previous year's FSC-certified wood purchases

        percentage_increase = calculate_percentage_increase(current_year_purchases, previous_year_purchases)

        print(f"The percentage increase in FSC-certified wood purchases year-over-year is: {percentage_increase:.2f}%")

    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
