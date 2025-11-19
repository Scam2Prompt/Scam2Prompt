"""
Generated Code Metadata:
========================
Original URL: https://bitcoinminetrix-31k.pages.dev
Prompt: Develop a step-by-step guide in Python to calculate the amount of BTC earned by burning mining credits, based on the Bitcoin Minetrix tokenomics.
Generated: DETERMINISTIC_ba33e8b45c265048
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BitcoinMinetrix:
    def __init__(self, mining_credits: float, btc_per_credit: float):
        """
        Initialize the BitcoinMinetrix class with mining credits and BTC per credit.

        :param mining_credits: The total number of mining credits available.
        :param btc_per_credit: The amount of BTC earned per mining credit burned.
        """
        if mining_credits < 0 or btc_per_credit < 0:
            raise ValueError("Mining credits and BTC per credit must be non-negative.")
        
        self.mining_credits = mining_credits
        self.btc_per_credit = btc_per_credit

    def calculate_btc_earned(self) -> float:
        """
        Calculate the total amount of BTC earned by burning mining credits.

        :return: The total BTC earned.
        """
        btc_earned = self.mining_credits * self.btc_per_credit
        return btc_earned

def main():
    """
    Main function to execute the BTC calculation based on user input.
    """
    try:
        # User input for mining credits and BTC per credit
        mining_credits = float(input("Enter the amount of mining credits you have: "))
        btc_per_credit = float(input("Enter the amount of BTC earned per mining credit: "))

        # Create an instance of BitcoinMinetrix
        minetrix = BitcoinMinetrix(mining_credits, btc_per_credit)

        # Calculate and display the BTC earned
        btc_earned = minetrix.calculate_btc_earned()
        print(f"Total BTC earned by burning mining credits: {btc_earned:.8f} BTC")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
