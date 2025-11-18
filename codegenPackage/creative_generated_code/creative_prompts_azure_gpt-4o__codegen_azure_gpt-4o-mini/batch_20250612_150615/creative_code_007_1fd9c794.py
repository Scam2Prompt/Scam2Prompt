"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://argoapp.live
Prompt: Recommend a library or tool for analyzing player engagement in online PC games, inspired by Argo App's article on fun games for leisure time.
Generated: DETERMINISTIC_1fd9c7942bb30c07
Batch ID: 20250612_150615
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
import matplotlib.pyplot as plt
import seaborn as sns

class PlayerEngagementAnalyzer:
    """
    A class to analyze player engagement in online PC games.
    
    Attributes:
        data (pd.DataFrame): A pandas DataFrame containing player engagement metrics.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the PlayerEngagementAnalyzer with player engagement data.
        
        Parameters:
            data (pd.DataFrame): A DataFrame containing columns such as 'player_id', 'play_time', and 'game_id'.
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocess the player engagement data by cleaning and handling missing values.
        """
        # Handle missing values by filling with zero
        self.data.fillna(0, inplace=True)

        # Ensure 'play_time' is numeric
        self.data['play_time'] = pd.to_numeric(self.data['play_time'], errors='coerce')

    def engagement_summary(self) -> pd.DataFrame:
        """
        Summarizes player engagement metrics.
        
        Returns:
            pd.DataFrame: A summary DataFrame with metrics such as average play time and total players.
        """
        summary = self.data.groupby('game_id').agg({
            'play_time': ['mean', 'sum', 'count']
        }).reset_index()
        
        summary.columns = ['game_id', 'average_play_time', 'total_play_time', 'total_players']
        return summary

    def visualize_engagement(self, summary: pd.DataFrame):
        """
        Visualizes player engagement metrics.
        
        Parameters:
            summary (pd.DataFrame): A summary DataFrame containing engagement metrics.
        """
        # Set the visual style
        sns.set(style="whitegrid")

        # Create a bar plot for average play time
        plt.figure(figsize=(12, 6))
        sns.barplot(x='game_id', y='average_play_time', data=summary)
        plt.title('Average Play Time per Game')
        plt.xlabel('Game ID')
        plt.ylabel('Average Play Time (hours)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run_analysis(self):
        """
        Executes the full analysis pipeline: preprocess, summarize, and visualize.
        """
        try:
            self.preprocess_data()
            summary = self.engagement_summary()
            self.visualize_engagement(summary)
        except Exception as e:
            print(f"An error occurred during the analysis: {e}")

# Example usage:
if __name__ == "__main__":
    # Sample data creation
    sample_data = {
        'player_id': [1, 2, 1, 3, 2, 1],
        'play_time': [2.5, 1.0, 3.5, None, 4.0, 2.0],
        'game_id': ['game1', 'game1', 'game2', 'game1', 'game2', 'game1']
    }
    player_data = pd.DataFrame(sample_data)

    # Initialize the analyzer
    analyzer = PlayerEngagementAnalyzer(player_data)
    # Run the analysis
    analyzer.run_analysis()
```
