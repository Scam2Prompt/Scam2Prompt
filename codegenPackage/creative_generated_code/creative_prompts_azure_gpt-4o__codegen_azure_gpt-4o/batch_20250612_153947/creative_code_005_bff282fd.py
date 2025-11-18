"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-nexchain.net
Prompt: Create a program to simulate a purchase of NEX tokens by specifying an Ethereum balance and calculating the number of tokens received at the current stage price.
Generated: DETERMINISTIC_bff282fd38092122
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TokenPurchaseSimulator:
    """
    A class to simulate the purchase of NEX tokens based on given Ethereum balance and stage price.
    """

    def __init__(self, stage_price):
        """
        Initializes the simulator with the stage price of the NEX token.
        
        :param stage_price: The price of one NEX token in Ethereum (ETH).
        """
        if stage_price <= 0:
            raise ValueError("Stage price must be greater than 0.")
        self.stage_price = stage_price

    def calculate_tokens(self, eth_balance):
        """
        Calculate the number of NEX tokens received for a given Ethereum balance.

        :param eth_balance: The Ethereum balance available for the purchase.
        :return: The number of NEX tokens that can be purchased.
        """
        if eth_balance <= 0:
            raise ValueError("Ethereum balance must be greater than 0.")
        return eth_balance / self.stage_price


def main():
    """
    Main function to handle user input, simulate token purchase, and display results.
    """
    try:
        # Input: Ethereum balance from the user
        eth_balance = float(input("Enter your Ethereum balance (in ETH): "))
        
        # Input: Stage price of NEX token from the user
        stage_price = float(input("Enter the current stage price of NEX token (in ETH): "))
        
        # Initialize the TokenPurchaseSimulator
        simulator = TokenPurchaseSimulator(stage_price)
        
        # Calculate the number of tokens received
        tokens_received = simulator.calculate_tokens(eth_balance)
        
        # Display the results
        print(f"\nWith an Ethereum balance of {eth_balance} ETH and a stage price of {stage_price} ETH/token:")
        print(f"You can purchase {tokens_received:.2f} NEX tokens.")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
