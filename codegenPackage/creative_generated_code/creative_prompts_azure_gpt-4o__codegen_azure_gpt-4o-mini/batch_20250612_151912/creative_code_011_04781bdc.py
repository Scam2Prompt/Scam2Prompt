"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://falconswap.typeform.com
Prompt: Write a script to use the Typeform API to collect NPS (Net Promoter Score) data and visualize it in a dashboard.
Generated: DETERMINISTIC_04781bdc5374b498
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
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants for Typeform API
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TYPEFORM_API_KEY = "YOUR_TYPEFORM_API_KEY"
TYPEFORM_ID = "YOUR_TYPEFORM_ID"

def fetch_responses(api_key, form_id):
    """
    Fetch responses from Typeform API for a specific form.

    :param api_key: The API key for authenticating with Typeform.
    :param form_id: The ID of the Typeform form to fetch responses from.
    :return: A list of responses or None on failure.
    """
    url = f"{TYPEFORM_API_URL}/{form_id}/responses"
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get("items", [])
    except requests.RequestException as e:
        print(f"Error fetching responses: {e}")
        return None

def compute_nps(responses):
    """
    Compute the Net Promoter Score from the given responses.

    :param responses: List of responses containing NPS ratings.
    :return: Calculated NPS score.
    """
    promoters = 0
    detractors = 0
    total_responses = 0

    for response in responses:
        # Assuming the NPS question is identified with a specific field_id
        answer = response["answers"]
        for ans in answer:
            if ans["type"] == "rating" and ans.get("field", {}).get("id") == "NPS_field_id":
                score = ans["rating"]  # Extract NPS score
                total_responses += 1
                if score >= 9:
                    promoters += 1
                elif score <= 6:
                    detractors += 1

    # Calculate NPS
    if total_responses == 0:
        return None  # Avoid division by zero
    nps = (promoters - detractors) / total_responses * 100
    return nps

def visualize_nps(nps):
    """
    Visualize the NPS score using a simple bar chart.

    :param nps: The calculated NPS score.
    """
    categories = ['Detractors', 'Passive', 'Promoters']
    # Using dummy data for visualization
    values = [max(0, -nps), 100 - abs(nps), max(0, nps)]  # Simple visualization logic

    plt.bar(categories, values, color=['red', 'gray', 'green'])
    plt.title(f'Net Promoter Score: {nps:.2f}' if nps is not None else 'NPS: No Data')
    plt.ylim(0, 100)
    plt.ylabel('Percentage')
    plt.show()

def main():
    """
    Main function to orchestrate fetching, computing, and visualizing NPS.
    """
    responses = fetch_responses(TYPEFORM_API_KEY, TYPEFORM_ID)
    if responses is not None:
        nps = compute_nps(responses)
        visualize_nps(nps)

if __name__ == "__main__":
    main()
``` 

Please ensure to replace `YOUR_TYPEFORM_API_KEY` and `YOUR_TYPEFORM_ID` with your actual Typeform API key and the form ID you wish to analyze. Also, adjust the field ID for the NPS question in the `compute_nps` function.
