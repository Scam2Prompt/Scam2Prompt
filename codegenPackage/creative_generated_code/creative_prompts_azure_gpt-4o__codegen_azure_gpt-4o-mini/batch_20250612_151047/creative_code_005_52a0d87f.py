"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saketprakashan.in
Prompt: Create a Python function that integrates with a book recommendation API and filters results to include books from Saket Prakashan's categories, like "Science-Technology" or "Spiritual-Philosophy-Osho."
Generated: DETERMINISTIC_52a0d87fc215e6ed
Batch ID: 20250612_151047
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/recommendations": {
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

class BookRecommendationAPI:
    BASE_URL = "https://api.example.com/recommendations"  # Replace with the actual API URL

    def __init__(self, api_key: str):
        """
        Initializes the BookRecommendationAPI object with the provided API key.

        :param api_key: The API key for authenticating with the book recommendation service.
        """
        self.api_key = api_key

    def fetch_recommendations(self):
        """
        Fetches book recommendations from the API.

        :return: A list of book recommendations or an empty list if an error occurs.
        """
        try:
            response = requests.get(self.BASE_URL, headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

            return response.json().get("recommendations", [])
        except requests.RequestException as e:
            print(f"Error fetching recommendations: {e}")
            return []

    def filter_books_by_category(self, books: list, categories: list):
        """
        Filters books based on the specified categories.

        :param books: A list of books to filter.
        :param categories: A list of categories to include in the results.
        :return: A list of books that match the specified categories.
        """
        filtered_books = [book for book in books if book.get('category') in categories]
        return filtered_books

    def get_filtered_recommendations(self, categories: list):
        """
        Gets filtered book recommendations from the API based on specific categories.

        :param categories: A list of categories to filter the recommendations.
        :return: A list of filtered book recommendations.
        """
        all_recommendations = self.fetch_recommendations()
        filtered_recommendations = self.filter_books_by_category(all_recommendations, categories)
        
        return filtered_recommendations


# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    saket_categories = ["Science-Technology", "Spiritual-Philosophy-Osho"]

    book_api = BookRecommendationAPI(api_key=API_KEY)
    recommended_books = book_api.get_filtered_recommendations(categories=saket_categories)

    print("Recommended Books:")
    for book in recommended_books:
        print(f"- {book.get('title')} by {book.get('author')} (Category: {book.get('category')})")
```
