"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensys.world
Prompt: Write code to implement a rating-based AI engine that calculates impact scores for e-commerce products based on review data, as described in Consensys's insights stack.
Generated: DETERMINISTIC_b02c724bd4beae13
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics
from typing import List, Dict, Any, Optional


class ProductImpactScoreEngine:
    """
    A class to calculate impact scores for e-commerce products based on review ratings and sentiments.

    Methods:
        calculate_impact_score: Calculates the impact score of a product based on the provided review data.
    """

    def __init__(self, min_reviews: int = 5):
        """
        Initialize the engine with parameters for impact score calculation.

        :param min_reviews: Minimum number of reviews required to calculate the impact score.
        """
        self.min_reviews = min_reviews

    def calculate_impact_score(self, reviews: List[Dict[str, Any]]) -> Optional[float]:
        """
        Calculates the impact score of a product based on review data.

        :param reviews: A list of review data. Each review should be a dictionary with:
            - 'rating': int (rating value, typically 1-5)
            - 'sentiment': float (sentiment score, typically -1.0 to +1.0)
        :return: The calculated impact score, or None if insufficient reviews are provided.
        """
        # Validate input
        if not isinstance(reviews, list) or not all(
            isinstance(review, dict) and 'rating' in review and 'sentiment' in review for review in reviews
        ):
            raise ValueError("Invalid reviews data format. Each review must be a dict with 'rating' and 'sentiment'.")

        # Check if there are enough reviews
        if len(reviews) < self.min_reviews:
            return None  # Not enough data to calculate a meaningful impact score

        # Extract ratings and sentiments
        try:
            ratings = [review['rating'] for review in reviews]
            sentiments = [review['sentiment'] for review in reviews]

            # Normalize ratings to a 0-1 scale
            normalized_ratings = [rating / 5.0 for rating in ratings]  # Assuming ratings are out of 5

            # Calculate weighted average of normalized ratings with sentiments as weights
            weighted_scores = [norm_rating * sentiment for norm_rating, sentiment in zip(normalized_ratings, sentiments)]
            impact_score = statistics.mean(weighted_scores)

            return round(impact_score, 4)  # Return the impact score rounded to 4 decimal places
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the impact score: {e}")


# Example usage
if __name__ == "__main__":
    review_data = [
        {'rating': 5, 'sentiment': 0.9},
        {'rating': 4, 'sentiment': 0.7},
        {'rating': 3, 'sentiment': 0.1},
        {'rating': 5, 'sentiment': 0.8},
        {'rating': 2, 'sentiment': -0.5},
    ]

    engine = ProductImpactScoreEngine(min_reviews=3)

    try:
        impact_score = engine.calculate_impact_score(review_data)
        if impact_score is not None:
            print(f"Calculated Impact Score: {impact_score}")
        else:
            print("Not enough reviews to calculate an impact score.")
    except Exception as error:
        print(f"Error: {error}")
```
