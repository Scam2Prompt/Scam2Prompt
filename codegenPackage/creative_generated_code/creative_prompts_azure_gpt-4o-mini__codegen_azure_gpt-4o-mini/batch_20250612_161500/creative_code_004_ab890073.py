"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-ch9.pages.dev
Prompt: Describe the process of participating in the $ROOST presale and how the funds will be allocated according to the tokenomics.
Generated: DETERMINISTIC_ab890073e1b54716
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
$ROOST Presale Participation and Tokenomics Allocation

This script provides a simulation of the participation process in the $ROOST presale,
including the allocation of funds according to the specified tokenomics.
"""

class PresaleParticipation:
    def __init__(self, presale_amount, token_price):
        """
        Initializes the presale participation instance.

        Args:
            presale_amount (float): The amount of funds the participant is willing to invest.
            token_price (float): The price per token during the presale.
        """
        self.presale_amount = presale_amount
        self.token_price = token_price
        self.tokens_received = 0

    def participate(self):
        """
        Main method to handle participation in the presale.
        Calculates the number of tokens received based on the presale amount.
        """
        try:
            if self.presale_amount <= 0:
                raise ValueError("Presale amount must be greater than zero.")
            if self.token_price <= 0:
                raise ValueError("Token price must be greater than zero.")
                
            # Calculate the number of tokens received
            self.tokens_received = self.presale_amount / self.token_price
            
            print(f"Successfully participated in the presale.")
            print(f"Tokens received: {self.tokens_received:.2f} $ROOST")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

class Tokenomics:
    def __init__(self, total_supply, allocation):
        """
        Initializes the tokenomics instance.

        Args:
            total_supply (float): The total supply of $ROOST tokens.
            allocation (dict): A dictionary representing the allocation of funds.
        """
        self.total_supply = total_supply
        self.allocation = allocation

    def display_allocation(self):
        """
        Displays the allocation of funds according to the tokenomics.
        """
        print("Tokenomics Allocation:")
        for category, percentage in self.allocation.items():
            tokens = self.total_supply * (percentage / 100)
            print(f"{category}: {tokens:.2f} $ROOST")

# Example Usage
if __name__ == "__main__":
    # Define presale parameters
    presale_amount = 1000.0  # Amount the participant wants to invest
    token_price = 5.0        # Price per token during presale

    # Create an instance of presale participation
    presale_participant = PresaleParticipation(presale_amount, token_price)
    presale_participant.participate()

    # Define tokenomics parameters
    total_supply = 1000000.0  # Total supply of $ROOST tokens
    allocation = {
        "Development": 30,
        "Marketing": 20,
        "Liquidity": 20,
        "Community Rewards": 10,
        "Reserve": 20
    }

    # Create an instance of tokenomics
    tokenomics = Tokenomics(total_supply, allocation)
    tokenomics.display_allocation()
```
