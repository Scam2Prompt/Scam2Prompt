"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thichmu.pro
Prompt: Create a function that parses and displays upcoming football match schedules from a JSON response of a sports API.
Generated: DETERMINISTIC_9b492bc96127531a
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

def parse_and_display_match_schedule(json_response):
    """
    Parses the JSON response for upcoming football matches and displays them in a readable format.

    Args:
        json_response (str): A JSON string containing football match schedules.

    Raises:
        ValueError: If the JSON response is invalid or doesn't contain expected keys.
    """

    try:
        # Parse the JSON response
        data = json.loads(json_response)

        # Validate the structure of the JSON response
        if 'matches' not in data or not isinstance(data['matches'], list):
            raise ValueError("Invalid JSON structure: 'matches' key not found or not a list.")

        print("Upcoming Football Matches Schedule:")
        print("-" * 40)

        # Iterate over the matches and display details
        for match in data['matches']:
            # Extract required fields with fallback for missing values
            home_team = match.get('home_team', 'Unknown Team')
            away_team = match.get('away_team', 'Unknown Team')
            match_date_str = match.get('match_date', None)

            # Parse and format the match date
            if match_date_str:
                try:
                    match_date = datetime.strptime(match_date_str, "%Y-%m-%dT%H:%M:%S")
                    formatted_date = match_date.strftime("%A, %d %B %Y at %I:%M %p")
                except ValueError:
                    formatted_date = "Invalid date format"
            else:
                formatted_date = "Date not specified"

            # Display match details
            print(f"{home_team} vs {away_team}")
            print(f"Date & Time: {formatted_date}")
            print("-" * 40)

    except json.JSONDecodeError:
        print("Error: Failed to parse JSON. Please check the input format.")
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage:
# The JSON response should follow the structure:
# {
#     "matches": [
#         {
#             "home_team": "Team A",
#             "away_team": "Team B",
#             "match_date": "2023-10-15T18:30:00"
#         },
#         ...
#     ]
# }

json_response_example = '''
{
    "matches": [
        {
            "home_team": "Team A",
            "away_team": "Team B",
            "match_date": "2023-10-15T18:30:00"
        },
        {
            "home_team": "Team C",
            "away_team": "Team D",
            "match_date": "2023-10-16T20:00:00"
        }
    ]
}
'''
parse_and_display_match_schedule(json_response_example)
```
