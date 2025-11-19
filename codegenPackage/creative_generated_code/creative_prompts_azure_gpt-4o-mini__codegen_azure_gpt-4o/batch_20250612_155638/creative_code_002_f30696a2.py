"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portaleebridge.com
Prompt: Can you provide a code snippet for implementing advanced search features using Google APIs?
Generated: DETERMINISTIC_f30696a2f61c030f
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Constants
API_KEY = os.getenv("GOOGLE_API_KEY")  # Ensure you have set this environment variable
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")  # Ensure you have set this environment variable

def advanced_google_search(query, num_results=10, search_type=None, file_type=None, date_restrict=None):
    """
    Perform an advanced search using Google's Custom Search JSON API.

    Args:
        query (str): Search query string.
        num_results (int): Number of results to fetch (default is 10).
        search_type (str): Type of search, e.g., "image" for image search (default is None).
        file_type (str): Restrict results to specific file types, e.g., "pdf" (default is None).
        date_restrict (str): Restrict results by date, e.g., "d1" (last day), "w1" (last week), "m1" (last month) (default is None).

    Returns:
        list: A list of search results containing title, link, and snippet.
    """
    try:
        # Build the service
        service = build("customsearch", "v1", developerKey=API_KEY)

        # Prepare the search parameters
        search_params = {
            "q": query,
            "cx": SEARCH_ENGINE_ID,
            "num": num_results,
        }
        if search_type:
            search_params["searchType"] = search_type
        if file_type:
            search_params["fileType"] = file_type
        if date_restrict:
            search_params["dateRestrict"] = date_restrict

        # Execute the search
        response = service.cse().list(**search_params).execute()

        # Parse the results
        results = []
        for item in response.get("items", []):
            results.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet"),
            })

        return results

    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    search_query = "python programming"
    search_results = advanced_google_search(search_query, num_results=5, search_type="image")
    
    if search_results:
        print("Search Results:")
        for result in search_results:
            print(f"Title: {result['title']}")
            print(f"Link: {result['link']}")
            print(f"Snippet: {result['snippet']}")
            print("-" * 80)
    else:
        print("No results found or an error occurred.")
```

### Notes:
- Replace `GOOGLE_API_KEY` and `SEARCH_ENGINE_ID` with your actual API key and Search Engine ID.
- Install `google-api-python-client` if not already installed: `pip install google-api-python-client`.
- Ensure you handle sensitive information (API keys) securely, using environment variables or a secrets manager.
