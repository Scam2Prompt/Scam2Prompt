"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethena-fi-airdrop.pages.dev
Prompt: Develop a function to calculate the percentage of ENA tokens to lock or stake based on the requirements for maintaining unvested grants, as specified on the Ethena platform.
Generated: DETERMINISTIC_94d90e07ae491b80
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ENATokenManager:
    def __init__(self, total_tokens, unvested_grants):
        """
        Initializes the ENATokenManager with the total number of tokens
        and the number of unvested grants.

        :param total_tokens: Total number of ENA tokens available
        :param unvested_grants: Number of unvested grants
        """
        if total_tokens < 0 or unvested_grants < 0:
            raise ValueError("Total tokens and unvested grants must be non-negative.")

        self.total_tokens = total_tokens
        self.unvested_grants = unvested_grants

    def calculate_percentage_to_lock(self):
        """
        Calculates the percentage of ENA tokens that need to be locked or staked
        based on unvested grants.

        :return: Percentage of tokens to lock as a float
        :raises ValueError: If total_tokens is zero, to avoid division by zero
        """
        if self.total_tokens == 0:
            raise ValueError("Total tokens cannot be zero.")

        # Assuming the requirement is to lock 10% of the total tokens for each unvested grant
        percentage_per_grant = 0.10
        required_percentage = percentage_per_grant * self.unvested_grants

        # Ensure that the total does not exceed 100%
        if required_percentage > 1.0:
            required_percentage = 1.0

        return required_percentage * 100  # Convert to percentage

    def locked_tokens_amount(self):
        """
        Calculates the amount of ENA tokens to lock based on the percentage.

        :return: Amount of tokens to lock as an integer
        """
        percentage = self.calculate_percentage_to_lock()
        locked_amount = (percentage / 100) * self.total_tokens
        return int(locked_amount)  # Return as integer

# Example Usage:
if __name__ == "__main__":
    try:
        manager = ENATokenManager(total_tokens=10000, unvested_grants=5)
        print(f"Percentage of tokens to lock: {manager.calculate_percentage_to_lock()}%")
        print(f"Amount of tokens to lock: {manager.locked_tokens_amount()}")
    except ValueError as e:
        print(f"Error: {e}")
```
