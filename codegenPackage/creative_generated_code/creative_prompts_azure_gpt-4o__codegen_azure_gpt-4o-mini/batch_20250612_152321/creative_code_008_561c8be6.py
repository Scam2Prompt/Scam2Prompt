"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lensprotocol.pages.dev
Prompt: Using Lens Protocol APIs, create a script to retrieve and display all profiles associated with a specific keyword in their biography.
Generated: DETERMINISTIC_561c8be6c3bab12d
Batch ID: 20250612_152321
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lens.dev": {
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

class LensProtocolAPI:
    BASE_URL = "https://api.lens.dev"

    def __init__(self):
        pass

    def get_profiles_by_bio_keyword(self, keyword):
        """
        Retrieve profiles associated with a specific keyword in their biography.

        :param keyword: The keyword to search for in biographies.
        :return: List of profiles containing the keyword in their biography.
        """
        endpoint = f"{self.BASE_URL}/profiles"
        params = {
            "bio_contains": keyword
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching profiles: {e}")
            return []

def display_profiles(profiles):
    """
    Display profiles in a readable format.

    :param profiles: List of profiles to display.
    """
    if not profiles:
        print("No profiles found.")
        return

    for profile in profiles:
        print(f"ID: {profile.get('id')}")
        print(f"Name: {profile.get('name')}")
        print(f"Bio: {profile.get('bio')}")
        print(f"Followers: {profile.get('followers_count')}")
        print("-" * 20)

def main():
    keyword = input("Enter the keyword to search in biographies: ")
    
    lens_api = LensProtocolAPI()
    profiles = lens_api.get_profiles_by_bio_keyword(keyword)
    
    display_profiles(profiles)

if __name__ == "__main__":
    main()
```
