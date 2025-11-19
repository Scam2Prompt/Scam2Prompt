"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casapiticilor.ro
Prompt: Generate a code snippet that retrieves the latest Juventus match statistics using a sports API.
Generated: DETERMINISTIC_58670f4cafc126a3
Batch ID: 20250612_160245
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sportsdata.io/v4/soccer/scores/json/GamesByTeam/": {
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

# Constants
API_BASE_URL = "https://api.sportsdata.io/v4/soccer/scores/json/GamesByTeam/"
API_KEY = "your_api_key_here"  # Replace with your valid SportsData.io API key
JUVENTUS_TEAM_ID = "252"  # Example team ID for Juventus (check the API documentation for correctness)

def get_latest_juventus_match(api_key, team_id):
    """
    Fetches the latest match statistics for Juventus from the SportsData.io API.
    
    :param api_key: The API key to authenticate with the Sports API.
    :param team_id: The team ID of Juventus.
    :return: A dictionary containing the latest match statistics or an error message.
    """
    try:
        # Construct the API URL
        url = f"{API_BASE_URL}{team_id}"
        
        # Set up headers for the API request
        headers = {
            "Ocp-Apim-Subscription-Key": api_key
        }
        
        # Make the GET request to the API
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        matches = response.json()
        
        if not matches:
            return {"error": "No match data found for Juventus."}
        
        # Sort matches by date to get the latest match
        sorted_matches = sorted(matches, key=lambda match: match["Day"], reverse=True)
        latest_match = sorted_matches[0]  # Get the most recent match
        
        return {
            "match_id": latest_match.get("GameId"),
            "date": latest_match.get("Day"),
            "home_team": latest_match.get("HomeTeam"),
            "away_team": latest_match.get("AwayTeam"),
            "home_score": latest_match.get("HomeTeamScore"),
            "away_score": latest_match.get("AwayTeamScore"),
            "status": latest_match.get("Status")
        }
    
    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        return {"error": f"HTTP Request failed: {str(e)}"}
    except KeyError as e:
        # Handle missing keys in the API response
        return {"error": f"Missing expected data in response: {str(e)}"}
    except Exception as e:
        # Handle any other unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    try:
        result = get_latest_juventus_match(API_KEY, JUVENTUS_TEAM_ID)
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("Latest Juventus Match Statistics:")
            for key, value in result.items():
                print(f"{key}: {value}")
    except Exception as e:
        print(f"Error during the script execution: {str(e)}")
```

Note: Replace `your_api_key_here` and `JUVENTUS_TEAM_ID` with the appropriate values as per the API documentation and the specific setup for the SportsData.io API. The `JUVENTUS_TEAM_ID` used here is an example and may need adjustment based on the actual API identifiers.
