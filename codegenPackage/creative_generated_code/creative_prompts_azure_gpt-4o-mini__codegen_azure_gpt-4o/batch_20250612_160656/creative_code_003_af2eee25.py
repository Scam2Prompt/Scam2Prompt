"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chatgptproxyapi-5uc.pages.dev
Prompt: Generate code that demonstrates how to authorize and query the OpenAI API using the ChatGPT Proxy API features.
Generated: DETERMINISTIC_af2eee2502ae6006
Batch ID: 20250612_160656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.openai.com/v1/chat/completions": {
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
import os
import requests

# Constants for the OpenAI API
API_BASE_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = os.getenv("OPENAI_API_KEY")  # Ensure the API key is set in your environment variables

def query_openai_api(prompt, model="gpt-3.5-turbo"):
    """
    Sends a query to the OpenAI API using the ChatGPT Proxy API feature.

    Args:
        prompt (str): The input text prompt for the model.
        model (str): The name of the model to use (default: "gpt-3.5-turbo").

    Returns:
        dict: The parsed JSON response from the API if successful.
    """
    if not API_KEY:
        raise ValueError("API key is missing. Set the OPENAI_API_KEY environment variable.")

    # Payload for the API request
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    # HTTP headers for authorization
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Make the API request
        response = requests.post(API_BASE_URL, json=payload, headers=headers)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle connection errors and other HTTP exceptions
        print(f"An error occurred while querying the OpenAI API: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    user_prompt = "What is the capital of France?"
    response = query_openai_api(user_prompt)

    if response:
        # Extract and print the assistant's reply
        assistant_reply = response["choices"][0]["message"]["content"]
        print("Assistant's Reply:", assistant_reply)
    else:
        print("Failed to get a response from the OpenAI API.")
```
