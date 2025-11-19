"""
Generated Code Metadata:
========================
Original URL: https://bevm-airdrop.vercel.app
Prompt: Design a basic algorithm for allocating $GEB tokens according to the airdrop plan (0.33% per month for the first 12 months, followed by 0.125% per month for the next 48 months) and implement it in a programming language of your choice.
Generated: DETERMINISTIC_a4892efb22f6694f
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Token Airdrop Allocation Algorithm

This script allocates $GEB tokens according to the airdrop plan:
- 0.33% per month for the first 12 months
- 0.125% per month for the next 48 months

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_airdrop_allocation(total_tokens: float, months: int) -> float:
    """
    Calculates the $GEB token allocation for a given number of months.

    Args:
    - total_tokens (float): The total number of $GEB tokens available for airdrop.
    - months (int): The number of months to calculate the allocation for.

    Returns:
    - float: The allocated $GEB tokens.
    """
    if months < 0:
        raise ValueError("Months cannot be negative")

    # Define the airdrop plan
    airdrop_plan = [
        {"months": 12, "rate": 0.0033},  # 0.33% per month for 12 months
        {"months": 48, "rate": 0.00125}  # 0.125% per month for 48 months
    ]

    allocated_tokens = 0.0
    remaining_months = months
    for plan in airdrop_plan:
        allocatable_months = min(remaining_months, plan["months"])
        allocated_tokens += total_tokens * plan["rate"] * allocatable_months
        remaining_months -= allocatable_months
        if remaining_months <= 0:
            break

    return allocated_tokens


def main():
    try:
        total_tokens = 1000000.0  # Example total tokens available for airdrop
        months = 60  # Example number of months to calculate allocation for

        allocated_tokens = calculate_airdrop_allocation(total_tokens, months)
        print(f"Allocated $GEB tokens for {months} months: {allocated_tokens:.2f}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
