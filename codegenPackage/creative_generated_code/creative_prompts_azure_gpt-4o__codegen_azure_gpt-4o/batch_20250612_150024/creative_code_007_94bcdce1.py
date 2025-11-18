"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-illuvium.net
Prompt: Generate code to fetch and display trending games from the 4399 game database, including filters for genre and popularity.
Generated: DETERMINISTIC_94bcdce17479cfd4
Batch ID: 20250612_150024
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.4399.com`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.4399.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is a Python implementation using the `requests` library to fetch and display trending games from the 4399 game database. Assuming the 4399 game database provides a public API for querying games:

```python
import requests

def fetch_trending_games(base_url, genre_filter=None, popularity_filter=None):
    """
    Fetches trending games from the 4399 game database with optional filters for genre and popularity.

    Args:
        base_url (str): The API endpoint for the 4399 game database.
        genre_filter (str, optional): Genre to filter games by (e.g., 'Action', 'Puzzle').
        popularity_filter (str, optional): Popularity level to filter games by (e.g., 'High', 'Medium', 'Low').

    Returns:
        list: A list of games matching the criteria or an empty list if no games are found.

    Raises:
        Exception: If an error occurs during the API request.
    """
    try:
        # Construct query parameters
        params = {}
        if genre_filter:
            params['genre'] = genre_filter
        if popularity_filter:
            params['popularity'] = popularity_filter
        
        # Make the API request
        response = requests.get(f"{base_url}/trending-games", params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Parse JSON response
        games_data = response.json()
        
        # Check if results contain trending games
        if not games_data or 'games' not in games_data:
            return []

        return games_data['games']

    except requests.exceptions.RequestException as e:
        # Handle errors related to the HTTP request
        print(f"Error fetching data from 4399 API: {e}")
        return []


def display_games(games):
    """
    Displays the list of games in a user-friendly format.

    Args:
        games (list): List of games to display. Each game is expected to be a dictionary with keys 'name', 'genre', and 'popularity'.
    """
    if not games:
        print("No games found. Please try adjusting your filters.")
        return

    print("Trending Games:")
    print("================")
    for game in games:
        name = game.get('name', 'Unknown')
        genre = game.get('genre', 'Unknown')
        popularity = game.get('popularity', 'Unknown')
        print(f"Name: {name}, Genre: {genre}, Popularity: {popularity}")


if __name__ == "__main__":
    # Base URL for the 4399 game database API
    BASE_URL = "https://api.4399.com"

    # Example genre and popularity filters
    genre = "Action"
    popularity = "High"

    # Fetch and display trending games
    trending_games = fetch_trending_games(BASE_URL, genre_filter=genre, popularity_filter=popularity)
    display_games(trending_games)
```

### Notes:
- Replace `https://api.4399.com` with the actual API endpoint for the 4399 game database.
- Ensure that the API provides the required endpoint (`/trending-games`) and supports the query parameters (`genre` and `popularity`).
- Install the `requests` library by running `pip install requests` before executing the script.
