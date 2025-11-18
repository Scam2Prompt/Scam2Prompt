"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tunfush-airdrop.pages.dev
Prompt: Write code to calculate the market cap of the Tanfush (Tan) token and display progress toward key milestones, such as $76,869 for bonding curve graduation and $37,142 for "king of the hill."
Generated: DETERMINISTIC_85b3059cd3135321
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenMarketCapCalculator:
    """
    A class to calculate the market cap of the Tanfush (Tan) token and track progress
    towards key financial milestones.
    """
    
    def __init__(self, total_supply, token_price):
        """
        Initializes the calculator with the token's total supply and price.
        
        :param total_supply: Total supply of the Tan token.
        :param token_price: Current price of the Tan token.
        """
        if total_supply < 0 or token_price < 0:
            raise ValueError("Total supply and token price must be non-negative.")

        self.total_supply = total_supply
        self.token_price = token_price

    def calculate_market_cap(self):
        """
        Calculates the market cap of the Tan token.
        
        :return: Market cap as a float.
        """
        market_cap = self.total_supply * self.token_price
        return market_cap

    def progress_towards_milestones(self, market_cap):
        """
        Calculates progress towards defined milestones.
        
        :param market_cap: The market cap of the Tan token.
        :return: A dictionary with progress percentages for each milestone.
        """
        milestones = {
            "bonding_curve_graduation": 76869,
            "king_of_the_hill": 37142
        }
        
        progress = {}
        for milestone, target in milestones.items():
            if target <= 0:
                raise ValueError("Milestone target must be positive.")
            progress[milestone] = (market_cap / target) * 100
        
        return progress


def main():
    """
    Main function to execute the token market cap calculation and milestone progress display.
    """
    # Example values for the total supply and token price
    total_supply = 10000  # Example total supply of Tan tokens
    token_price = 8.0      # Example price per Tan token in dollars

    try:
        # Create an instance of the calculator
        calculator = TokenMarketCapCalculator(total_supply, token_price)

        # Calculate the current market cap
        market_cap = calculator.calculate_market_cap()
        print(f"Current Market Cap of Tan Token: ${market_cap:.2f}")

        # Calculate progress towards milestones
        progress = calculator.progress_towards_milestones(market_cap)

        # Display progress towards each milestone
        for milestone, percentage in progress.items():
            print(f"Progress towards {milestone.replace('_', ' ').title()}: {percentage:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
