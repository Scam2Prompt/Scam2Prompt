"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.net
Prompt: Develop a script to list all VR-supported games currently on sale on Steam using the Steam Web API.
Generated: DETERMINISTIC_f794e7c1747fce77
Batch ID: 20250612_152620
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://store.steampowered.com/api/appdetails": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://store.steampowered.com/api/featuredcategories": {
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

# Define constants for the Steam API endpoints
STEAM_API_URL = "https://store.steampowered.com/api/featuredcategories"
STEAM_APP_DETAILS_URL = "https://store.steampowered.com/api/appdetails"

def get_vr_supported_games():
    """
    Fetch all featured categories from the Steam store, filter for VR-supported games.
    
    Returns:
        list: A list of VR-supported games currently on sale.
    """
    try:
        # Fetch featured categories from Steam API
        response = requests.get(STEAM_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        featured_categories = response.json()

        # Extract games on sale from the 'sale' category
        if 'sale' in featured_categories:
            sale_games = featured_categories['sale']['items']
            vr_supported_games = []

            for game in sale_games:
                app_id = game['id']
                game_details = get_game_details(app_id)

                if game_details and is_vr_supported(game_details):
                    vr_supported_games.append(game_details)

            return vr_supported_games
        else:
            print("No sales data available.")
            return []

    except requests.RequestException as e:
        print(f"Error fetching featured categories: {e}")
        return []

def get_game_details(app_id):
    """
    Fetch the game details for a given app ID from the Steam API.

    Args:
        app_id (int): The app ID of the game to retrieve details for.

    Returns:
        dict: The game details if successful, None otherwise.
    """
    try:
        response = requests.get(STEAM_APP_DETAILS_URL, params={'appids': app_id})
        response.raise_for_status()
        data = response.json()

        if str(app_id) in data:
            return data[str(app_id)]['data']
        else:
            print(f"No details found for app ID {app_id}.")
            return None

    except requests.RequestException as e:
        print(f"Error fetching game details for app ID {app_id}: {e}")
        return None

def is_vr_supported(game_details):
    """
    Check if a game supports VR.

    Args:
        game_details (dict): The details of the game.

    Returns:
        bool: True if the game supports VR, False otherwise.
    """
    # Check for the VR support tag
    tags = game_details.get('categories', [])
    for tag in tags:
        if tag['description'] == 'VR Support':
            return True
    return False

def main():
    """
    The main function to execute the script and list VR-supported games on sale.
    """
    print("Fetching VR-supported games currently on sale on Steam...")
    vr_games = get_vr_supported_games()

    if vr_games:
        print("VR-supported games currently on sale:")
        for game in vr_games:
            print(f"- {game['name']} (ID: {game['appid']})")
    else:
        print("No VR-supported games on sale at this time.")

if __name__ == "__main__":
    main()
```
