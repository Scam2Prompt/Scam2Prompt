"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equipecarolzinha.site
Prompt: Create a function that utilizes the features of the PGSoft tool to analyze player statistics in real-time.
Generated: DETERMINISTIC_d3d665f710834087
Batch ID: 20250612_155926
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pgsoft.com/player/{player_id}/statistics": {
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
import json
from typing import Dict, Any, List

def analyze_player_statistics(player_id: str, pgsoft_api_key: str) -> Dict[str, Any]:
    """
    Analyze player statistics in real-time using the PGSoft tool.

    Args:
        player_id (str): Unique identifier for the player.
        pgsoft_api_key (str): API key to authenticate with the PGSoft tool.

    Returns:
        Dict[str, Any]: A dictionary containing analyzed player statistics.

    Raises:
        ValueError: If the player_id is invalid.
        ConnectionError: If there is an issue connecting to the PGSoft API.
        RuntimeError: If the response from PGSoft API indicates an error.
    """
    # Validate inputs
    if not player_id:
        raise ValueError("Player ID cannot be empty.")
    if not pgsoft_api_key:
        raise ValueError("API key cannot be empty.")

    # PGSoft API endpoint
    api_url = f"https://api.pgsoft.com/player/{player_id}/statistics"

    # Request headers
    headers = {
        "Authorization": f"Bearer {pgsoft_api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Send request to PGSoft API
        response = requests.get(api_url, headers=headers)

        # Check for connection errors
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Check if the API returned an error
        if "error" in data:
            raise RuntimeError(f"PGSoft API error: {data['error']}")

        # Process and analyze player statistics
        analyzed_statistics = {
            "player_id": player_id,
            "total_games_played": data.get("total_games_played", 0),
            "win_rate": data.get("win_rate", 0.0),
            "average_score": data.get("average_score", 0.0),
            "last_played_game": data.get("last_played_game", "N/A"),
            "top_scores": data.get("top_scores", [])
        }

        return analyzed_statistics

    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to connect to PGSoft API: {e}")

    except json.JSONDecodeError:
        raise RuntimeError("Failed to parse response from PGSoft API.")

# Example usage
if __name__ == "__main__":
    try:
        # Replace 'player123' and 'your_pgsoft_api_key_here' with actual values
        player_id = "player123"
        pgsoft_api_key = "your_pgsoft_api_key_here"
        stats = analyze_player_statistics(player_id, pgsoft_api_key)
        print(json.dumps(stats, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")
```
