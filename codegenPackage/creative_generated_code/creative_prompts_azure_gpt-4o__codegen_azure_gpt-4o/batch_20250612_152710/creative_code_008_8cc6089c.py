"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-st.pages.dev
Prompt: Write a script to simulate the tokenomics allocation for $GBTC, including presale, staking rewards, marketing, liquidity, and community rewards.
Generated: DETERMINISTIC_8cc6089ca37f405b
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TokenomicsAllocation:
    """
    Class to handle the allocation of tokens for $GBTC.
    This simulates presale, staking rewards, marketing, liquidity, and community rewards.
    """
    
    def __init__(self, total_supply):
        """
        Initialize the TokenomicsAllocation class.

        :param total_supply: The total supply of tokens.
        """
        self.total_supply = total_supply
        self.allocation = {
            "presale": 0.0,
            "staking_rewards": 0.0,
            "marketing": 0.0,
            "liquidity": 0.0,
            "community_rewards": 0.0
        }

    def allocate_tokens(self, presale_pct, staking_rewards_pct, marketing_pct, liquidity_pct, community_rewards_pct):
        """
        Allocate tokens based on percentages provided.

        :param presale_pct: Percentage of total supply allocated for presale.
        :param staking_rewards_pct: Percentage of total supply allocated for staking rewards.
        :param marketing_pct: Percentage of total supply allocated for marketing.
        :param liquidity_pct: Percentage of total supply allocated for liquidity.
        :param community_rewards_pct: Percentage of total supply allocated for community rewards.
        :raises ValueError: If the total percentage exceeds 100%.
        """
        total_percentage = (presale_pct + staking_rewards_pct + 
                            marketing_pct + liquidity_pct + community_rewards_pct)

        if total_percentage > 100:
            raise ValueError("Total allocation percentage cannot exceed 100%.")
        
        # Calculate allocations
        self.allocation["presale"] = self.total_supply * (presale_pct / 100)
        self.allocation["staking_rewards"] = self.total_supply * (staking_rewards_pct / 100)
        self.allocation["marketing"] = self.total_supply * (marketing_pct / 100)
        self.allocation["liquidity"] = self.total_supply * (liquidity_pct / 100)
        self.allocation["community_rewards"] = self.total_supply * (community_rewards_pct / 100)

    def get_allocation(self):
        """
        Retrieve the current token allocation.

        :return: A dictionary containing token allocations.
        """
        return self.allocation

    def save_allocation_to_file(self, filename):
        """
        Save the allocation to a JSON file.

        :param filename: The name of the file to save the allocation.
        :raises IOError: If there's an issue with file writing.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.allocation, file, indent=4)
        except IOError as e:
            print(f"Error saving allocation to file: {e}")
            raise

# Main execution
if __name__ == "__main__":
    # Example usage: Simulate $GBTC tokenomics with a total supply of 1,000,000 tokens
    total_supply = 1_000_000

    # Instantiate the TokenomicsAllocation class
    tokenomics = TokenomicsAllocation(total_supply)

    # Configure allocation percentages
    try:
        tokenomics.allocate_tokens(
            presale_pct=20,        # 20% for presale
            staking_rewards_pct=30, # 30% for staking rewards
            marketing_pct=15,      # 15% for marketing
            liquidity_pct=25,      # 25% for liquidity
            community_rewards_pct=10 # 10% for community rewards
        )

        # Display allocation summary
        print("Token Allocation Summary:")
        allocation = tokenomics.get_allocation()
        for category, amount in allocation.items():
            print(f"{category.capitalize()}: {amount:.2f} tokens")

        # Save allocation to file
        tokenomics.save_allocation_to_file("tokenomics_allocation.json")
        print("\nAllocation successfully saved to 'tokenomics_allocation.json'.")
    except ValueError as ve:
        print(f"Allocation error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
