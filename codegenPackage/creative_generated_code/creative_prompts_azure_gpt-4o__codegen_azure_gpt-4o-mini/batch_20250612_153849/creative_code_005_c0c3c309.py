"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmkjdwoihjif.com
Prompt: Generate code to simulate the impact of airdropping 30% of a token supply to users, ensuring community ownership, as outlined in KittenSwap's ethos.
Generated: DETERMINISTIC_c0c3c309fba6b042
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Token:
    def __init__(self, total_supply):
        """
        Initialize the Token with a specified total supply.
        
        :param total_supply: Total number of tokens available.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.airdrop_percentage = 0.30  # 30% airdrop
        self.airdrop_amount = self.calculate_airdrop_amount()
        self.holders = {}  # Dictionary to hold user addresses and their token amounts

    def calculate_airdrop_amount(self):
        """
        Calculate the amount of tokens to be airdropped based on the total supply.
        
        :return: Amount of tokens to be airdropped.
        """
        return self.total_supply * self.airdrop_percentage

    def airdrop_tokens(self, user_addresses):
        """
        Airdrop tokens to a list of user addresses.

        :param user_addresses: List of user addresses to receive tokens.
        :raise ValueError: If no addresses are provided or if airdrop amount is insufficient.
        """
        if not user_addresses:
            raise ValueError("User addresses list cannot be empty.")
        
        if self.airdrop_amount <= 0:
            raise ValueError("Insufficient airdrop amount.")

        num_users = len(user_addresses)
        tokens_per_user = self.airdrop_amount / num_users

        for address in user_addresses:
            if address in self.holders:
                self.holders[address] += tokens_per_user
            else:
                self.holders[address] = tokens_per_user

        # After airdrop, we set the airdrop_amount to zero as it's fully distributed
        self.airdrop_amount = 0  

    def get_holder_balance(self, address):
        """
        Retrieve the balance of a given user address.
        
        :param address: User address to check the balance.
        :return: The token balance of the user.
        :raise KeyError: If the address does not exist in the holders.
        """
        if address not in self.holders:
            raise KeyError(f"No tokens found for address: {address}")
        return self.holders[address]


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the token with a total supply of 1,000,000 tokens
        token = Token(total_supply=1_000_000)

        # List of user addresses for the airdrop
        user_addresses = ["user1", "user2", "user3", "user4", "user5"]

        # Execute the airdrop
        token.airdrop_tokens(user_addresses)

        # Print the balance for each user
        for address in user_addresses:
            print(f"Balance of {address}: {token.get_holder_balance(address)} tokens")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
