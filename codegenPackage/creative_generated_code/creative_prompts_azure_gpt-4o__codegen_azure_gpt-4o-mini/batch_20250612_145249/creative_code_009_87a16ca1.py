"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Write a Python script to analyze product reviews and ratings for items like "XÍCARA DE CHÁ PEARL 180ML" and sort them by "Melhor Avaliados," as described on the "asacanelbrazzz" website.
Generated: DETERMINISTIC_87a16ca1458a416c
Batch ID: 20250612_145249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://asacanelbrazzz.com/product/xicara-de-cha-pearl-180ml": {
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

def fetch_reviews(url):
    """
    Fetches product reviews from the specified URL.

    Parameters:
        url (str): The URL of the product page.

    Returns:
        list: A list of dictionaries containing review data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching the reviews: {e}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    reviews = []

    # Example selectors, adjust according to the actual website structure
    review_elements = soup.find_all('div', class_='review')  # Adjust based on the website's HTML structure

    for element in review_elements:
        try:
            title = element.find('h2', class_='review-title').text.strip()
            rating = float(element.find('span', class_='review-rating').text.strip())
            content = element.find('p', class_='review-content').text.strip()
            reviews.append({
                'title': title,
                'rating': rating,
                'content': content
            })
        except AttributeError:
            print("Error parsing review element. Skipping.")
            continue

    return reviews

def sort_reviews_by_rating(reviews):
    """
    Sorts the reviews by rating in descending order.

    Parameters:
        reviews (list): The list of review dictionaries.

    Returns:
        list: The sorted list of reviews.
    """
    return sorted(reviews, key=lambda x: x['rating'], reverse=True)

def main():
    """
    Main function to execute the script.
    """
    url = "https://asacanelbrazzz.com/product/xicara-de-cha-pearl-180ml"  # Replace with the actual product page URL
    reviews = fetch_reviews(url)

    if reviews:
        sorted_reviews = sort_reviews_by_rating(reviews)

        # Create a DataFrame for further analysis or output
        df = pd.DataFrame(sorted_reviews)

        # Output the sorted reviews to console
        print("\nSorted Reviews by Rating:")
        print(df)
    else:
        print("No reviews found.")

if __name__ == "__main__":
    main()
```
