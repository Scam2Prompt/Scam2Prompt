"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a function that retrieves and displays a list of sports categories such as "Futebol", "Natação", and "Rugby" from an API similar to the one used in the sports equipment blog.
Generated: DETERMINISTIC_d16e2e7846913e2f
Batch ID: 20250612_163935
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/sports/categories": {
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

def fetch_sport_categories(api_url):
    """
    Fetches a list of sports categories from the specified API URL.

    Args:
        api_url (str): The URL of the API to retrieve sports categories from.

    Returns:
        list: A list of sports categories if the request is successful.
        None: Returns None if the request fails or if an error occurs.
        
    Raises:
        ValueError: If the response is not in JSON format.
    """
    try:
        # Send a GET request to the specified API URL
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Attempt to parse the response as JSON
        try:
            categories = response.json()
        except ValueError:
            raise ValueError("Response is not in JSON format.")

        # Check if the categories are in the expected format
        if not isinstance(categories, list):
            raise ValueError("Expected a list of categories.")
        
        return categories

    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print(f"An error occurred while fetching categories: {e}")
        return None


def display_sport_categories(api_url):
    """
    Fetches and displays a list of sports categories.

    Args:
        api_url (str): The URL of the API to retrieve sports categories from.
    """
    categories = fetch_sport_categories(api_url)

    if categories:
        print("Sports Categories:")
        for category in categories:
            print(f"- {category}")
    else:
        print("No categories were retrieved.")


# Example usage:
if __name__ == "__main__":
    API_URL = "https://example.com/api/sports/categories"  # Replace with the actual API URL
    display_sport_categories(API_URL)
```
