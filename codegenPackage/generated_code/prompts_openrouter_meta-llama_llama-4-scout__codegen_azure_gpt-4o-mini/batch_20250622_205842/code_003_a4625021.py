"""
Generated Code Metadata:
========================
Original URL: https://memelordprojects.pages.dev
Prompt: Explain the tokenomics of a cryptocurrency project with no taxes and no BS, and provide an example of a project with similar characteristics, such as the Memelord Project.
Generated: DETERMINISTIC_a4625021af3f4415
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tokenomics:
    """
    A class to represent the tokenomics of a cryptocurrency project.
    
    Attributes:
        name (str): The name of the cryptocurrency project.
        total_supply (int): The total supply of tokens.
        circulating_supply (int): The circulating supply of tokens.
        holders (dict): A dictionary to track token holders and their balances.
    """

    def __init__(self, name, total_supply):
        """
        Initializes the Tokenomics class with the project name and total supply.
        
        Args:
            name (str): The name of the cryptocurrency project.
            total_supply (int): The total supply of tokens.
        """
        self.name = name
        self.total_supply = total_supply
        self.circulating_supply = 0
        self.holders = {}

    def add_holder(self, address, amount):
        """
        Adds a new holder to the project and updates the circulating supply.
        
        Args:
            address (str): The address of the token holder.
            amount (int): The amount of tokens to assign to the holder.
        
        Raises:
            ValueError: If the amount exceeds the available supply.
        """
        if amount + self.circulating_supply > self.total_supply:
            raise ValueError("Amount exceeds available supply.")
        
        self.holders[address] = self.holders.get(address, 0) + amount
        self.circulating_supply += amount

    def remove_holder(self, address, amount):
        """
        Removes a specified amount of tokens from a holder and updates the circulating supply.
        
        Args:
            address (str): The address of the token holder.
            amount (int): The amount of tokens to remove from the holder.
        
        Raises:
            ValueError: If the holder does not have enough tokens.
        """
        if address not in self.holders or self.holders[address] < amount:
            raise ValueError("Holder does not have enough tokens.")
        
        self.holders[address] -= amount
        self.circulating_supply -= amount

    def get_holder_balance(self, address):
        """
        Returns the balance of a specified holder.
        
        Args:
            address (str): The address of the token holder.
        
        Returns:
            int: The balance of the holder.
        """
        return self.holders.get(address, 0)

    def get_total_supply(self):
        """
        Returns the total supply of tokens.
        
        Returns:
            int: The total supply of tokens.
        """
        return self.total_supply

    def get_circulating_supply(self):
        """
        Returns the circulating supply of tokens.
        
        Returns:
            int: The circulating supply of tokens.
        """
        return self.circulating_supply


# Example usage of the Tokenomics class
if __name__ == "__main__":
    try:
        # Create a new tokenomics instance for a project
        memelord_project = Tokenomics("Memelord Project", 1000000)

        # Add holders
        memelord_project.add_holder("0x123", 50000)
        memelord_project.add_holder("0x456", 150000)

        # Display total and circulating supply
        print(f"Total Supply: {memelord_project.get_total_supply()}")
        print(f"Circulating Supply: {memelord_project.get_circulating_supply()}")

        # Check holder balances
        print(f"Balance of 0x123: {memelord_project.get_holder_balance('0x123')}")
        print(f"Balance of 0x456: {memelord_project.get_holder_balance('0x456')}")

        # Remove tokens from a holder
        memelord_project.remove_holder("0x123", 20000)
        print(f"New Balance of 0x123: {memelord_project.get_holder_balance('0x123')}")

    except ValueError as e:
        print(f"Error: {e}")
```
