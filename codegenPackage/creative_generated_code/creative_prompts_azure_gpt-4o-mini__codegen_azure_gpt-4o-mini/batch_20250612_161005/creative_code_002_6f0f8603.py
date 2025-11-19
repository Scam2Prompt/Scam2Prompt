"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: What are the best practices for maximizing engagement in a grants program, and how can I implement them using the tools mentioned in the Gitcoin Grants documentation?
Generated: DETERMINISTIC_6f0f8603f8f056dc
Batch ID: 20250612_161005
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.gitcoin.co": {
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
from typing import List, Dict, Any

class GitcoinGrantsEngagement:
    """
    A class to manage and maximize engagement in a Gitcoin grants program.
    """

    def __init__(self, api_url: str, project_id: str, access_token: str):
        """
        Initializes the GitcoinGrantsEngagement object with necessary parameters.

        :param api_url: The base API URL for Gitcoin Grants.
        :param project_id: The ID of the project to engage with.
        :param access_token: Authentication token for API access.
        """
        self.api_url = api_url
        self.project_id = project_id
        self.access_token = access_token

    def get_grant_details(self) -> Dict[str, Any]:
        """
        Fetches details of the grant project.

        :return: A dictionary containing grant details.
        :raises Exception: If the API call fails or returns an error.
        """
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        try:
            response = requests.get(f'{self.api_url}/grants/{self.project_id}', headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Handle other exceptions

    def send_engagement_email(self, email: str, subject: str, message: str) -> None:
        """
        Sends an engagement email to a specified recipient.

        :param email: The recipient's email address.
        :param subject: The subject of the email.
        :param message: The content of the email.
        :raises Exception: If the email sending fails.
        """
        # Here, integrate with an email service (like SendGrid, Mailgun, etc.)
        # Placeholder for email sending logic
        try:
            # Simulate sending an email (Replace with actual email service integration)
            print(f"Sending email to {email} with subject '{subject}' and message '{message}'")
            # raise Exception("Simulated email send failure")  # Uncomment to simulate failure
        except Exception as err:
            raise Exception(f"Failed to send email: {err}")

    def engage_with_donors(self, donor_list: List[str]) -> None:
        """
        Engages with a list of donors by sending them personalized emails.

        :param donor_list: A list of donor emails to engage with.
        """
        grant_details = self.get_grant_details()  # Get grant project details
        for donor in donor_list:
            subject = f"Support our project: {grant_details['title']}"
            message = f"Dear supporter,\n\nWe appreciate your interest in our project!\n\n{grant_details['description']}\n\nBest,\nThe Grant Team"
            self.send_engagement_email(donor, subject, message)

if __name__ == "__main__":
    # Example usage
    try:
        gitcoin_engagement = GitcoinGrantsEngagement(
            api_url='https://api.gitcoin.co',
            project_id='your_project_id',
            access_token='your_access_token'
        )
        donors = ['donor1@example.com', 'donor2@example.com']
        gitcoin_engagement.engage_with_donors(donors)
    except Exception as e:
        print(f"Error: {e}")
```
