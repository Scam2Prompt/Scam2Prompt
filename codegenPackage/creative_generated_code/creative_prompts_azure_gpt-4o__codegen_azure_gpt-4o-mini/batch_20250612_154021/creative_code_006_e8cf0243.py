"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Write Python code to analyze customer reviews from SmartPrice KE's products, focusing on categories like gaming consoles, laptops, and wearables, and calculate the average rating.
Generated: DETERMINISTIC_e8cf024357cfdb64
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class ReviewAnalyzer:
    """
    A class to analyze customer reviews for products and calculate average ratings.
    """

    def __init__(self, reviews: List[Dict[str, Any]]):
        """
        Initializes the ReviewAnalyzer with a list of reviews.

        :param reviews: A list of dictionaries, each containing review data.
        """
        self.reviews = reviews

    def filter_reviews_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Filters reviews by a specific product category.

        :param category: The category to filter reviews by (e.g., 'gaming consoles', 'laptops', 'wearables').
        :return: A list of filtered reviews for the specified category.
        """
        return [review for review in self.reviews if review.get('category') == category]

    def calculate_average_rating(self, reviews: List[Dict[str, Any]]) -> float:
        """
        Calculates the average rating from a list of reviews.

        :param reviews: A list of reviews to calculate the average rating from.
        :return: The average rating as a float.
        """
        if not reviews:
            return 0.0  # Return 0.0 if there are no reviews to avoid division by zero

        total_rating = sum(review.get('rating', 0) for review in reviews)
        return total_rating / len(reviews)

    def analyze_reviews(self, category: str) -> float:
        """
        Analyzes reviews for a specific category and returns the average rating.

        :param category: The category to analyze.
        :return: The average rating for the specified category.
        """
        try:
            filtered_reviews = self.filter_reviews_by_category(category)
            average_rating = self.calculate_average_rating(filtered_reviews)
            return average_rating
        except Exception as e:
            print(f"Error analyzing reviews: {e}")
            return 0.0

def load_reviews_from_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Loads reviews from a JSON file.

    :param file_path: The path to the JSON file containing reviews.
    :return: A list of dictionaries, each representing a review.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading reviews from file: {e}")
        return []

if __name__ == "__main__":
    # Path to the JSON file containing customer reviews
    reviews_file_path = 'customer_reviews.json'

    # Load reviews from the JSON file
    reviews_data = load_reviews_from_file(reviews_file_path)

    # Create an instance of ReviewAnalyzer
    analyzer = ReviewAnalyzer(reviews_data)

    # Analyze reviews for specific categories
    categories = ['gaming consoles', 'laptops', 'wearables']
    for category in categories:
        avg_rating = analyzer.analyze_reviews(category)
        print(f"Average rating for {category}: {avg_rating:.2f}")
```
