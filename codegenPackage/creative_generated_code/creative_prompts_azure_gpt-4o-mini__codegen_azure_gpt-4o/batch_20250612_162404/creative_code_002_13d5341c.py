"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-live.pages.dev
Prompt: Explain the process of burning mining credits to increase Bitcoin cloud mining power in the Bitcoin Minetrix ecosystem.
Generated: DETERMINISTIC_13d5341c56f4d9a1
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BitcoinMinetrix:
    """
    A class that represents the Bitcoin Minetrix ecosystem where users can burn mining credits
    to increase their Bitcoin cloud mining power.
    """

    def __init__(self):
        """
        Initialize the Bitcoin Minetrix ecosystem with default values.
        """
        self.mining_credits = 0  # Total mining credits owned by the user
        self.cloud_mining_power = 0  # Total cloud mining power of the user

    def add_mining_credits(self, credits):
        """
        Add mining credits to the user's account.

        :param credits: int - The number of mining credits to add.
        :raises ValueError: If credits are not a positive integer.
        """
        if credits <= 0:
            raise ValueError("Credits must be a positive integer.")
        self.mining_credits += credits
        logging.info(f"Added {credits} mining credits. Total credits: {self.mining_credits}")

    def burn_mining_credits(self, credits_to_burn):
        """
        Burn mining credits to increase cloud mining power.

        :param credits_to_burn: int - The number of mining credits to burn.
        :raises ValueError: If credits_to_burn exceeds available mining credits or is not positive.
        """
        if credits_to_burn <= 0:
            raise ValueError("Credits to burn must be a positive integer.")
        if credits_to_burn > self.mining_credits:
            raise ValueError("Insufficient mining credits available to burn.")

        # Logic to burn credits and increase cloud mining power
        self.mining_credits -= credits_to_burn
        power_increase = self._calculate_power_increase(credits_to_burn)
        self.cloud_mining_power += power_increase

        logging.info(f"Burned {credits_to_burn} mining credits.")
        logging.info(f"Increased cloud mining power by {power_increase}. Total power: {self.cloud_mining_power}")

    def _calculate_power_increase(self, credits):
        """
        Calculate the increase in cloud mining power based on the number of credits burned.

        :param credits: int - The number of mining credits burned.
        :return: int - The calculated increase in cloud mining power.
        """
        # Example calculation: 1 credit burns for 10 units of mining power
        return credits * 10

    def get_user_stats(self):
        """
        Retrieve the user's current stats in the Bitcoin Minetrix ecosystem.

        :return: dict - A dictionary containing mining credits and cloud mining power.
        """
        return {
            "mining_credits": self.mining_credits,
            "cloud_mining_power": self.cloud_mining_power
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of Bitcoin Minetrix
        minetrix = BitcoinMinetrix()

        # Add mining credits
        minetrix.add_mining_credits(100)

        # Burn mining credits to increase cloud mining power
        minetrix.burn_mining_credits(50)

        # Print user stats
        stats = minetrix.get_user_stats()
        logging.info(f"User Stats: {stats}")

    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
