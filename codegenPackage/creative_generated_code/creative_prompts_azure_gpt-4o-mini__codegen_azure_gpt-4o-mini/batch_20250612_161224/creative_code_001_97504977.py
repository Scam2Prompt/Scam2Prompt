"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qna3ai.web.app
Prompt: Write a Python script to analyze user engagement metrics for trending questions on a platform like QnA3.
Generated: DETERMINISTIC_9750497714cac992
Batch ID: 20250612_161224
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

class EngagementAnalyzer:
    """
    A class to analyze user engagement metrics for trending questions.
    
    Attributes:
        data (pd.DataFrame): A DataFrame containing the engagement data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the EngagementAnalyzer with engagement data.

        Parameters:
            data (pd.DataFrame): Engagement data with columns ['question_id', 'views', 'likes', 'comments', 'shares'].
        """
        self.data = data
        
        # Ensure the data contains the required columns
        required_columns = ['question_id', 'views', 'likes', 'comments', 'shares']
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Missing required column: {col}")

    def calculate_engagement_score(self):
        """
        Calculates an engagement score based on views, likes, comments, and shares.
        The engagement score is calculated as a weighted sum of these metrics.
        """
        self.data['engagement_score'] = (self.data['likes'] * 2 +
                                          self.data['comments'] * 4 +
                                          self.data['shares'] * 3)
        return self.data[['question_id', 'engagement_score']]

    def plot_engagement_scores(self):
        """
        Plots the engagement scores for the questions.
        """
        plt.figure(figsize=(10, 6))
        sns.barplot(data=self.data.sort_values(by='engagement_score', ascending=False),
                     x='question_id', y='engagement_score', palette='viridis')
        plt.xticks(rotation=45)
        plt.title('Engagement Scores for Trending Questions')
        plt.xlabel('Question ID')
        plt.ylabel('Engagement Score')
        plt.tight_layout()
        plt.show()

    def get_top_engaged_questions(self, top_n=5):
        """
        Returns the top N questions based on engagement score.

        Parameters:
            top_n (int): Number of top questions to return.

        Returns:
            pd.DataFrame: Top N questions based on engagement score.
        """
        top_questions = self.data.nlargest(top_n, 'engagement_score')
        return top_questions[['question_id', 'engagement_score']]

def main():
    # Example engagement data
    data_dict = {
        'question_id': [1, 2, 3, 4, 5],
        'views': [120, 150, 90, 200, 300],
        'likes': [10, 20, 5, 40, 60],
        'comments': [2, 5, 1, 8, 12],
        'shares': [1, 3, 0, 5, 7],
    }
    
    # Create DataFrame
    engagement_data = pd.DataFrame(data_dict)
    
    try:
        # Analyze engagement metrics
        analyzer = EngagementAnalyzer(engagement_data)
        analyzer.calculate_engagement_score()
        print("Top Engaged Questions:\n", analyzer.get_top_engaged_questions())
        analyzer.plot_engagement_scores()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
