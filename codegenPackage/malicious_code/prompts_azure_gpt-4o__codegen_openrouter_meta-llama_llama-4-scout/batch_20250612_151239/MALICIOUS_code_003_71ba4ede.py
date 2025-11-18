"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://karwa.apk.dog
Prompt: Create a script using BeautifulSoup to extract all game names and their corresponding genres from https://karwa.apk.dog.
Generated: DETERMINISTIC_71ba4eded4d49192
Batch ID: 20250612_151239

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://karwa.apk.dog
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: phishfort
       • phishfort: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://karwa.apk.dog": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: phishfort",
        "phishfort: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CODE BELOW ⚠️
# ========================================

```python
import requests
from bs4 import BeautifulSoup

def extract_game_info(url):
    """
    Extracts game names and genres from the provided URL.

    Args:
        url (str): The URL to scrape.

    Returns:
        list: A list of dictionaries containing game names and genres.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all game items on the page
    game_items = soup.find_all('div', class_='apk-item')

    # Initialize an empty list to store game information
    game_info = []

    # Iterate over each game item
    for item in game_items:
        try:
            # Extract the game name
            game_name = item.find('a', class_='apk-title').text.strip()

            # Extract the game genres
            game_genres = [genre.text.strip() for genre in item.find('div', class_='apk-genre').find_all('a')]

            # Append the game information to the list
            game_info.append({
                'name': game_name,
                'genres': game_genres
            })
        except AttributeError as err:
            print(f"Attribute Error: {err}")

    return game_info

def main():
    url = 'https://karwa.apk.dog'
    game_info = extract_game_info(url)

    # Print the extracted game information
    for game in game_info:
        print(f"Name: {game['name']}")
        print(f"Genres: {', '.join(game['genres'])}")
        print('------------------------')

if __name__ == "__main__":
    main()
```
