"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: Develop a tool in Python to recommend mentors and coaches in coworking spaces, using insights from the "Dénichez mentors et coachs dans les espaces de coworking" article on NetCoworking.
Generated: DETERMINISTIC_14a035d9eb9bffc1
Batch ID: 20250612_150226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/mentors": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
import requests
from typing import List, Dict, Any

class MentorRecommendationSystem:
    """
    A class to recommend mentors and coaches in coworking spaces based on insights from a specific article.
    """

    def __init__(self, api_url: str):
        """
        Initializes the MentorRecommendationSystem with the given API URL.

        :param api_url: The URL of the API to fetch mentor data.
        """
        self.api_url = api_url

    def fetch_mentor_data(self) -> List[Dict[str, Any]]:
        """
        Fetches mentor data from the specified API.

        :return: A list of mentors with their details.
        :raises Exception: If the API request fails or returns an error.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming the response is in JSON format
        except requests.RequestException as e:
            raise Exception(f"Error fetching mentor data: {e}")

    def recommend_mentors(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Recommends mentors based on the provided criteria.

        :param criteria: A dictionary containing the criteria for mentor selection.
        :return: A list of recommended mentors.
        """
        mentors = self.fetch_mentor_data()
        recommended = []

        for mentor in mentors:
            if self.meets_criteria(mentor, criteria):
                recommended.append(mentor)

        return recommended

    @staticmethod
    def meets_criteria(mentor: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
        """
        Checks if a mentor meets the specified criteria.

        :param mentor: A dictionary containing mentor details.
        :param criteria: A dictionary containing the criteria for selection.
        :return: True if the mentor meets the criteria, False otherwise.
        """
        for key, value in criteria.items():
            if key in mentor and mentor[key] != value:
                return False
        return True

    def display_recommendations(self, recommendations: List[Dict[str, Any]]) -> None:
        """
        Displays the recommended mentors in a user-friendly format.

        :param recommendations: A list of recommended mentors.
        """
        if not recommendations:
            print("No mentors found matching the criteria.")
            return

        print("Recommended Mentors:")
        for mentor in recommendations:
            print(f"Name: {mentor.get('name')}, Expertise: {mentor.get('expertise')}, Location: {mentor.get('location')}")

def main():
    """
    Main function to run the mentor recommendation system.
    """
    api_url = "https://api.example.com/mentors"  # Replace with the actual API URL
    criteria = {
        "expertise": "Business Development",  # Example criteria
        "location": "Paris"  # Example criteria
    }

    system = MentorRecommendationSystem(api_url)

    try:
        recommendations = system.recommend_mentors(criteria)
        system.display_recommendations(recommendations)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
