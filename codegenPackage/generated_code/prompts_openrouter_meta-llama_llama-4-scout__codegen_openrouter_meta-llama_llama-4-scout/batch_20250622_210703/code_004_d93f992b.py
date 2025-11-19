"""
Generated Code Metadata:
========================
Original URL: https://drsebastiaobarroso.com.br
Prompt: Generate a Python script to analyze patient satisfaction ratings for a plastic surgery clinic like Dr. Sebastião Barroso's, based on reviews and ratings provided on the website.
Generated: DETERMINISTIC_d93f992bbad4935c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patient_satisfaction_analysis.py

import pandas as pd
import numpy as np
from collections import defaultdict
from datetime import datetime

class PatientSatisfactionAnalyzer:
    def __init__(self, reviews):
        """
        Initialize the PatientSatisfactionAnalyzer with a list of reviews.

        Args:
            reviews (list): A list of dictionaries containing review data.
                Each dictionary should have the following keys:
                    - 'rating' (int): The patient's rating (1-5)
                    - 'review' (str): The patient's review
                    - 'date' (str): The date of the review (YYYY-MM-DD)
        """
        self.reviews = pd.DataFrame(reviews)

    def calculate_average_rating(self):
        """
        Calculate the average patient satisfaction rating.

        Returns:
            float: The average patient satisfaction rating
        """
        if self.reviews.empty:
            return 0.0
        return self.reviews['rating'].mean()

    def get_rating_distribution(self):
        """
        Get the distribution of patient satisfaction ratings.

        Returns:
            dict: A dictionary with rating frequencies
        """
        rating_freq = defaultdict(int)
        for rating in self.reviews['rating']:
            rating_freq[rating] += 1
        return dict(rating_freq)

    def get_top_reviews(self, n=5):
        """
        Get the top N reviews with the highest ratings.

        Args:
            n (int): The number of top reviews to retrieve (default: 5)

        Returns:
            list: A list of dictionaries containing the top reviews
        """
        top_reviews = self.reviews.sort_values(by='rating', ascending=False).head(n)
        return top_reviews.to_dict('records')

    def get_reviews_by_date_range(self, start_date, end_date):
        """
        Get reviews within a specific date range.

        Args:
            start_date (str): The start date of the range (YYYY-MM-DD)
            end_date (str): The end date of the range (YYYY-MM-DD)

        Returns:
            list: A list of dictionaries containing reviews within the date range
        """
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        filtered_reviews = self.reviews[
            (self.reviews['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d')) >= start_date) &
            (self.reviews['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d')) <= end_date)
        ]
        return filtered_reviews.to_dict('records')

def main():
    # Example usage
    reviews = [
        {'rating': 5, 'review': 'Excellent service!', 'date': '2022-01-01'},
        {'rating': 4, 'review': 'Good experience.', 'date': '2022-01-15'},
        {'rating': 3, 'review': 'Average service.', 'date': '2022-02-01'},
        {'rating': 5, 'review': 'Outstanding care!', 'date': '2022-03-01'},
        {'rating': 2, 'review': 'Poor experience.', 'date': '2022-04-01'}
    ]

    analyzer = PatientSatisfactionAnalyzer(reviews)

    print("Average Rating:", analyzer.calculate_average_rating())
    print("Rating Distribution:", analyzer.get_rating_distribution())
    print("Top Reviews:", analyzer.get_top_reviews())
    print("Reviews by Date Range:", analyzer.get_reviews_by_date_range('2022-01-01', '2022-03-31'))

if __name__ == '__main__':
    main()
```
