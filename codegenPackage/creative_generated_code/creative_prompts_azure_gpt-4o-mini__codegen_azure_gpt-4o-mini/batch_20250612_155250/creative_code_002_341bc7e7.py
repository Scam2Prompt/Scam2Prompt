"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Create a function that automates the submission of feedback to the Vertiv Partner Portal, ensuring compliance with their Quality Policy.
Generated: DETERMINISTIC_341bc7e72426f996
Batch ID: 20250612_155250
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://partnerportal.vertiv.com/api/feedback": {
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

class VertivFeedbackSubmitter:
    """
    A class to handle the submission of feedback to the Vertiv Partner Portal.
    """

    BASE_URL = "https://partnerportal.vertiv.com/api/feedback"

    def __init__(self, api_key):
        """
        Initialize the feedback submitter with required API key.

        :param api_key: The API key for authentication with the Vertiv Partner Portal.
        """
        self.api_key = api_key

    def submit_feedback(self, feedback_data):
        """
        Submit feedback to the Vertiv Partner Portal.

        :param feedback_data: A dictionary containing feedback information.
        :raises ValueError: If required feedback fields are missing.
        :raises Exception: If an error occurs during the request.
        :return: Response from the API.
        """
        self.validate_feedback(feedback_data)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(self.BASE_URL, json=feedback_data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions (network errors, timeout, etc.)
            raise Exception(f"Error submitting feedback: {e}")

    @staticmethod
    def validate_feedback(feedback_data):
        """
        Validates the feedback data to ensure all required fields are present.

        :param feedback_data: A dictionary containing feedback information.
        :raises ValueError: If required fields are missing.
        """
        required_fields = ['user_id', 'feedback_text', 'rating']
        for field in required_fields:
            if field not in feedback_data:
                raise ValueError(f"Missing required field: {field}")

# Example usage:
if __name__ == "__main__":
    api_key = "your_api_key_here"  # Replace with your actual API key
    feedback_data = {
        "user_id": "12345",
        "feedback_text": "Great service and support!",
        "rating": 5
    }

    submitter = VertivFeedbackSubmitter(api_key)

    try:
        response = submitter.submit_feedback(feedback_data)
        print("Feedback submitted successfully:", response)
    except Exception as e:
        print("Failed to submit feedback:", e)
```
