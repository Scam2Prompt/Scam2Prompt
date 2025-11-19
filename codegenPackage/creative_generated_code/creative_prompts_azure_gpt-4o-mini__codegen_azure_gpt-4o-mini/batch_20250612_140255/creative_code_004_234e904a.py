"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbglobal-auth.me
Prompt: Create a function that evaluates the success rate of investment strategies used by financial consultants like Bryan Decker.
Generated: DETERMINISTIC_234e904a1e13e313
Batch ID: 20250612_140255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class InvestmentStrategyEvaluator:
    """
    A class to evaluate the success rate of investment strategies.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the InvestmentStrategyEvaluator with the provided data.

        :param data: A pandas DataFrame containing investment strategy performance data
                     with 'strategy_name', 'successful_investments', and 'total_investments' columns.
        """
        self.data = data

        # Validate the input data structure
        self._validate_data()

    def _validate_data(self):
        """ Validates the DataFrame structure for required columns. """
        required_columns = ['strategy_name', 'successful_investments', 'total_investments']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")
            if self.data[column].dtype not in [int, float]:
                raise TypeError(f"Column {column} must be of type int or float.")

    def evaluate_success_rate(self) -> pd.DataFrame:
        """
        Evaluates the success rate of each investment strategy.

        :return: A pandas DataFrame containing the strategy name and its success rate.
        """
        try:
            # Calculate success rate
            self.data['success_rate'] = self.data['successful_investments'] / self.data['total_investments']
            self.data['success_rate'].fillna(0, inplace=True)  # Handle division by zero

            # Select relevant columns for the result
            result = self.data[['strategy_name', 'success_rate']]
            return result

        except Exception as e:
            raise RuntimeError("An error occurred while evaluating success rates.") from e

# Example usage
if __name__ == "__main__":
    # Sample data for testing
    data = {
        'strategy_name': ['Strategy A', 'Strategy B', 'Strategy C'],
        'successful_investments': [10, 8, 0],
        'total_investments': [20, 10, 5]
    }
    df = pd.DataFrame(data)

    evaluator = InvestmentStrategyEvaluator(df)
    success_rates = evaluator.evaluate_success_rate()
    print(success_rates)
```
