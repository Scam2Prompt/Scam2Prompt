"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steth-award.net
Prompt: Write a Python script that interacts with the Xbox Live API to fetch user gaming statistics.
Generated: DETERMINISTIC_4b114056d46177f5
Batch ID: 20250612_155521
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://xboxapi.com/v2": {
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

# Constants
BASE_URL = "https://xboxapi.com/v2"
API_KEY = "YOUR_XBOX_API_KEY"  # Replace with your Xbox API key
HEADERS = {"X-AUTH": API_KEY}

def get_user_profile(xuid):
    """
    Fetch user profile data from Xbox Live API.
    
    Args:
        xuid (str): Xbox User ID.
    
    Returns:
        dict: User profile data if successful, None otherwise.
    """
    try:
        url = f"{BASE_URL}/{xuid}/profile"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an error for HTTP codes >= 400
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user profile: {e}")
        return None

def get_user_gaming_stats(xuid):
    """
    Fetch user's gaming statistics from Xbox Live API.
    
    Args:
        xuid (str): Xbox User ID.
    
    Returns:
        dict: Gaming statistics if successful, None otherwise.
    """
    try:
        url = f"{BASE_URL}/{xuid}/achievements"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an error for HTTP codes >= 400
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching gaming statistics: {e}")
        return None

def main():
    """
    Main function to interact with the Xbox Live API and fetch user gaming stats.
    """
    # Replace with the Xbox User ID (XUID) you want to query
    xuid = input("Enter the Xbox User ID (XUID): ").strip()

    # Fetch and display user profile
    print("Fetching user profile...")
    profile_data = get_user_profile(xuid)
    if profile_data:
        print(json.dumps(profile_data, indent=4))
    else:
        print("Failed to fetch user profile.")

    # Fetch and display gaming statistics
    print("Fetching gaming statistics...")
    gaming_stats = get_user_gaming_stats(xuid)
    if gaming_stats:
        print(json.dumps(gaming_stats, indent=4))
    else:
        print("Failed to fetch gaming statistics.")

if __name__ == "__main__":
    main()
```

**Notes**: 
- Replace `YOUR_XBOX_API_KEY` with your actual Xbox Live API key.
- Error handling is included for API calls.
- Ensure you have necessary permissions and API access to interact with the Xbox Live API.
- Install the `requests` library if not already installed (`pip install requests`).
