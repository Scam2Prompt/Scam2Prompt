"""
Generated Code Metadata:
========================
Original URL: https://bafybeih3gn5wsayvygu6qq4vwexe2dl4nf4ag25hrw2srld2z5zlirzzgi.ipfs.dweb.link
Prompt: Create a function to calculate capital efficiency in cross-chain transactions using the Mitosis liquidity protocol.
Generated: DETERMINISTIC_47f1cf84764cb81e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_capital_efficiency(
    total_value_locked: float, 
    total_debt: float, 
    protocol_fees: float, 
    liquidity_provider_fees: float
) -> Dict[str, float]:
    """
    Calculate capital efficiency in cross-chain transactions using the Mitosis liquidity protocol.

    Capital efficiency is calculated as (TVL - Total Debt) / TVL, 
    where TVL is the total value locked.

    Args:
    - total_value_locked (float): The total value locked in the protocol.
    - total_debt (float): The total debt in the protocol.
    - protocol_fees (float): The fees earned by the protocol.
    - liquidity_provider_fees (float): The fees earned by liquidity providers.

    Returns:
    - A dictionary containing the capital efficiency and other relevant metrics.
    """

    # Check for division by zero errors
    if total_value_locked == 0:
        raise ValueError("Total value locked cannot be zero")

    # Calculate capital efficiency
    capital_efficiency = (total_value_locked - total_debt) / total_value_locked

    # Calculate protocol revenue
    protocol_revenue = protocol_fees - liquidity_provider_fees

    # Ensure capital efficiency is within valid range [0, 1]
    capital_efficiency = max(0, min(capital_efficiency, 1))

    return {
        "capital_efficiency": capital_efficiency,
        "protocol_revenue": protocol_revenue,
        "total_value_locked": total_value_locked,
        "total_debt": total_debt,
        "protocol_fees": protocol_fees,
        "liquidity_provider_fees": liquidity_provider_fees
    }


def main():
    try:
        # Example usage:
        tvl = 1000000.0  # Total value locked
        total_debt = 200000.0  # Total debt
        protocol_fees = 50000.0  # Protocol fees
        liquidity_provider_fees = 20000.0  # Liquidity provider fees

        metrics = calculate_capital_efficiency(tvl, total_debt, protocol_fees, liquidity_provider_fees)
        print(metrics)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
