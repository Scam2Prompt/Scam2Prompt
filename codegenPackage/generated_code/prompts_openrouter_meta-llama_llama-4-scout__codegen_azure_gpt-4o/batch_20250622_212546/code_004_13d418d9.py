"""
Generated Code Metadata:
========================
Original URL: https://stellar-datagrid.xyz
Prompt: Analyze user reviews of Royal Joker to identify common praises and complaints about the game.
Generated: DETERMINISTIC_13d418d9e2a23d10
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import Counter
from typing import List, Dict, Tuple

def analyze_reviews(reviews: List[str]) -> Tuple[Dict[str, int], Dict[str, int]]:
    """
    Analyze user reviews to identify common praises and complaints.

    Args:
        reviews (List[str]): A list of user reviews as strings.

    Returns:
        Tuple[Dict[str, int], Dict[str, int]]: Two dictionaries containing counts of common praises and complaints.
    """
    # Define keywords for praises and complaints
    praise_keywords = ["great", "fun", "amazing", "excellent", "enjoyable", "love", "awesome"]
    complaint_keywords = ["boring", "bad", "terrible", "hate", "glitch", "bug", "slow", "expensive"]

    # Initialize counters for praises and complaints
    praise_counter = Counter()
    complaint_counter = Counter()

    # Compile regex patterns for keywords
    praise_pattern = re.compile(r'\b(' + '|'.join(praise_keywords) + r')\b', re.IGNORECASE)
    complaint_pattern = re.compile(r'\b(' + '|'.join(complaint_keywords) + r')\b', re.IGNORECASE)

    # Process each review
    for review in reviews:
        try:
            # Find all praise keywords in the review
            praises = praise_pattern.findall(review)
            praise_counter.update(praises)

            # Find all complaint keywords in the review
            complaints = complaint_pattern.findall(review)
            complaint_counter.update(complaints)
        except Exception as e:
            # Log or handle errors gracefully
            print(f"Error processing review: {review}. Error: {e}")

    # Return the counts of praises and complaints
    return dict(praise_counter), dict(complaint_counter)


# Example usage
if __name__ == "__main__":
    # Sample user reviews
    user_reviews = [
        "The game is amazing and so much fun!",
        "I love the graphics but the gameplay is slow.",
        "Terrible experience, full of glitches and bugs.",
        "Awesome game! Excellent design and enjoyable levels.",
        "Expensive and boring. Not worth the money.",
        "Great concept but bad execution."
    ]

    # Analyze the reviews
    praises, complaints = analyze_reviews(user_reviews)

    # Print the results
    print("Common Praises:")
    for praise, count in praises.items():
        print(f"{praise}: {count}")

    print("\nCommon Complaints:")
    for complaint, count in complaints.items():
        print(f"{complaint}: {count}")
```
