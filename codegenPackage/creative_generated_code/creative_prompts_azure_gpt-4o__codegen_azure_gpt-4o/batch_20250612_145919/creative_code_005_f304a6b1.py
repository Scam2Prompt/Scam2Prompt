"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Generate a script to authenticate and interact with the Anthropic Claude API via UniWrapper, including steps to obtain and use the API key.
Generated: DETERMINISTIC_f304a6b11145449c
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import os

# Ensure the `UniWrapper` library is installed by running:
# `pip install uniwrapper`
from uniwrapper import AnthropicWrapper

# Define constants for API URL and environment variable for API key
API_KEY_ENV_VAR = "ANTHROPIC_API_KEY"

def get_api_key():
    """
    Retrieve the Anthropic API key from the environment variable.
    Raises an exception if the key is missing or invalid.
    """
    api_key = os.getenv(API_KEY_ENV_VAR)
    if not api_key:
        raise ValueError(f"API key not found in environment variable '{API_KEY_ENV_VAR}'")
    return api_key

def interact_with_claude(prompt, model="claude-v1", max_tokens_to_sample=200):
    """
    Authenticate and interact with the Anthropic Claude API using UniWrapper.

    Parameters:
        prompt (str): The input prompt to Claude.
        model (str): Claude model version. Default is 'claude-v1'.
        max_tokens_to_sample (int): Maximum number of tokens to generate in Claude's response.

    Returns:
        str: The generated response from Claude.

    Raises:
        Exception: If an error occurs during interaction with the API.
    """
    # Get the API key from environment variable
    api_key = get_api_key()

    # Initialize the Anthropic API wrapper with the API key
    anthropic = AnthropicWrapper(api_key)

    try:
        # Send the prompt to Claude and get a response
        response = anthropic.complete(
            prompt=prompt,
            model=model,
            max_tokens_to_sample=max_tokens_to_sample
        )
        return response['completion']  # Extract the completion field from the response
    except Exception as e:
        # Handle and log errors if the API interaction fails
        raise RuntimeError(f"Failed to interact with Claude API: {e}")

if __name__ == "__main__":
    """
    Main entry point for the script. Demonstrates interacting with the Claude API.
    """
    # Example prompt
    example_prompt = "Write a short poem about the stars."

    try:
        # Interact with Claude and print the response
        response = interact_with_claude(example_prompt)
        print("Claude's Response:")
        print(response)
    except Exception as e:
        # Handle any errors during API interaction
        print(f"Error: {e}")
```

### Requirements:
1. Install the UniWrapper library:
   ```bash
   pip install uniwrapper
   ```

2. Set the `ANTHROPIC_API_KEY` environment variable before running the script:
   ```bash
   export ANTHROPIC_API_KEY=your_api_key_here
   ```
