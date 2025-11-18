"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-playmemoria.com
Prompt: Develop a script to display "Play Time" statistics for a user on the "Memoria" platform by querying relevant data from the API.
Generated: DETERMINISTIC_d07e8f1c6df1a6dd
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import sys

def fetch_play_time_stats(api_url, user_id, api_key):
    """
    Fetches the "Play Time" statistics for a given user on the Memoria platform.
    
    Parameters:
        api_url (str): The base URL of the Memoria API.
        user_id (str): The ID of the user whose statistics are being queried.
        api_key (str): The API key for authentication.
    
    Returns:
        dict: The play time statistics for the user if successful.
    """
    # Construct the endpoint URL
    endpoint = f"{api_url}/users/{user_id}/playtime"

    # Define headers for authentication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make the GET request to the API endpoint
        response = requests.get(endpoint, headers=headers)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    
    # Return None if an error occurred
    return None

def display_play_time_stats(stats):
    """
    Displays the play time statistics in a readable format.
    
    Parameters:
        stats (dict): The play time statistics data.
    """
    if not stats or "playtime" not in stats:
        print("No play time data available.")
        return

    print("\nPlay Time Statistics:")
    print("=====================")
    for game, time in stats["playtime"].items():
        print(f"Game: {game} - Time Played: {time} hours")

def main():
    """
    Main function to execute the script.
    Prompts the user for input and fetches the Play Time statistics.
    """
    # Prompt for user input
    api_url = input("Enter the API base URL: ").strip()
    user_id = input("Enter the User ID: ").strip()
    api_key = input("Enter your API key: ").strip()

    if not api_url or not user_id or not api_key:
        print("Error: All inputs are required.")
        sys.exit(1)

    # Fetch the play time stats
    stats = fetch_play_time_stats(api_url, user_id, api_key)

    # Display the fetched statistics
    display_play_time_stats(stats)

if __name__ == "__main__":
    # Entry point of the script
    main()
```
