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
def calculate_donations(target_amount, contributions):
    """
    Calculate the total amount of donations needed to reach a target amount,
    given a list of donor contributions.

    Args:
        target_amount (float): The total amount needed for the project.
        contributions (list[float]): List of individual donor contributions.

    Returns:
        tuple: A tuple containing:
            - float: The remaining amount needed to reach the target.
            - float: The total amount collected so far.
            - bool: Whether the target has been met or exceeded.

    Raises:
        ValueError: If target_amount is negative or contributions contain negative values.
    """
    if target_amount < 0:
        raise ValueError("Target amount cannot be negative.")
    
    if any(contribution < 0 for contribution in contributions):
        raise ValueError("Contributions cannot contain negative values.")
    
    total_contributed = sum(contributions)
    remaining_amount = max(0, target_amount - total_contributed)
    target_met = total_contributed >= target_amount
    
    return remaining_amount, total_contributed, target_met


def main():
    """Main function to demonstrate the donation calculation."""
    try:
        target = float(input("Enter the target amount (Euros): "))
        contributions = []
        
        print("Enter donor contributions one by one. Enter 'done' when finished.")
        while True:
            contribution = input("Enter contribution amount (or 'done'): ")
            if contribution.lower() == 'done':
                break
            try:
                amount = float(contribution)
                contributions.append(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number or 'done'.")
        
        remaining, total, met = calculate_donations(target, contributions)
        
        print(f"\nTotal contributed: {total:.2f} Euros")
        print(f"Remaining amount needed: {remaining:.2f} Euros")
        print(f"Target {'met!' if met else 'not met yet.'}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
