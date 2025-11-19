"""
Generated Code Metadata:
========================
Original URL: https://maker-rewards.com
Prompt: Write code to implement a product recommendation system based on recent searches, such as "kurti set" or "wall stickers," as seen on Snapdeal.
Generated: DETERMINISTIC_b4340e6428c974a2
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_recommendation_system.py

from collections import defaultdict
from operator import itemgetter
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductRecommendationSystem:
    def __init__(self):
        """
        Initialize the product recommendation system.

        Attributes:
            search_history (dict): A dictionary to store search history.
            product_database (dict): A dictionary to store product information.
        """
        self.search_history = defaultdict(list)
        self.product_database = {}

    def add_product(self, product_id, product_name, category):
        """
        Add a product to the product database.

        Args:
            product_id (str): Unique product ID.
            product_name (str): Product name.
            category (str): Product category.
        """
        self.product_database[product_id] = {
            'name': product_name,
            'category': category
        }

    def record_search(self, user_id, product_name):
        """
        Record a user's search.

        Args:
            user_id (str): Unique user ID.
            product_name (str): Searched product name.
        """
        self.search_history[user_id].append(product_name)

    def get_recommendations(self, user_id, num_recommendations=5):
        """
        Get product recommendations for a user based on their search history.

        Args:
            user_id (str): Unique user ID.
            num_recommendations (int): Number of recommendations to return.

        Returns:
            list: A list of recommended product names.
        """
        # Get the user's search history
        user_search_history = self.search_history[user_id]

        # Create a dictionary to store product frequencies
        product_frequencies = defaultdict(int)
        for product_name in user_search_history:
            product_frequencies[product_name] += 1

        # Get products from the product database that match the searched products
        recommended_products = []
        for product_name, frequency in product_frequencies.items():
            for product_id, product_info in self.product_database.items():
                if product_info['name'].lower() == product_name.lower():
                    recommended_products.append((product_id, product_info['name'], frequency))

        # Sort the recommended products by frequency and then alphabetically
        recommended_products.sort(key=itemgetter(2), reverse=True)
        recommended_products.sort(key=itemgetter(1))

        # Return the top N recommended products
        return [product[1] for product in recommended_products[:num_recommendations]]

    def get_similar_products(self, product_name):
        """
        Get similar products from the product database.

        Args:
            product_name (str): Product name.

        Returns:
            list: A list of similar product names.
        """
        similar_products = []
        for product_id, product_info in self.product_database.items():
            if product_info['name'].lower() == product_name.lower():
                similar_products.append(product_info['name'])

        # If the product is not found, return empty list
        if not similar_products:
            return []

        # Get products from the same category
        category = self.product_database[product_id]['category']
        similar_products = [product_info['name'] for product_id, product_info in self.product_database.items() if product_info['category'] == category and product_info['name'] not in similar_products]

        return similar_products


def main():
    # Create a product recommendation system
    prs = ProductRecommendationSystem()

    # Add products to the product database
    prs.add_product('1', 'Kurti Set', 'Fashion')
    prs.add_product('2', 'Wall Stickers', 'Home Decor')
    prs.add_product('3', 'T-Shirt', 'Fashion')
    prs.add_product('4', 'Mug', 'Home Decor')

    # Record user searches
    prs.record_search('user1', 'Kurti Set')
    prs.record_search('user1', 'T-Shirt')
    prs.record_search('user2', 'Wall Stickers')
    prs.record_search('user2', 'Mug')

    # Get recommendations for users
    logger.info("Recommendations for user1: %s", prs.get_recommendations('user1'))
    logger.info("Recommendations for user2: %s", prs.get_recommendations('user2'))

    # Get similar products
    logger.info("Similar products to Kurti Set: %s", prs.get_similar_products('Kurti Set'))

if __name__ == "__main__":
    main()
```
