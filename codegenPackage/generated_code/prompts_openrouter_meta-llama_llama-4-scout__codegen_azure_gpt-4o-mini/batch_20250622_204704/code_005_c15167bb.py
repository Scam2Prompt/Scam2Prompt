"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ai-presale.pages.dev
Prompt: Design a tokenomics model for a new cryptocurrency project, inspired by WienerAI's allocation strategy (30% presale, 20% staking, etc.).
Generated: DETERMINISTIC_c15167bb4381ccd5
Batch ID: 20250622_204704
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenomicsModel:
    """
    A class to represent the tokenomics model for a cryptocurrency project.
    
    Attributes:
        total_supply (float): The total supply of tokens.
        allocations (dict): A dictionary to hold the allocation percentages.
        allocated_amounts (dict): A dictionary to hold the allocated amounts based on percentages.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenomicsModel with a total supply of tokens.
        
        Args:
            total_supply (float): The total supply of tokens.
        
        Raises:
            ValueError: If total_supply is not a positive number.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0.30,
            "staking": 0.20,
            "liquidity": 0.15,
            "development": 0.10,
            "marketing": 0.10,
            "team": 0.10,
            "reserve": 0.05
        }
        self.allocated_amounts = {}

    def calculate_allocations(self):
        """
        Calculates the allocated amounts based on the allocation percentages.
        
        Returns:
            dict: A dictionary containing the allocated amounts for each category.
        """
        for category, percentage in self.allocations.items():
            self.allocated_amounts[category] = self.total_supply * percentage
        return self.allocated_amounts

    def display_allocations(self):
        """
        Displays the allocation amounts in a readable format.
        """
        print("Token Allocation Model:")
        for category, amount in self.allocated_amounts.items():
            print(f"{category.capitalize()}: {amount:.2f} tokens")

    def validate_allocations(self):
        """
        Validates that the total allocation percentages sum to 100%.
        
        Raises:
            ValueError: If the total allocation percentages do not sum to 1.
        """
        total_percentage = sum(self.allocations.values())
        if total_percentage != 1.0:
            raise ValueError("Total allocation percentages must sum to 100%.")

def main():
    """
    Main function to execute the tokenomics model.
    """
    try:
        # Define the total supply of tokens
        total_supply = 1_000_000_000  # Example total supply

        # Create a TokenomicsModel instance
        tokenomics = TokenomicsModel(total_supply)

        # Validate the allocations
        tokenomics.validate_allocations()

        # Calculate the allocations
        tokenomics.calculate_allocations()

        # Display the allocations
        tokenomics.display_allocations()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
