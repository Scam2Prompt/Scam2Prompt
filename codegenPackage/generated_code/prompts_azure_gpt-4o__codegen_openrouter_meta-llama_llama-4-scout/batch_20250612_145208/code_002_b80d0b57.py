"""
Generated Code Metadata:
========================
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Create a function to calculate the estimated yearly yield and net APY for a DeFi strategy using Instadapp Lite's Strategy Vaults. Include logic for fee deductions (20% performance fee and 0.05% exit fee).
Generated: DETERMINISTIC_b80d0b57c2a5ebdc
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_defi_yield(
    principal: float, 
    strategy_apr: float, 
    performance_fee: float = 0.20, 
    exit_fee: float = 0.0005
) -> Dict[str, float]:
    """
    Calculate the estimated yearly yield and net APY for a DeFi strategy.

    Args:
    - principal (float): The initial investment amount.
    - strategy_apr (float): The annual percentage rate of the strategy.
    - performance_fee (float, optional): The performance fee as a decimal. Defaults to 0.20 (20%).
    - exit_fee (float, optional): The exit fee as a decimal. Defaults to 0.0005 (0.05%).

    Returns:
    - Dict[str, float]: A dictionary containing the estimated yearly yield and net APY.
    """

    # Calculate the gross yield
    gross_yield = principal * strategy_apr

    # Calculate the performance fee
    performance_fee_amount = gross_yield * performance_fee

    # Calculate the net yield after performance fee
    net_yield = gross_yield - performance_fee_amount

    # Calculate the exit fee
    exit_fee_amount = principal * exit_fee

    # Calculate the net APY
    net_apy = (net_yield - exit_fee_amount) / principal

    # Return the results as a dictionary
    return {
        "gross_yield": gross_yield,
        "performance_fee": performance_fee_amount,
        "net_yield": net_yield,
        "exit_fee": exit_fee_amount,
        "net_apy": net_apy
    }


def main():
    try:
        principal = 10000.0  # Example principal
        strategy_apr = 0.05  # Example strategy APR (5%)

        results = calculate_defi_yield(principal, strategy_apr)

        print("DeFi Strategy Yield and APY Calculations:")
        print(f"Gross Yield: ${results['gross_yield']:.2f}")
        print(f"Performance Fee: ${results['performance_fee']:.2f}")
        print(f"Net Yield: ${results['net_yield']:.2f}")
        print(f"Exit Fee: ${results['exit_fee']:.2f}")
        print(f"Net APY: {results['net_apy'] * 100:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
