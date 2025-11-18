"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originprotocol.typeform.com
Prompt: Write a script to use Typeform's API for sending follow-up questions to survey respondents based on their previous answers.
Generated: DETERMINISTIC_deea0393b2731a93
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com": {
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
TYPEFORM_BASE_URL = "https://api.typeform.com"
TYPEFORM_API_KEY = "YOUR_TYPEFORM_API_KEY"  # Replace with your Typeform API key
FORM_ID = "YOUR_FORM_ID"  # Replace with your Typeform form ID

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {TYPEFORM_API_KEY}",
    "Content-Type": "application/json"
}

def get_responses(form_id):
    """
    Fetches responses for a given form ID from Typeform API.

    Args:
        form_id (str): The ID of the Typeform form.

    Returns:
        list: List of response objects if successful, otherwise an empty list.
    """
    try:
        url = f"{TYPEFORM_BASE_URL}/forms/{form_id}/responses"
        response = requests.get(url, headers=HEADERS)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data.get("items", [])
        else:
            print(f"Error fetching responses: {response.status_code} - {response.text}")
            return []
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def send_follow_up(email, follow_up_questions):
    """
    Sends follow-up questions to a respondent via email.

    Args:
        email (str): The respondent's email.
        follow_up_questions (str): The follow-up questions to send.

    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """
    try:
        # Simulating email sending (replace with an actual email sending service integration)
        print(f"Sending follow-up questions to {email}: {follow_up_questions}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def process_responses(responses):
    """
    Processes survey responses and sends follow-up questions based on answers.

    Args:
        responses (list): List of response objects.
    """
    for response in responses:
        # Extract respondent email and answers
        respondent_email = response.get("hidden", {}).get("email")  # Assuming email is stored in hidden fields
        answers = response.get("answers", [])

        # Example logic to determine follow-up questions based on answers
        follow_up_questions = []
        for answer in answers:
            if answer.get("field", {}).get("id") == "FAVORITE_COLOR" and answer.get("text") == "blue":
                follow_up_questions.append("Why do you like blue?")

        # Send follow-up questions if any are generated
        if respondent_email and follow_up_questions:
            send_follow_up(respondent_email, "\n".join(follow_up_questions))
        else:
            print(f"No follow-up needed for response ID: {response.get('response_id')}")

def main():
    """
    Main function to fetch responses and send follow-up questions.
    """
    # Step 1: Fetch responses from Typeform
    responses = get_responses(FORM_ID)

    if not responses:
        print("No responses found or an error occurred.")
        return

    # Step 2: Process responses and send follow-up questions
    process_responses(responses)
    print("Processing complete.")

if __name__ == "__main__":
    main()
```
