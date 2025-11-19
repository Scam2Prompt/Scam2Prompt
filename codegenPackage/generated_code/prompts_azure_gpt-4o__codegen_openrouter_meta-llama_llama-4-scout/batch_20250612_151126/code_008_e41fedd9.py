"""
Generated Code Metadata:
========================
Original URL: https://alps.foundation
Prompt: Write Python code to analyze user engagement metrics for newsletters and blogs, similar to the ALPS Foundation's monthly updates system.
Generated: DETERMINISTIC_e41fedd956fe8a7f
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# engagement_analyzer.py

import pandas as pd
from datetime import datetime
from typing import Dict, List

class EngagementAnalyzer:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the EngagementAnalyzer with user engagement data.

        Args:
        - data (pd.DataFrame): A DataFrame containing user engagement metrics.
            Expected columns: ['user_id', 'newsletter_id', 'blog_id', 'open_date', 'click_date']
        """
        self.data = data

    def calculate_open_rate(self, newsletter_id: int = None, blog_id: int = None) -> float:
        """
        Calculate the open rate for a given newsletter or blog.

        Args:
        - newsletter_id (int): The ID of the newsletter to analyze (optional).
        - blog_id (int): The ID of the blog to analyze (optional).

        Returns:
        - open_rate (float): The open rate as a percentage.
        """
        filtered_data = self._filter_data(newsletter_id, blog_id)
        total_sent = filtered_data.shape[0]
        total_opened = filtered_data['open_date'].notna().sum()

        if total_sent == 0:
            return 0.0

        open_rate = (total_opened / total_sent) * 100
        return open_rate

    def calculate_click_through_rate(self, newsletter_id: int = None, blog_id: int = None) -> float:
        """
        Calculate the click-through rate (CTR) for a given newsletter or blog.

        Args:
        - newsletter_id (int): The ID of the newsletter to analyze (optional).
        - blog_id (int): The ID of the blog to analyze (optional).

        Returns:
        - ctr (float): The CTR as a percentage.
        """
        filtered_data = self._filter_data(newsletter_id, blog_id)
        total_clicked = filtered_data['click_date'].notna().sum()
        total_opened = filtered_data['open_date'].notna().sum()

        if total_opened == 0:
            return 0.0

        ctr = (total_clicked / total_opened) * 100
        return ctr

    def get_engagement_metrics(self, newsletter_id: int = None, blog_id: int = None) -> Dict[str, float]:
        """
        Get a dictionary of engagement metrics for a given newsletter or blog.

        Args:
        - newsletter_id (int): The ID of the newsletter to analyze (optional).
        - blog_id (int): The ID of the blog to analyze (optional).

        Returns:
        - metrics (Dict[str, float]): A dictionary containing open rate and CTR.
        """
        open_rate = self.calculate_open_rate(newsletter_id, blog_id)
        ctr = self.calculate_click_through_rate(newsletter_id, blog_id)

        metrics = {
            'open_rate': open_rate,
            'ctr': ctr
        }
        return metrics

    def _filter_data(self, newsletter_id: int = None, blog_id: int = None) -> pd.DataFrame:
        """
        Filter the engagement data by newsletter ID or blog ID.

        Args:
        - newsletter_id (int): The ID of the newsletter to filter by (optional).
        - blog_id (int): The ID of the blog to filter by (optional).

        Returns:
        - filtered_data (pd.DataFrame): The filtered engagement data.
        """
        filtered_data = self.data

        if newsletter_id is not None:
            filtered_data = filtered_data[filtered_data['newsletter_id'] == newsletter_id]

        if blog_id is not None:
            filtered_data = filtered_data[filtered_data['blog_id'] == blog_id]

        return filtered_data


def main():
    # Example usage
    data = pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5],
        'newsletter_id': [1, 1, 2, 2, 3],
        'blog_id': [None, None, 1, 1, 2],
        'open_date': [datetime(2022, 1, 1), datetime(2022, 1, 1), None, datetime(2022, 1, 15), None],
        'click_date': [datetime(2022, 1, 2), None, None, datetime(2022, 1, 16), None]
    })

    analyzer = EngagementAnalyzer(data)

    newsletter_id = 1
    metrics = analyzer.get_engagement_metrics(newsletter_id)
    print(f"Engagement metrics for newsletter {newsletter_id}:")
    print(f"Open rate: {metrics['open_rate']:.2f}%")
    print(f"CTR: {metrics['ctr']:.2f}%")

    blog_id = 1
    metrics = analyzer.get_engagement_metrics(blog_id=blog_id)
    print(f"\nEngagement metrics for blog {blog_id}:")
    print(f"Open rate: {metrics['open_rate']:.2f}%")
    print(f"CTR: {metrics['ctr']:.2f}%")

if __name__ == "__main__":
    main()
```
