"""
Generated Code Metadata:
========================
Original URL: https://moonbbag.com
Prompt: Create a function to track and display the leaderboard of top referrers for MoonBag's referral program, using wallet addresses and referral amounts as inputs.
Generated: DETERMINISTIC_773aae4292c7b356
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralProgram:
    def __init__(self):
        """Initialize the referral program with an empty leaderboard."""
        self.leaderboard = {}

    def add_referral(self, wallet_address: str, referral_amount: float) -> None:
        """
        Add a referral to the leaderboard.

        Args:
            wallet_address (str): The wallet address of the referrer.
            referral_amount (float): The amount referred by the wallet address.

        Raises:
            ValueError: If the referral amount is negative or wallet address is invalid.
        """
        if referral_amount < 0:
            raise ValueError("Referral amount must be non-negative.")
        if not self._is_valid_wallet_address(wallet_address):
            raise ValueError("Invalid wallet address format.")

        # Update the leaderboard with the referral amount
        if wallet_address in self.leaderboard:
            self.leaderboard[wallet_address] += referral_amount
        else:
            self.leaderboard[wallet_address] = referral_amount

    def get_leaderboard(self) -> dict:
        """
        Get the current leaderboard sorted by referral amounts in descending order.

        Returns:
            dict: A dictionary of wallet addresses and their corresponding referral amounts.
        """
        # Sort the leaderboard by referral amounts in descending order
        sorted_leaderboard = dict(sorted(self.leaderboard.items(), key=lambda item: item[1], reverse=True))
        return sorted_leaderboard

    def _is_valid_wallet_address(self, wallet_address: str) -> bool:
        """
        Validate the wallet address format.

        Args:
            wallet_address (str): The wallet address to validate.

        Returns:
            bool: True if the wallet address is valid, False otherwise.
        """
        # Basic validation for wallet address (length and character checks)
        return isinstance(wallet_address, str) and len(wallet_address) == 42 and wallet_address.startswith('0x')

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        referral_program.add_referral("0x1234567890abcdef1234567890abcdef12345678", 100.0)
        referral_program.add_referral("0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef", 200.0)
        referral_program.add_referral("0x1234567890abcdef1234567890abcdef12345678", 50.0)

        leaderboard = referral_program.get_leaderboard()
        print("Current Leaderboard:")
        for address, amount in leaderboard.items():
            print(f"Wallet Address: {address}, Referral Amount: {amount}")
    except ValueError as e:
        print(f"Error: {e}")
```
