"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbdfinancialsmig.pages.dev
Prompt: Develop a Python script to analyze the reward model for the Marketplace Gem/Reward system mentioned in the Q2 roadmap, including calculations for user incentives.
Generated: DETERMINISTIC_3d76b6f8b6dd4719
Batch ID: 20250612_151329
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

class MarketplaceRewardAnalyzer:
    """
    A class to analyze the reward model for a Marketplace Gem/Reward system.
    """

    def __init__(self, user_data):
        """
        Initializes the analyzer with user data.
        
        Parameters:
        user_data (pd.DataFrame): Dataframe containing user activity and earnings.
        """
        self.user_data = user_data
        self.user_data['reward'] = 0.0  # Initialize reward column

    def calculate_incentives(self):
        """
        Calculate user incentives based on their activity.
        Incentives are calculated based on predefined rules.
        """
        try:
            self.user_data['reward'] = np.where(
                self.user_data['activity_level'] >= 100,
                self.user_data['activity_level'] * 0.1,  # 10% reward for high activity
                self.user_data['activity_level'] * 0.05   # 5% reward for low activity
            )
        except KeyError as e:
            print(f"Error: Missing expected column in user data - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def summarize_rewards(self):
        """
        Summarize total rewards for each user.
        
        Returns:
        pd.DataFrame: A dataframe summarizing total rewards.
        """
        try:
            return self.user_data.groupby('user_id')['reward'].sum().reset_index()
        except KeyError as e:
            print(f"Error: Missing expected column in user data - {e}")
            return pd.DataFrame()  # Return empty DataFrame on error
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error

    def export_rewards(self, filename):
        """
        Export the rewards summary to a CSV file.
        
        Parameters:
        filename (str): The name of the file to save the rewards summary.
        """
        try:
            rewards_summary = self.summarize_rewards()
            rewards_summary.to_csv(filename, index=False)
            print(f"Rewards summary exported to {filename}")
        except Exception as e:
            print(f"Failed to export rewards summary: {e}")

# Example usage
if __name__ == "__main__":
    # Sample user data for demonstration
    data = {
        'user_id': [1, 2, 1, 2, 3],
        'activity_level': [120, 90, 150, 70, 200]
    }

    user_data = pd.DataFrame(data)

    # Create an instance of the reward analyzer
    analyzer = MarketplaceRewardAnalyzer(user_data)

    # Calculate incentives and export results
    analyzer.calculate_incentives()
    analyzer.export_rewards('rewards_summary.csv')
```
