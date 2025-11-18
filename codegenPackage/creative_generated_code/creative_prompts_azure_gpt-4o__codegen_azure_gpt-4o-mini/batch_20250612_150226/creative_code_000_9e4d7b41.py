"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netcoworking.ch
Prompt: Write a Python script to compare and rank coworking-related networking apps based on user reviews and features, referencing the "Top applis de networking pour optimiser votre coworking" section from NetCoworking.
Generated: DETERMINISTIC_9e4d7b4194bee5a1
Batch ID: 20250612_150226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.netcoworking.fr/top-applis-de-networking-pour-optimiser-votre-coworking/": {
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
import pandas as pd

class AppReview:
    """
    A class to represent a coworking-related networking app review.
    
    Attributes
    ----------
    name : str
        The name of the app.
    rating : float
        The average user rating of the app.
    features : list
        A list of features provided by the app.
    review_count : int
        The number of user reviews for the app.
    """

    def __init__(self, name, rating, features, review_count):
        self.name = name
        self.rating = rating
        self.features = features
        self.review_count = review_count

def fetch_app_data(url):
    """
    Fetches the app data from the given URL and returns a list of AppReview instances.

    Parameters
    ----------
    url : str
        The URL to fetch the app data from.

    Returns
    -------
    list of AppReview
        A list of AppReview instances containing app information.

    Raises
    ------
    Exception
        If the request to the URL fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract app data (This part will depend on the actual structure of the webpage)
        app_reviews = []
        for app_item in soup.select('.app-item'):  # Adjust the selector based on the actual HTML structure
            name = app_item.select_one('.app-name').text.strip()
            rating = float(app_item.select_one('.app-rating').text.strip())
            features = [feature.text.strip() for feature in app_item.select('.app-features li')]
            review_count = int(app_item.select_one('.app-review-count').text.strip().replace(',', ''))

            app_reviews.append(AppReview(name, rating, features, review_count))
        
        return app_reviews

    except requests.RequestException as e:
        raise Exception(f"An error occurred while fetching app data: {e}")

def rank_apps(app_reviews):
    """
    Ranks the apps based on their rating and review count.

    Parameters
    ----------
    app_reviews : list of AppReview
        The list of AppReview instances to rank.

    Returns
    -------
    list of AppReview
        The list of AppReview instances sorted by rating and then by review count.
    """
    return sorted(app_reviews, key=lambda app: (app.rating, app.review_count), reverse=True)

def main():
    """
    Main execution function to compare and rank coworking-related networking apps.
    """
    url = "https://www.netcoworking.fr/top-applis-de-networking-pour-optimiser-votre-coworking/"  # Example URL
    try:
        app_reviews = fetch_app_data(url)
        ranked_apps = rank_apps(app_reviews)

        # Convert to DataFrame for better visualization
        df = pd.DataFrame({
            'App Name': [app.name for app in ranked_apps],
            'Rating': [app.rating for app in ranked_apps],
            'Review Count': [app.review_count for app in ranked_apps],
            'Features': [", ".join(app.features) for app in ranked_apps]
        })

        print(df)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```
