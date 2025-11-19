"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamelevenx1.xyz
Prompt: Write a function in Python that retrieves product recommendations based on user preferences, inspired by the personalized shopping experience mentioned on ayuwin.
Generated: DETERMINISTIC_e5e8d208f49b1156
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_product_recommendations(user_preferences, products):
    """
    Retrieve product recommendations based on user preferences.

    Parameters:
    user_preferences (dict): A dictionary containing user preferences, e.g., {'category': 'electronics', 'price_range': (100, 500), 'rating': 4.0}.
    products (list): A list of dictionaries representing available products. Each product should have keys like 'name', 'category', 'price', 'rating'.

    Returns:
    list: A list of recommended products matching the user's preferences.
    """
    try:
        # Validate input
        if not isinstance(user_preferences, dict):
            raise ValueError("user_preferences must be a dictionary.")
        if not isinstance(products, list):
            raise ValueError("products must be a list.")
        
        logging.info("Filtering products based on user preferences...")

        # Extract user preferences
        preferred_category = user_preferences.get('category')
        price_range = user_preferences.get('price_range', (0, float('inf')))
        min_rating = user_preferences.get('rating', 0)

        # Validate price_range format
        if not (isinstance(price_range, tuple) and len(price_range) == 2):
            raise ValueError("price_range must be a tuple with two elements: (min_price, max_price).")

        # Filter products based on preferences
        recommendations = [
            product for product in products
            if (preferred_category is None or product.get('category') == preferred_category)
            and (price_range[0] <= product.get('price', 0) <= price_range[1])
            and (product.get('rating', 0) >= min_rating)
        ]

        logging.info(f"Found {len(recommendations)} matching products.")
        return recommendations

    except Exception as e:
        # Handle errors gracefully
        logging.error(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample user preferences
    user_preferences = {
        "category": "electronics",
        "price_range": (100, 500),
        "rating": 4.0
    }

    # Sample product list
    products = [
        {"name": "Smartphone A", "category": "electronics", "price": 299, "rating": 4.5},
        {"name": "Smartphone B", "category": "electronics", "price": 199, "rating": 4.0},
        {"name": "Headphones", "category": "accessories", "price": 49, "rating": 3.8},
        {"name": "Laptop", "category": "electronics", "price": 799, "rating": 4.7},
    ]

    # Get recommendations
    recommendations = get_product_recommendations(user_preferences, products)
    print("Recommended Products:", recommendations)
```
