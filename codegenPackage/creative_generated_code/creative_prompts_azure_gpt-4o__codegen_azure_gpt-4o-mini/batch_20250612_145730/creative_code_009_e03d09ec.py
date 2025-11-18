"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dmax.site
Prompt: Write a program to calculate and display the maximum daily bonus for new members based on PANSOS4D's slot deposit promotion rules.
Generated: DETERMINISTIC_e03d09ecede20276
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PANSOS4D:
    def __init__(self):
        # Initialize the promotion rules
        self.deposit_bonus_rules = {
            '10000': 1000,  # Deposit 10,000 get 1,000 bonus
            '50000': 5000,  # Deposit 50,000 get 5,000 bonus
            '100000': 10000 # Deposit 100,000 get 10,000 bonus
        }

    def calculate_bonus(self, deposit_amount):
        """
        Calculate the maximum bonus based on the deposit amount.

        :param deposit_amount: The amount deposited by the new member
        :return: The maximum bonus that can be earned
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        
        # Initialize the maximum bonus
        max_bonus = 0
        
        # Iterate through the deposit rules to find applicable bonus
        for limit, bonus in self.deposit_bonus_rules.items():
            if deposit_amount >= int(limit):
                max_bonus = bonus
        
        return max_bonus

    def display_bonus(self, deposit_amount):
        """
        Display the calculated bonus for a given deposit amount.

        :param deposit_amount: The amount deposited by the new member
        """
        try:
            bonus = self.calculate_bonus(deposit_amount)
            print(f"For a deposit of {deposit_amount}, the maximum daily bonus is: {bonus}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    pansos4d = PANSOS4D()
    
    # Test deposit amounts
    test_deposits = [0, 9999, 10000, 50000, 100000, 150000, -100]
    
    for deposit in test_deposits:
        pansos4d.display_bonus(deposit)
```
