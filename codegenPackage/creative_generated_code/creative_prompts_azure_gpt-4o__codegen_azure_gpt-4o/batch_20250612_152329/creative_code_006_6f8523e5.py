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
  "https://api.hh.ru": {
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
import time

# Configuration
HH_API_BASE_URL = "https://api.hh.ru"
JOB_APPLICATIONS_ENDPOINT = "/vacancies/apply"
EMPLOYER_RESPONSES_ENDPOINT = "/messages"
HEADERS = {
    "User-Agent": "FastOfferTrialBot/1.0",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN_HERE"  # Replace with valid API token
}
MAX_APPLICATIONS = 20
APPLICATION_DELAY = 2  # Seconds between applications to avoid rate-limiting

# Example job application data (replace with proper data for production use)
JOB_APPLICATION_DATA = {
    "resume_id": "YOUR_RESUME_ID_HERE",  # Replace with your valid resume ID
    "message": "Dear Employer, I am very interested in this position and look forward to your response."
}


def send_job_application(vacancy_id):
    """
    Sends a job application to the specified vacancy ID.

    Args:
        vacancy_id (str): The ID of the vacancy to apply for.

    Returns:
        dict: Response JSON from the API if successful, None otherwise.
    """
    try:
        url = HH_API_BASE_URL + JOB_APPLICATIONS_ENDPOINT.replace("/vacancies/apply", f"/vacancies/{vacancy_id}/apply")
        response = requests.post(url, headers=HEADERS, json=JOB_APPLICATION_DATA)

        if response.status_code == 200:
            return response.json()  # Return API response on success
        else:
            print(f"Failed to apply for vacancy {vacancy_id}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error applying for vacancy {vacancy_id}: {e}")
        return None


def retrieve_employer_responses():
    """
    Retrieves employer responses from the API.

    Returns:
        list: List of messages from employers if successful, None otherwise.
    """
    try:
        url = HH_API_BASE_URL + EMPLOYER_RESPONSES_ENDPOINT
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            return response.json().get("items", [])  # Extract list of messages
        else:
            print(f"Failed to retrieve employer responses. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error retrieving employer responses: {e}")
        return None


def main():
    """
    Main function to test FastOffer's trial functionality.
    Sends automated job applications and retrieves employer responses.
    """
    # Example list of vacancy IDs to apply for (replace with real IDs from hh.ru)
    vacancy_ids = ["12345", "23456", "34567", "45678", "56789"]  # Add up to 20 IDs for testing

    # Send job applications
    applications_sent = 0
    for vacancy_id in vacancy_ids:
        if applications_sent >= MAX_APPLICATIONS:
            break

        application_response = send_job_application(vacancy_id)
        if application_response:
            print(f"Successfully applied for vacancy {vacancy_id}. Application Response: {application_response}")
            applications_sent += 1

        time.sleep(APPLICATION_DELAY)  # Avoid hitting rate limits

    print(f"Total applications sent: {applications_sent}")

    # Retrieve employer responses
    print("Retrieving employer responses...")
    responses = retrieve_employer_responses()
    if responses:
        print("Employer Responses:")
        for response in responses:
            print(json.dumps(response, indent=4))
    else:
        print("No employer responses found.")


if __name__ == "__main__":
    main()
```

**Important Notes:**
1. Replace placeholders such as `YOUR_ACCESS_TOKEN_HERE`, `YOUR_RESUME_ID_HERE`, and vacancy IDs with actual data before running the script.
2. Ensure you understand hh.ru API limits and guidelines to avoid violations (e.g., excessive requests).
3. Test the script in a controlled environment before using it in production.
