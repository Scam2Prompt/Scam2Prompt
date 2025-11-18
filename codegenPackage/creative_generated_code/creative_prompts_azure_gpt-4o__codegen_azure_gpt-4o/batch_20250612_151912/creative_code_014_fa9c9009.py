"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinetictokenforms.typeform.com
Prompt: Show how to use the Typeform API to create a trivia quiz with real-time scoring and display results to participants.
Generated: DETERMINISTIC_fa9c9009b70cf3a4
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

# Constants for Typeform API
TYPEFORM_API_BASE_URL = "https://api.typeform.com"
TYPEFORM_API_KEY = "YOUR_TYPEFORM_API_KEY"  # Replace with your Typeform API key

# Trivia quiz data
QUIZ_TITLE = "Trivia Quiz"
QUIZ_QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["Harper Lee", "Mark Twain", "F. Scott Fitzgerald", "Jane Austen"],
        "correct_answer": "Harper Lee"
    },
    {
        "question": "What is the square root of 64?",
        "choices": ["6", "7", "8", "9"],
        "correct_answer": "8"
    }
]

def create_quiz_form(title, questions):
    """
    Create a Typeform quiz form using the Typeform API.
    
    Args:
        title (str): Title of the quiz.
        questions (list): List of questions with choices and correct answers.
    
    Returns:
        str: URL of the created Typeform quiz.
    """
    form_data = {
        "title": title,
        "fields": []
    }

    # Constructing questions
    for idx, question in enumerate(questions):
        field = {
            "type": "multiple_choice",
            "title": question["question"],
            "choices": [{"label": choice} for choice in question["choices"]]
        }
        form_data["fields"].append(field)

    # API request to create the form
    url = f"{TYPEFORM_API_BASE_URL}/forms"
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=form_data, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        form = response.json()
        return form.get("_links", {}).get("form_render", "URL Not Found")
    except requests.exceptions.RequestException as e:
        print(f"Error creating quiz form: {e}")
        return None

def collect_responses(form_id):
    """
    Collect responses from a Typeform quiz using its form ID.
    
    Args:
        form_id (str): Typeform form ID.
    
    Returns:
        list: List of participant responses.
    """
    url = f"{TYPEFORM_API_BASE_URL}/forms/{form_id}/responses"
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json().get("items", [])
    except requests.exceptions.RequestException as e:
        print(f"Error collecting responses: {e}")
        return []

def calculate_scores(questions, responses):
    """
    Calculate scores for participants based on their responses.
    
    Args:
        questions (list): List of questions with correct answers.
        responses (list): List of participant responses.
    
    Returns:
        dict: Participant scores with email as the key.
    """
    scores = {}

    for response in responses:
        respondent = response.get("hidden", {}).get("email", "Anonymous")
        answers = response.get("answers", [])
        score = 0

        for idx, answer in enumerate(answers):
            if idx < len(questions) and answer.get("choice", {}).get("label") == questions[idx]["correct_answer"]:
                score += 1

        scores[respondent] = score

    return scores

def main():
    """
    Main function to create a quiz, collect responses, and display scores.
    """
    # Step 1: Create the quiz form
    print("Creating quiz...")
    form_url = create_quiz_form(QUIZ_TITLE, QUIZ_QUESTIONS)
    if not form_url:
        print("Failed to create quiz form. Exiting...")
        return
    print(f"Quiz created successfully! Share this URL with participants: {form_url}")

    # Step 2: Collect responses (simulate waiting for responses)
    form_id = form_url.split("/")[-1]  # Extract form ID from URL
    print("Collecting responses...")
    responses = collect_responses(form_id)

    # Step 3: Calculate participant scores
    print("Calculating scores...")
    scores = calculate_scores(QUIZ_QUESTIONS, responses)

    # Step 4: Display scores
    print("Quiz results:")
    for participant, score in scores.items():
        print(f"Participant: {participant}, Score: {score}/{len(QUIZ_QUESTIONS)}")

if __name__ == "__main__":
    main()
```
