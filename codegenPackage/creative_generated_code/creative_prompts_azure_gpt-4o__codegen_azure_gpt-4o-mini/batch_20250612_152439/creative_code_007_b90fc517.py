"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveyry.pages.dev
Prompt: Build a Python tool to calculate and display the environmental impact of Everyworld's contributions based on user engagement metrics and token distribution data.
Generated: DETERMINISTIC_b90fc51784e46cb8
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class EnvironmentalImpactCalculator:
    """
    A tool to calculate and display the environmental impact of Everyworld's contributions
    based on user engagement metrics and token distribution data.
    """

    def __init__(self, engagement_data: pd.DataFrame, token_data: pd.DataFrame):
        """
        Initializes the calculator with engagement and token data.
        
        Parameters:
            engagement_data (pd.DataFrame): DataFrame containing user engagement metrics.
            token_data (pd.DataFrame): DataFrame containing token distribution data.
        """
        self.engagement_data = engagement_data
        self.token_data = token_data

    def validate_data(self):
        """
        Validates the input data for required columns and data types.
        
        Raises:
            ValueError: If the data is not valid.
        """
        required_engagement_columns = ['user_id', 'engagement_score']
        required_token_columns = ['user_id', 'tokens']

        if not all(col in self.engagement_data.columns for col in required_engagement_columns):
            raise ValueError("Engagement data must contain columns: " + ", ".join(required_engagement_columns))
        
        if not all(col in self.token_data.columns for col in required_token_columns):
            raise ValueError("Token data must contain columns: " + ", ".join(required_token_columns))

    def calculate_impact(self) -> pd.DataFrame:
        """
        Calculates the environmental impact based on engagement metrics and token distribution.
        
        Returns:
            pd.DataFrame: A DataFrame containing user_id, engagement_score, tokens, and impact_score.
        """
        self.validate_data()

        # Merging engagement metrics with token distribution data
        merged_data = pd.merge(self.engagement_data, self.token_data, on='user_id', how='inner')
        
        # Calculate impact score as a function of engagement and token distribution
        merged_data['impact_score'] = np.sqrt(merged_data['engagement_score'] * merged_data['tokens'])

        return merged_data[['user_id', 'engagement_score', 'tokens', 'impact_score']]

    def display_impact(self):
        """
        Displays the calculated environmental impact in a user-friendly format.
        """
        impact_data = self.calculate_impact()
        
        print("Environmental Impact of Everyworld's Contributions:")
        print("=" * 45)
        print(impact_data.to_string(index=False))

def main():
    # Sample data for engagement and token distribution
    engagement_data = pd.DataFrame({
        'user_id': [1, 2, 3],
        'engagement_score': [10, 20, 15]
    })

    token_data = pd.DataFrame({
        'user_id': [1, 2, 3],
        'tokens': [50, 80, 60]
    })

    try:
        # Create impact calculator instance
        calculator = EnvironmentalImpactCalculator(engagement_data, token_data)

        # Display environmental impact
        calculator.display_impact()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
