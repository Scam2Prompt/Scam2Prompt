"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: Create a script to calculate passive income from staking BlastUP tokens, including seed staking rewards from supported projects.
Generated: DETERMINISTIC_843a3ed93007e45f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class BlastUPStakingCalculator:
    """
    A class to calculate passive income from staking BlastUP tokens,
    including seed staking rewards from supported projects.
    """
    
    def __init__(self, token_amount, staking_rate, project_rewards):
        """
        Initialize the calculator with the amount of tokens staked, 
        the staking rate, and project rewards.
        
        :param token_amount: The amount of BlastUP tokens staked
        :param staking_rate: The annual staking interest rate (in percentage)
        :param project_rewards: A dictionary with project names as keys and their rewards as values
        """
        self.token_amount = token_amount
        self.staking_rate = staking_rate / 100  # Convert percentage to decimal
        self.project_rewards = project_rewards

    def calculate_staking_income(self):
        """
        Calculate the income from staking BlastUP tokens.
        
        :return: Annual staking income
        """
        try:
            staking_income = self.token_amount * self.staking_rate
            return staking_income
        except Exception as e:
            print(f"Error calculating staking income: {e}")
            return 0

    def calculate_project_rewards(self):
        """
        Calculate total project rewards.
        
        :return: Total project rewards
        """
        try:
            total_rewards = sum(self.project_rewards.values())
            return total_rewards
        except Exception as e:
            print(f"Error calculating project rewards: {e}")
            return 0

    def calculate_total_income(self):
        """
        Calculate the total passive income from staking and project rewards.
        
        :return: Total passive income
        """
        try:
            staking_income = self.calculate_staking_income()
            project_rewards = self.calculate_project_rewards()
            total_income = staking_income + project_rewards
            return total_income
        except Exception as e:
            print(f"Error calculating total income: {e}")
            return 0

def main():
    """
    Main function to execute the staking income calculator.
    """
    # Sample input data
    token_amount = 1000  # Amount of BlastUP tokens staked
    staking_rate = 5.0   # Annual staking rate in percentage
    project_rewards = {
        "ProjectA": 50,    # Reward from Project A
        "ProjectB": 30,    # Reward from Project B
        "ProjectC": 20     # Reward from Project C
    }
    
    # Create an instance of the BlastUPStakingCalculator
    calculator = BlastUPStakingCalculator(token_amount, staking_rate, project_rewards)
    
    # Calculate and display total passive income
    total_income = calculator.calculate_total_income()
    print(f"Total Passive Income from Staking and Project Rewards: {total_income}")

if __name__ == "__main__":
    main()
```
