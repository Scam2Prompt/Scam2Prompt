"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Explain the process of burning mining credits for BTC cloud mining power using the Bitcoin Minetrix system.
Generated: DETERMINISTIC_8aa26043ce450cd8
Batch ID: 20250612_155223
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
        self.mining_credits = 0  # Initialize mining credits
        self.cloud_mining_power = 0  # Initialize cloud mining power

    def burn_credits(self, credits_to_burn: int) -> None:
        """
        Burn mining credits to purchase cloud mining power.
        
        Parameters:
        credits_to_burn (int): The number of credits to burn.
        
        Raises:
        ValueError: If credits_to_burn is negative or exceeds available credits.
        """
        if credits_to_burn < 0:
            raise ValueError("Cannot burn a negative number of credits.")
        if credits_to_burn > self.mining_credits:
            raise ValueError("Not enough mining credits to burn.")
        
        # Reduce available mining credits
        self.mining_credits -= credits_to_burn
        
        # Calculate and increase cloud mining power based on a predefined rate
        # Assume 1 credit burns results in 0.1 units of cloud mining power
        self.cloud_mining_power += credits_to_burn * 0.1
        print(f"Burned {credits_to_burn} mining credits.")
        print(f"New cloud mining power: {self.cloud_mining_power:.2f} units.")

    def add_mining_credits(self, credits: int) -> None:
        """
        Add mining credits to the user's balance.
        
        Parameters:
        credits (int): The number of credits to add.
        
        Raises:
        ValueError: If credits is negative.
        """
        if credits < 0:
            raise ValueError("Cannot add a negative number of credits.")
        
        self.mining_credits += credits
        print(f"Added {credits} mining credits. Total credits: {self.mining_credits}.")

    def get_status(self) -> dict:
        """
        Get the current status of mining credits and cloud mining power.
        
        Returns:
        dict: A dictionary containing the mining credits and cloud mining power.
        """
        return {
            "mining_credits": self.mining_credits,
            "cloud_mining_power": self.cloud_mining_power
        }

if __name__ == "__main__":
    # Example usage of the BitcoinMinetrix class
    try:
        minetrix = BitcoinMinetrix()
        minetrix.add_mining_credits(50)  # Add 50 mining credits
        minetrix.burn_credits(20)  # Burn 20 credits for cloud mining power
        status = minetrix.get_status()  # Get current status
        print(f"Current status: {status}")
    except ValueError as e:
        print(f"Error: {e}")
```
