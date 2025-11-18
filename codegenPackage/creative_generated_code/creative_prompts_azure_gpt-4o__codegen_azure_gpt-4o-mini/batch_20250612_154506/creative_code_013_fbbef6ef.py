"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Write a Python script to calculate and distribute promotional bonuses based on user deposits, as outlined in VZ99's first deposit promotion.
Generated: DETERMINISTIC_fbbef6ef4ce23420
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class BonusCalculator:
    def __init__(self, deposit_data):
        """
        Initializes the BonusCalculator with deposit data.
        
        :param deposit_data: A pandas DataFrame containing user deposit information.
                             It should have columns ['user_id', 'deposit_amount'].
        """
        self.deposit_data = deposit_data
    
    def validate_data(self):
        """
        Validates the deposit data to ensure it has the required columns and valid values.
        
        :raises ValueError: If the data is invalid.
        """
        required_columns = ['user_id', 'deposit_amount']
        for col in required_columns:
            if col not in self.deposit_data.columns:
                raise ValueError(f"Missing required column: {col}")

        if self.deposit_data['deposit_amount'].isnull().any():
            raise ValueError("Deposit amounts contain null values.")
        if (self.deposit_data['deposit_amount'] < 0).any():
            raise ValueError("Deposit amounts must be non-negative.")

    def calculate_bonuses(self):
        """
        Calculates promotional bonuses based on user deposits.

        The bonus distribution criteria:
        - 10% bonus for deposits less than or equal to $1000
        - $100 flat bonus for deposits greater than $1000

        :return: A pandas DataFrame containing user_id and their respective bonuses.
        """
        # Create a copy of the deposit data to avoid modifying the original
        bonuses = self.deposit_data.copy()
        bonuses['bonus'] = bonuses['deposit_amount'].apply(self._determine_bonus)
        return bonuses[['user_id', 'bonus']]

    def _determine_bonus(self, deposit):
        """
        Determines the bonus amount based on the deposit amount.
        
        :param deposit: The deposit amount.
        :return: The calculated bonus.
        """
        if deposit <= 1000:
            return deposit * 0.10  # 10% bonus
        else:
            return 100  # Flat $100 bonus

    def distribute_bonuses(self):
        """
        Validates the data, calculates bonuses, and returns the bonus distribution.
        
        :return: A pandas DataFrame with user_id and their calculated bonuses.
        """
        self.validate_data()
        return self.calculate_bonuses()

if __name__ == "__main__":
    # Example deposit data
    data = {
        'user_id': [1, 2, 3, 4],
        'deposit_amount': [500, 1500, 1000, 2500]
    }

    # Convert data to DataFrame
    deposit_df = pd.DataFrame(data)

    try:
        # Initialize the BonusCalculator with the deposit data
        calculator = BonusCalculator(deposit_df)
        
        # Distribute bonuses and print the result
        bonus_distribution = calculator.distribute_bonuses()
        print(bonus_distribution)
        
    except ValueError as e:
        print(f"Error in processing bonuses: {e}")
```
