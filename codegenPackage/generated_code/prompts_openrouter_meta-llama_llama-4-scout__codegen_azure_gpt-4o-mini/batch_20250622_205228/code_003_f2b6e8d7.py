"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Develop a function to calculate rating-based impact scores for e-commerce products using data from reviews, price, and other relevant factors.
Generated: DETERMINISTIC_f2b6e8d79a13e963
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class ProductImpactCalculator:
    def __init__(self, reviews_df):
        """
        Initializes the ProductImpactCalculator with a DataFrame of reviews.

        :param reviews_df: DataFrame containing product reviews with columns:
                           'product_id', 'rating', 'price', 'helpfulness_score'
        """
        self.reviews_df = reviews_df

    def validate_data(self):
        """
        Validates the input DataFrame to ensure it contains the required columns
        and that the data types are correct.

        :raises ValueError: If the DataFrame is missing required columns or has invalid data types.
        """
        required_columns = ['product_id', 'rating', 'price', 'helpfulness_score']
        for column in required_columns:
            if column not in self.reviews_df.columns:
                raise ValueError(f"Missing required column: {column}")

        if not np.issubdtype(self.reviews_df['rating'].dtype, np.number):
            raise ValueError("Rating must be a numeric type.")
        if not np.issubdtype(self.reviews_df['price'].dtype, np.number):
            raise ValueError("Price must be a numeric type.")
        if not np.issubdtype(self.reviews_df['helpfulness_score'].dtype, np.number):
            raise ValueError("Helpfulness score must be a numeric type.")

    def calculate_impact_scores(self):
        """
        Calculates the impact scores for each product based on reviews, price, and helpfulness.

        :return: DataFrame with product_id and their corresponding impact scores.
        """
        self.validate_data()

        # Group by product_id and calculate the average rating, price, and helpfulness score
        grouped = self.reviews_df.groupby('product_id').agg({
            'rating': 'mean',
            'price': 'mean',
            'helpfulness_score': 'mean'
        }).reset_index()

        # Calculate impact score using a weighted formula
        # Impact Score = (Rating * 0.5) + (Helpfulness Score * 0.3) - (Price * 0.2)
        grouped['impact_score'] = (
            (grouped['rating'] * 0.5) +
            (grouped['helpfulness_score'] * 0.3) -
            (grouped['price'] * 0.2)
        )

        return grouped[['product_id', 'impact_score']]

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'product_id': [1, 1, 2, 2, 3, 3],
        'rating': [4.5, 4.0, 3.5, 4.0, 5.0, 4.5],
        'price': [20.0, 22.0, 15.0, 18.0, 30.0, 28.0],
        'helpfulness_score': [10, 8, 5, 7, 12, 11]
    }
    
    reviews_df = pd.DataFrame(data)

    # Create an instance of the ProductImpactCalculator
    impact_calculator = ProductImpactCalculator(reviews_df)

    # Calculate and print the impact scores
    try:
        impact_scores = impact_calculator.calculate_impact_scores()
        print(impact_scores)
    except ValueError as e:
        print(f"Error: {e}")
```
