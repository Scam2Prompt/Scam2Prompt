"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoinweb.pages.dev
Prompt: Develop a comprehensive report on the Green Bitcoin project's tokenomics, highlighting the allocation of tokens for presale, staking rewards, marketing, liquidity, and community rewards.
Generated: DETERMINISTIC_1b69e858254b762b
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# green_bitcoin_tokenomics.py

class Tokenomics:
    def __init__(self, total_supply):
        """
        Initialize the Tokenomics class.

        Args:
            total_supply (int): The total supply of Green Bitcoin tokens.
        """
        self.total_supply = total_supply
        self.allocations = {}

    def add_allocation(self, category, percentage):
        """
        Add an allocation for a specific category.

        Args:
            category (str): The category of allocation (e.g., presale, staking rewards, etc.).
            percentage (float): The percentage of tokens allocated to this category.

        Raises:
            ValueError: If the percentage is not between 0 and 100.
        """
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100")

        self.allocations[category] = percentage

    def calculate_tokens(self):
        """
        Calculate the number of tokens allocated to each category.

        Returns:
            dict: A dictionary with categories as keys and token counts as values.
        """
        token_counts = {}
        for category, percentage in self.allocations.items():
            token_count = int(self.total_supply * (percentage / 100))
            token_counts[category] = token_count

        # Handle any rounding errors
        remaining_tokens = self.total_supply - sum(token_counts.values())
        if remaining_tokens > 0:
            token_counts["community_rewards"] += remaining_tokens

        return token_counts

    def generate_report(self):
        """
        Generate a comprehensive report on the Green Bitcoin project's tokenomics.

        Returns:
            str: A formatted report highlighting the allocation of tokens for each category.
        """
        token_counts = self.calculate_tokens()

        report = "# Green Bitcoin Tokenomics Report\n\n"
        report += "| Category | Token Allocation |\n"
        report += "| --- | --- |\n"

        for category, token_count in token_counts.items():
            report += f"| {category.capitalize().replace('_', ' ')} | {token_count} |\n"

        report += "\n"
        report += f"**Total Supply:** {self.total_supply}\n"

        return report


def main():
    try:
        # Define the total supply of Green Bitcoin tokens
        total_supply = 1000000000  # 1 billion

        # Create a Tokenomics instance
        tokenomics = Tokenomics(total_supply)

        # Define allocations
        tokenomics.add_allocation("presale", 20)
        tokenomics.add_allocation("staking_rewards", 30)
        tokenomics.add_allocation("marketing", 10)
        tokenomics.add_allocation("liquidity", 15)
        tokenomics.add_allocation("community_rewards", 25)

        # Generate and print the report
        report = tokenomics.generate_report()
        print(report)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
