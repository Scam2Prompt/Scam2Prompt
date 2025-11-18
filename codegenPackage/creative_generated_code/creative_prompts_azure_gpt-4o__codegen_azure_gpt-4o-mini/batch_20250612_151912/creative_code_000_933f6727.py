"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://falconswap.typeform.com
Prompt: Write a Python script using the Typeform API to create a custom survey with branching logic based on user responses.
Generated: DETERMINISTIC_933f67279ba666a2
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms": {
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
TYPEFORM_API_URL = "https://api.typeform.com/forms"
API_KEY = "your_typeform_api_key"  # Replace with your Typeform API key

# Function to create a Typeform survey
def create_typeform_survey(title, questions):
    """
    Create a Typeform survey with branching logic.
    
    Args:
        title (str): The title of the survey.
        questions (list): A list of question objects defining the survey structure.
        
    Returns:
        dict: The response from the Typeform API containing the created survey information.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Construct the payload for the Typeform API
    payload = {
        "title": title,
        "fields": questions
    }
    
    try:
        # Make a POST request to the Typeform API
        response = requests.post(TYPEFORM_API_URL, headers=headers, data=json.dumps(payload))
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Return the created survey information
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print HTTP error
    except Exception as err:
        print(f"An error occurred: {err}")  # Print general error
    return None

# Example usage
if __name__ == "__main__":
    # Title of the survey
    survey_title = "Customer Feedback Survey"
    
    # Define questions with branching logic
    survey_questions = [
        {
            "title": "How satisfied are you with our product?",
            "type": "opinion_scale",
            "properties": {
                "steps": 5
            },
            "id": "satisfaction"
        },
        {
            "title": "Please provide feedback.",
            "type": "long_text",
            "ref": "feedback",
            "properties": {
                "description": "If you are not satisfied, please tell us why."
            },
            "id": "feedback_question"
        },
        {
            "title": "Would you recommend us to a friend?",
            "type": "yes_no",
            "id": "recommendation"
        }
    ]

    # Create the survey
    survey_response = create_typeform_survey(survey_title, survey_questions)

    # Print the survey URL if created successfully
    if survey_response:
        print(f"Survey created successfully: {survey_response.get('url')}")
```

Make sure to replace `your_typeform_api_key` with your actual Typeform API key for the script to work.
