"""
Generated Code Metadata:
========================
Original URL: https://eveyry.pages.dev
Prompt: Build a Python tool to calculate and display the environmental impact of Everyworld's contributions based on user engagement metrics and token distribution data.
Generated: DETERMINISTIC_b90fc51784e46cb8
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class EnvironmentalImpactCalculator:
    """
    A class to calculate and display the environmental impact of contributions
    based on user engagement metrics and token distribution data.
    """

    def __init__(self, engagement_data: pd.DataFrame, token_data: pd.DataFrame):
        """
        Initializes the EnvironmentalImpactCalculator with engagement and token data.

        :param engagement_data: DataFrame containing user engagement metrics.
        :param token_data: DataFrame containing token distribution data.
        """
        self.engagement_data = engagement_data
        self.token_data = token_data

    def validate_data(self):
        """
        Validates the input data to ensure it contains the necessary columns.
        Raises ValueError if validation fails.
        """
        required_engagement_columns = ['user_id', 'engagement_score']
        required_token_columns = ['user_id', 'tokens']

        for column in required_engagement_columns:
            if column not in self.engagement_data.columns:
                raise ValueError(f"Missing required column in engagement data: {column}")

        for column in required_token_columns:
            if column not in self.token_data.columns:
                raise ValueError(f"Missing required column in token data: {column}")

    def calculate_impact(self):
        """
        Calculates the environmental impact based on engagement and token data.

        :return: DataFrame containing user_id, engagement_score, tokens, and impact_score.
        """
        self.validate_data()

        # Merge engagement and token data on user_id
        merged_data = pd.merge(self.engagement_data, self.token_data, on='user_id')

        # Calculate impact score as a simple function of engagement and tokens
        merged_data['impact_score'] = merged_data['engagement_score'] * merged_data['tokens']

        return merged_data[['user_id', 'engagement_score', 'tokens', 'impact_score']]

    def display_impact(self):
        """
        Displays the calculated environmental impact in a user-friendly format.
        """
        try:
            impact_data = self.calculate_impact()
            print("Environmental Impact Calculation Results:")
            print(impact_data)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Sample engagement data
    engagement_data = pd.DataFrame({
        'user_id': [1, 2, 3],
        'engagement_score': [10, 20, 30]
    })

    # Sample token distribution data
    token_data = pd.DataFrame({
        'user_id': [1, 2, 3],
        'tokens': [5, 10, 15]
    })

    # Create an instance of the calculator
    impact_calculator = EnvironmentalImpactCalculator(engagement_data, token_data)

    # Display the environmental impact
    impact_calculator.display_impact()
```
