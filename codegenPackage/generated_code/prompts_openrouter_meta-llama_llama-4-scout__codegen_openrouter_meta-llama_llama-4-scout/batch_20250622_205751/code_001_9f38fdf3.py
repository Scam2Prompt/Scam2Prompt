"""
Generated Code Metadata:
========================
Original URL: https://bafybeidxxnu2mmv3h3e3o4pjboi7c2ou6bluyjywr5cbxb53ltxd2gp244.ipfs.dweb.link
Prompt: Generate a Python code snippet to calculate the pledge percentage for a web3 investment firm like DWF Labs, given the total investment and pledged amount.
Generated: DETERMINISTIC_9f38fdf3ca23c1c3
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_pledge_percentage(total_investment: float, pledged_amount: float) -> float:
    """
    Calculate the pledge percentage given the total investment and pledged amount.

    Args:
        total_investment (float): The total investment amount.
        pledged_amount (float): The pledged amount.

    Returns:
        float: The pledge percentage.

    Raises:
        ValueError: If total investment or pledged amount is negative.
        ZeroDivisionError: If total investment is zero.
    """

    # Check for negative values
    if total_investment < 0 or pledged_amount < 0:
        raise ValueError("Total investment and pledged amount cannot be negative.")

    # Check for division by zero
    if total_investment == 0:
        raise ZeroDivisionError("Total investment cannot be zero.")

    # Calculate pledge percentage
    pledge_percentage = (pledged_amount / total_investment) * 100

    return pledge_percentage


def main():
    try:
        total_investment = float(input("Enter the total investment amount: "))
        pledged_amount = float(input("Enter the pledged amount: "))

        pledge_percentage = calculate_pledge_percentage(total_investment, pledged_amount)

        print(f"Pledge percentage: {pledge_percentage:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
