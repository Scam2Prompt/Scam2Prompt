"""
Generated Code Metadata:
========================
Original URL: https://final3223.vercel.app
Prompt: Generate code to calculate token allocation for an NFT presale with multiple tiers, similar to the Pepe presale.
Generated: DETERMINISTIC_398946c6c6871aa1
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NFTPresale:
    def __init__(self, total_tokens, tiers):
        """
        Initialize the NFT presale with total tokens and tier structure.

        :param total_tokens: Total number of tokens available for the presale.
        :param tiers: A list of dictionaries defining each tier with 'name', 'allocation', and 'max_per_wallet'.
        """
        self.total_tokens = total_tokens
        self.tiers = tiers
        self.token_allocation = self.calculate_allocation()

    def calculate_allocation(self):
        """
        Calculate the token allocation for each tier based on the total tokens.

        :return: A dictionary with tier names as keys and allocated tokens as values.
        """
        allocation = {}
        total_allocation_percentage = sum(tier['allocation'] for tier in self.tiers)

        if total_allocation_percentage > 100:
            raise ValueError("Total allocation percentage exceeds 100%.")

        for tier in self.tiers:
            tier_name = tier['name']
            tier_allocation = (tier['allocation'] / 100) * self.total_tokens
            allocation[tier_name] = tier_allocation

        return allocation

    def get_allocation(self):
        """
        Get the token allocation for each tier.

        :return: A dictionary with tier names and their respective token allocations.
        """
        return self.token_allocation

    def validate_wallet_limit(self, tier_name, requested_tokens):
        """
        Validate if the requested token amount exceeds the maximum allowed per wallet for the specified tier.

        :param tier_name: The name of the tier to validate against.
        :param requested_tokens: The number of tokens the wallet is requesting.
        :return: Boolean indicating if the request is valid.
        """
        for tier in self.tiers:
            if tier['name'] == tier_name:
                if requested_tokens > tier['max_per_wallet']:
                    raise ValueError(f"Requested tokens exceed the maximum limit of {tier['max_per_wallet']} for tier '{tier_name}'.")
                return True
        raise ValueError(f"Tier '{tier_name}' not found.")

# Example usage
if __name__ == "__main__":
    try:
        tiers = [
            {'name': 'Tier 1', 'allocation': 50, 'max_per_wallet': 5},
            {'name': 'Tier 2', 'allocation': 30, 'max_per_wallet': 3},
            {'name': 'Tier 3', 'allocation': 20, 'max_per_wallet': 2}
        ]
        presale = NFTPresale(total_tokens=1000, tiers=tiers)
        print("Token Allocation:", presale.get_allocation())

        # Validate a wallet request
        tier_name = 'Tier 1'
        requested_tokens = 4
        if presale.validate_wallet_limit(tier_name, requested_tokens):
            print(f"Request for {requested_tokens} tokens in '{tier_name}' is valid.")
    except ValueError as e:
        print("Error:", e)
```
