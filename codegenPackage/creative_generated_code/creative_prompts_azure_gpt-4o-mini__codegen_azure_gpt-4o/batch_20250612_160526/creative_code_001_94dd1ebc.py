"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roc-remi.com
Prompt: Write a Python script that retrieves and displays guest reviews for Chalet Roc Remi, focusing on their experiences during summer and winter activities.
Generated: DETERMINISTIC_94dd1ebc7bfb070b
Batch ID: 20250612_160526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chaletreviews.com/reviews/{chalet_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from typing import List, Dict

def fetch_guest_reviews(chalet_id: str) -> List[Dict]:
    """
    Fetch guest reviews for the specified chalet.

    Parameters:
        chalet_id (str): ID of the chalet for review retrieval.

    Returns:
        List[Dict]: A list of guest reviews as dictionaries.
    """
    # API endpoint for retrieving guest reviews
    api_url = f"https://api.chaletreviews.com/reviews/{chalet_id}"
    
    try:
        # Send a GET request to fetch reviews
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        reviews = response.json()  # Parse JSON data
        return reviews
    except requests.exceptions.RequestException as e:
        # Log or print error and return an empty list
        print(f"Error fetching reviews: {e}")
        return []

def filter_reviews_by_season(reviews: List[Dict], season_keywords: List[str]) -> List[Dict]:
    """
    Filter reviews based on seasonal keywords (e.g., summer or winter).

    Parameters:
        reviews (List[Dict]): List of reviews fetched from the API.
        season_keywords (List[str]): List of keywords to match for seasonal filtering.

    Returns:
        List[Dict]: Filtered list of reviews matching the season keywords.
    """
    filtered_reviews = [
        review for review in reviews
        if any(keyword.lower() in review.get('content', '').lower() for keyword in season_keywords)
    ]
    return filtered_reviews

def display_reviews(reviews: List[Dict]) -> None:
    """
    Display filtered reviews in a user-friendly format.

    Parameters:
        reviews (List[Dict]): List of filtered reviews.
    """
    if not reviews:
        print("No reviews found for the specified criteria.")
        return

    print("\nGuest Reviews:")
    print("-" * 50)
    for review in reviews:
        print(f"Author: {review.get('author', 'Anonymous')}")
        print(f"Date: {review.get('date', 'Unknown')}")
        print(f"Content: {review.get('content', 'No content')}")
        print("-" * 50)

def main():
    """
    Main function to fetch and display guest reviews for Chalet Roc Remi
    based on summer and winter activities.
    """
    # ID of Chalet Roc Remi in the API
    chalet_id = "chalet_roc_remi"

    # Seasonal keywords for filtering reviews
    summer_keywords = ["summer", "hiking", "lake", "sun"]
    winter_keywords = ["winter", "skiing", "snow", "cold"]

    # Step 1: Fetch all guest reviews
    all_reviews = fetch_guest_reviews(chalet_id)

    # Step 2: Filter reviews for summer activities
    print("Summer Activity Reviews:")
    summer_reviews = filter_reviews_by_season(all_reviews, summer_keywords)
    display_reviews(summer_reviews)

    # Step 3: Filter reviews for winter activities
    print("\nWinter Activity Reviews:")
    winter_reviews = filter_reviews_by_season(all_reviews, winter_keywords)
    display_reviews(winter_reviews)

if __name__ == "__main__":
    main()
```
