"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autobux.top
Prompt: Write a program to calculate the weekly contest results based on user activity data provided by the AUTOBUX platform.
Generated: DETERMINISTIC_d49124ad5e5b4eb9
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class ContestResultsCalculator:
    """
    A class to calculate weekly contest results based on user activity data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the ContestResultsCalculator with user activity data.

        :param data: A DataFrame containing user activity data with columns:
                     ['user_id', 'activity_score', 'timestamp']
        """
        self.data = data
        self.results = None

    def preprocess_data(self):
        """
        Preprocess the user activity data to ensure it's suitable for analysis.
        Removes any entries without user_id or activity_score.
        Also converts the timestamp to a datetime object.
        """
        try:
            # Ensure required columns are present
            required_columns = ['user_id', 'activity_score', 'timestamp']
            for col in required_columns:
                if col not in self.data.columns:
                    raise ValueError(f"Missing required column: {col}")

            # Drop rows with missing values in critical columns
            self.data.dropna(subset=['user_id', 'activity_score'], inplace=True)

            # Convert 'timestamp' to datetime
            self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
        except Exception as e:
            print(f"Error in preprocessing data: {e}")
            raise

    def calculate_weekly_results(self):
        """
        Calculates the weekly contest results by summing up the activity scores
        for each user per week.
        """
        try:
            # Group by user_id and week
            self.data['week'] = self.data['timestamp'].dt.to_period('W').apply(lambda r: r.start_time)
            self.results = (
                self.data.groupby(['user_id', 'week'])['activity_score']
                .sum()
                .reset_index()
                .rename(columns={'activity_score': 'total_score'})
            )
        except Exception as e:
            print(f"Error in calculating weekly results: {e}")
            raise

    def get_results(self) -> pd.DataFrame:
        """
        Returns the calculated results.

        :return: A DataFrame containing the weekly contest results.
        """
        if self.results is None:
            print("Results have not been calculated yet. Please run calculate_weekly_results() first.")
            return pd.DataFrame()
        return self.results

if __name__ == "__main__":
    # Sample data for testing
    data = {
        'user_id': ['user1', 'user2', 'user1', 'user1', 'user2'],
        'activity_score': [10, 20, 30, 5, 15],
        'timestamp': [
            '2023-10-01 10:00:00',
            '2023-10-02 11:00:00',
            '2023-10-04 12:00:00',
            '2023-10-08 14:00:00',
            '2023-10-09 15:00:00'
        ]
    }

    # Convert sample data to DataFrame
    user_activity_data = pd.DataFrame(data)

    # Create a ContestResultsCalculator instance
    calculator = ContestResultsCalculator(user_activity_data)

    # Preprocess the data
    calculator.preprocess_data()

    # Calculate weekly contest results
    calculator.calculate_weekly_results()

    # Get and print the results
    results = calculator.get_results()
    print(results)
```
