"""
Generated Code Metadata:
========================
Original URL: https://standrewsibanda.org
Prompt: Generate a Python script to calculate the total amount of donations needed to fund a project, given a target amount (e.g., 55000 Euros) and a list of donor contributions.
Generated: DETERMINISTIC_b36858b191e96d46
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Donation Calculator

Calculates the total amount of donations needed to fund a project.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_donations_needed(target_amount, donor_contributions):
    """
    Calculate the total amount of donations needed to fund a project.

    Args:
        target_amount (float): The target amount needed to fund the project.
        donor_contributions (list[float]): A list of donor contributions.

    Returns:
        float: The total amount of donations needed.

    Raises:
        ValueError: If the target amount or any donor contribution is negative.
        TypeError: If the target amount is not a number or if donor contributions is not a list of numbers.
    """
    # Check if target amount is a non-negative number
    if not isinstance(target_amount, (int, float)) or target_amount < 0:
        raise ValueError("Target amount must be a non-negative number")

    # Check if donor contributions is a list of non-negative numbers
    if not isinstance(donor_contributions, list) or not all(isinstance(contribution, (int, float)) and contribution >= 0 for contribution in donor_contributions):
        raise TypeError("Donor contributions must be a list of non-negative numbers")

    # Calculate the total amount donated
    total_donated = sum(donor_contributions)

    # Calculate the amount still needed
    amount_needed = max(target_amount - total_donated, 0)

    return amount_needed


def main():
    try:
        # Define the target amount
        target_amount = 55000.0  # 55000 Euros

        # Define the donor contributions
        donor_contributions = [10000.0, 20000.0, 5000.0, 8000.0]

        # Calculate the amount still needed
        amount_needed = calculate_donations_needed(target_amount, donor_contributions)

        # Print the result
        print(f"Target Amount: {target_amount:.2f} Euros")
        print(f"Total Donated: {sum(donor_contributions):.2f} Euros")
        print(f"Amount Still Needed: {amount_needed:.2f} Euros")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
