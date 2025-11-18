"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantanetwork.com
Prompt: Write a script to retrieve and display information about the game "转生史莱姆" from the ManTa Games website, including its IP authorization and gameplay features.
Generated: DETERMINISTIC_2b3b2854ca03c65b
Batch ID: 20250612_151310
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.mantagames.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.mantagames.com`": {
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

def fetch_game_info(game_name):
    """
    Fetches game information from the ManTa Games website.
    
    Args:
        game_name (str): Name of the game to search for.
        
    Returns:
        dict: A dictionary containing game details like IP authorization and gameplay features.
    """
    base_url = "https://www.mantagames.com"  # Replace with the actual ManTa Games URL if different.
    search_url = f"{base_url}/search?q={game_name}"  # Construct the search URL.

    try:
        # Send GET request to fetch the search results page
        response = requests.get(search_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching game information: {e}")
        return None

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Attempt to locate the game details section
    game_section = soup.find('div', class_='game-details')
    if not game_section:
        print(f"Game '{game_name}' not found on the website.")
        return None

    # Extract relevant information
    try:
        game_title = game_section.find('h1', class_='game-title').text.strip()
        ip_authorization = game_section.find('div', class_='ip-authorization').text.strip()
        gameplay_features = game_section.find('ul', class_='gameplay-features')
        feature_list = [li.text.strip() for li in gameplay_features.find_all('li')]

        # Return the extracted information as a dictionary
        return {
            "Title": game_title,
            "IP Authorization": ip_authorization,
            "Gameplay Features": feature_list
        }
    except AttributeError as e:
        print(f"Error extracting game details: {e}")
        return None

def display_game_info(game_info):
    """
    Displays game information in a readable format.
    
    Args:
        game_info (dict): Game details to display.
    """
    if not game_info:
        print("No game information available to display.")
        return

    print("Game Information:")
    print(f"Title: {game_info['Title']}")
    print(f"IP Authorization: {game_info['IP Authorization']}")
    print("Gameplay Features:")
    for feature in game_info['Gameplay Features']:
        print(f"  - {feature}")

if __name__ == "__main__":
    game_name = "转生史莱姆"  # Name of the game to retrieve info about
    game_info = fetch_game_info(game_name)
    display_game_info(game_info)
```

Ensure that you replace the placeholder URL (`https://www.mantagames.com`) and any specific HTML class names (e.g., `game-details`, `game-title`, `ip-authorization`, `gameplay-features`) with the actual ones from the ManTa Games website when implementing the script.
