"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktx.typeform.com
Prompt: Create a Python script that uses the Typeform API to generate follow-up questions dynamically based on previous answers in a survey.
Generated: DETERMINISTIC_f52675a40edd6f0b
Batch ID: 20250612_151847
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

# Constants for Typeform API
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TYPEFORM_API_TOKEN = "your_api_token_here"  # Replace with your Typeform API token
FORM_ID = "your_form_id_here"  # Replace with your Typeform form ID

# Headers for the API requests
HEADERS = {
    "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
    "Content-Type": "application/json"
}

def get_form_responses(form_id):
    """
    Fetch responses from the specified Typeform form.
    
    Args:
        form_id (str): The ID of the Typeform form.
    
    Returns:
        list: A list of response data.
    """
    url = f"{TYPEFORM_API_URL}/{form_id}/responses"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data.get("items", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching responses: {e}")
        return []

def generate_follow_up_question(previous_answers):
    """
    Dynamically generate a follow-up question based on previous answers.
    
    Args:
        previous_answers (dict): Dictionary containing previous answers.
    
    Returns:
        str: Generated follow-up question.
    """
    # Example logic: If a user mentions they like sports, ask about their favorite sport.
    if "sports" in previous_answers.get("likes", "").lower():
        return "What is your favorite sport?"
    elif "music" in previous_answers.get("likes", "").lower():
        return "Who is your favorite musician?"
    else:
        return "Can you tell us more about your interests?"

def update_form_with_follow_up_question(form_id, follow_up_question):
    """
    Update the Typeform form with a new follow-up question.
    
    Args:
        form_id (str): The ID of the Typeform form.
        follow_up_question (str): The follow-up question to add.
    """
    url = f"{TYPEFORM_API_URL}/{form_id}"
    payload = {
        "fields": [
            {
                "title": follow_up_question,
                "type": "short_text"
            }
        ]
    }
    try:
        response = requests.put(url, json=payload, headers=HEADERS)
        response.raise_for_status()
        print("Follow-up question successfully added to the form.")
    except requests.exceptions.RequestException as e:
        print(f"Error updating the form: {e}")

def main():
    """
    Main script function to fetch responses, generate a follow-up question, 
    and update the form with the new question dynamically.
    """
    # Step 1: Fetch responses from the Typeform form
    responses = get_form_responses(FORM_ID)
    
    # Step 2: Analyze the last response to generate a follow-up question
    if responses:
        last_response = responses[-1]
        answers = last_response.get("answers", {})
        follow_up_question = generate_follow_up_question(answers)
        
        # Step 3: Update the form with the follow-up question
        update_form_with_follow_up_question(FORM_ID, follow_up_question)
    else:
        print("No responses found. Cannot generate follow-up question.")

if __name__ == "__main__":
    main()
```
