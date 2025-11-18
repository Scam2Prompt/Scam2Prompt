"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-pogai.com
Prompt: Explain how to implement a presale system for cryptocurrency tokens, using the $POGAI token distribution process as an example.
Generated: DETERMINISTIC_ab981c3036fb8d92
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Define a presale system for cryptocurrency tokens
class PresaleSystem:
    def __init__(self, token_name, total_supply, presale_price, hard_cap):
        """
        Initialize the presale system.

        :param token_name: The name of the token being sold.
        :param total_supply: The total number of tokens available for sale.
        :param presale_price: The price per token during the presale.
        :param hard_cap: The maximum amount of funds that can be raised.
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.presale_price = presale_price
        self.hard_cap = hard_cap
        
        self.tokens_sold = 0
        self.funds_raised = 0
        self.participants = {}

    def buy_tokens(self, participant, amount):
        """
        Handle the purchase of tokens by a participant.

        :param participant: The address of the participant buying tokens.
        :param amount: The amount of tokens the participant wants to buy.
        :raises ValueError: If the purchase amount exceeds the available tokens or hard cap.
        """
        # Calculate the total cost for the requested amount of tokens
        total_cost = amount * self.presale_price
        
        # Check if the purchase does not exceed the hard cap
        if self.funds_raised + total_cost > self.hard_cap:
            raise ValueError("Purchase exceeds hard cap")

        # Check if there are enough tokens available
        if self.tokens_sold + amount > self.total_supply:
            raise ValueError("Not enough tokens available for sale")

        # Update the state of the presale
        if participant in self.participants:
            self.participants[participant] += amount
        else:
            self.participants[participant] = amount
        
        self.tokens_sold += amount
        self.funds_raised += total_cost

        print(f"{amount} tokens sold to {participant}. Total funds raised: {self.funds_raised}")

    def get_presale_info(self):
        """
        Get the current status of the presale.

        :return: A dictionary containing presale information.
        """
        return {
            "token_name": self.token_name,
            "total_supply": self.total_supply,
            "tokens_sold": self.tokens_sold,
            "funds_raised": self.funds_raised,
            "presale_price": self.presale_price,
            "hard_cap": self.hard_cap,
            "participants": self.participants
        }

# Example usage
if __name__ == "__main__":
    # Initialize the presale for $POGAI token
    try:
        presale = PresaleSystem(token_name="$POGAI", total_supply=1000000, presale_price=0.1, hard_cap=100000)
        
        # Simulate participants buying tokens
        presale.buy_tokens('0xParticipantA', 5000)
        presale.buy_tokens('0xParticipantB', 2000)
        
        # Print presale information
        print(presale.get_presale_info())
        
    except ValueError as e:
        print(f"Error: {e}")
```
