"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pokemoney.info
Prompt: Create a function in Python to calculate promotional rewards for new users based on the UW99 "Nạp đầu nhận 888k" offer mentioned on https://pokemoney.info.
Generated: DETERMINISTIC_7fcaab120f1f0141
Batch ID: 20250612_151136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardCalculator:
    """
    Class to calculate promotional rewards for new users based on the UW99 'Nạp đầu nhận 888k' offer.
    """

    def __init__(self):
        # Constant value for the promotional reward
        self.promo_reward = 888000  # Reward amount in the base currency

    def calculate_reward(self, deposit_amount):
        """
        Calculate the promotional reward based on the deposit amount.

        Parameters:
        deposit_amount (float): The amount deposited by the new user.

        Returns:
        float: The calculated reward based on the deposit amount.
        """
        # Validate the deposit amount
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        # Determine the reward based on the deposit amount
        # For the sake of this example, assume:
        # - Deposit of 100k to 888k gets a reward of 888k
        # - Any deposit above 888k gets a reward capped at 888k
        if deposit_amount >= 100000:  # Minimum deposit to qualify for the reward
            return min(self.promo_reward, deposit_amount)
        else:
            return 0.0  # No reward for deposits less than 100k

def main():
    """
    Main function to execute the reward calculation.
    """
    calculator = RewardCalculator()
    
    try:
        # Example deposit amount for testing
        deposit = float(input("Enter the deposit amount: "))
        reward = calculator.calculate_reward(deposit)
        print(f"Calculated reward for a deposit of {deposit} is: {reward}")
    except ValueError as e:
        print(f"Error: {e}")  # Handle value errors, such as invalid deposit input

if __name__ == "__main__":
    main()
```
