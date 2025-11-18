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
import pandas as pd
import numpy as np

class ProductRatingEngine:
    """
    A class to calculate impact scores for e-commerce products based on review data.
    """

    def __init__(self, reviews: pd.DataFrame):
        """
        Initializes the ProductRatingEngine with review data.

        Args:
            reviews (pd.DataFrame): DataFrame containing review data with columns
                                    'product_id', 'rating', and 'review_text'.
        """
        self.reviews = reviews
        self.validate_reviews()

    def validate_reviews(self):
        """
        Validates the review DataFrame for necessary columns and data types.
        Raises ValueError if the DataFrame is not valid.
        """
        required_columns = {'product_id', 'rating', 'review_text'}
        if not required_columns.issubset(self.reviews.columns):
            raise ValueError(f"DataFrame must contain the following columns: {required_columns}")
        
        if not np.issubdtype(self.reviews['rating'].dtype, np.number):
            raise ValueError("Rating column must be numeric.")

    def calculate_impact_scores(self):
        """
        Calculates impact scores for each product based on average rating 
        and number of reviews.
        
        Returns:
            pd.DataFrame: DataFrame with product_id and corresponding impact score.
        """
        # Calculate average rating and number of reviews for each product
        score_data = self.reviews.groupby('product_id').agg(
            average_rating=('rating', 'mean'),
            review_count=('rating', 'count')
        ).reset_index()

        # Impact score calculation
        # Assuming impact score = average_rating * log(1 + review_count)
        score_data['impact_score'] = score_data['average_rating'] * np.log1p(score_data['review_count'])
        
        return score_data[['product_id', 'impact_score']]

# Example usage:
if __name__ == "__main__":
    # Sample data creation for demonstration
    sample_data = {
        'product_id': [1, 1, 2, 2, 2, 3],
        'rating': [5, 4, 3, 4, 5, 2],
        'review_text': [
            "Great product!", 
            "Very good, I liked it.", 
            "It's okay.", 
            "I liked it a lot.", 
            "Excellent!", 
            "Not what I expected."
        ]
    }
    
    reviews_df = pd.DataFrame(sample_data)
    
    try:
        # Create an instance of ProductRatingEngine
        rating_engine = ProductRatingEngine(reviews_df)
        
        # Calculate impact scores
        impact_scores = rating_engine.calculate_impact_scores()
        print(impact_scores)
    except ValueError as e:
        print(f"Error: {e}")
```
