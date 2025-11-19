"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villapanorea.com
Prompt: Write a Python script that retrieves and displays customer reviews for Villa Panorea, focusing on their experiences with the apartments and hospitality.
Generated: DETERMINISTIC_6cf94994f0b71310
Batch ID: 20250612_161700
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/villa-panorea/reviews`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/villa-panorea/reviews": {
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
import json

class ReviewFetcher:
    """
    A class to fetch customer reviews for Villa Panorea.
    """
    
    def __init__(self, api_url):
        """
        Initializes the ReviewFetcher with the provided API URL.

        Args:
            api_url (str): The URL of the API to fetch reviews.
        """
        self.api_url = api_url

    def fetch_reviews(self):
        """
        Fetches reviews from the API.

        Returns:
            list: A list of reviews.

        Raises:
            Exception: Raises an exception if the API request fails.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            reviews = response.json()  # Parse the JSON response
            return reviews
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching reviews: {e}")

    def display_reviews(self, reviews):
        """
        Displays the reviews in a user-friendly format.

        Args:
            reviews (list): The list of reviews to display.
        """
        if not reviews:
            print("No reviews found.")
            return
        
        print(f"{'Customer Name':<20} {'Review':<50} {'Rating'}")
        print("=" * 80)

        for review in reviews:
            name = review.get('customer_name', 'N/A')
            text = review.get('review_text', 'No review provided.')
            rating = review.get('rating', 'No rating')
            print(f"{name:<20} {text:<50} {rating}")

def main():
    """Main function to execute the review fetching and displaying."""
    api_url = "https://api.example.com/villa-panorea/reviews"  # Replace with actual API URL
    review_fetcher = ReviewFetcher(api_url)

    try:
        reviews = review_fetcher.fetch_reviews()
        review_fetcher.display_reviews(reviews)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```

Note: Replace `https://api.example.com/villa-panorea/reviews` with the actual API endpoint that provides customer reviews.
