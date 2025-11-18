"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burnfi.pages.dev
Prompt: Write a Python script to simulate the minting process of $build tokens based on the burn value of $burn tokens, including the reflection mechanism for existing $build holders.
Generated: DETERMINISTIC_6adf6da4ed6da9cb
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenMintingSimulation:
    def __init__(self):
        self.burn_tokens = 0  # Total $burn tokens that have been burned
        self.build_holders = {}  # Dictionary to track $build holders and their balances
        self.total_build_supply = 0  # Total supply of $build tokens

    def mint_build_tokens(self, burn_value):
        """
        Simulate the minting process of $build tokens based on the burn value of $burn tokens.
        
        Args:
            burn_value (float): The amount of $burn tokens that are being burned to mint $build tokens.

        Raises:
            ValueError: If burn_value is not positive.
        """
        if burn_value <= 0:
            raise ValueError("Burn value must be positive.")

        # Calculate the number of $build tokens to mint (1:1 for simplicity)
        build_tokens_to_mint = burn_value
        
        # Update burn tokens
        self.burn_tokens += burn_value
        
        # Mint new $build tokens
        self.total_build_supply += build_tokens_to_mint
        
        # Distribute reflection to existing $build holders
        self.distribute_reflection(build_tokens_to_mint)
        
        print(f"Minted {build_tokens_to_mint} $build tokens from {burn_value} $burn tokens.")
        
    def distribute_reflection(self, minted_amount):
        """
        Distribute reflection to existing $build holders based on the amount minted.
        
        Args:
            minted_amount (float): The amount of $build tokens minted.
        """
        if not self.build_holders:
            print("No $build holders to distribute reflection.")
            return
        
        for holder, balance in self.build_holders.items():
            reflection_amount = (balance / self.total_build_supply) * minted_amount
            self.build_holders[holder] += reflection_amount
            print(f"Distributed {reflection_amount} $build tokens to holder {holder}.")

    def add_holder(self, holder, amount):
        """
        Add a new holder or update an existing holder's balance.
        
        Args:
            holder (str): The address or identifier of the $build holder.
            amount (float): The amount of $build tokens to add.
        """
        if holder in self.build_holders:
            self.build_holders[holder] += amount
        else:
            self.build_holders[holder] = amount
        
        print(f"Added {amount} $build tokens to holder {holder}. New balance: {self.build_holders[holder]}.")

    def get_holder_balance(self, holder):
        """
        Retrieve the balance of a specific $build holder.
        
        Args:
            holder (str): The address or identifier of the $build holder.

        Returns:
            float: The balance of the holder or 0 if not found.
        """
        return self.build_holders.get(holder, 0.0)

    def get_total_minted(self):
        """
        Get the total amount of $build tokens minted.
        
        Returns:
            float: The total supply of $build tokens.
        """
        return self.total_build_supply


# Example usage of TokenMintingSimulation
if __name__ == "__main__":
    simulation = TokenMintingSimulation()
    
    # Add initial holders with some $build token balances
    simulation.add_holder("holder1", 100)
    simulation.add_holder("holder2", 200)
    
    # Simulate burning $burn tokens to mint $build tokens
    try:
        simulation.mint_build_tokens(50)  # Burn 50 $burn tokens
    except ValueError as e:
        print(f"Error: {e}")
    
    # Check holders' balances
    print(f"Holder1 balance: {simulation.get_holder_balance('holder1')}")
    print(f"Holder2 balance: {simulation.get_holder_balance('holder2')}")
    print(f"Total minted $build tokens: {simulation.get_total_minted()}")
```
