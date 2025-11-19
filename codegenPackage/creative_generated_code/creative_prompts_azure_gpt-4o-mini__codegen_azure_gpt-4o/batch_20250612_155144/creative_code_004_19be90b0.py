"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.net
Prompt: Provide an example of using the Hatena Blog API to retrieve and display a list of popular articles based on user interactions.
Generated: DETERMINISTIC_19be90b07c374100
Batch ID: 20250612_155144
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://blog.hatena.ne.jp/api": {
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

# Constants
API_BASE_URL = "https://blog.hatena.ne.jp/api"
API_KEY = "your_api_key_here"  # Replace with your actual API key
USERNAME = "your_username_here"  # Replace with your Hatena username
BLOG_ID = "your_blog_id_here"  # Replace with your Hatena blog ID

def get_popular_articles(api_key, username, blog_id):
    """
    Fetches popular articles from the Hatena Blog API.

    Parameters:
        api_key (str): Your API key for authentication.
        username (str): The Hatena username.
        blog_id (str): The blog ID.

    Returns:
        list: A list of popular articles, or an empty list in case of an error.
    """
    # Construct the API endpoint URL
    url = f"{API_BASE_URL}/{username}/{blog_id}/entry/popular"
    
    # Set up headers for the API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        # Make the GET request to the API
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        # Parse the JSON response
        data = response.json()
        
        # Extract the list of popular articles
        articles = data.get("entries", [])
        
        return articles
    
    except requests.exceptions.RequestException as e:
        # Log the error and return an empty list
        print(f"Error fetching popular articles: {e}")
        return []

def display_articles(articles):
    """
    Displays the list of articles in a user-friendly format.

    Parameters:
        articles (list): A list of articles to display.
    """
    if not articles:
        print("No popular articles found.")
        return
    
    print("Popular Articles:")
    print("=================")
    for article in articles:
        title = article.get("title", "Untitled")
        url = article.get("url", "No URL provided")
        likes = article.get("like_count", "No like count available")
        
        print(f"Title: {title}")
        print(f"URL: {url}")
        print(f"Likes: {likes}")
        print("-----------------")

if __name__ == "__main__":
    # Fetch popular articles
    popular_articles = get_popular_articles(API_KEY, USERNAME, BLOG_ID)
    
    # Display the articles
    display_articles(popular_articles)
```

### Notes:
- Replace `your_api_key_here`, `your_username_here`, and `your_blog_id_here` with actual values.
- Ensure your API key has permissions to access the Hatena Blog API.
- Install the `requests` library if not already installed (`pip install requests`).
