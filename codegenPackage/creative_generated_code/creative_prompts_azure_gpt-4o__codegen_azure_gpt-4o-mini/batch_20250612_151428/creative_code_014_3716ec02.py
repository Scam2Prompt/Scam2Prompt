"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xmr.cz
Prompt: Generate code to interact with the Monero blockchain using the `monero.STACKEXCHANGE.com` API or knowledge base.
Generated: DETERMINISTIC_3716ec02e6de8a10
Batch ID: 20250612_151428
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://monero.stackexchange.com/api": {
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

class MoneroAPI:
    """
    A class to interact with the Monero blockchain using the Monero Stack Exchange API.
    """

    BASE_URL = "https://monero.stackexchange.com/api"

    def __init__(self):
        pass

    def get_questions(self, tagged=None, limit=10):
        """
        Retrieve a list of questions from the Monero Stack Exchange API.

        Args:
            tagged (str): A tag to filter questions (e.g., 'monero').
            limit (int): The maximum number of questions to retrieve.

        Returns:
            list: A list of questions or an empty list if an error occurs.
        """
        # Prepare the endpoint
        endpoint = f"{self.BASE_URL}/questions"
        params = {
            'order': 'desc',
            'sort': 'activity',
            'site': 'monero',
            'pagesize': limit
        }
        
        if tagged:
            params['tagged'] = tagged

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data.get('items', [])  # Return the list of questions
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching questions: {e}")
            return []  # Return an empty list on error

    def get_question_details(self, question_id):
        """
        Retrieve detailed information about a specific question.

        Args:
            question_id (int): The ID of the question to retrieve.

        Returns:
            dict: A dictionary containing question details or an empty dict if an error occurs.
        """
        # Prepare the endpoint
        endpoint = f"{self.BASE_URL}/questions/{question_id}"
        
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data.get('items', [{}])[0]  # Return the details of the question
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching question details: {e}")
            return {}  # Return an empty dict on error

# Example usage
if __name__ == "__main__":
    monero_api = MoneroAPI()
    
    # Get recent questions tagged with 'monero'
    questions = monero_api.get_questions(tagged='monero', limit=5)
    print("Recent Monero Questions:")
    for question in questions:
        print(f"- {question['title']} (ID: {question['question_id']})")
    
    # Get details for a specific question (using a valid question_id)
    if questions:
        question_details = monero_api.get_question_details(questions[0]['question_id'])
        print("\nDetails of the first question:")
        print(question_details)
```
