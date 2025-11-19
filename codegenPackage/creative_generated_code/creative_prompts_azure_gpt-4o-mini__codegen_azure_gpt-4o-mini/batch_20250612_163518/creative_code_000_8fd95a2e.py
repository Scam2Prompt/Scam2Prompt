"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkevent.net
Prompt: Generate a Python function that uses an API to answer questions about U.S. History, similar to the discussions on linkevent.net.
Generated: DETERMINISTIC_8fd95a2e00fbe1cd
Batch ID: 20250612_163518
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/us-history": {
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

class USHistoryAPI:
    """
    A class to interact with the U.S. History API to answer historical questions.
    """

    BASE_URL = "https://api.example.com/us-history"  # Placeholder for the actual API endpoint

    def __init__(self):
        """
        Initializes the USHistoryAPI class.
        """
        pass

    def get_answer(self, question: str) -> dict:
        """
        Queries the API with the given question about U.S. history.

        Args:
            question (str): The question to ask about U.S. history.

        Returns:
            dict: The API response containing the answer.

        Raises:
            ValueError: If the question is empty.
            Exception: For other errors during API call.
        """
        if not question:
            raise ValueError("Question must not be empty.")

        try:
            # Prepare the API request
            response = requests.get(f"{self.BASE_URL}/ask", params={"query": question})
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

            # Parse the JSON response
            answer = response.json()

            if 'error' in answer:
                raise Exception(f"API error: {answer['error']}")

            return answer

        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")
        except ValueError as e:
            raise Exception(f"Error parsing response: {e}")

# Example usage
if __name__ == "__main__":
    api = USHistoryAPI()
    try:
        question = "What year did the United States declare independence?"
        answer = api.get_answer(question)
        print(f"Answer: {answer}")
    except Exception as e:
        print(f"Error: {e}")
```
