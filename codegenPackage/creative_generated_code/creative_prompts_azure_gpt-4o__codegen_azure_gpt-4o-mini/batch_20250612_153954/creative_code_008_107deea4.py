"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepetoken.network
Prompt: Create a script to calculate the token allocation percentages for marketing, rewards, development, and exchanges based on MIND of Pepe's tokenomics.
Generated: DETERMINISTIC_107deea40332ae93
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    def __init__(self, total_supply):
        """
        Initializes the Tokenomics class with the total supply of tokens.

        :param total_supply: Total number of tokens in circulation.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.allocations = {
            'marketing': 0.15,  # 15% for marketing
            'rewards': 0.20,    # 20% for rewards
            'development': 0.25,  # 25% for development
            'exchanges': 0.10    # 10% for exchanges
        }

    def calculate_allocations(self):
        """
        Calculates the token allocation for each category based on the total supply.

        :return: A dictionary containing the number of tokens allocated to each category.
        """
        allocation_results = {}
        
        for category, percentage in self.allocations.items():
            tokens_allocated = self.total_supply * percentage
            allocation_results[category] = tokens_allocated
        
        return allocation_results

def main():
    """
    Main function to execute the token allocation calculation.
    """
    try:
        # Define the total supply of tokens (example value)
        total_supply = 1_000_000_000  # Total supply of tokens
        
        # Create an instance of the Tokenomics class
        tokenomics = Tokenomics(total_supply)
        
        # Calculate token allocations
        allocations = tokenomics.calculate_allocations()
        
        # Print the allocation results
        for category, amount in allocations.items():
            print(f"{category.capitalize()} allocation: {amount:.2f} tokens")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
