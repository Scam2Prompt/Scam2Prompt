"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bi-verse.org
Prompt: Write a Python function that calculates potential returns on multi-asset investments based on the strategies outlined by bi-verse.org.
Generated: DETERMINISTIC_2cb6c625f98a0259
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class InvestmentCalculator:
    """
    A class to calculate potential returns on multi-asset investments based on specified strategies.
    """

    def __init__(self, investment_data):
        """
        Initializes the InvestmentCalculator with investment data.

        Parameters:
        investment_data (pd.DataFrame): A DataFrame containing investment assets with their respective returns.
        """
        self.investment_data = investment_data

    def validate_data(self):
        """
        Validates the investment data to ensure it contains necessary fields and data types.
        
        Raises:
        ValueError: If the input data is missing required fields or has incorrect data types.
        """
        required_columns = ['Asset', 'ExpectedReturn']
        
        # Check if all required columns are present
        for col in required_columns:
            if col not in self.investment_data.columns:
                raise ValueError(f'Missing required column: {col}')
        
        # Check if ExpectedReturn column contains numeric data
        if not np.issubdtype(self.investment_data['ExpectedReturn'].dtype, np.number):
            raise ValueError('ExpectedReturn column must contain numeric data.')
    
    def calculate_total_expected_return(self, weights):
        """
        Calculates the expected return of the investment portfolio based on asset weights.

        Parameters:
        weights (dict): A dictionary with asset names as keys and their respective weights as values.

        Returns:
        float: The total expected return of the portfolio.

        Raises:
        ValueError: If the total weight is not equal to 1 or if weights do not match the assets.
        """
        # Validate weights
        if not np.isclose(sum(weights.values()), 1):
            raise ValueError('Total weight must equal 1.')

        # Calculate expected return
        total_return = 0
        for asset, weight in weights.items():
            if asset not in self.investment_data['Asset'].values:
                raise ValueError(f'Asset {asset} not found in investment data.')

            asset_return = self.investment_data.loc[self.investment_data['Asset'] == asset, 'ExpectedReturn'].values[0]
            total_return += asset_return * weight
        
        return total_return

# Example usage
if __name__ == "__main__":
    # Sample investment data
    data = {
        'Asset': ['Stock A', 'Stock B', 'Bond A', 'Bond B'],
        'ExpectedReturn': [0.08, 0.06, 0.03, 0.04]
    }
    investment_df = pd.DataFrame(data)

    # Create an instance of InvestmentCalculator
    calculator = InvestmentCalculator(investment_df)

    try:
        # Validate investment data
        calculator.validate_data()

        # Define asset weights for the portfolio
        weights = {
            'Stock A': 0.5,
            'Stock B': 0.3,
            'Bond A': 0.1,
            'Bond B': 0.1
        }
        
        # Calculate the total expected return of the portfolio
        expected_return = calculator.calculate_total_expected_return(weights)
        print(f'The expected return of the portfolio is: {expected_return:.2%}')
    
    except ValueError as e:
        print(f'Error: {e}')
```
