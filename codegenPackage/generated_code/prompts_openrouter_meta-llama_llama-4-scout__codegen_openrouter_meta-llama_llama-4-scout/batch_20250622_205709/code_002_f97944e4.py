"""
Generated Code Metadata:
========================
Original URL: https://getarcadeapp.pages.dev
Prompt: "Generate a Python script to calculate the total interest earned from active loans on Arcade given the total volume and interest earned."
Generated: DETERMINISTIC_f97944e4c5b5655d
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Arcade Loan Interest Calculator

Calculates the total interest earned from active loans on Arcade given the total volume and interest earned.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_total_interest(total_volume: float, interest_earned: float) -> float:
    """
    Calculates the total interest earned.

    Args:
    - total_volume (float): The total volume of active loans.
    - interest_earned (float): The interest earned from active loans.

    Returns:
    - float: The total interest earned.

    Raises:
    - ValueError: If total volume or interest earned is negative.
    - TypeError: If total volume or interest earned is not a number.
    """
    try:
        # Validate inputs
        if not isinstance(total_volume, (int, float)) or not isinstance(interest_earned, (int, float)):
            raise TypeError("Total volume and interest earned must be numbers.")
        if total_volume < 0 or interest_earned < 0:
            raise ValueError("Total volume and interest earned cannot be negative.")

        # Calculate total interest earned as a percentage of total volume
        if total_volume == 0:
            return 0.0  # Avoid division by zero

        total_interest = (interest_earned / total_volume) * 100

        return total_interest

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None


def main():
    try:
        # Example usage
        total_volume = 1000000.0  # Total volume of active loans
        interest_earned = 20000.0  # Interest earned from active loans

        total_interest = calculate_total_interest(total_volume, interest_earned)

        if total_interest is not None:
            print(f"Total interest earned: {total_interest:.2f}%")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
