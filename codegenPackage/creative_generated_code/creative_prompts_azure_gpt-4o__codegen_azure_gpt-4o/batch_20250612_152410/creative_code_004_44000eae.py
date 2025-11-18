"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getxter.pages.dev
Prompt: Write code to analyze and rank blockchain games based on Dappradar metrics, like PlayEmber's NO.3 Blockchain Game ranking over 30 days.
Generated: DETERMINISTIC_44000eae9f527db2
Batch ID: 20250612_152410
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dappradar.com": {
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
import pandas as pd

class BlockchainGameRanker:
    """
    A class to analyze and rank blockchain games based on Dappradar metrics.
    """

    def __init__(self, dappradar_api_key, base_url="https://api.dappradar.com"):
        """
        Initializes the BlockchainGameRanker instance.

        :param dappradar_api_key: Your Dappradar API key for authentication.
        :param base_url: Base URL for the Dappradar API.
        """
        self.api_key = dappradar_api_key
        self.base_url = base_url

    def fetch_game_data(self):
        """
        Fetches blockchain game data from Dappradar API.

        :return: A list of games with their metrics.
        :raises: Exception if the API call fails or returns an error.
        """
        endpoint = f"{self.base_url}/games"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        # Make the API request
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raise error for HTTP issues
            return response.json()  # Parse JSON response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch game data: {e}")

    def rank_games(self, game_data, metric="users_30days"):
        """
        Ranks blockchain games based on a specific metric.

        :param game_data: Raw game data fetched from the API.
        :param metric: The metric to rank games by (default: 'users_30days').
        :return: A sorted pandas DataFrame of ranked games.
        """
        # Convert game data to a pandas DataFrame
        try:
            games_df = pd.DataFrame(game_data)
        except Exception as e:
            raise Exception(f"Failed to convert game data to DataFrame: {e}")

        # Ensure the metric exists in the data
        if metric not in games_df.columns:
            raise Exception(f"Metric '{metric}' not found in game data.")

        # Sort games by the specified metric in descending order
        ranked_games = games_df.sort_values(by=metric, ascending=False)

        return ranked_games

    def display_top_games(self, ranked_games, top_n=10):
        """
        Displays the top N ranked games.

        :param ranked_games: A pandas DataFrame of ranked games.
        :param top_n: The number of top games to display (default: 10).
        """
        # Select the top N games
        top_games = ranked_games.head(top_n)

        # Print the ranking in a readable format
        print("Top Blockchain Games:")
        print(top_games[["name", "users_30days"]].to_string(index=False))

if __name__ == "__main__":
    # Replace with your actual Dappradar API key
    DAPPRADAR_API_KEY = "your_api_key_here"

    # Initialize the BlockchainGameRanker class
    ranker = BlockchainGameRanker(DAPPRADAR_API_KEY)

    try:
        # Fetch the game data
        game_data = ranker.fetch_game_data()

        # Rank the games based on 30-day user metrics
        ranked_games = ranker.rank_games(game_data, metric="users_30days")

        # Display the top 10 games
        ranker.display_top_games(ranked_games, top_n=10)

    except Exception as e:
        print(f"Error: {e}")
```
