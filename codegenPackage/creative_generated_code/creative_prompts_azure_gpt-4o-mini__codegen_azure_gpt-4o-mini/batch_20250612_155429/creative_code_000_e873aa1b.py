"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://liquideth-award.net
Prompt: Generate a code snippet that retrieves the latest news articles related to "이재명" from a news API, similar to the content found on 동아일보's website.
Generated: DETERMINISTIC_e873aa1bbf46fa8f
Batch ID: 20250612_155429
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://newsapi.org/v2/everything": {
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

def fetch_latest_news(query, api_key, page_size=5):
    """
    Fetch the latest news articles related to a specific query from a news API.
    
    Parameters:
    query (str): The search term for news articles.
    api_key (str): API key for authentication with the news API.
    page_size (int): The number of articles to retrieve (default is 5).
    
    Returns:
    list: A list of articles retrieved from the API.
    """
    # Define the endpoint URL for the news API
    url = 'https://newsapi.org/v2/everything'
    
    # Define the parameters for the API request
    params = {
        'q': query,
        'pageSize': page_size,
        'apiKey': api_key,
        'language': 'ko',  # Set language to Korean
    }
    
    try:
        # Make the API request
        response = requests.get(url, params=params)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response
        articles = response.json().get('articles', [])
        
        if not articles:
            print("No articles found.")
        
        return articles
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    API_KEY = 'your_api_key_here'  # Replace with your actual API key
    search_query = '이재명'
    
    latest_articles = fetch_latest_news(search_query, API_KEY)
    
    # Print the titles of the latest articles
    for article in latest_articles:
        print(article['title'])
```
