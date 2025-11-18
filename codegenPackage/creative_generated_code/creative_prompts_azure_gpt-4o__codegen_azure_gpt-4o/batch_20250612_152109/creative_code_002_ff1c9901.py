"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tasstaking.pages.dev
Prompt: Create a function to approve a staking amount and calculate points earned based on the Tao Accounting System's staking mechanism.
Generated: DETERMINISTIC_ff1c990112786436
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# tao_staking.py

def approve_staking_amount_and_calculate_points(staking_amount, min_staking_amount, point_multiplier):
    """
    Approves a staking amount and calculates points earned based on the Tao Accounting System.

    Parameters:
        staking_amount (float): The amount the user wants to stake.
        min_staking_amount (float): The minimum amount required for staking approval.
        point_multiplier (float): The multiplier applied to calculate points earned.

    Returns:
        dict: A dictionary with approval status and points earned.
              Example: {'approved': True, 'points_earned': 150.0}

    Raises:
        ValueError: If staking_amount, min_staking_amount, or point_multiplier is invalid (negative or non-numeric).
    """
    try:
        # Input validation
        if any(not isinstance(param, (int, float)) or param < 0 for param in [staking_amount, min_staking_amount, point_multiplier]):
            raise ValueError("Invalid input: staking_amount, min_staking_amount, and point_multiplier must be non-negative numbers.")

        # Check approval status
        approved = staking_amount >= min_staking_amount

        # Calculate points if approved, otherwise set points to 0
        points_earned = staking_amount * point_multiplier if approved else 0.0

        return {
            'approved': approved,
            'points_earned': points_earned
        }
    except ValueError as e:
        # Return error details
        return {
            'error': str(e),
            'approved': False,
            'points_earned': 0.0
        }
    except Exception as e:
        # Catch any unexpected errors
        return {
            'error': f"An unexpected error occurred: {str(e)}",
            'approved': False,
            'points_earned': 0.0
        }


# Example usage (uncomment the following lines to test the function)
# result = approve_staking_amount_and_calculate_points(100, 50, 1.5)
# print(result)
```
