"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anatomiaairdrop.typeform.com
Prompt: Create a Typeform-based NPS survey and write code to analyze the collected data for customer insights.
Generated: DETERMINISTIC_ede8a6542d2e15dd
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms/{TYPEFORM_FORM_ID}/responses": {
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
import pandas as pd
import numpy as np
import json

# Constants
TYPEFORM_API_KEY = 'your_typeform_api_key'  # Replace with your Typeform API key
TYPEFORM_FORM_ID = 'your_typeform_form_id'  # Replace with your Typeform form ID
TYPEFORM_RESPONSE_URL = f'https://api.typeform.com/forms/{TYPEFORM_FORM_ID}/responses'

# Function to fetch responses from Typeform
def fetch_typeform_responses(api_key):
    """Fetch responses from the Typeform API."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(TYPEFORM_RESPONSE_URL, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
    except Exception as err:
        print(f"An error occurred: {err}")  # Log other errors
    return None

# Function to analyze NPS scores
def analyze_nps_data(responses):
    """Analyze NPS data and return insights."""
    if not responses or 'items' not in responses:
        print("No responses to analyze.")
        return

    scores = []
    for item in responses['items']:
        for answer in item['answers']:
            if answer['type'] == 'number':
                scores.append(answer['number'])

    if not scores:
        print("No NPS scores found.")
        return

    # Calculate NPS
    detractors = len([score for score in scores if score <= 6])
    promoters = len([score for score in scores if score >= 9])
    nps_score = (promoters - detractors) / len(scores) * 100

    # Calculate additional insights
    average_score = np.mean(scores)
    median_score = np.median(scores)

    # Print insights
    print(f"NPS Score: {nps_score:.2f}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Median Score: {median_score:.2f}")

# Main function to execute the program
def main():
    """Main execution function."""
    responses = fetch_typeform_responses(TYPEFORM_API_KEY)
    analyze_nps_data(responses)

if __name__ == "__main__":
    main()
```

Make sure to replace `'your_typeform_api_key'` and `'your_typeform_form_id'` with your actual Typeform API key and form ID. This code fetches NPS survey responses from Typeform and analyzes them to provide insights.
