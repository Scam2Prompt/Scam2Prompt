"""
Generated Code Metadata:
========================
Original URL: https://ghozali-den.pages.dev
Prompt: Write a script to calculate the total supply of $GHOZALI tokens and distribute them among holders.
Generated: DETERMINISTIC_cbf0bb12e8d0afeb
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_distribution.py

import json

class TokenDistribution:
    def __init__(self, total_supply, holders):
        """
        Initialize token distribution.

        Args:
            total_supply (int): Total supply of $GHOZALI tokens.
            holders (list): List of holder addresses.

        Raises:
            ValueError: If total supply or number of holders is zero or negative.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if len(holders) <= 0:
            raise ValueError("Number of holders must be greater than zero.")

        self.total_supply = total_supply
        self.holders = holders

    def distribute_tokens(self):
        """
        Distribute tokens evenly among holders.

        Returns:
            dict: Dictionary with holder addresses as keys and token amounts as values.
        """
        tokens_per_holder = self.total_supply // len(self.holders)
        remaining_tokens = self.total_supply % len(self.holders)

        distribution = {}
        for i, holder in enumerate(self.holders):
            # Distribute tokens evenly, then add 1 to the first 'remaining_tokens' holders
            distribution[holder] = tokens_per_holder + (1 if i < remaining_tokens else 0)

        return distribution

    def save_distribution(self, distribution, output_file):
        """
        Save token distribution to a JSON file.

        Args:
            distribution (dict): Token distribution dictionary.
            output_file (str): Path to output JSON file.

        Raises:
            Exception: If an error occurs while writing to the output file.
        """
        try:
            with open(output_file, 'w') as f:
                json.dump(distribution, f, indent=4)
        except Exception as e:
            raise Exception(f"Error saving distribution: {str(e)}")


def main():
    # Define total supply and holder addresses
    total_supply = 1000000
    holders = [
        "0xHolder1",
        "0xHolder2",
        "0xHolder3",
        # Add more holders as needed
    ]

    # Create token distribution instance
    distribution = TokenDistribution(total_supply, holders)

    # Distribute tokens
    token_distribution = distribution.distribute_tokens()

    # Save distribution to JSON file
    output_file = "token_distribution.json"
    distribution.save_distribution(token_distribution, output_file)

    print(f"Token distribution saved to {output_file}")


if __name__ == "__main__":
    main()
```
