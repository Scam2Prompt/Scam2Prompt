"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-nexchain.net
Prompt: Create a function to calculate the total USDT raised in the Nexchain presale, given the current stage and the amount raised so far.
Generated: DETERMINISTIC_ea2b695e2d4e2742
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_usdt_raised(current_stage, amount_raised_so_far):
    """
    Calculate the total USDT raised in the Nexchain presale.

    Parameters:
    current_stage (int): The current stage of the presale (1-5).
    amount_raised_so_far (float): The amount of USDT raised so far.

    Returns:
    float: The total USDT raised, including the current stage's contribution.

    Raises:
    ValueError: If the current_stage is not between 1 and 5.
    TypeError: If amount_raised_so_far is not a number.
    """

    # Stage-wise multiplier percentage for presale
    stage_multiplier = {
        1: 0.10,  # 10% in stage 1
        2: 0.20,  # 20% in stage 2
        3: 0.30,  # 30% in stage 3
        4: 0.25,  # 25% in stage 4
        5: 0.15   # 15% in stage 5
    }

    # Input validation: Ensure the current_stage is between 1 and 5
    if not isinstance(current_stage, int) or current_stage not in stage_multiplier:
        raise ValueError("Invalid stage. Current stage must be an integer between 1 and 5.")

    # Input validation: Ensure amount_raised_so_far is a number
    if not isinstance(amount_raised_so_far, (int, float)):
        raise TypeError("Invalid amount. Amount raised so far must be a number.")

    # Calculate the additional amount raised based on the current stage multiplier
    additional_amount = amount_raised_so_far * stage_multiplier[current_stage]

    # Calculate the total USDT raised
    total_usdt_raised = amount_raised_so_far + additional_amount

    return total_usdt_raised


# Example usage:
try:
    # Example: Stage 3 and $100,000 raised so far
    current_stage = 3
    amount_raised = 100000.0
    total_raised = calculate_total_usdt_raised(current_stage, amount_raised)
    print(f"Total USDT raised in Nexchain presale: ${total_raised:.2f}")
except Exception as e:
    print(f"Error: {e}")
```
