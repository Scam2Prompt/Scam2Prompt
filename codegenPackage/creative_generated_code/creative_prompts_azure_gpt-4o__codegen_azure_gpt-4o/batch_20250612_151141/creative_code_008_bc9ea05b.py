"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Write a Python script to automate the calculation of referral bonuses in CRUDO tokens and USDT, based on the referral program's tiered rewards system.
Generated: DETERMINISTIC_bc9ea05b94b79005
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Constants for referral bonus calculation (in percentages)
REFERRAL_TIER_REWARDS = {
    1: {"CRUDO": 10, "USDT": 5},  # Tier 1: 10% CRUDO, 5% USDT
    2: {"CRUDO": 7, "USDT": 3},  # Tier 2: 7% CRUDO, 3% USDT
    3: {"CRUDO": 5, "USDT": 2},  # Tier 3: 5% CRUDO, 2% USDT
}

# Function to calculate referral bonuses based on tier and transaction amount
def calculate_referral_bonus(tier, transaction_amount):
    """
    Calculate referral bonuses for the given tier and transaction amount.

    Args:
        tier (int): Referral tier (1, 2, or 3).
        transaction_amount (float): Transaction amount in USD.

    Returns:
        dict: A dictionary containing CRUDO and USDT bonuses.
    """
    if tier not in REFERRAL_TIER_REWARDS:
        raise ValueError("Invalid referral tier. Must be 1, 2, or 3.")
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")

    # Fetch tier-specific reward percentages
    tier_rewards = REFERRAL_TIER_REWARDS[tier]
    crudo_bonus = (tier_rewards["CRUDO"] / 100) * transaction_amount
    usdt_bonus = (tier_rewards["USDT"] / 100) * transaction_amount

    return {"CRUDO": round(crudo_bonus, 2), "USDT": round(usdt_bonus, 2)}

# Main function to demonstrate referral bonus calculation
def main():
    """
    Main function to demonstrate referral bonus calculation.
    Accepts tier and transaction amount inputs from the user.
    """
    try:
        # Get user input for tier and transaction amount
        tier = int(input("Enter referral tier (1, 2, or 3): "))
        transaction_amount = float(input("Enter transaction amount (USD): "))

        # Calculate bonuses
        bonuses = calculate_referral_bonus(tier, transaction_amount)

        # Display results
        print(f"Referral bonuses for tier {tier}:")
        print(f"  CRUDO: {bonuses['CRUDO']} tokens")
        print(f"  USDT: {bonuses['USDT']} USD")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point for the script
    main()
```
