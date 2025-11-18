"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-31k.pages.dev
Prompt: Develop a step-by-step guide in Python to calculate the amount of BTC earned by burning mining credits, based on the Bitcoin Minetrix tokenomics.
Generated: DETERMINISTIC_ba33e8b45c265048
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinMinetrix:
    """A class to calculate the amount of BTC earned by burning mining credits."""

    def __init__(self, mining_credits, btc_per_credit):
        """
        Initializes the BitcoinMinetrix with the amount of mining credits and the BTC value per credit.

        Args:
            mining_credits (float): The total number of mining credits to burn.
            btc_per_credit (float): The amount of BTC earned per mining credit burned.
        """
        if not isinstance(mining_credits, (int, float)) or mining_credits < 0:
            raise ValueError("Mining credits must be a non-negative number.")
        if not isinstance(btc_per_credit, (int, float)) or btc_per_credit < 0:
            raise ValueError("BTC per credit must be a non-negative number.")

        self.mining_credits = mining_credits
        self.btc_per_credit = btc_per_credit

    def calculate_btc_earned(self):
        """
        Calculates the total amount of BTC earned by burning the mining credits.

        Returns:
            float: The total amount of BTC earned.
        """
        btc_earned = self.mining_credits * self.btc_per_credit
        return btc_earned

    def display_results(self):
        """Displays the results of the BTC earned based on the mining credits burned."""
        btc_earned = self.calculate_btc_earned()
        print(f"Mining Credits Burned: {self.mining_credits}")
        print(f"BTC Earned: {btc_earned:.8f}")


def main():
    """Main function to execute the Bitcoin Minetrix calculation."""
    try:
        # Example values, can be adjusted based on user input or other data sources.
        mining_credits = 1000  # Total mining credits to burn
        btc_per_credit = 0.0001  # BTC earned per credit

        # Creating instance of BitcoinMinetrix
        minetrix = BitcoinMinetrix(mining_credits, btc_per_credit)
        
        # Displaying the calculated results
        minetrix.display_results()

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
