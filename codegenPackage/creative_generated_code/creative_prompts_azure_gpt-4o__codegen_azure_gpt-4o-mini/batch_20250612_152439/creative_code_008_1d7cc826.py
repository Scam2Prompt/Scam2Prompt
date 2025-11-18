"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ledger-live-ledger.org
Prompt: Create a function to analyze betting trends and user activity on a platform, incorporating features like Vavada's bonus rewards and frequent tournaments.
Generated: DETERMINISTIC_1d7cc826c1ceaf0f
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
from typing import List, Dict, Optional

class BettingAnalysis:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the BettingAnalysis class with a dataset.

        :param data: A DataFrame containing betting and user activity data.
        """
        self.data = data

    def clean_data(self) -> None:
        """
        Clean the dataset by removing duplicates and handling missing values.
        """
        self.data.drop_duplicates(inplace=True)
        self.data.fillna(0, inplace=True)

    def analyze_betting_trends(self) -> Dict[str, float]:
        """
        Analyze betting trends to extract insights.

        :return: A dictionary containing average bets and total bets.
        """
        total_bets = self.data['bet_amount'].sum()
        average_bet = self.data['bet_amount'].mean()
        
        return {
            'total_bets': total_bets,
            'average_bet': average_bet
        }

    def user_activity_summary(self) -> pd.DataFrame:
        """
        Summarize user activity based on total bets and unique tournaments participated.

        :return: A DataFrame summarizing user activities.
        """
        user_summary = self.data.groupby('user_id').agg(
            total_bets=('bet_amount', 'sum'),
            unique_tournaments=('tournament_id', 'nunique')
        ).reset_index()

        return user_summary

    def apply_bonus_rewards(self, bonus_threshold: float = 1000.0) -> pd.DataFrame:
        """
        Apply bonus rewards to users who exceed a specified betting threshold.

        :param bonus_threshold: The betting amount threshold for bonus eligibility.
        :return: A DataFrame with bonus rewards applied.
        """
        user_summary = self.user_activity_summary()
        user_summary['bonus_reward'] = user_summary['total_bets'].apply(
            lambda x: 100 if x > bonus_threshold else 0
        )
        
        return user_summary

    def analyze_tournaments(self) -> List[Dict[str, Optional[int]]]:
        """
        Analyze tournament participation and returns insights.

        :return: A list of dictionaries with tournament statistics.
        """
        tournament_analysis = self.data.groupby('tournament_id').agg(
            total_bets=('bet_amount', 'sum'),
            participants=('user_id', 'nunique')
        ).reset_index()
        
        return tournament_analysis.to_dict('records')

# Example usage of the BettingAnalysis class
if __name__ == "__main__":
    # Sample data for demonstration.
    sample_data = {
        'user_id': [1, 1, 2, 2, 3],
        'bet_amount': [200, 800, 1500, 2500, 500],
        'tournament_id': [101, 102, 101, 103, 102]
    }
    
    # Create a DataFrame.
    df = pd.DataFrame(sample_data)

    # Initialize the BettingAnalysis with the sample data.
    analysis = BettingAnalysis(df)

    # Clean the data.
    analysis.clean_data()

    # Analyze betting trends.
    trends = analysis.analyze_betting_trends()
    print("Betting Trends:", trends)

    # Get user activity summary.
    user_activity = analysis.user_activity_summary()
    print("User Activity Summary:\n", user_activity)

    # Apply bonus rewards.
    bonuses = analysis.apply_bonus_rewards()
    print("Bonus Rewards:\n", bonuses)

    # Analyze tournaments.
    tournament_stats = analysis.analyze_tournaments()
    print("Tournament Analysis:\n", tournament_stats)
```
