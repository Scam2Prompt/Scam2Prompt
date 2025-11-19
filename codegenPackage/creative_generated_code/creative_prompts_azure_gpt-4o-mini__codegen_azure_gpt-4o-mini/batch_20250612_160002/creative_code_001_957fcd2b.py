"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepearab.pages.dev
Prompt: Write a function to calculate the amount of $PEAB tokens received when swapping ETH, BNB, or USDT based on the exchange rates mentioned in the PepeArab presale details.
Generated: DETERMINISTIC_957fcd2b2ade1603
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenSwap:
    def __init__(self):
        # Define the exchange rates for swapping
        self.exchange_rates = {
            'ETH': 1000,  # 1 ETH = 1000 PEAB
            'BNB': 500,   # 1 BNB = 500 PEAB
            'USDT': 200    # 1 USDT = 200 PEAB
        }

    def calculate_peab_tokens(self, amount, token_type):
        """
        Calculate the amount of PEAB tokens received for a given amount of cryptocurrency.

        Args:
            amount (float): The amount of the token being swapped.
            token_type (str): The type of token being swapped ('ETH', 'BNB', or 'USDT').

        Returns:
            float: The amount of PEAB tokens received.

        Raises:
            ValueError: If the token_type is invalid or amount is non-positive.
        """
        # Validate inputs
        if token_type not in self.exchange_rates:
            raise ValueError(f"Invalid token type: {token_type}. Must be one of {list(self.exchange_rates.keys())}.")
        
        if amount <= 0:
            raise ValueError("Amount must be a positive value.")

        # Calculate the amount of PEAB tokens
        peab_tokens = amount * self.exchange_rates[token_type]
        return peab_tokens

# Example usage
if __name__ == "__main__":
    swap = TokenSwap()
    
    try:
        # Example: Swap 0.5 ETH
        eth_amount = 0.5
        received_tokens = swap.calculate_peab_tokens(eth_amount, 'ETH')
        print(f"Received {received_tokens} PEAB tokens for {eth_amount} ETH.")
        
        # Example: Swap 2 BNB
        bnb_amount = 2
        received_tokens = swap.calculate_peab_tokens(bnb_amount, 'BNB')
        print(f"Received {received_tokens} PEAB tokens for {bnb_amount} BNB.")
        
        # Example: Swap 100 USDT
        usdt_amount = 100
        received_tokens = swap.calculate_peab_tokens(usdt_amount, 'USDT')
        print(f"Received {received_tokens} PEAB tokens for {usdt_amount} USDT.")
        
    except ValueError as e:
        print(f"Error: {e}")
```
