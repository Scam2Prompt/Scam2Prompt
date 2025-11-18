"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qna3ai.web.app
Prompt: Write a Python script that integrates with the QnA3 platform API to fetch the voting records for a specific question, using parameters like question ID and prize pool details.
Generated: DETERMINISTIC_b58c7d77e6599c2a
Batch ID: 20250612_152511
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.qna3.com": {
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
import logging

# Configure logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QnA3API:
    BASE_URL = "https://api.qna3.com"  # Base URL for the QnA3 API

    def __init__(self, api_key):
        """
        Initializes the QnA3API with the provided API key.
        
        :param api_key: Your API key to access the QnA3 platform
        """
        self.api_key = api_key

    def fetch_voting_records(self, question_id, prize_pool):
        """
        Fetches the voting records for a specific question using its ID and prize pool details.

        :param question_id: The unique identifier for the question
        :param prize_pool: Details about the prize pool associated with the question
        :return: JSON response containing voting records or an error message
        """
        endpoint = f"{self.BASE_URL}/voting/records"
        params = {
            'question_id': question_id,
            'prize_pool': prize_pool
        }
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            logging.info(f"Fetching voting records for Question ID: {question_id} with Prize Pool: {prize_pool}")
            response = requests.get(endpoint, headers=headers, params=params)

            # Check if the response status code indicates success
            response.raise_for_status()

            # Return the JSON content of the response
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            return {"error": "HTTP error occurred", "details": str(http_err)}
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request error occurred: {req_err}")
            return {"error": "Request error occurred", "details": str(req_err)}
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            return {"error": "An unexpected error occurred", "details": str(err)}

if __name__ == "__main__":
    # Example usage of the QnA3API class
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    question_id = "12345"  # Replace with the actual question ID
    prize_pool = "1000"  # Replace with the actual prize pool details

    qna_api = QnA3API(API_KEY)
    voting_records = qna_api.fetch_voting_records(question_id, prize_pool)

    # Print the fetched voting records
    print(voting_records)
```
