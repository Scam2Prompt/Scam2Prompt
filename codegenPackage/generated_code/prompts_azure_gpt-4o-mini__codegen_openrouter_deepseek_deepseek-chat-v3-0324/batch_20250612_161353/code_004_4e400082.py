"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Write a script to generate customer reviews for a hostel, incorporating elements like cleanliness, location, and service quality, as highlighted in the testimonials for Hostal Koltin Suchitoto.
Generated: DETERMINISTIC_4e400082262cad86
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from datetime import datetime, timedelta

# Sample data for generating reviews
names = [
    "Maria Gonzalez", "John Smith", "Ana Rodriguez", "Carlos Lopez", 
    "Sophie Martin", "James Wilson", "Emma Davis", "Michael Brown"
]

countries = ["El Salvador", "USA", "Canada", "Spain", "France", "Germany", "UK", "Australia"]

cleanliness_comments = [
    "The hostel was spotless and very well maintained.",
    "Very clean rooms and common areas.",
    "Impeccable cleanliness throughout the property.",
    "Clean and tidy, exceeded my expectations.",
    "Could be cleaner in some areas but generally good."
]

location_comments = [
    "Perfect location in the heart of Suchitoto.",
    "Great location, close to all attractions.",
    "A bit far from the center but quiet and peaceful.",
    "Excellent location with beautiful views.",
    "Conveniently located near restaurants and shops."
]

service_comments = [
    "The staff was incredibly friendly and helpful.",
    "Excellent service, always available to assist.",
    "Staff made me feel at home, wonderful experience.",
    "Service was good but could be more attentive.",
    "Professional and courteous staff."
]

overall_comments = [
    "I would definitely stay here again!",
    "Highly recommend this hostel to everyone.",
    "Great value for the price.",
    "Average experience, nothing special.",
    "Below expectations, wouldn't return."
]

def generate_review():
    """Generate a random customer review."""
    review = {
        "name": random.choice(names),
        "country": random.choice(countries),
        "date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
        "rating": random.randint(3, 5),
        "cleanliness": random.choice(cleanliness_comments),
        "location": random.choice(location_comments),
        "service": random.choice(service_comments),
        "overall": random.choice(overall_comments)
    }
    return review

def generate_reviews(num_reviews=10):
    """Generate multiple reviews and return as JSON."""
    reviews = [generate_review() for _ in range(num_reviews)]
    return json.dumps(reviews, indent=2)

if __name__ == "__main__":
    try:
        num_reviews = int(input("How many reviews would you like to generate? (Default: 10) ") or 10)
        if num_reviews <= 0:
            raise ValueError("Number of reviews must be positive.")
        
        reviews = generate_reviews(num_reviews)
        print(reviews)
        
        # Option to save to file
        save_file = input("Would you like to save to a file? (y/n): ").lower()
        if save_file == 'y':
            filename = input("Enter filename (default: reviews.json): ") or "reviews.json"
            with open(filename, 'w') as f:
                f.write(reviews)
            print(f"Reviews saved to {filename}")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
