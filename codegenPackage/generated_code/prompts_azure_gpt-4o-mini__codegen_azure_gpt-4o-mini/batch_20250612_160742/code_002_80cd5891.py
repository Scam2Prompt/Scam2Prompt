"""
Generated Code Metadata:
========================
Original URL: https://coingecko-ventures-evx.pages.dev
Prompt: Create a function that evaluates the financial metrics of blockchain startups, inspired by the investment strategies of CoinGecko Ventures.
Generated: DETERMINISTIC_80cd58913835a544
Batch ID: 20250612_160742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class BlockchainStartupEvaluator:
    """
    A class to evaluate financial metrics of blockchain startups.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the evaluator with a DataFrame containing startup data.

        :param data: A pandas DataFrame with columns ['name', 'funding', 'revenue', 'users', 'growth_rate']
        """
        self.data = data

    def validate_data(self):
        """
        Validates the input DataFrame to ensure it contains the required columns and correct data types.
        Raises ValueError if validation fails.
        """
        required_columns = ['name', 'funding', 'revenue', 'users', 'growth_rate']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")
        
        if not all(self.data['funding'].apply(lambda x: isinstance(x, (int, float)))):
            raise ValueError("Funding must be numeric.")
        if not all(self.data['revenue'].apply(lambda x: isinstance(x, (int, float)))):
            raise ValueError("Revenue must be numeric.")
        if not all(self.data['users'].apply(lambda x: isinstance(x, int))):
            raise ValueError("Users must be integers.")
        if not all(self.data['growth_rate'].apply(lambda x: isinstance(x, (int, float)))):
            raise ValueError("Growth rate must be numeric.")

    def calculate_metrics(self):
        """
        Calculates financial metrics for each startup and returns a DataFrame with the results.

        :return: A pandas DataFrame with the startup name and calculated metrics.
        """
        self.validate_data()
        
        # Calculate metrics
        self.data['revenue_per_user'] = self.data['revenue'] / self.data['users']
        self.data['funding_to_revenue_ratio'] = self.data['funding'] / self.data['revenue']
        
        # Select relevant columns for output
        metrics = self.data[['name', 'funding', 'revenue', 'users', 'growth_rate', 
                             'revenue_per_user', 'funding_to_revenue_ratio']]
        
        return metrics

    def evaluate_startups(self):
        """
        Evaluates the startups based on calculated metrics and returns a summary.

        :return: A summary DataFrame with startups ranked by revenue per user and funding to revenue ratio.
        """
        metrics = self.calculate_metrics()
        
        # Rank startups by revenue per user and funding to revenue ratio
        metrics['rank_revenue_per_user'] = metrics['revenue_per_user'].rank(ascending=False)
        metrics['rank_funding_to_revenue'] = metrics['funding_to_revenue_ratio'].rank(ascending=True)
        
        # Sort by revenue per user and then by funding to revenue ratio
        summary = metrics.sort_values(by=['rank_revenue_per_user', 'rank_funding_to_revenue'])
        
        return summary.reset_index(drop=True)

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = {
        'name': ['Startup A', 'Startup B', 'Startup C'],
        'funding': [1000000, 500000, 2000000],
        'revenue': [200000, 150000, 500000],
        'users': [1000, 500, 2000],
        'growth_rate': [0.1, 0.2, 0.15]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(sample_data)
    
    # Initialize the evaluator
    evaluator = BlockchainStartupEvaluator(df)
    
    # Evaluate startups and print the summary
    try:
        summary = evaluator.evaluate_startups()
        print(summary)
    except ValueError as e:
        print(f"Error: {e}")
```
