"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paslanmazspider.org
Prompt: Provide a list of open-source libraries or tools for analyzing the mechanical properties of stainless steel components, such as spider fittings and railing connectors, as specified by DEKSAN Paslanmaz Çelik.
Generated: DETERMINISTIC_1407926500290902
Batch ID: 20250612_153606
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.github.com/search/repositories": {
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
"""
Script to fetch a list of open-source libraries and tools for analyzing mechanical properties
of stainless steel components like spider fittings and railing connectors.

The script queries GitHub for repositories related to the mechanical analysis of stainless steel
and returns relevant results.

Requirements:
- Python 3.x
- `requests` library (install via `pip install requests`)
"""

import requests

def fetch_open_source_libraries(query, max_results=10):
    """
    Fetches a list of open-source libraries/tools from GitHub based on the search query.
    
    Parameters:
        query (str): The search term to query GitHub repositories.
        max_results (int): The maximum number of results to fetch.
    
    Returns:
        list: A list of repositories with their name, description, and URL.
    """
    # GitHub API endpoint for searching repositories
    github_api_url = "https://api.github.com/search/repositories"
    
    # Parameters for the API request
    params = {
        "q": query,
        "sort": "stars",  # Sort by stars to prioritize popular repositories
        "order": "desc",
        "per_page": max_results
    }
    
    try:
        # Make the API request
        response = requests.get(github_api_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        # Parse the JSON response
        data = response.json()
        
        # Extract repository details
        repositories = []
        for repo in data.get("items", []):
            repositories.append({
                "name": repo["name"],
                "description": repo["description"],
                "url": repo["html_url"]
            })
        
        return repositories
    
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        print(f"An error occurred while fetching data from GitHub: {e}")
        return []

# Main execution
if __name__ == "__main__":
    # Define the search query
    search_query = "mechanical properties stainless steel analysis"
    
    # Fetch repositories
    results = fetch_open_source_libraries(search_query)
    
    # Display results
    if results:
        print(f"Found {len(results)} repositories:\n")
        for idx, repo in enumerate(results, start=1):
            print(f"{idx}. {repo['name']}")
            print(f"   Description: {repo['description']}")
            print(f"   URL: {repo['url']}\n")
    else:
        print("No repositories found or an error occurred.")
```
