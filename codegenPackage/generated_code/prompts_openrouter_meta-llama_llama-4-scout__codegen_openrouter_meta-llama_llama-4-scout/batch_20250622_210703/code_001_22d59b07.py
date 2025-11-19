"""
Generated Code Metadata:
========================
Original URL: https://futureforai.com
Prompt: Generate a code snippet demonstrating how to integrate DeepSeek R1's cost-effective AI model into a natural language processing (NLP) application.
Generated: DETERMINISTIC_22d59b07ee5866ed
Batch ID: 20250622_210703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.deepseekr1.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
import json

class DeepSeekR1Client:
    """
    A client for interacting with the DeepSeek R1 AI model.
    """

    def __init__(self, api_key, base_url="https://api.deepseekr1.com"):
        """
        Initializes the client with an API key and base URL.

        Args:
            api_key (str): The API key for authenticating requests.
            base_url (str): The base URL for the DeepSeek R1 API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _handle_response(self, response):
        """
        Handles the response from the DeepSeek R1 API.

        Args:
            response (requests.Response): The response from the API.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the response was not successful.
        """
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"Other error occurred: {err}")

        return response.json()

    def generate_text(self, prompt, max_length=1024):
        """
        Generates text using the DeepSeek R1 AI model.

        Args:
            prompt (str): The prompt for generating text.
            max_length (int): The maximum length of the generated text.

        Returns:
            dict: The response from the API, including the generated text.

        Raises:
            Exception: If an error occurs while generating text.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "prompt": prompt,
            "max_length": max_length
        }

        response = requests.post(
            f"{self.base_url}/generate",
            headers=headers,
            data=json.dumps(data)
        )

        return self._handle_response(response)

    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of the given text using the DeepSeek R1 AI model.

        Args:
            text (str): The text to analyze.

        Returns:
            dict: The response from the API, including the sentiment analysis.

        Raises:
            Exception: If an error occurs while analyzing sentiment.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "text": text
        }

        response = requests.post(
            f"{self.base_url}/sentiment",
            headers=headers,
            data=json.dumps(data)
        )

        return self._handle_response(response)


def main():
    # Replace with your DeepSeek R1 API key
    api_key = "your_api_key_here"

    client = DeepSeekR1Client(api_key)

    # Example usage: Generate text
    prompt = "Tell me a story about a character who learns a new skill."
    try:
        response = client.generate_text(prompt)
        print(json.dumps(response, indent=4))
    except Exception as e:
        print(f"Error generating text: {e}")

    # Example usage: Analyze sentiment
    text = "I love using the DeepSeek R1 AI model!"
    try:
        response = client.analyze_sentiment(text)
        print(json.dumps(response, indent=4))
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")


if __name__ == "__main__":
    main()
```
