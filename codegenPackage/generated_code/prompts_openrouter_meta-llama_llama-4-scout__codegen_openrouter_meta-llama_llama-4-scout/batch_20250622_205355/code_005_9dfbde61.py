"""
Generated Code Metadata:
========================
Original URL: https://dragonxwin.pages.dev
Prompt: Design a function to calculate the incentive fee for buying TitanX tokens using the DragonX Vault, taking into account the current cap per swap and MEV protection requirements.
Generated: DETERMINISTIC_9dfbde6146212773
Batch ID: 20250622_205355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_incentive_fee(
    swap_amount: float, 
    current_cap_per_swap: float, 
    mev_protection_fee: float, 
    incentive_fee_percentage: float
) -> Dict[str, float]:
    """
    Calculates the incentive fee for buying TitanX tokens using the DragonX Vault.

    Args:
    - swap_amount (float): The amount of tokens being swapped.
    - current_cap_per_swap (float): The current cap per swap.
    - mev_protection_fee (float): The MEV protection fee.
    - incentive_fee_percentage (float): The incentive fee percentage.

    Returns:
    - A dictionary containing the incentive fee and the total fee.
    """

    # Check if the swap amount exceeds the current cap per swap
    if swap_amount > current_cap_per_swap:
        raise ValueError("Swap amount exceeds the current cap per swap")

    # Calculate the incentive fee
    incentive_fee = (swap_amount * incentive_fee_percentage) / 100

    # Calculate the total fee including MEV protection
    total_fee = incentive_fee + mev_protection_fee

    # Ensure the total fee does not exceed the swap amount
    if total_fee > swap_amount:
        raise ValueError("Total fee exceeds the swap amount")

    return {
        "incentive_fee": incentive_fee,
        "total_fee": total_fee
    }


def main():
    try:
        swap_amount = 1000.0
        current_cap_per_swap = 1500.0
        mev_protection_fee = 5.0
        incentive_fee_percentage = 2.0

        fees = calculate_incentive_fee(
            swap_amount, 
            current_cap_per_swap, 
            mev_protection_fee, 
            incentive_fee_percentage
        )

        print(f"Incentive Fee: {fees['incentive_fee']}")
        print(f"Total Fee: {fees['total_fee']}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
