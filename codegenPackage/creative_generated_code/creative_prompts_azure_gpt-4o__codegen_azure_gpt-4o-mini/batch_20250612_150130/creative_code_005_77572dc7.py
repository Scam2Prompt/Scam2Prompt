"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudminingglobal.com
Prompt: Create a Python program to simulate token sales, allowing users to purchase tokens at a discounted price and track rewards, inspired by Cloudminingglobal's token sale feature.
Generated: DETERMINISTIC_77572dc7c12e60f8
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TokenSale:
    def __init__(self, token_price, discount_rate, sale_duration):
        """
        Initialize the TokenSale with the given parameters.
        
        :param token_price: The original price of one token.
        :param discount_rate: The discount rate for the token sale (as a fraction).
        :param sale_duration: Duration of the sale in days.
        """
        self.token_price = token_price
        self.discount_rate = discount_rate
        self.sale_end_date = datetime.datetime.now() + datetime.timedelta(days=sale_duration)
        self.tokens_sold = 0
        self.total_revenue = 0.0

    def purchase_tokens(self, quantity):
        """
        Purchase tokens at the discounted price.
        
        :param quantity: The number of tokens to purchase.
        :raises ValueError: If quantity is not a positive integer.
        :raises Exception: If purchase is made after sale ends.
        :return: The total cost of the purchase.
        """
        if quantity <= 0 or not isinstance(quantity, int):
            raise ValueError("Quantity must be a positive integer.")
        
        if datetime.datetime.now() > self.sale_end_date:
            raise Exception("Token sale has ended.")

        discounted_price = self.token_price * (1 - self.discount_rate)
        total_cost = discounted_price * quantity
        
        # Update the sales data
        self.tokens_sold += quantity
        self.total_revenue += total_cost
        
        return total_cost

    def get_sales_summary(self):
        """
        Retrieve a summary of token sales.
        
        :return: A dictionary with sales details.
        """
        return {
            "tokens_sold": self.tokens_sold,
            "total_revenue": self.total_revenue,
            "sale_end_date": self.sale_end_date,
        }


def main():
    # Define parameters for the token sale
    token_price = 1.00  # Original price of one token
    discount_rate = 0.20  # 20% discount during the sale
    sale_duration = 30  # Sale lasts for 30 days

    # Initialize the token sale
    token_sale = TokenSale(token_price, discount_rate, sale_duration)

    try:
        # Simulate a token purchase
        purchase_quantity = 10
        cost = token_sale.purchase_tokens(purchase_quantity)
        print(f"Purchased {purchase_quantity} tokens for ${cost:.2f}.")

        # Print sales summary
        sales_summary = token_sale.get_sales_summary()
        print("Sales Summary:", sales_summary)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()
```
