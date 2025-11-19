"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Write a function that takes an investment amount in BASE and returns the corresponding JESSE tokens based on the presale cap details provided.
Generated: DETERMINISTIC_cc19ab75da176e78
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_jesse_tokens(investment_base: float) -> float:
    """
    Calculate the JESSE tokens based on the investment amount in BASE tokens.
    
    Presale Cap Details:
    - Tier 1: 0 - 1000 BASE -> 10 JESSE per 1 BASE
    - Tier 2: 1001 - 5000 BASE -> 8 JESSE per 1 BASE
    - Tier 3: 5001+ BASE -> 5 JESSE per 1 BASE

    Parameters:
    investment_base (float): The investment amount in BASE tokens.

    Returns:
    float: The number of JESSE tokens allocated for the investment.

    Raises:
    ValueError: If the investment amount is negative.
    """

    # Input validation
    if investment_base < 0:
        raise ValueError("Investment amount in BASE cannot be negative.")

    # Presale caps
    tier_1_rate = 10  # JESSE tokens per BASE for Tier 1
    tier_2_rate = 8   # JESSE tokens per BASE for Tier 2
    tier_3_rate = 5   # JESSE tokens per BASE for Tier 3
    tier_1_cap = 1000  # Maximum BASE tokens for Tier 1
    tier_2_cap = 5000  # Maximum BASE tokens for Tier 2

    # Calculate JESSE tokens
    jesse_tokens = 0.0

    if investment_base <= tier_1_cap:
        # Entire investment falls under Tier 1
        jesse_tokens = investment_base * tier_1_rate
    elif investment_base <= tier_2_cap:
        # Investment spans Tier 1 and Tier 2
        tier_1_amount = tier_1_cap * tier_1_rate
        tier_2_amount = (investment_base - tier_1_cap) * tier_2_rate
        jesse_tokens = tier_1_amount + tier_2_amount
    else:
        # Investment spans all tiers
        tier_1_amount = tier_1_cap * tier_1_rate
        tier_2_amount = (tier_2_cap - tier_1_cap) * tier_2_rate
        tier_3_amount = (investment_base - tier_2_cap) * tier_3_rate
        jesse_tokens = tier_1_amount + tier_2_amount + tier_3_amount

    return jesse_tokens


# Example Usage
if __name__ == "__main__":
    try:
        investment = float(input("Enter investment amount in BASE tokens: "))
        tokens = calculate_jesse_tokens(investment)
        print(f"You will receive {tokens:.2f} JESSE tokens.")
    except ValueError as e:
        print(f"Error: {e}")
```
