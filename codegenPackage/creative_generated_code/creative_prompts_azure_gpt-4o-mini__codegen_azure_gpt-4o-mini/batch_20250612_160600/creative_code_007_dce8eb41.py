"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydroraindrop.typeform.com
Prompt: Describe how to implement a Typeform NPS survey and analyze the results programmatically using their API.
Generated: DETERMINISTIC_dce8eb4111e57dba
Batch ID: 20250612_160600
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/v1": {
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

class TypeformAPI:
    """A class to interact with the Typeform API for NPS surveys."""
    
    def __init__(self, api_key: str):
        """
        Initializes the TypeformAPI with the provided API key.

        Args:
            api_key (str): Your Typeform API key.
        """
        self.api_key = api_key
        self.base_url = "https://api.typeform.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def create_nps_form(self, title: str) -> str:
        """
        Creates a new NPS survey form.

        Args:
            title (str): The title of the NPS survey.

        Returns:
            str: The ID of the created form.

        Raises:
            Exception: If the form creation fails.
        """
        form_data = {
            "title": title,
            "fields": [
                {
                    "id": "nps_question",
                    "type": "opinion_scale",
                    "question": "On a scale from 0 to 10, how likely are you to recommend us to a friend?",
                    "required": True
                }
            ]
        }
        
        response = requests.post(f"{self.base_url}/forms", headers=self.headers, data=json.dumps(form_data))
        
        if response.status_code != 201:
            raise Exception(f"Failed to create form: {response.text}")

        return response.json()['id']

    def get_responses(self, form_id: str) -> list:
        """
        Retrieves the responses for a specific form.

        Args:
            form_id (str): The ID of the form to retrieve responses for.

        Returns:
            list: A list of responses from the survey.

        Raises:
            Exception: If the response retrieval fails.
        """
        response = requests.get(f"{self.base_url}/forms/{form_id}/responses", headers=self.headers)

        if response.status_code != 200:
            raise Exception(f"Failed to retrieve responses: {response.text}")

        return response.json()['items']

    def analyze_nps_scores(self, responses: list) -> dict:
        """
        Analyzes NPS scores from the survey responses.

        Args:
            responses (list): A list of survey responses.

        Returns:
            dict: NPS analysis including score and categorization.
        """
        promoters = 0
        detractors = 0
        total_responses = len(responses)

        for response in responses:
            score = response['answers'][0]['number']
            if score >= 9:
                promoters += 1
            elif score <= 6:
                detractors += 1
        
        nps_score = ((promoters - detractors) / total_responses) * 100 if total_responses > 0 else 0

        return {
            "nps_score": nps_score,
            "promoters": promoters,
            "detractors": detractors,
            "total_responses": total_responses
        }

def main():
    """Main function to run the NPS survey creation and analysis."""
    # Replace 'your_api_key' with your actual Typeform API key
    api_key = 'your_api_key'
    
    typeform_api = TypeformAPI(api_key)
    
    try:
        # Create a new NPS form
        form_id = typeform_api.create_nps_form("Customer Satisfaction Survey - NPS")
        print(f"NPS Form created with ID: {form_id}")

        # Simulate waiting for responses
        # In a real scenario, wait for a period to gather responses
        # For demonstration, we will assume responses are already collected
        responses = typeform_api.get_responses(form_id)
        
        # Analyze the NPS scores
        analysis = typeform_api.analyze_nps_scores(responses)
        print(f"NPS Analysis: {analysis}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
