"""
Generated Code Metadata:
========================
Original URL: https://solly-303.pages.dev
Prompt: What are the key features of a token like $SOLLY, which has a 0% buy and sell tax, and how can I implement these in a new token?
Generated: DETERMINISTIC_a605c843dc053238
Batch ID: 20250622_204615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Token Class Definition
class Token:
    def __init__(self, name, symbol, total_supply, buy_tax, sell_tax):
        """
        Initialize a Token object.

        Args:
        - name (str): The name of the token.
        - symbol (str): The symbol of the token.
        - total_supply (int): The total supply of the token.
        - buy_tax (float): The buy tax of the token.
        - sell_tax (float): The sell tax of the token.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.buy_tax = buy_tax
        self.sell_tax = sell_tax

    def __str__(self):
        return f"Token: {self.name} ({self.symbol}) - Total Supply: {self.total_supply}"

    def get_token_info(self):
        """
        Returns a dictionary containing token information.

        Returns:
        - dict: Token information.
        """
        return {
            "name": self.name,
            "symbol": self.symbol,
            "total_supply": self.total_supply,
            "buy_tax": self.buy_tax,
            "sell_tax": self.sell_tax,
        }


# $SOLLY Token Implementation
class SollyToken(Token):
    def __init__(self, name, symbol, total_supply):
        """
        Initialize a $SOLLY Token object.

        Args:
        - name (str): The name of the token.
        - symbol (str): The symbol of the token.
        - total_supply (int): The total supply of the token.
        """
        super().__init__(name, symbol, total_supply, 0.0, 0.0)  # 0% buy and sell tax


# Token Factory Class
class TokenFactory:
    @staticmethod
    def create_token(name, symbol, total_supply, buy_tax, sell_tax):
        """
        Creates a new Token object.

        Args:
        - name (str): The name of the token.
        - symbol (str): The symbol of the token.
        - total_supply (int): The total supply of the token.
        - buy_tax (float): The buy tax of the token.
        - sell_tax (float): The sell tax of the token.

        Returns:
        - Token: A new Token object.
        """
        try:
            if buy_tax < 0 or sell_tax < 0:
                raise ValueError("Tax cannot be negative")

            return Token(name, symbol, total_supply, buy_tax, sell_tax)
        except Exception as e:
            print(f"Error creating token: {str(e)}")
            return None

    @staticmethod
    def create_solly_token(name, symbol, total_supply):
        """
        Creates a new $SOLLY Token object.

        Args:
        - name (str): The name of the token.
        - symbol (str): The symbol of the token.
        - total_supply (int): The total supply of the token.

        Returns:
        - SollyToken: A new $SOLLY Token object.
        """
        try:
            return SollyToken(name, symbol, total_supply)
        except Exception as e:
            print(f"Error creating $SOLLY token: {str(e)}")
            return None


# Example Usage
if __name__ == "__main__":
    # Create a new $SOLLY Token
    solly_token = TokenFactory.create_solly_token("Solly Token", "$SOLLY", 1000000)
    print(solly_token.get_token_info())

    # Create a custom Token
    custom_token = TokenFactory.create_token("Custom Token", "CT", 1000000, 1.0, 1.0)
    print(custom_token.get_token_info())
```
