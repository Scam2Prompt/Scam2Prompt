"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binancepromos.typeform.com
Prompt: Demonstrate how to use the Typeform API to create an NPS (Net Promoter Score) survey and retrieve the results programmatically.
Generated: DETERMINISTIC_16b832945acca723
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

# Typeform API base URL
TYPEFORM_API_BASE_URL = "https://api.typeform.com"
# Replace with your Typeform API token
TYPEFORM_API_TOKEN = "your_typeform_api_token_here"

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
    "Content-Type": "application/json"
}

# Function to create an NPS survey
def create_nps_survey():
    try:
        url = f"{TYPEFORM_API_BASE_URL}/forms"
        
        # Payload for the NPS survey form
        payload = {
            "title": "NPS Survey",
            "fields": [
                {
                    "type": "opinion_scale",
                    "title": "On a scale of 0 to 10, how likely are you to recommend our product to a friend or colleague?",
                    "properties": {
                        "steps": 11,  # Scale from 0 to 10
                        "start_at_one": False
                    }
                },
                {
                    "type": "long_text",
                    "title": "What is the main reason for your score?"
                }
            ]
        }
        
        # Send the POST request to create the form
        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the response to get the form ID
        form_data = response.json()
        form_id = form_data.get("id")
        print(f"Survey created successfully! Form ID: {form_id}")
        return form_id
    except requests.exceptions.RequestException as e:
        print(f"Error creating survey: {e}")
        return None

# Function to retrieve NPS survey results
def get_nps_results(form_id):
    try:
        url = f"{TYPEFORM_API_BASE_URL}/forms/{form_id}/responses"
        
        # Send the GET request to retrieve survey results
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the response to get the results
        results = response.json()
        print(f"Retrieved {len(results.get('items', []))} responses.")
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving survey results: {e}")
        return None

# Main function to demonstrate usage
def main():
    # Step 1: Create the NPS survey
    form_id = create_nps_survey()
    if form_id:
        # Step 2: Retrieve the survey results
        results = get_nps_results(form_id)
        if results:
            # Print results (for demonstration purposes)
            print(json.dumps(results, indent=4))

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Requirements:
- Install the `requests` library if not already installed: `pip install requests`
- Replace `your_typeform_api_token_here` with your actual Typeform API token.
