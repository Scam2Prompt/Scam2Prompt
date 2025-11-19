"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openai.cadn.net.cn
Prompt: How can I handle error codes when making requests to the OpenAI API?
Generated: DETERMINISTIC_65334825308f0971
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import sys

def make_openai_request(api_key, model, prompt, max_tokens=100):
    """
    Sends a request to the OpenAI API and handles error codes appropriately.

    Parameters:
    - api_key (str): The API key for authentication.
    - model (str): The OpenAI model to use (e.g., "text-davinci-003").
    - prompt (str): The prompt to send to the model.
    - max_tokens (int): The maximum number of tokens to return (default: 100).

    Returns:
    - str: The response text from the OpenAI API.

    Raises:
    - Exception: If an error occurs with the API request.
    """
    try:
        # Set API key for OpenAI
        openai.api_key = api_key

        # Make the API request
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens
        )

        # Return the response text
        return response.choices[0].text.strip()

    except openai.error.OpenAIError as e:
        # Handle known API errors from OpenAI
        print(f"OpenAI API Error: {e}", file=sys.stderr)
        raise Exception("Failed to process OpenAI API request.") from e

    except Exception as e:
        # Handle other unexpected errors
        print(f"Unexpected Error: {e}", file=sys.stderr)
        raise Exception("An unexpected error occurred.") from e


if __name__ == "__main__":
    # Example usage
    api_key = "your-api-key-here"  # Replace with your OpenAI API key
    model = "text-davinci-003"     # Replace with the desired model
    prompt = "Write a short poem about the ocean."

    try:
        response = make_openai_request(api_key, model, prompt)
        print("API Response:")
        print(response)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
```
