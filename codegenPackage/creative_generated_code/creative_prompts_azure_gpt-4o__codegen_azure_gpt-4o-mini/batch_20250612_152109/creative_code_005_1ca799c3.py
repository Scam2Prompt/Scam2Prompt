"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-humanizedai.web.app
Prompt: Write code for calculating the number of tokens a user should receive based on the price of 1 HMZ token in USDT, as described on the HumanizedAi presale page.
Generated: DETERMINISTIC_1ca799c3eda0e7bc
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenCalculator:
    def __init__(self, token_price_usdt):
        """
        Initializes the TokenCalculator with the price of one HMZ token in USDT.
        
        :param token_price_usdt: Price of one HMZ token in USDT
        """
        if token_price_usdt <= 0:
            raise ValueError("Token price must be greater than zero.")
        
        self.token_price_usdt = token_price_usdt

    def calculate_tokens(self, investment_usdt):
        """
        Calculates the number of HMZ tokens a user should receive based on their investment in USDT.
        
        :param investment_usdt: Amount of USDT the user wants to invest
        :return: Number of HMZ tokens the user receives
        """
        if investment_usdt < 0:
            raise ValueError("Investment amount cannot be negative.")
        
        # Calculate the number of tokens
        tokens = investment_usdt / self.token_price_usdt
        
        return tokens

def main():
    try:
        # Example HMZ token price in USDT
        hmz_token_price = 0.05  # Example price for one HMZ token
        calculator = TokenCalculator(hmz_token_price)
        
        # User's investment amount in USDT
        investment_amount = 10  # Example investment
        tokens_received = calculator.calculate_tokens(investment_amount)
        
        print(f"Tokens received for {investment_amount} USDT: {tokens_received:.2f} HMZ")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
