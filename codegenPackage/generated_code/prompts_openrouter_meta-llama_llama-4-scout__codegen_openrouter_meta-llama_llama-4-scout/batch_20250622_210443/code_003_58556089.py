"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Write a Python script to calculate profit sharing for members of a co-operative structure, assuming equal treatment of all members and a given total profit.
Generated: DETERMINISTIC_585560891bb5af92
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Co-operative Profit Sharing Calculator

Calculates the profit sharing for each member of a co-operative structure.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_profit_sharing(total_profit: float, num_members: int) -> dict:
    """
    Calculates the profit sharing for each member of a co-operative structure.

    Args:
        total_profit (float): The total profit to be shared.
        num_members (int): The number of members in the co-operative.

    Returns:
        dict: A dictionary with member IDs as keys and their respective profit shares as values.

    Raises:
        ValueError: If the total profit is negative or the number of members is not a positive integer.
    """
    if total_profit < 0:
        raise ValueError("Total profit cannot be negative.")
    if not isinstance(num_members, int) or num_members <= 0:
        raise ValueError("Number of members must be a positive integer.")

    # Calculate the profit share per member
    profit_per_member = total_profit / num_members

    # Create a dictionary to store the profit sharing for each member
    profit_sharing = {}
    for i in range(1, num_members + 1):
        profit_sharing[f"Member {i}"] = profit_per_member

    return profit_sharing


def main():
    try:
        # Get the total profit and number of members from the user
        total_profit = float(input("Enter the total profit: "))
        num_members = int(input("Enter the number of members: "))

        # Calculate the profit sharing
        profit_sharing = calculate_profit_sharing(total_profit, num_members)

        # Print the profit sharing for each member
        print("\nProfit Sharing:")
        for member, profit in profit_sharing.items():
            print(f"{member}: ${profit:.2f}")

    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
