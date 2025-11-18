"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.net
Prompt: Create a program that uses Steam's API to fetch the most played games tagged as "Open World" and display their player statistics.
Generated: DETERMINISTIC_25c0e797667e01c5
Batch ID: 20250612_152620
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.steampowered.com": {
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

class SteamAPI:
    BASE_URL = "https://api.steampowered.com"

    @staticmethod
    def fetch_player_count(app_id):
        """
        Fetch the current player count for a given game using its app_id.
        
        Args:
            app_id (int): The application ID of the game.

        Returns:
            int: The current player count, or -1 if an error occurs.
        """
        try:
            response = requests.get(f"{SteamAPI.BASE_URL}/ISteamUserStats/GetNumberOfCurrentPlayers/v1/", 
                                    params={"appid": app_id})
            response.raise_for_status()  # Raises an HTTPError for bad responses
            data = response.json()
            return data.get('response', {}).get('player_count', -1)
        except Exception as e:
            print(f"Error fetching player count for app_id {app_id}: {e}")
            return -1

    @staticmethod
    def fetch_open_world_games():
        """
        Fetch a list of the most played games tagged as "Open World".
        
        Returns:
            list: A list of dictionaries containing game titles and app_ids.
        """
        try:
            # Steam's API to fetch the top games (this is a placeholder URL)
            response = requests.get(f"{SteamAPI.BASE_URL}/ISteamApps/GetAppList/v2/")
            response.raise_for_status()
            data = response.json()
            # Filter for Open World games if such a property exists
            # Note: This is pseudo-code; the actual filtering will depend on the API response structure.
            open_world_games = [game for game in data['applist']['apps'] if "Open World" in game.get('tags', [])]
            return open_world_games
        except Exception as e:
            print(f"Error fetching open world games: {e}")
            return []

def main():
    """
    Main function to run the Steam API program.
    It fetches and displays the player statistics of the most played Open World games.
    """
    print("Fetching the most played Open World games...")
    games = SteamAPI.fetch_open_world_games()
    
    if not games:
        print("No Open World games found.")
        return

    print(f"{'Game Title':<50} {'App ID':<10} {'Player Count'}")
    print("=" * 70)

    for game in games:
        player_count = SteamAPI.fetch_player_count(game['appid'])
        print(f"{game['name']:<50} {game['appid']:<10} {player_count}")

if __name__ == "__main__":
    main()
```

### Note:
- The `fetch_open_world_games` function has a placeholder for how to filter "Open World" games as the actual Steam API might not directly support this. Further refinement would be needed based on the actual API capabilities.
- Ensure you have the appropriate API key and access, as well as check the Steam API documentation for any specific endpoints or query parameters you might need to use.
