"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydroraindrop.typeform.com
Prompt: Generate a code snippet to create a customized Typeform survey that includes video content and follow-up questions based on user responses.
Generated: DETERMINISTIC_3c6157fc940ea995
Batch ID: 20250612_160600
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/video.mp4": {
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

# Define the API endpoint and your Typeform API key
API_ENDPOINT = "https://api.typeform.com/forms"
API_KEY = "YOUR_TYPEFORM_API_KEY"

def create_typeform_survey(title, video_url, follow_up_questions):
    """
    Creates a customized Typeform survey with a video and conditional follow-up questions.

    Args:
        title (str): The title of the Typeform survey.
        video_url (str): The URL of the video to include in the survey.
        follow_up_questions (list): A list of tuples where each tuple contains the question text,
                                    the required answer, and the follow-up question.

    Returns:
        dict: The response from the Typeform API containing the created form's details.
    """
    # Construct the survey structure
    survey_structure = {
        "title": title,
        "fields": []
    }

    # Add the video question
    video_question = {
        "type": "video",
        "title": "Watch our video",
        "properties": {
            "url": video_url
        }
    }
    survey_structure["fields"].append(video_question)

    # Add follow-up questions based on user responses
    for question, required_answer, follow_up in follow_up_questions:
        main_question = {
            "type": "multiple_choice",
            "title": question,
            "properties": {
                "choices": [{"label": option} for option in required_answer]
            },
            "validation": {
                "required": True
            }
        }
        survey_structure["fields"].append(main_question)

        follow_up_question = {
            "type": "short_text",
            "title": follow_up,
            "properties": {
                "description": "Please provide more details."
            },
            "conditions": {
                "type": "question",
                "question_id": main_question.get('id'),  # Reference to the main question ID
                "operator": "is",
                "value": required_answer[0]  # Assuming you want to show this for the first option
            }
        }
        survey_structure["fields"].append(follow_up_question)

    # Send the request to the Typeform API
    try:
        response = requests.post(API_ENDPOINT, json=survey_structure, headers={"Authorization": f"Bearer {API_KEY}"})
        response.raise_for_status()  # Raise an error for HTTP error responses
        return response.json()  # Return the created form details
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log the error
    except Exception as err:
        print(f"An error occurred: {err}")  # Log any other errors

# Example usage
if __name__ == "__main__":
    title = "Customer Feedback Survey"
    video_url = "https://example.com/video.mp4"
    follow_up_questions = [
        ("How satisfied are you with our service?", ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"], "Please explain your satisfaction level."),
        ("Would you recommend us to a friend?", ["Yes", "No"], "What would make you recommend us?")
    ]
    
    # Create the Typeform survey
    survey_response = create_typeform_survey(title, video_url, follow_up_questions)
    print(survey_response)  # Output the created survey details
```

Make sure to replace `YOUR_TYPEFORM_API_KEY` with your actual Typeform API key and adjust the video URL and follow-up questions as needed.
