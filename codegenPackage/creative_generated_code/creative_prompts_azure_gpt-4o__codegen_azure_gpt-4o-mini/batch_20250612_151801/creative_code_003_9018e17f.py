"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Create an algorithm to calculate withdrawal eligibility based on the "to 5x bebas ip" rule described in the slot bonus system.
Generated: DETERMINISTIC_9018e17fcfb58bfa
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WithdrawalEligibility:
    """
    A class to determine withdrawal eligibility based on the 'to 5x bebas ip' rule.
    """

    def __init__(self, deposit_amount: float, bonus_amount: float):
        """
        Initializes the WithdrawalEligibility instance.

        :param deposit_amount: The total amount deposited by the user.
        :param bonus_amount: The total bonus amount received by the user.
        """
        self.deposit_amount = deposit_amount
        self.bonus_amount = bonus_amount

    def calculate_withdrawal_limit(self) -> float:
        """
        Calculates the maximum withdrawal limit based on the 'to 5x bebas ip' rule.

        :return: The maximum amount that can be withdrawn.
        """
        # The withdrawal limit is capped at 5 times the deposit amount
        return min(5 * self.deposit_amount, self.deposit_amount + self.bonus_amount)

    def is_withdrawal_eligible(self, withdrawal_amount: float) -> bool:
        """
        Determines if the user is eligible to withdraw a specific amount.

        :param withdrawal_amount: The amount the user wishes to withdraw.
        :return: True if the withdrawal is eligible, False otherwise.
        """
        # Validate the withdrawal amount
        if withdrawal_amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        
        withdrawal_limit = self.calculate_withdrawal_limit()
        
        # Check if the withdrawal amount does not exceed the withdrawal limit
        return withdrawal_amount <= withdrawal_limit

def main():
    """
    Main function to execute the withdrawal eligibility check
    """
    try:
        deposit = float(input("Enter your total deposit amount: "))
        bonus = float(input("Enter your total bonus amount: "))
        withdrawal_request = float(input("Enter the amount you wish to withdraw: "))
        
        eligibility_checker = WithdrawalEligibility(deposit, bonus)
        
        if eligibility_checker.is_withdrawal_eligible(withdrawal_request):
            print(f"You are eligible to withdraw ${withdrawal_request:.2f}.")
        else:
            print(f"You are not eligible to withdraw ${withdrawal_request:.2f}.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
