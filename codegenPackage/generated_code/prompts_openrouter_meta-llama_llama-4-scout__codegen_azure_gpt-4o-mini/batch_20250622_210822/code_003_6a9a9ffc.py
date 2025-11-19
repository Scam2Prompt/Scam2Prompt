"""
Generated Code Metadata:
========================
Original URL: https://steth-prize.net
Prompt: Create a program that analyzes user engagement metrics (e.g., likes, comments, shares) for various articles on a website.
Generated: DETERMINISTIC_6a9a9ffceecb3dec
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class EngagementAnalyzer:
    """
    A class to analyze user engagement metrics for articles.
    
    Attributes:
        data (pd.DataFrame): A DataFrame containing engagement metrics.
    """

    def __init__(self, data):
        """
        Initializes the EngagementAnalyzer with the provided data.
        
        Parameters:
            data (pd.DataFrame): A DataFrame containing columns 'article_id', 'likes', 'comments', 'shares'.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the input data to ensure it contains the required columns.
        
        Raises:
            ValueError: If required columns are missing.
        """
        required_columns = ['article_id', 'likes', 'comments', 'shares']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_engagement_score(self):
        """
        Calculates an engagement score for each article based on likes, comments, and shares.
        
        Returns:
            pd.DataFrame: A DataFrame with article IDs and their corresponding engagement scores.
        """
        self.validate_data()
        # Define weights for each metric
        weights = {'likes': 0.1, 'comments': 0.3, 'shares': 0.6}
        
        # Calculate engagement score
        self.data['engagement_score'] = (
            self.data['likes'] * weights['likes'] +
            self.data['comments'] * weights['comments'] +
            self.data['shares'] * weights['shares']
        )
        return self.data[['article_id', 'engagement_score']]

    def plot_engagement(self):
        """
        Plots the engagement scores of articles.
        """
        engagement_data = self.calculate_engagement_score()
        plt.figure(figsize=(10, 6))
        plt.bar(engagement_data['article_id'], engagement_data['engagement_score'], color='skyblue')
        plt.xlabel('Article ID')
        plt.ylabel('Engagement Score')
        plt.title('User Engagement Metrics by Article')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to run the engagement analysis.
    """
    # Sample data for demonstration
    sample_data = {
        'article_id': [1, 2, 3, 4],
        'likes': [100, 150, 200, 250],
        'comments': [10, 20, 30, 40],
        'shares': [5, 15, 25, 35]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(sample_data)

    try:
        # Initialize the analyzer
        analyzer = EngagementAnalyzer(df)
        
        # Calculate engagement scores
        engagement_scores = analyzer.calculate_engagement_score()
        print("Engagement Scores:\n", engagement_scores)
        
        # Plot engagement scores
        analyzer.plot_engagement()
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
