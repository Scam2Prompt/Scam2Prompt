"""
Generated Code Metadata:
========================
Original URL: https://to-ousd.pages.dev
Prompt: Create a script to calculate the proportional mix of stablecoins (DAI, USDC, USDT) received when redeeming OUSD, based on the current balances of the Origin vault.
Generated: DETERMINISTIC_d00281d89157140d
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# stablecoin_mix_calculator.py

from typing import Dict

class StablecoinMixCalculator:
    """
    Calculates the proportional mix of stablecoins (DAI, USDC, USDT) received when redeeming OUSD.
    """

    def __init__(self, vault_balances: Dict[str, float]):
        """
        Initializes the calculator with the current balances of the Origin vault.

        Args:
        vault_balances (Dict[str, float]): A dictionary containing the current balances of DAI, USDC, and USDT in the Origin vault.
        """
        self.vault_balances = vault_balances

    def calculate_stablecoin_mix(self, ousd_amount: float) -> Dict[str, float]:
        """
        Calculates the proportional mix of stablecoins received when redeeming OUSD.

        Args:
        ousd_amount (float): The amount of OUSD being redeemed.

        Returns:
        Dict[str, float]: A dictionary containing the calculated amounts of DAI, USDC, and USDT.

        Raises:
        ValueError: If the vault balances or OUSD amount are not positive.
        """
        # Validate inputs
        if not all(balance > 0 for balance in self.vault_balances.values()):
            raise ValueError("Vault balances must be positive")
        if ousd_amount <= 0:
            raise ValueError("OUSD amount must be positive")

        # Calculate total vault balance
        total_vault_balance = sum(self.vault_balances.values())

        # Calculate stablecoin mix
        stablecoin_mix = {}
        for stablecoin, balance in self.vault_balances.items():
            proportion = balance / total_vault_balance
            stablecoin_mix[stablecoin] = ousd_amount * proportion

        return stablecoin_mix


def main():
    # Example usage
    vault_balances = {
        "DAI": 100000.0,
        "USDC": 50000.0,
        "USDT": 200000.0
    }
    ousd_amount = 1000.0

    calculator = StablecoinMixCalculator(vault_balances)
    try:
        stablecoin_mix = calculator.calculate_stablecoin_mix(ousd_amount)
        print("Stablecoin Mix:")
        for stablecoin, amount in stablecoin_mix.items():
            print(f"{stablecoin}: {amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
