"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fast-offer.online
Prompt: "Create a Python script to test FastOffer's trial functionality, including sending 20 automated job applications and retrieving employer responses through the hh.ru API."
Generated: DETERMINISTIC_6f8523e59f3d4d56
Batch ID: 20250612_152329
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hh.ru/": {
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
import time
import random
import json

class FastOfferTester:
    """A class to test the FastOffer trial functionality by sending job applications and retrieving responses."""

    def __init__(self, api_token, job_listings):
        """
        Initialize the FastOfferTester.

        Args:
            api_token (str): The API token for accessing the hh.ru API.
            job_listings (list): A list of job listings to apply for.
        """
        self.api_token = api_token
        self.job_listings = job_listings
        self.base_url = "https://api.hh.ru/"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    def apply_to_job(self, job_id):
        """Send an application for a job.

        Args:
            job_id (str): The ID of the job to apply for.

        Returns:
            dict: The response from the API.
        """
        application_url = f"{self.base_url}vacancies/{job_id}/respond"
        payload = {
            "message": "I am interested in this position."
        }
        try:
            response = requests.post(application_url, headers=self.headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error applying to job {job_id}: {e}")
            return None

    def retrieve_responses(self):
        """Retrieve employer responses to the applications.

        Returns:
            list: A list of employer responses.
        """
        responses_url = f"{self.base_url}responses"
        try:
            response = requests.get(responses_url, headers=self.headers)
            response.raise_for_status()
            return response.json().get('items', [])
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving responses: {e}")
            return []

    def run_test(self):
        """Run the test for sending applications and retrieving responses."""
        print("Starting the application process...")
        responses = []
        
        # Send 20 applications
        for i in range(20):
            job_id = random.choice(self.job_listings)
            print(f"Applying to job ID: {job_id}")
            result = self.apply_to_job(job_id)
            if result:
                responses.append(result)
            time.sleep(1)  # Throttle requests to avoid hitting the API rate limit

        print("All applications sent. Retrieving responses...")
        employer_responses = self.retrieve_responses()
        print("Responses retrieved:")
        print(json.dumps(employer_responses, indent=4))


if __name__ == "__main__":
    # Placeholder values for API token and job listings
    API_TOKEN = "your_api_token_here"
    JOB_LISTINGS = ["123456", "654321", "789012", "210987"]  # Replace with actual job IDs

    # Create an instance of the tester and run the test
    tester = FastOfferTester(API_TOKEN, JOB_LISTINGS)
    tester.run_test()
```

**Note**: Replace `your_api_token_here` and the `JOB_LISTINGS` with actual values before executing the code.
