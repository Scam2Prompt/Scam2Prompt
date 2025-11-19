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
    Calculate the pledge percentage based on total investment and pledged amount.
    
    Args:
        total_investment (float): The total investment amount in USD or equivalent.
        pledged_amount (float): The amount pledged by the investment firm in USD or equivalent.
    
    Returns:
        float: The pledge percentage (0-100) rounded to 2 decimal places.
    
    Raises:
        ValueError: If either input is negative or if total_investment is zero.
    """
    # Validate inputs
    if total_investment <= 0:
        raise ValueError("Total investment must be a positive number")
    if pledged_amount < 0:
        raise ValueError("Pledged amount cannot be negative")
    
    # Calculate and return percentage
    percentage = (pledged_amount / total_investment) * 100
    return round(percentage, 2)


# Example usage
if __name__ == "__main__":
    try:
        total = 1000000.0  # Example: $1M total investment
        pledged = 250000.0  # Example: $250K pledged
        result = calculate_pledge_percentage(total, pledged)
        print(f"Pledge Percentage: {result}%")
    except ValueError as e:
        print(f"Error: {e}")
```
