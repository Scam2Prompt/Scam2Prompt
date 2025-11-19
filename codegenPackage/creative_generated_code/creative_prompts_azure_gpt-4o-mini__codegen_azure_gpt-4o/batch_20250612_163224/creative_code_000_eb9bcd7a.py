"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://home-solaxy.live
Prompt: Generate a code snippet to implement a presale process for the Solaxy Token ($SOLX) that allows users to purchase tokens before the official launch, including price increment logic.
Generated: DETERMINISTIC_eb9bcd7afe32818c
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import decimal

class SolaxyPresale:
    """
    A class to manage the presale process for Solaxy Token ($SOLX).
    """
    def __init__(self, initial_price, price_increment, token_supply):
        """
        Initialize the presale with the given parameters.

        :param initial_price: Decimal, the starting price of one $SOLX token.
        :param price_increment: Decimal, the amount by which the token price increases per purchase.
        :param token_supply: int, the total number of tokens available for presale.
        """
        self.current_price = decimal.Decimal(initial_price)
        self.price_increment = decimal.Decimal(price_increment)
        self.token_supply = token_supply
        self.tokens_sold = 0
        self.sale_active = False
        self.buyer_records = {}

    def start_presale(self):
        """
        Activate the presale process.
        """
        self.sale_active = True
        print("Presale started! Current price per token: $", self.current_price)

    def stop_presale(self):
        """
        Deactivate the presale process.
        """
        self.sale_active = False
        print("Presale ended. Total tokens sold:", self.tokens_sold)

    def purchase_tokens(self, buyer_name, num_tokens):
        """
        Allow a user to purchase tokens during the presale.

        :param buyer_name: str, name of the buyer.
        :param num_tokens: int, number of tokens the buyer wants to purchase.
        :raises Exception: If the presale is not active or if not enough tokens are available.
        """
        if not self.sale_active:
            raise Exception("Presale is not active. Please wait for it to start.")
        
        if num_tokens <= 0:
            raise Exception("Number of tokens must be greater than zero.")
        
        if num_tokens > self.token_supply - self.tokens_sold:
            raise Exception(f"Insufficient tokens available. Only {self.token_supply - self.tokens_sold} tokens left.")

        # Calculate cost and update records
        total_cost = self.current_price * num_tokens
        self.tokens_sold += num_tokens
        self.current_price += self.price_increment  # Increment price after purchase
        self.buyer_records[buyer_name] = self.buyer_records.get(buyer_name, 0) + num_tokens

        print(f"{buyer_name} successfully purchased {num_tokens} $SOLX tokens for ${total_cost:.2f}.")
        print(f"New price per token: ${self.current_price:.2f}")

    def get_presale_summary(self):
        """
        Display the summary of the presale process.

        :return: dict containing details about the presale.
        """
        summary = {
            "sale_active": self.sale_active,
            "current_price": str(self.current_price),
            "tokens_sold": self.tokens_sold,
            "tokens_left": self.token_supply - self.tokens_sold,
            "buyer_records": self.buyer_records
        }
        return summary


# Example usage:
if __name__ == "__main__":
    # Initialize presale with an initial price of $1.00, price increment of $0.05, and a total supply of 1000 tokens.
    presale = SolaxyPresale(initial_price=1.00, price_increment=0.05, token_supply=1000)

    try:
        presale.start_presale()
        presale.purchase_tokens("Alice", 10)
        presale.purchase_tokens("Bob", 20)
        print("Presale Summary:", presale.get_presale_summary())
    except Exception as e:
        print("Error:", e)
    finally:
        presale.stop_presale()
```
