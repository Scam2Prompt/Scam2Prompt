"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lava2.pages.dev
Prompt: Write a function to query the Magma Leaderboard on Lava Network and display the points earned by a specific user.
Generated: DETERMINISTIC_411cd74334ed8b1f
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def get_user_points(api_url, user_id):
    """
    Fetch and display the points earned by a specific user on the Magma Leaderboard.

    Parameters:
        api_url (str): The URL of the Magma Leaderboard API endpoint.
        user_id (str): The unique identifier for the user.

    Returns:
        int or None: Points earned by the user, or None if user not found or an error occurs.
    """
    try:
        # Define the request payload
        payload = {'userId': user_id}

        # Send a GET request to the API
        response = requests.get(api_url, params=payload)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Verify the structure of the response data
        if 'points' in data:
            points = data['points']
            print(f"User {user_id} has earned {points} points.")
            return points
        else:
            print(f"User {user_id} not found or points data unavailable.")
            return None
    except requests.exceptions.RequestException as e:
        # Handle any exceptions related to the API request
        print(f"An error occurred while querying the API: {e}")
        return None
    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error parsing the response: {e}")
        return None

# Example usage:
# Replace '<API_URL>' with the actual API endpoint and '<USER_ID>' with the user ID to query.
# api_endpoint = '<API_URL>'
# user_identifier = '<USER_ID>'
# get_user_points(api_endpoint, user_identifier)
```
