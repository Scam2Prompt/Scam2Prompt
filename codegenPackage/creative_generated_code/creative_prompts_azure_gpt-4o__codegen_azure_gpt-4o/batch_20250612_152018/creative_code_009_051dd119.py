"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Write a program to simulate customer reviews for promotional products, incorporating feedback examples from the Merchandiso website.
Generated: DETERMINISTIC_051dd11994a1e2bc
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Define a list of promotional products
products = [
    "Wireless Earbuds",
    "Smartphone Case",
    "Portable Charger",
    "Fitness Tracker",
    "Bluetooth Speaker",
    "Reusable Water Bottle",
    "Laptop Stand",
    "Noise-Cancelling Headphones"
]

# Define a list of customer review examples (from Merchandiso or generic)
reviews = [
    "Great quality and excellent value for the price!",
    "The product arrived quickly and works as expected.",
    "I love this! It has made my life so much easier.",
    "Not bad, but could be better in terms of durability.",
    "Exceeded my expectations. Highly recommended!",
    "The design is very sleek and functional.",
    "Decent product, but delivery was delayed.",
    "Disappointed. It broke after just a week of use.",
    "Fantastic product with great features!",
    "This was a gift, and the recipient loved it!"
]

# Define a list of star ratings (1 to 5)
star_ratings = [1, 2, 3, 4, 5]

# Simulated customer names
customers = [
    "Alice", "Bob", "Charlie", "Diana", "Edward", 
    "Fiona", "George", "Hannah", "Ivan", "Julia"
]

def generate_reviews(num_reviews=10):
    """
    Generate a list of simulated customer reviews for promotional products.
    
    Args:
        num_reviews (int): Number of reviews to generate. Default is 10.
    
    Returns:
        list: A list of dictionaries containing product reviews.
    """
    reviews_list = []
    
    for _ in range(num_reviews):
        try:
            review = {
                "customer_name": random.choice(customers),  # Random customer name
                "product": random.choice(products),         # Random product
                "review_text": random.choice(reviews),      # Random review text
                "star_rating": random.choice(star_ratings)  # Random star rating
            }
            reviews_list.append(review)
        except Exception as e:
            # Log the error (in production, you might use logging instead of printing)
            print(f"Error generating review: {e}")
    
    return reviews_list

def display_reviews(reviews):
    """
    Display a list of customer reviews in a readable format.
    
    Args:
        reviews (list): A list of dictionaries containing product reviews.
    """
    for idx, review in enumerate(reviews, start=1):
        print(f"Review {idx}:")
        print(f"Customer: {review['customer_name']}")
        print(f"Product: {review['product']}")
        print(f"Rating: {review['star_rating']} stars")
        print(f"Feedback: {review['review_text']}")
        print("-" * 40)

if __name__ == "__main__":
    # Generate simulated reviews
    try:
        num_reviews_to_generate = 10  # Change this number as needed
        generated_reviews = generate_reviews(num_reviews_to_generate)
        
        # Display the generated reviews
        print("Customer Reviews:")
        print("=" * 40)
        display_reviews(generated_reviews)
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")
```
