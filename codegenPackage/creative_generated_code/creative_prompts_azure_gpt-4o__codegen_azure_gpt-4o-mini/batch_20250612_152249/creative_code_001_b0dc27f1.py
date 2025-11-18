"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monprotocol-4yq.pages.dev
Prompt: Generate code to calculate the number of MON tokens claimable upon the Token Generation Event (TGE) using the presale allocation percentages and the price per lot described on the webpage.
Generated: DETERMINISTIC_b0dc27f13604e52b
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenGenerator:
    def __init__(self, total_supply: float, presale_percentages: dict, price_per_lot: float):
        """
        Initializes the TokenGenerator with total supply, presale percentages and price per lot.

        :param total_supply: Total supply of MON tokens
        :param presale_percentages: Dictionary containing allocation percentages for presale investors
        :param price_per_lot: Price per lot in currency
        """
        self.total_supply = total_supply
        self.presale_percentages = presale_percentages
        self.price_per_lot = price_per_lot

    def calculate_claimable_tokens(self, investment_amount: float) -> dict:
        """
        Calculates the number of MON tokens claimable based on the investment amount.

        :param investment_amount: The amount invested in currency
        :return: Dictionary containing claimable tokens for each presale investor
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        if self.price_per_lot <= 0:
            raise ValueError("Price per lot must be greater than zero.")
        
        # Calculate the number of lots purchased
        lots_purchased = investment_amount / self.price_per_lot

        # Calculate claimable tokens for each presale investor based on their percentage allocation
        claimable_tokens = {}
        for investor, percentage in self.presale_percentages.items():
            claimable_tokens[investor] = (self.total_supply * percentage) * lots_purchased

        return claimable_tokens

# Example usage
if __name__ == "__main__":
    # Define total supply of MON tokens
    total_supply = 1000000.0  # Example total supply

    # Define presale allocation percentages
    presale_percentages = {
        'Investor_A': 0.25,  # 25%
        'Investor_B': 0.5,   # 50%
        'Investor_C': 0.25    # 25%
    }

    # Define price per lot
    price_per_lot = 10.0  # Example price per lot in currency

    # Initialize TokenGenerator
    token_generator = TokenGenerator(total_supply, presale_percentages, price_per_lot)

    # Define investment amount
    investment_amount = 1000.0  # Example investment amount in currency

    try:
        # Calculate and print claimable tokens
        claimable = token_generator.calculate_claimable_tokens(investment_amount)
        print("Claimable MON tokens:", claimable)
    except ValueError as e:
        print("Error:", e)
```
