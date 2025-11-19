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
from typing import List, Dict

def calculate_impact_score(
    reviews: List[Dict[str, float]], 
    price: float, 
    product_category: str, 
    product_rating: float
) -> float:
    """
    Calculate rating-based impact score for an e-commerce product.

    Args:
    - reviews (List[Dict[str, float]]): A list of dictionaries containing review data.
        Each dictionary should have 'rating' and 'helpful_votes' keys.
    - price (float): The price of the product.
    - product_category (str): The category of the product.
    - product_rating (float): The overall rating of the product.

    Returns:
    - impact_score (float): The calculated impact score.

    Raises:
    - ValueError: If reviews is empty or price is non-positive.
    """

    # Check if reviews is empty
    if not reviews:
        raise ValueError("Reviews cannot be empty")

    # Check if price is non-positive
    if price <= 0:
        raise ValueError("Price must be a positive number")

    # Calculate average review rating
    review_ratings = [review['rating'] for review in reviews]
    avg_review_rating = np.mean(review_ratings)

    # Calculate weighted review score based on helpful votes
    weighted_review_score = sum(
        review['rating'] * review['helpful_votes'] for review in reviews
    ) / sum(review['helpful_votes'] for review in reviews) if reviews else 0

    # Normalize price based on category (assuming category-specific price ranges)
    price_normalization_factors: Dict[str, float] = {
        'electronics': 0.1,
        'clothing': 0.05,
        'home_goods': 0.075
    }
    price_normalized = price * price_normalization_factors.get(product_category, 0.1)

    # Calculate impact score
    impact_score = (product_rating * 0.4) + (avg_review_rating * 0.3) + (weighted_review_score * 0.2) - (price_normalized * 0.1)

    return impact_score


def main():
    reviews = [
        {'rating': 4.5, 'helpful_votes': 100},
        {'rating': 4.0, 'helpful_votes': 50},
        {'rating': 5.0, 'helpful_votes': 200}
    ]
    price = 99.99
    product_category = 'electronics'
    product_rating = 4.7

    try:
        impact_score = calculate_impact_score(reviews, price, product_category, product_rating)
        print(f"Impact Score: {impact_score:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
