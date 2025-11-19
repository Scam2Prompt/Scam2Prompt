"""
Generated Code Metadata:
========================
Original URL: https://ifesty.com.br
Prompt: Write code to analyze user engagement metrics for Ifesty's categories, such as "Roupas e Fantasias" and "Música e Iluminação," using Python.
Generated: DETERMINISTIC_9257b00d852348c9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from typing import Dict, List

class UserEngagementAnalyzer:
    """
    Analyzes user engagement metrics for Ifesty's categories.

    Attributes:
    - data (pd.DataFrame): DataFrame containing user engagement metrics.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the UserEngagementAnalyzer with user engagement data.

        Args:
        - data (pd.DataFrame): DataFrame containing user engagement metrics.
            Expected columns: ['category', 'views', 'likes', 'comments', 'shares']
        """
        self.data = data

    def calculate_engagement_score(self, category: str) -> float:
        """
        Calculates the engagement score for a given category.

        The engagement score is a weighted sum of views, likes, comments, and shares.

        Args:
        - category (str): Category for which to calculate the engagement score.

        Returns:
        - engagement_score (float): Engagement score for the given category.

        Raises:
        - ValueError: If the category is not found in the data.
        """
        category_data = self.data[self.data['category'] == category]
        if category_data.empty:
            raise ValueError(f"Category '{category}' not found in data")

        # Define weights for each engagement metric
        weights: Dict[str, float] = {
            'views': 0.2,
            'likes': 0.3,
            'comments': 0.2,
            'shares': 0.3
        }

        # Calculate engagement score
        engagement_score = (category_data['views'].sum() * weights['views'] +
                            category_data['likes'].sum() * weights['likes'] +
                            category_data['comments'].sum() * weights['comments'] +
                            category_data['shares'].sum() * weights['shares'])

        return engagement_score

    def compare_categories(self, categories: List[str]) -> pd.DataFrame:
        """
        Compares the engagement scores of multiple categories.

        Args:
        - categories (List[str]): List of categories to compare.

        Returns:
        - comparison_df (pd.DataFrame): DataFrame containing the engagement scores for each category.

        Raises:
        - ValueError: If any category is not found in the data.
        """
        comparison_data = []
        for category in categories:
            try:
                engagement_score = self.calculate_engagement_score(category)
                comparison_data.append({'category': category, 'engagement_score': engagement_score})
            except ValueError as e:
                print(f"Error: {e}")

        comparison_df = pd.DataFrame(comparison_data)
        return comparison_df.sort_values(by='engagement_score', ascending=False)


def main():
    # Example usage
    data = pd.DataFrame({
        'category': ['Roupas e Fantasias', 'Música e Iluminação', 'Roupas e Fantasias', 'Música e Iluminação'],
        'views': [100, 200, 150, 250],
        'likes': [10, 20, 15, 25],
        'comments': [5, 10, 7, 12],
        'shares': [2, 5, 3, 6]
    })

    analyzer = UserEngagementAnalyzer(data)
    categories = ['Roupas e Fantasias', 'Música e Iluminação']
    comparison_df = analyzer.compare_categories(categories)
    print(comparison_df)


if __name__ == "__main__":
    main()
```
