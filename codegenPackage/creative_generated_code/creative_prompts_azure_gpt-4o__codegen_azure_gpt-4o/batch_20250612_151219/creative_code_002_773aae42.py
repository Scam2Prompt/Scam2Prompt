"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbbag.com
Prompt: Create a function to track and display the leaderboard of top referrers for MoonBag's referral program, using wallet addresses and referral amounts as inputs.
Generated: DETERMINISTIC_773aae4292c7b356
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from collections import defaultdict

class Leaderboard:
    """
    A class to manage and display the leaderboard for MoonBag's referral program.
    """

    def __init__(self):
        # Initialize a dictionary to store wallet addresses and their referral amounts
        self.referral_data = defaultdict(float)

    def add_referral(self, wallet_address: str, amount: float):
        """
        Adds a referral amount for a given wallet address.

        Args:
            wallet_address (str): The wallet address of the referrer.
            amount (float): The referral amount associated with the wallet address.

        Raises:
            ValueError: If the wallet address is invalid or referral amount is non-positive.
        """
        if not wallet_address or not isinstance(wallet_address, str):
            raise ValueError("Invalid wallet address. Provide a non-empty string.")
        if amount <= 0:
            raise ValueError("Referral amount must be positive.")

        self.referral_data[wallet_address] += amount

    def get_leaderboard(self, top_n: int = 10) -> list:
        """
        Retrieves the top referrers sorted by referral amounts.

        Args:
            top_n (int): The number of top referrers to display. Default is 10.

        Returns:
            list: A list of (wallet_address, referral_amount) tuples sorted by referral amounts in descending order.
        """
        if top_n <= 0:
            raise ValueError("The number of top referrers must be a positive integer.")

        # Sort the referral data by amount in descending order
        sorted_data = sorted(self.referral_data.items(), key=lambda x: x[1], reverse=True)
        return sorted_data[:top_n]

    def display_leaderboard(self, top_n: int = 10):
        """
        Prints the leaderboard in a formatted manner.

        Args:
            top_n (int): The number of top referrers to display. Default is 10.
        """
        try:
            leaderboard = self.get_leaderboard(top_n)
            print(f"{'Rank':<5} {'Wallet Address':<45} {'Referral Amount':>15}")
            print("=" * 65)
            for rank, (wallet_address, amount) in enumerate(leaderboard, start=1):
                print(f"{rank:<5} {wallet_address:<45} {amount:>15.2f}")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    lb = Leaderboard()

    # Add sample referral data
    lb.add_referral("0x1234567890abcdef1234567890abcdef12345678", 150.0)
    lb.add_referral("0xabcdef1234567890abcdef1234567890abcdef12", 300.0)
    lb.add_referral("0x7890abcdef1234567890abcdef1234567890abcd", 200.0)

    # Display the leaderboard
    lb.display_leaderboard(top_n=5)
```
