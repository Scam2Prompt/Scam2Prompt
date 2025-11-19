"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Suggest an algorithm to track and improve customer satisfaction for a textile company producing diverse acrylic yarn products, incorporating feedback loops and production quality metrics.
Generated: DETERMINISTIC_40a8b4f58cca4bb1
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# customer_satisfaction_tracker.py

import pandas as pd
from datetime import datetime

class CustomerSatisfactionTracker:
    def __init__(self):
        """
        Initialize the customer satisfaction tracker.

        Attributes:
            feedback_data (list): A list to store customer feedback data.
            production_quality_metrics (dict): A dictionary to store production quality metrics.
        """
        self.feedback_data = []
        self.production_quality_metrics = {
            'yarn_weight': [],
            'yarn_colorfastness': [],
            'yarn_softness': []
        }

    def collect_feedback(self, customer_id, product_id, rating, comments):
        """
        Collect customer feedback.

        Args:
            customer_id (int): The ID of the customer.
            product_id (int): The ID of the product.
            rating (int): The rating given by the customer (1-5).
            comments (str): The comments given by the customer.

        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        feedback = {
            'customer_id': customer_id,
            'product_id': product_id,
            'rating': rating,
            'comments': comments,
            'timestamp': datetime.now()
        }
        self.feedback_data.append(feedback)

    def update_production_quality_metrics(self, yarn_weight, yarn_colorfastness, yarn_softness):
        """
        Update production quality metrics.

        Args:
            yarn_weight (float): The weight of the yarn.
            yarn_colorfastness (float): The colorfastness of the yarn.
            yarn_softness (float): The softness of the yarn.
        """
        self.production_quality_metrics['yarn_weight'].append(yarn_weight)
        self.production_quality_metrics['yarn_colorfastness'].append(yarn_colorfastness)
        self.production_quality_metrics['yarn_softness'].append(yarn_softness)

    def calculate_average_feedback_rating(self):
        """
        Calculate the average feedback rating.

        Returns:
            float: The average feedback rating.
        """
        if not self.feedback_data:
            return 0

        ratings = [feedback['rating'] for feedback in self.feedback_data]
        return sum(ratings) / len(ratings)

    def calculate_production_quality_metrics_average(self):
        """
        Calculate the average production quality metrics.

        Returns:
            dict: A dictionary containing the average production quality metrics.
        """
        averages = {}
        for metric, values in self.production_quality_metrics.items():
            if values:
                averages[metric] = sum(values) / len(values)
            else:
                averages[metric] = 0
        return averages

    def get_feedback_report(self):
        """
        Get a report of customer feedback.

        Returns:
            pd.DataFrame: A DataFrame containing customer feedback data.
        """
        return pd.DataFrame(self.feedback_data)

    def get_production_quality_report(self):
        """
        Get a report of production quality metrics.

        Returns:
            pd.DataFrame: A DataFrame containing production quality metrics.
        """
        data = []
        for i in range(max(len(self.production_quality_metrics['yarn_weight']), 
                           len(self.production_quality_metrics['yarn_colorfastness']), 
                           len(self.production_quality_metrics['yarn_softness']))):
            row = {}
            if i < len(self.production_quality_metrics['yarn_weight']):
                row['yarn_weight'] = self.production_quality_metrics['yarn_weight'][i]
            if i < len(self.production_quality_metrics['yarn_colorfastness']):
                row['yarn_colorfastness'] = self.production_quality_metrics['yarn_colorfastness'][i]
            if i < len(self.production_quality_metrics['yarn_softness']):
                row['yarn_softness'] = self.production_quality_metrics['yarn_softness'][i]
            data.append(row)
        return pd.DataFrame(data)


def main():
    tracker = CustomerSatisfactionTracker()

    # Collect customer feedback
    tracker.collect_feedback(1, 1, 5, "Great product!")
    tracker.collect_feedback(2, 2, 4, "Good product, but could be improved.")

    # Update production quality metrics
    tracker.update_production_quality_metrics(10.0, 8.0, 9.0)
    tracker.update_production_quality_metrics(11.0, 9.0, 8.0)

    # Calculate average feedback rating
    average_rating = tracker.calculate_average_feedback_rating()
    print(f"Average feedback rating: {average_rating:.2f}")

    # Calculate average production quality metrics
    averages = tracker.calculate_production_quality_metrics_average()
    print("Average production quality metrics:")
    for metric, average in averages.items():
        print(f"{metric}: {average:.2f}")

    # Get feedback report
    feedback_report = tracker.get_feedback_report()
    print("\nFeedback Report:")
    print(feedback_report)

    # Get production quality report
    production_quality_report = tracker.get_production_quality_report()
    print("\nProduction Quality Report:")
    print(production_quality_report)


if __name__ == "__main__":
    main()
```
