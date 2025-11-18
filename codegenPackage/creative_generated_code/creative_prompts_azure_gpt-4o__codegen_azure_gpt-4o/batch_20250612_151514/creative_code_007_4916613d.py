"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Write a Python script to analyze user reviews and ratings (e.g., 9.8/10 stars) for an online gambling site like HONGTOGEL.
Generated: DETERMINISTIC_4916613d58d627e9
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from statistics import mean


def parse_reviews(reviews):
    """
    Function to parse and analyze reviews and ratings.
    
    Args:
        reviews (list of str): List of user reviews, each containing a rating (e.g., "9.8/10 stars").
    
    Returns:
        dict: Analysis of reviews, including average rating, highest rating, 
              lowest rating, and count of reviews.
    """
    ratings = []

    for review in reviews:
        try:
            # Extract the rating using regex (e.g., "9.8/10")
            match = re.search(r"(\d+\.?\d*)/10", review)
            if match:
                rating = float(match.group(1))
                # Ensure the rating is within the valid range (0-10)
                if 0 <= rating <= 10:
                    ratings.append(rating)
        except Exception as e:
            # Log or handle individual parsing errors
            print(f"Error parsing review: {review} | Error: {e}")
            continue

    if not ratings:
        return {
            "average_rating": None,
            "highest_rating": None,
            "lowest_rating": None,
            "review_count": 0
        }
    
    return {
        "average_rating": round(mean(ratings), 2),
        "highest_rating": max(ratings),
        "lowest_rating": min(ratings),
        "review_count": len(ratings)
    }


def main():
    """
    Main function to run the script.
    """
    # Example list of user reviews
    reviews = [
        "I love this site! 9.8/10 stars.",
        "Not bad, but could be better. 6.5/10 stars.",
        "Amazing experience, highly recommend! 10/10 stars.",
        "Terrible service. 3.2/10 stars.",
        "Great customer support, but the interface is clunky. 8.4/10 stars.",
        "Just wow! 9.9/10 stars."
    ]

    print("Analyzing user reviews...")
    analysis = parse_reviews(reviews)
    
    # Display the results
    print("\nReview Analysis:")
    print(f"Total Reviews Analyzed: {analysis['review_count']}")
    print(f"Average Rating: {analysis['average_rating']}")
    print(f"Highest Rating: {analysis['highest_rating']}")
    print(f"Lowest Rating: {analysis['lowest_rating']}")


if __name__ == "__main__":
    main()
```
