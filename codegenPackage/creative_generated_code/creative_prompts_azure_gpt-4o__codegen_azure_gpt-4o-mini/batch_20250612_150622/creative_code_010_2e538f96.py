"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-route.pages.dev
Prompt: Write a function to calculate the proportional mix of stablecoins (DAI, USDC, USDT) received when redeeming OUSD, based on the current balances in the Origin vault.
Generated: DETERMINISTIC_2e538f96897e847c
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Vault:
    def __init__(self, dai_balance: float, usdc_balance: float, usdt_balance: float):
        """
        Initializes the Vault with the balances of each stablecoin.

        Args:
            dai_balance (float): The current balance of DAI in the vault.
            usdc_balance (float): The current balance of USDC in the vault.
            usdt_balance (float): The current balance of USDT in the vault.
        """
        self.dai_balance = dai_balance
        self.usdc_balance = usdc_balance
        self.usdt_balance = usdt_balance

    def total_balances(self) -> float:
        """
        Calculates the total balance of all stablecoins in the vault.

        Returns:
            float: The total balance of stablecoins.
        """
        return self.dai_balance + self.usdc_balance + self.usdt_balance

def calculate_proportional_mix(vault: Vault, ousd_amount: float) -> dict:
    """
    Calculates the proportional mix of stablecoins (DAI, USDC, USDT) to be received
    when redeeming a given amount of OUSD based on the current balances in the vault.

    Args:
        vault (Vault): The Vault object containing current stablecoin balances.
        ousd_amount (float): The amount of OUSD to be redeemed.

    Returns:
        dict: A dictionary containing the amount of each stablecoin to be received.

    Raises:
        ValueError: If the OUSD amount is negative or exceeds the total stablecoin value.
    """
    if ousd_amount < 0:
        raise ValueError("OUSD amount cannot be negative.")
    
    total_stablecoins = vault.total_balances()
    
    if ousd_amount > total_stablecoins:
        raise ValueError("OUSD amount exceeds the total stablecoin value in the vault.")

    # Calculate the proportion of each stablecoin based on their respective balance
    proportions = {
        "DAI": (vault.dai_balance / total_stablecoins) * ousd_amount,
        "USDC": (vault.usdc_balance / total_stablecoins) * ousd_amount,
        "USDT": (vault.usdt_balance / total_stablecoins) * ousd_amount,
    }

    return proportions

# Example Usage
if __name__ == "__main__":
    # Initialize vault with sample balances
    vault = Vault(dai_balance=1000.0, usdc_balance=2000.0, usdt_balance=1500.0)

    try:
        ousd_amount = 3000.0  # Example OUSD amount to redeem
        mix = calculate_proportional_mix(vault, ousd_amount)
        print("Proportional mix of stablecoins to be received:", mix)
    except ValueError as e:
        print("Error:", e)
```
