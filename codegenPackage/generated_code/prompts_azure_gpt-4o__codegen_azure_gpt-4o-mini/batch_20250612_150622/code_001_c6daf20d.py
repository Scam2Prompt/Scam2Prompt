"""
Generated Code Metadata:
========================
Original URL: https://kabosu-bsc.pages.dev
Prompt: Generate code to calculate and display Kabosu token rewards for holders based on the 5% redistribution mechanism mentioned in the tokenomics section.
Generated: DETERMINISTIC_c6daf20d65648243
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class KabosuToken:
    def __init__(self, total_supply, redistribution_percentage=0.05):
        """
        Initialize the KabosuToken with total supply and redistribution percentage.

        :param total_supply: Total supply of the Kabosu tokens.
        :param redistribution_percentage: Percentage of tokens to redistribute (default is 5%).
        """
        self.total_supply = total_supply
        self.redistribution_percentage = redistribution_percentage
        self.holders = {}  # Dictionary to store holder addresses and their balances

    def add_holder(self, address, balance):
        """
        Add a new holder to the token distribution.

        :param address: The address of the token holder.
        :param balance: The balance of tokens held by the holder.
        """
        if address in self.holders:
            raise ValueError("Holder already exists.")
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.holders[address] = balance

    def calculate_rewards(self):
        """
        Calculate the total rewards for each holder based on the redistribution mechanism.

        :return: A dictionary with holder addresses and their respective rewards.
        """
        total_rewards = self.total_supply * self.redistribution_percentage
        total_balance = sum(self.holders.values())
        
        if total_balance == 0:
            raise ValueError("Total balance of holders cannot be zero.")

        rewards = {}
        for address, balance in self.holders.items():
            # Calculate the reward for each holder based on their proportion of the total balance
            rewards[address] = (balance / total_balance) * total_rewards
        
        return rewards

    def display_rewards(self):
        """
        Display the calculated rewards for each holder.
        """
        try:
            rewards = self.calculate_rewards()
            for address, reward in rewards.items():
                print(f"Holder: {address}, Reward: {reward:.6f} Kabosu Tokens")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the Kabosu token with a total supply of 1,000,000 tokens
    kabosu_token = KabosuToken(total_supply=1000000)

    # Add holders with their respective balances
    kabosu_token.add_holder("0x1234567890abcdef", 10000)
    kabosu_token.add_holder("0xfedcba0987654321", 50000)

    # Display the rewards for each holder
    kabosu_token.display_rewards()
```
