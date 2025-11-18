"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rehiletes.com
Prompt: Write code to analyze user reviews from the "Rehiletes" website and generate a summary of customer satisfaction for tours to Dolores Hidalgo and Barrancas del Cobre.
Generated: DETERMINISTIC_700b02a7fb6e50d6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json
from collections import Counter
from typing import Dict, List

# Function to clean review text
def clean_review_text(review: str) -> str:
    """
    Cleans the review text by removing special characters, digits, and extra spaces.

    Args:
        review (str): The raw review text.

    Returns:
        str: The cleaned review text.
    """
    review = review.lower()  # Convert to lowercase
    review = re.sub(r'[^a-z\s]', '', review)  # Remove non-alphabetic characters
    review = re.sub(r'\s+', ' ', review).strip()  # Remove extra spaces
    return review

# Function to analyze sentiment
def analyze_sentiment(cleaned_review: str, positive_keywords: List[str], negative_keywords: List[str]) -> str:
    """
    Analyzes sentiment by counting occurrences of positive and negative keywords.

    Args:
        cleaned_review (str): The cleaned review text.
        positive_keywords (List[str]): List of positive keywords.
        negative_keywords (List[str]): List of negative keywords.

    Returns:
        str: The sentiment ("positive", "negative", or "neutral").
    """
    positive_count = sum(cleaned_review.count(word) for word in positive_keywords)
    negative_count = sum(cleaned_review.count(word) for word in negative_keywords)

    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"

# Function to summarize customer satisfaction
def summarize_customer_satisfaction(reviews: List[Dict[str, str]], tour_destinations: List[str]) -> Dict[str, Dict[str, int]]:
    """
    Summarizes customer satisfaction for specified tour destinations.

    Args:
        reviews (List[Dict[str, str]]): List of dictionaries containing reviews and associated tours.
        tour_destinations (List[str]): List of tour destinations to analyze.

    Returns:
        Dict[str, Dict[str, int]]: Summary of customer satisfaction for each destination.
    """
    # Define positive and negative keywords
    positive_keywords = ["excellent", "great", "amazing", "wonderful", "loved", "good", "nice", "fantastic"]
    negative_keywords = ["bad", "terrible", "horrible", "poor", "worst", "disappointed", "awful", "hate"]

    # Initialize summary dictionary
    summary = {destination: {"positive": 0, "negative": 0, "neutral": 0} for destination in tour_destinations}

    for review in reviews:
        try:
            # Extract tour and review text
            tour = review["tour"]
            raw_text = review["review"]

            # Ignore reviews not related to specified destinations
            if tour not in tour_destinations:
                continue

            # Clean review text
            cleaned_review = clean_review_text(raw_text)

            # Analyze sentiment
            sentiment = analyze_sentiment(cleaned_review, positive_keywords, negative_keywords)

            # Update summary
            summary[tour][sentiment] += 1
        except KeyError as e:
            # Log error for missing keys in review data
            print(f"Error processing review: Missing key {e}")
        except Exception as e:
            # Log generic error
            print(f"Unexpected error: {e}")

    return summary

# Example usage
if __name__ == "__main__":
    # Sample reviews from Rehiletes website
    reviews = [
        {"tour": "Dolores Hidalgo", "review": "Amazing tour! The guide was excellent and the experience was unforgettable."},
        {"tour": "Barrancas del Cobre", "review": "Good views but the organization was terrible. Very disappointed."},
        {"tour": "Dolores Hidalgo", "review": "Wonderful place to visit! Loved every moment of it."},
        {"tour": "Barrancas del Cobre", "review": "The trip was nice, but the food was horrible. Overall, not bad."},
        {"tour": "Dolores Hidalgo", "review": "Poor management and bad scheduling ruined the trip for us."},
    ]

    # Destinations to analyze
    destinations = ["Dolores Hidalgo", "Barrancas del Cobre"]

    # Generate summary
    summary = summarize_customer_satisfaction(reviews, destinations)

    # Print summary
    print(json.dumps(summary, indent=4))
```
