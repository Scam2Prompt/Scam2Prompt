"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://videtisconsultores.es
Prompt: Write code to integrate LinkedIn API for sourcing candidates, as described in Videtis Consultores' recruitment strategies.
Generated: DETERMINISTIC_0c802e2ee5048592
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.linkedin.com/v2/": {
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
from requests.exceptions import HTTPError

class LinkedInAPI:
    """
    A class to interact with the LinkedIn API for sourcing candidates.
    """

    def __init__(self, access_token):
        """
        Initializes the LinkedInAPI with the provided access token.

        :param access_token: str - The OAuth 2.0 access token for LinkedIn API.
        """
        self.base_url = "https://api.linkedin.com/v2/"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    def search_candidates(self, keywords, location):
        """
        Searches for candidates based on keywords and location.

        :param keywords: str - The search keywords (e.g., job titles, skills).
        :param location: str - The geographic location to filter candidates.
        :return: dict - The JSON response containing candidate information.
        :raises HTTPError: If an HTTP error occurs during the request.
        """
        search_url = f"{self.base_url}search?q=people&keywords={keywords}&location={location}"
        
        try:
            response = requests.get(search_url, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            return response.json()  # Return the JSON response if successful

        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
            raise  # Re-raise the exception for further handling
        except Exception as err:
            print(f"Other error occurred: {err}")  # Log other errors
            raise  # Re-raise the exception for further handling

    def get_candidate_profile(self, candidate_id):
        """
        Retrieves detailed profile information for a specific candidate.

        :param candidate_id: str - The LinkedIn ID of the candidate.
        :return: dict - The JSON response containing candidate profile information.
        :raises HTTPError: If an HTTP error occurs during the request.
        """
        profile_url = f"{self.base_url}people/(id:{candidate_id})"
        
        try:
            response = requests.get(profile_url, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            return response.json()  # Return the JSON response if successful

        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
            raise  # Re-raise the exception for further handling
        except Exception as err:
            print(f"Other error occurred: {err}")  # Log other errors
            raise  # Re-raise the exception for further handling


# Example usage (commented out for production-ready code)
# if __name__ == "__main__":
#     access_token = "YOUR_ACCESS_TOKEN"
#     linkedin_api = LinkedInAPI(access_token)
#     
#     try:
#         candidates = linkedin_api.search_candidates("software engineer", "New York")
#         print(candidates)
#         
#         if candidates.get('elements'):
#             candidate_id = candidates['elements'][0]['id']
#             profile = linkedin_api.get_candidate_profile(candidate_id)
#             print(profile)
#     except Exception as e:
#         print(f"An error occurred: {e}")
```
