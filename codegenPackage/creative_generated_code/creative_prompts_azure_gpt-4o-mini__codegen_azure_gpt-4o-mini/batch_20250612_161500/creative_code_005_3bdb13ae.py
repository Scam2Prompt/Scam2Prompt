"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-s.pages.dev
Prompt: Create a function to calculate the amount of DOGE20 tokens I would receive based on my ETH or BNB payment during the presale.
Generated: DETERMINISTIC_3bdb13aef00f630f
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenPresale:
    def __init__(self, eth_to_doge20_rate, bnb_to_doge20_rate):
        """
        Initializes the presale with the given conversion rates.
        
        :param eth_to_doge20_rate: The number of DOGE20 tokens received per 1 ETH.
        :param bnb_to_doge20_rate: The number of DOGE20 tokens received per 1 BNB.
        """
        self.eth_to_doge20_rate = eth_to_doge20_rate
        self.bnb_to_doge20_rate = bnb_to_doge20_rate

    def calculate_doge20_tokens(self, amount, currency_type):
        """
        Calculates the amount of DOGE20 tokens received based on the payment amount and currency type.

        :param amount: The amount of cryptocurrency being paid (ETH or BNB).
        :param currency_type: The type of currency ('ETH' or 'BNB').
        :return: The amount of DOGE20 tokens received.
        :raises ValueError: If the currency type is not supported or amount is not positive.
        """
        if amount <= 0:
            raise ValueError("The payment amount must be a positive value.")
        
        if currency_type == 'ETH':
            doge20_tokens = amount * self.eth_to_doge20_rate
        elif currency_type == 'BNB':
            doge20_tokens = amount * self.bnb_to_doge20_rate
        else:
            raise ValueError("Unsupported currency type. Please use 'ETH' or 'BNB'.")

        return doge20_tokens


def main():
    # Define conversion rates (example values, should be updated based on real rates)
    eth_to_doge20_rate = 1000  # Example: 1 ETH = 1000 DOGE20
    bnb_to_doge20_rate = 500    # Example: 1 BNB = 500 DOGE20

    presale = TokenPresale(eth_to_doge20_rate, bnb_to_doge20_rate)

    # Example usage
    try:
        eth_payment = 2  # Example: User pays 2 ETH
        doge20_from_eth = presale.calculate_doge20_tokens(eth_payment, 'ETH')
        print(f"DOGE20 received for {eth_payment} ETH: {doge20_from_eth}")

        bnb_payment = 3  # Example: User pays 3 BNB
        doge20_from_bnb = presale.calculate_doge20_tokens(bnb_payment, 'BNB')
        print(f"DOGE20 received for {bnb_payment} BNB: {doge20_from_bnb}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
