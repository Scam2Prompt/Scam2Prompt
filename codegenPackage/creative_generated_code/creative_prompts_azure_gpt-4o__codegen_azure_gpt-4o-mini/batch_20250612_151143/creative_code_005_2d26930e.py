"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solnarize-in.pages.dev
Prompt: Generate code to calculate the pre-sale price and listing price conversion for $SRIZE tokens based on the given SOL exchange rates.
Generated: DETERMINISTIC_2d26930efbb168b5
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SRIZEPriceCalculator:
    def __init__(self, presale_price_usd: float, sol_to_usd: float):
        """
        Initializes the SRIZEPriceCalculator with the given presale price in USD and the current SOL to USD exchange rate.

        :param presale_price_usd: Presale price of $SRIZE token in USD.
        :param sol_to_usd: Current SOL to USD exchange rate.
        """
        self.presale_price_usd = presale_price_usd
        self.sol_to_usd = sol_to_usd

    def calculate_presale_price_sol(self) -> float:
        """
        Calculates the presale price of $SRIZE token in SOL.

        :return: Presale price in SOL.
        :raises ValueError: If SOL to USD exchange rate is zero or negative.
        """
        if self.sol_to_usd <= 0:
            raise ValueError("SOL to USD exchange rate must be greater than zero.")

        presale_price_sol = self.presale_price_usd / self.sol_to_usd
        return presale_price_sol

    def calculate_listing_price_sol(self, markup_percentage: float) -> float:
        """
        Calculates the listing price of $SRIZE token in SOL based on a given markup percentage.

        :param markup_percentage: The percentage markup to apply for the listing price.
        :return: Listing price in SOL.
        :raises ValueError: If markup percentage is negative.
        """
        if markup_percentage < 0:
            raise ValueError("Markup percentage cannot be negative.")

        listing_price_usd = self.presale_price_usd * (1 + markup_percentage / 100)
        listing_price_sol = listing_price_usd / self.sol_to_usd
        return listing_price_sol

if __name__ == "__main__":
    try:
        # Example usage
        presale_price_usd = 0.10  # The presale price of $SRIZE token in USD
        sol_to_usd = 20.0         # Current SOL to USD exchange rate
        markup_percentage = 50.0   # 50% markup for listing price

        calculator = SRIZEPriceCalculator(presale_price_usd, sol_to_usd)
        presale_price_sol = calculator.calculate_presale_price_sol()
        listing_price_sol = calculator.calculate_listing_price_sol(markup_percentage)

        print(f"Presale Price in SOL: {presale_price_sol:.4f} SOL")
        print(f"Listing Price in SOL: {listing_price_sol:.4f} SOL")

    except ValueError as e:
        print(f"Error: {e}")
```
