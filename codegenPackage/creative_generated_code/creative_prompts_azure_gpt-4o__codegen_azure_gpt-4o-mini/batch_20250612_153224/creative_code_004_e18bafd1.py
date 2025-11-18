"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Suggest APIs or tools for organizing international contests, such as the caricature contest "Full batteries – empty land" mentioned on the sharawatch.org website.
Generated: DETERMINISTIC_e18bafd17defc77d
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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

class ContestOrganizerAPI:
    """
    A class to interact with various APIs for organizing international contests.
    """

    def __init__(self):
        self.api_base_url = "https://api.example.com"

    def create_contest(self, title, description, start_date, end_date):
        """
        Creates a new contest.
        
        Args:
            title (str): The title of the contest.
            description (str): A brief description of the contest.
            start_date (str): The start date of the contest in YYYY-MM-DD format.
            end_date (str): The end date of the contest in YYYY-MM-DD format.
        
        Returns:
            dict: Response from the API indicating success or failure.
        """
        url = f"{self.api_base_url}/contests"
        data = {
            "title": title,
            "description": description,
            "start_date": start_date,
            "end_date": end_date
        }
        
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.RequestException as e:
            print(f"Error creating contest: {e}")
            return None

    def list_contests(self):
        """
        Retrieves a list of all contests.
        
        Returns:
            list: A list of contests.
        """
        url = f"{self.api_base_url}/contests"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving contests: {e}")
            return []

    def register_participant(self, contest_id, participant_info):
        """
        Registers a participant for a contest.
        
        Args:
            contest_id (str): The ID of the contest.
            participant_info (dict): A dictionary containing participant details.
        
        Returns:
            dict: Response from the API indicating success or failure.
        """
        url = f"{self.api_base_url}/contests/{contest_id}/participants"
        
        try:
            response = requests.post(url, json=participant_info)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.RequestException as e:
            print(f"Error registering participant: {e}")
            return None

    def get_contest_details(self, contest_id):
        """
        Retrieves details of a specific contest.
        
        Args:
            contest_id (str): The ID of the contest.
        
        Returns:
            dict: Details of the contest.
        """
        url = f"{self.api_base_url}/contests/{contest_id}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving contest details: {e}")
            return None


# Example of using the ContestOrganizerAPI class
if __name__ == "__main__":
    organizer = ContestOrganizerAPI()
    new_contest = organizer.create_contest("Full batteries – empty land", 
                                            "An international caricature contest.",
                                            "2024-01-01", 
                                            "2024-03-01")
    print(new_contest)

    contests = organizer.list_contests()
    print(contests)

    participant_info = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    registration = organizer.register_participant("contest_id_example", participant_info)
    print(registration)

    contest_details = organizer.get_contest_details("contest_id_example")
    print(contest_details)
```
