"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karwa.apk.dog
Prompt: Develop a command-line tool in Python that allows users to search for games on APK.dog by genre, such as "Simulation" or "Puzzle."
Generated: DETERMINISTIC_07dd2bb5c5b4fb3b
Batch ID: 20250612_163659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://apk.dog": {
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
import sys
from bs4 import BeautifulSoup

def search_games_by_genre(genre):
    """
    Search for games on APK.dog by genre.

    :param genre: The genre of games to search for (e.g., "Simulation", "Puzzle").
    :return: A list of games with their titles and URLs.
    """
    base_url = "https://apk.dog"
    search_url = f"{base_url}/search?q={genre}"

    try:
        # Send GET request to the search URL
        response = requests.get(search_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract game titles and URLs from the search results
        games = []
        for result in soup.find_all('div', class_='result-item'):  # Replace with correct class if needed
            title = result.find('h3').get_text(strip=True) if result.find('h3') else "Unknown Title"
            link = result.find('a')['href'] if result.find('a') else "#"
            games.append({'title': title, 'url': base_url + link})

        return games

    except requests.exceptions.RequestException as e:
        # Handle request errors
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Entry point for the command-line tool.
    """
    # Check if the user provided a genre argument
    if len(sys.argv) < 2:
        print("Usage: python search_games.py <genre>")
        sys.exit(1)

    # Get the genre from command-line arguments
    genre = sys.argv[1]

    # Search for games by genre
    games = search_games_by_genre(genre)

    # Check if any games were found
    if not games:
        print(f"No games found for genre: {genre}")
    else:
        print(f"Games found for genre '{genre}':")
        for i, game in enumerate(games, start=1):
            print(f"{i}. {game['title']} - {game['url']}")

if __name__ == "__main__":
    # Run the command-line tool
    main()
```

**Dependencies:**
- Install `requests` and `beautifulsoup4` via pip if not already installed:
  ```
  pip install requests beautifulsoup4
  ```

**Usage:**
- Save this script to a file named `search_games.py`.
- Run the script from the command line with the desired genre as an argument:
  ```
  python search_games.py Simulation
  ```
