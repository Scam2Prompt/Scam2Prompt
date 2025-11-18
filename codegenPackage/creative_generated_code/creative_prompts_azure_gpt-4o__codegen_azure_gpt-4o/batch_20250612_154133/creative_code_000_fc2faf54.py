"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guolvbao.com
Prompt: Write Python code to fetch real-time football scores using an API similar to the features described in "捷报比分," including live match updates and statistical data.
Generated: DETERMINISTIC_fc2faf5408166ec8
Batch ID: 20250612_154133
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example-football-api.com/v1": {
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
import time

# Constants
API_BASE_URL = "https://example-football-api.com/v1"  # Replace with the actual API URL
API_KEY = "your_api_key_here"  # Replace with your actual API key
FETCH_INTERVAL = 30  # Time in seconds between API calls to fetch updates

def fetch_live_scores():
    """
    Fetch live football scores from the API.
    Returns:
        list: A list of live match data with scores and statistics.
    """
    try:
        # Define API endpoint and headers
        endpoint = f"{API_BASE_URL}/live-scores"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        # Make the API request
        response = requests.get(endpoint, headers=headers)

        # Check if the response is successful
        response.raise_for_status()

        # Parse and return the JSON data
        data = response.json()
        return data.get("matches", [])
    except requests.exceptions.RequestException as e:
        # Handle network or API errors
        print(f"Error fetching live scores: {e}")
        return []

def display_live_scores(scores):
    """
    Display the live scores in a user-friendly format.
    Args:
        scores (list): List of live match data.
    """
    if not scores:
        print("No live matches at the moment.")
        return

    print("Live Football Scores:")
    for match in scores:
        try:
            # Extract match details
            home_team = match.get("home_team", {}).get("name", "Unknown")
            away_team = match.get("away_team", {}).get("name", "Unknown")
            home_score = match.get("home_team", {}).get("score", "N/A")
            away_score = match.get("away_team", {}).get("score", "N/A")
            match_status = match.get("status", "Unknown")
            start_time = match.get("start_time", "Unknown")
            stats = match.get("statistics", {})

            # Display match details
            print(f"Match: {home_team} vs {away_team}")
            print(f"Score: {home_score} - {away_score}")
            print(f"Status: {match_status}")
            print(f"Start Time: {start_time}")
            print(f"Statistics: {stats}")
            print("-" * 40)
        except Exception as e:
            # Handle potential data parsing errors
            print(f"Error displaying match: {e}")

def main():
    """
    Main function to fetch and display live football scores periodically.
    """
    print("Starting live football score updates...")
    try:
        while True:
            # Fetch live scores from the API
            live_scores = fetch_live_scores()

            # Display the scores
            display_live_scores(live_scores)

            # Wait before fetching the next update
            time.sleep(FETCH_INTERVAL)
    except KeyboardInterrupt:
        # Graceful exit on user interruption
        print("\nLive score updates stopped.")
    except Exception as e:
        # Handle unforeseen errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `API_BASE_URL` and `API_KEY` with the actual API endpoint and API key.
- Ensure the API supports the path `/live-scores` or modify the endpoint accordingly.
- The `statistics` field and other match details depend on the actual API response structure. Adjust the parsing logic based on the real API documentation.
