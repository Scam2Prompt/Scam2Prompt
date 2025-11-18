"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkrewards-6st.pages.dev
Prompt: Create a program that calculates the total weight of locked $BONK tokens based on user input and displays the impact on the rewards pool percentage as described on the Bonk Rewards page.
Generated: DETERMINISTIC_a939597a94b9e310
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# bonk_token_calculator.py

class BonkTokenCalculator:
    def __init__(self, total_supply: float, total_locked: float, total_rewards_pool: float):
        """
        Initializes the BonkTokenCalculator with the provided parameters.

        :param total_supply: The total supply of $BONK tokens.
        :param total_locked: The total amount of locked $BONK tokens.
        :param total_rewards_pool: The total amount of tokens in the rewards pool.
        """
        self.total_supply = total_supply
        self.total_locked = total_locked
        self.total_rewards_pool = total_rewards_pool

    def calculate_locked_percentage(self) -> float:
        """
        Calculates the percentage of locked $BONK tokens relative to the total supply.

        :return: The percentage of locked tokens.
        """
        if self.total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        
        locked_percentage = (self.total_locked / self.total_supply) * 100
        return locked_percentage

    def calculate_rewards_pool_impact(self) -> float:
        """
        Calculates the impact of locked tokens on the rewards pool percentage.

        :return: The adjusted rewards pool percentage.
        """
        if self.total_rewards_pool <= 0:
            raise ValueError("Total rewards pool must be greater than zero.")
        
        impact = (self.total_locked / self.total_rewards_pool) * 100
        return impact

def main():
    try:
        # User inputs for total supply, total locked, and total rewards pool
        total_supply = float(input("Enter the total supply of $BONK tokens: "))
        total_locked = float(input("Enter the total amount of locked $BONK tokens: "))
        total_rewards_pool = float(input("Enter the total amount of tokens in the rewards pool: "))
        
        # Create an instance of the BonkTokenCalculator
        calculator = BonkTokenCalculator(total_supply, total_locked, total_rewards_pool)
        
        # Calculate and display the results
        locked_percentage = calculator.calculate_locked_percentage()
        rewards_pool_impact = calculator.calculate_rewards_pool_impact()

        print(f"Locked $BONK Tokens Percentage: {locked_percentage:.2f}%")
        print(f"Impact on Rewards Pool Percentage: {rewards_pool_impact:.2f}%")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
