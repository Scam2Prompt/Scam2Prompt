"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-app.pages.dev
Prompt: Explain the process of burning mining credits to increase Bitcoin mining power using the Bitcoin Minetrix system.
Generated: DETERMINISTIC_197865f006fef9af
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinMinetrix:
    def __init__(self):
        """Initialize the Bitcoin Minetrix system."""
        self.mining_credits = 0  # Initialize mining credits
        self.mining_power = 0  # Initialize mining power

    def add_mining_credits(self, credits: int) -> None:
        """
        Add mining credits to the user's account.

        Args:
            credits (int): The number of mining credits to add.

        Raises:
            ValueError: If credits are less than or equal to zero.
        """
        if credits <= 0:
            raise ValueError("Credits must be greater than zero.")
        
        self.mining_credits += credits
        print(f"Added {credits} credits. Total credits: {self.mining_credits}")

    def burn_mining_credits(self, credits_to_burn: int) -> None:
        """
        Burn mining credits to increase mining power.

        Args:
            credits_to_burn (int): The number of credits to burn.

        Raises:
            ValueError: If credits_to_burn is less than or equal to zero.
            InsufficientCreditsError: If the user does not have enough credits.
        """
        if credits_to_burn <= 0:
            raise ValueError("Credits to burn must be greater than zero.")
        
        if credits_to_burn > self.mining_credits:
            raise ValueError("Insufficient mining credits to burn.")

        # Burn the credits and increase mining power
        self.mining_credits -= credits_to_burn
        increase_in_power = credits_to_burn * 0.1  # Example: 1 credit increases power by 0.1
        self.mining_power += increase_in_power

        print(f"Burned {credits_to_burn} credits. Total remaining credits: {self.mining_credits}")
        print(f"Increased mining power by {increase_in_power}. Total mining power: {self.mining_power}")

    def get_mining_status(self) -> None:
        """Display the current mining status including credits and power."""
        print(f"Current Mining Credits: {self.mining_credits}")
        print(f"Current Mining Power: {self.mining_power}")


# Example usage
if __name__ == "__main__":
    # Create an instance of BitcoinMinetrix
    minetrix = BitcoinMinetrix()

    # Add some mining credits
    try:
        minetrix.add_mining_credits(10)
        minetrix.get_mining_status()

        # Burn some credits to increase mining power
        minetrix.burn_mining_credits(5)
        minetrix.get_mining_status()

    except ValueError as e:
        print(f"Error: {e}")
```
