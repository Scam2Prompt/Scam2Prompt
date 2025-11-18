"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Write Python code to analyze user interaction data from an online educational platform, focusing on engagement metrics like session duration and page views, as described in the КарьераОнлайн program.
Generated: DETERMINISTIC_14770c2b86dab9b0
Batch ID: 20250612_150651
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

class UserInteractionAnalyzer:
    """
    A class to analyze user interaction data from an online educational platform.
    It focuses on engagement metrics like session duration and page views.
    """

    def __init__(self, data_file):
        """
        Initializes the UserInteractionAnalyzer with the data from a specified CSV file.

        Args:
            data_file (str): Path to the CSV file containing user interaction data.
        """
        try:
            self.data = pd.read_csv(data_file)
            self._validate_data()
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")

    def _validate_data(self):
        """
        Validates the required structure and data types of the loaded DataFrame.
        Raises an error if the data is not as expected.
        """
        required_columns = ['user_id', 'session_duration', 'page_views', 'session_date']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")
        
        if not np.issubdtype(self.data['session_duration'].dtype, np.number):
            raise TypeError("session_duration must be numeric.")
        if not np.issubdtype(self.data['page_views'].dtype, np.number):
            raise TypeError("page_views must be numeric.")

    def calculate_engagement_metrics(self):
        """
        Calculates engagement metrics such as average session duration and total page views.
        
        Returns:
            dict: A dictionary containing the average session duration and total page views.
        """
        try:
            avg_session_duration = self.data['session_duration'].mean()
            total_page_views = self.data['page_views'].sum()
            return {
                'average_session_duration': avg_session_duration,
                'total_page_views': total_page_views
            }
        except Exception as e:
            raise RuntimeError(f"Error calculating engagement metrics: {e}")

    def session_statistics(self):
        """
        Provides session statistics, including counts and summaries.

        Returns:
            pd.DataFrame: A DataFrame containing user session statistics.
        """
        try:
            session_stats = self.data.groupby('user_id').agg(
                total_sessions=('session_duration', 'count'),
                avg_session_duration=('session_duration', 'mean'),
                total_page_views=('page_views', 'sum')
            ).reset_index()
            return session_stats
        except Exception as e:
            raise RuntimeError(f"Error generating session statistics: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        analyzer = UserInteractionAnalyzer('user_interaction_data.csv')
        engagement_metrics = analyzer.calculate_engagement_metrics()
        print("Engagement Metrics:", engagement_metrics)
        
        session_stats = analyzer.session_statistics()
        print("Session Statistics:\n", session_stats)
    except Exception as e:
        print(f"An error occurred: {e}")
```
