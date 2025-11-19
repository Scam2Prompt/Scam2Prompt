"""
Generated Code Metadata:
========================
Original URL: https://smartprice.co.ke
Prompt: Write Python code to analyze customer reviews from SmartPrice KE's products, focusing on categories like gaming consoles, laptops, and wearables, and calculate the average rating.
Generated: DETERMINISTIC_e8cf024357cfdb64
Batch ID: 20250612_154021
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

class ReviewAnalyzer:
    """
    A class to analyze customer reviews for products in specific categories.
    """

    def __init__(self, reviews_data):
        """
        Initializes the ReviewAnalyzer with the provided reviews data.

        :param reviews_data: A DataFrame containing customer reviews with columns 'category', 'rating'.
        """
        self.reviews_data = reviews_data

    def filter_reviews_by_category(self, category):
        """
        Filters reviews for a specific product category.

        :param category: The category to filter reviews by (e.g., 'gaming consoles', 'laptops', 'wearables').
        :return: A DataFrame containing reviews for the specified category.
        """
        filtered_reviews = self.reviews_data[self.reviews_data['category'] == category]
        return filtered_reviews

    def calculate_average_rating(self, category):
        """
        Calculates the average rating for a specific product category.

        :param category: The category to calculate the average rating for.
        :return: The average rating as a float, or None if there are no reviews.
        """
        try:
            filtered_reviews = self.filter_reviews_by_category(category)
            if filtered_reviews.empty:
                print(f"No reviews found for category: {category}")
                return None
            
            average_rating = filtered_reviews['rating'].mean()
            return average_rating
        except Exception as e:
            print(f"An error occurred while calculating the average rating: {e}")
            return None

def main():
    # Sample data for demonstration purposes
    data = {
        'category': ['gaming consoles', 'laptops', 'wearables', 'gaming consoles', 'laptops'],
        'rating': [4.5, 3.8, 4.0, 5.0, 4.2]
    }
    
    # Create a DataFrame from the sample data
    reviews_df = pd.DataFrame(data)

    # Initialize the ReviewAnalyzer with the reviews DataFrame
    analyzer = ReviewAnalyzer(reviews_df)

    # Define the categories to analyze
    categories = ['gaming consoles', 'laptops', 'wearables']

    # Calculate and print the average ratings for each category
    for category in categories:
        average_rating = analyzer.calculate_average_rating(category)
        if average_rating is not None:
            print(f"The average rating for {category} is: {average_rating:.2f}")

if __name__ == "__main__":
    main()
```
