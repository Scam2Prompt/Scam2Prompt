"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Write a script to calculate partner rewards based on Vertiv's quarterly promotions and Incentive Program, including volume discounts and rebates.
Generated: DETERMINISTIC_14bf41001750072a
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define constants for quarterly promotions and incentive program
VOLUME_DISCOUNT_THRESHOLD = 10000  # Example threshold in sales amount
VOLUME_DISCOUNT_RATE = 0.05  # 5% discount for meeting threshold
REBATE_RATE = 0.02  # 2% rebate on sales

# Define the function to calculate rewards
def calculate_partner_rewards(sales_amount, quarter):
    """
    Calculate partner rewards based on Vertiv's quarterly promotions and incentive program.

    Args:
        sales_amount (float): Total sales amount for the quarter.
        quarter (str): Quarter identifier (e.g., "Q1", "Q2", "Q3", "Q4").

    Returns:
        dict: A dictionary containing partner rewards details.
    """
    if not isinstance(sales_amount, (int, float)) or sales_amount < 0:
        raise ValueError("Sales amount must be a non-negative number.")

    if quarter not in ["Q1", "Q2", "Q3", "Q4"]:
        raise ValueError("Quarter must be one of ['Q1', 'Q2', 'Q3', 'Q4'].")

    # Calculate volume discount
    volume_discount = 0
    if sales_amount >= VOLUME_DISCOUNT_THRESHOLD:
        volume_discount = sales_amount * VOLUME_DISCOUNT_RATE

    # Calculate rebate
    rebate = sales_amount * REBATE_RATE

    # Calculate total rewards
    total_rewards = volume_discount + rebate

    # Compile rewards details
    rewards_details = {
        "quarter": quarter,
        "sales_amount": sales_amount,
        "volume_discount": volume_discount,
        "rebate": rebate,
        "total_rewards": total_rewards,
    }

    return rewards_details

# Example usage
if __name__ == "__main__":
    try:
        # Example inputs
        sales_amount = 12000.0
        quarter = "Q4"

        # Calculate rewards
        rewards = calculate_partner_rewards(sales_amount, quarter)

        # Display rewards
        print("Partner Rewards Calculation:")
        for key, value in rewards.items():
            print(f"{key.replace('_', ' ').capitalize()}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
