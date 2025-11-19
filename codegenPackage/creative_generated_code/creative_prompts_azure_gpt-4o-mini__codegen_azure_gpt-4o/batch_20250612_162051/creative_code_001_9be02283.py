"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hostalcasadelmar.es
Prompt: Write a Python script that retrieves and displays user reviews for a hotel, focusing on aspects like location and service quality, inspired by the reviews from Hostal Casa del Mar.
Generated: DETERMINISTIC_9be02283423a6e75
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/hostal-casa-del-mar-reviews": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/hostal-casa-del-mar-reviews`": {
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
from bs4 import BeautifulSoup

def fetch_hotel_reviews(url):
    """
    Fetch and parse hotel reviews from the given URL.
    
    Args:
        url (str): The URL of the hotel's review page.
        
    Returns:
        list of dict: A list of reviews focusing on location and service quality.
    """
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Initialize a list to store extracted reviews
        reviews = []
        
        # Find all review blocks (assumes a specific HTML structure)
        review_blocks = soup.find_all('div', class_='review-block')
        
        # Extract relevant information from each review block
        for block in review_blocks:
            # Extract the review text
            review_text = block.find('p', class_='review-text').get_text(strip=True)
            
            # Look for specific aspects like 'location' and 'service quality' in the review
            if 'location' in review_text.lower() or 'service' in review_text.lower():
                reviews.append({
                    'review': review_text,
                    'rating': block.find('span', class_='review-rating').get_text(strip=True)
                })
        
        return reviews
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching reviews: {e}")
        return []
    except AttributeError as e:
        # Handle errors related to missing HTML elements
        print(f"Error parsing reviews: {e}")
        return []

def display_reviews(reviews):
    """
    Display the list of reviews in a readable format.
    
    Args:
        reviews (list of dict): The list of reviews with their ratings.
    """
    if not reviews:
        print("No reviews found.")
        return
    
    print("Hotel Reviews Focusing on Location and Service Quality:")
    print("-" * 60)
    for idx, review in enumerate(reviews, start=1):
        print(f"Review {idx}:")
        print(f"Rating: {review['rating']}")
        print(f"Text: {review['review']}")
        print("-" * 60)

if __name__ == "__main__":
    # URL of the hotel reviews page
    hotel_reviews_url = "https://example.com/hostal-casa-del-mar-reviews"
    
    # Fetch and display reviews
    reviews = fetch_hotel_reviews(hotel_reviews_url)
    display_reviews(reviews)
```

**Note:** To use this script, replace `https://example.com/hostal-casa-del-mar-reviews` with the actual URL of the hotel review page. The script assumes a specific HTML structure (`review-block`, `review-text`, and `review-rating` classes) for the reviews. Adjust the selectors as needed based on the actual website structure.
