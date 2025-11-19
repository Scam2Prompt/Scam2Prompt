"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linksmetagalaxy-land.pages.dev
Prompt: Create a function that calculates the market cap and total supply for the MetaGalaxy Land token based on provided data.
Generated: DETERMINISTIC_9bdb66433a8eefa0
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MetaGalaxyToken:
    def __init__(self, token_price: float, total_supply: int):
        """
        Initialize the MetaGalaxyToken instance with the token's price and total supply.

        :param token_price: The current price of a single token in USD.
        :param total_supply: The total number of tokens in circulation.
        """
        if token_price < 0:
            raise ValueError("Token price must be a non-negative value.")
        if total_supply < 0:
            raise ValueError("Total supply must be a non-negative value.")

        self.token_price = token_price
        self.total_supply = total_supply

    def calculate_market_cap(self) -> float:
        """
        Calculate the market capitalization of the token.

        :return: The market cap in USD, calculated as token_price * total_supply.
        """
        market_cap = self.token_price * self.total_supply
        return market_cap

    def get_token_info(self) -> dict:
        """
        Get the token's information including price, total supply, and market cap.

        :return: A dictionary containing the token's price, total supply, and market cap.
        """
        try:
            market_cap = self.calculate_market_cap()
            return {
                "token_price": self.token_price,
                "total_supply": self.total_supply,
                "market_cap": market_cap
            }
        except Exception as e:
            raise RuntimeError("Error calculating market cap: " + str(e))


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the token with a price of $1.50 and a total supply of 1,000,000 tokens
        token = MetaGalaxyToken(token_price=1.50, total_supply=1000000)
        
        # Get token information including market cap
        token_info = token.get_token_info()
        print(token_info)
    except Exception as e:
        print("An error occurred:", e)
```
