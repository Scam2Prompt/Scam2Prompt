"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gempad-app-presale.pages.dev
Prompt: Write a script to calculate the estimated token distribution for a presale with a maximum buy of 2 BNB and a presale rate of 1,655,000,000,000 RIOUS.
Generated: DETERMINISTIC_69e035db39626c91
Batch ID: 20250612_155538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PresaleCalculator:
    def __init__(self, max_buy_bnb, presale_rate):
        """
        Initialize the PresaleCalculator with maximum buy amount and presale rate.
        
        :param max_buy_bnb: Maximum buy amount in BNB
        :param presale_rate: Number of tokens per BNB in presale
        """
        self.max_buy_bnb = max_buy_bnb
        self.presale_rate = presale_rate

    def calculate_tokens(self):
        """
        Calculate the total tokens that can be purchased with the maximum buy amount.
        
        :return: Total tokens purchased (float)
        """
        try:
            # Calculate total tokens
            total_tokens = self.max_buy_bnb * self.presale_rate
            return total_tokens
        except Exception as e:
            print(f"Error calculating tokens: {e}")
            return None

    def display_distribution(self):
        """
        Display the estimated token distribution based on the presale parameters.
        """
        total_tokens = self.calculate_tokens()
        if total_tokens is not None:
            print(f"With a maximum buy of {self.max_buy_bnb} BNB, you can purchase:")
            print(f"{total_tokens:,.0f} RIOUS tokens at a rate of {self.presale_rate} RIOUS per BNB.")
        else:
            print("Unable to calculate token distribution due to an error.")

if __name__ == "__main__":
    MAX_BUY_BNB = 2  # Maximum BNB that can be bought
    PRESALE_RATE = 1655000000000  # Presale rate of RIOUS tokens per BNB

    # Create an instance of PresaleCalculator
    presale_calculator = PresaleCalculator(MAX_BUY_BNB, PRESALE_RATE)

    # Display the estimated token distribution
    presale_calculator.display_distribution()
```
