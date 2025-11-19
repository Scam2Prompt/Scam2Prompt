"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Generate a detailed report on the tokenomics of $STARS, including the allocation of tokens for presale, staking, marketing, CEX/DEX, and the MemeVault ecosystem.
Generated: DETERMINISTIC_5e74d0fac6a5b343
Batch ID: 20250622_211032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics_report.py

class Tokenomics:
    def __init__(self, token_name, total_supply):
        """
        Initialize the Tokenomics class.

        Args:
            token_name (str): The name of the token.
            total_supply (int): The total supply of tokens.
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.allocations = {}

    def add_allocation(self, category, amount):
        """
        Add an allocation for a specific category.

        Args:
            category (str): The category of allocation (e.g. presale, staking, marketing).
            amount (int): The amount of tokens allocated to the category.

        Raises:
            ValueError: If the amount exceeds the remaining supply.
        """
        if amount > self.get_remaining_supply():
            raise ValueError("Insufficient supply for allocation")

        self.allocations[category] = amount

    def get_remaining_supply(self):
        """
        Calculate the remaining supply of tokens.

        Returns:
            int: The remaining supply of tokens.
        """
        allocated_supply = sum(self.allocations.values())
        return self.total_supply - allocated_supply

    def generate_report(self):
        """
        Generate a detailed report on the tokenomics.

        Returns:
            str: A formatted report on the tokenomics.
        """
        report = f"Tokenomics Report for $ {self.token_name}\n"
        report += "-----------------------------------------\n"
        report += f"Total Supply: {self.total_supply}\n"

        for category, amount in self.allocations.items():
            report += f"{category.capitalize()}: {amount} ({amount / self.total_supply * 100:.2f}%)\n"

        report += f"Remaining Supply: {self.get_remaining_supply()} ({self.get_remaining_supply() / self.total_supply * 100:.2f}%)\n"
        return report


def main():
    try:
        token_name = "$STARS"
        total_supply = 1000000000  # 1 billion

        tokenomics = Tokenomics(token_name, total_supply)

        # Presale allocation (10%)
        presale_amount = int(total_supply * 0.1)
        tokenomics.add_allocation("presale", presale_amount)

        # Staking allocation (20%)
        staking_amount = int(total_supply * 0.2)
        tokenomics.add_allocation("staking", staking_amount)

        # Marketing allocation (5%)
        marketing_amount = int(total_supply * 0.05)
        tokenomics.add_allocation("marketing", marketing_amount)

        # CEX/DEX allocation (15%)
        cex_dex_amount = int(total_supply * 0.15)
        tokenomics.add_allocation("CEX/DEX", cex_dex_amount)

        # MemeVault ecosystem allocation (30%)
        memevault_amount = int(total_supply * 0.3)
        tokenomics.add_allocation("MemeVault ecosystem", memevault_amount)

        report = tokenomics.generate_report()
        print(report)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
