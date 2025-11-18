"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Provide a script that uses UniWrapper to integrate personal API keys for GPT and Claude, ensuring privacy while accessing AI models.
Generated: DETERMINISTIC_dcb198f46390a2a4
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# UniWrapper integration script for accessing GPT and Claude APIs securely
# This script ensures privacy and security while using personal API keys.

import os
import uniwrapper
from uniwrapper.providers import OpenAIProvider, AnthropicProvider

def load_api_keys():
    """
    Loads API keys from environment variables for security.
    Returns:
        dict: A dictionary containing API keys for GPT and Claude.
    """
    try:
        # Load API keys from environment variables
        gpt_api_key = os.getenv("GPT_API_KEY")
        claude_api_key = os.getenv("CLAUDE_API_KEY")
        
        if not gpt_api_key or not claude_api_key:
            raise ValueError("API keys are not set in the environment variables.")
        
        return {
            "gpt_api_key": gpt_api_key,
            "claude_api_key": claude_api_key
        }
    except Exception as e:
        # Handle missing or invalid API keys
        raise RuntimeError(f"Error loading API keys: {e}")

def main():
    """
    Main function to set up UniWrapper with GPT and Claude providers
    and demonstrate making requests to both models.
    """
    try:
        # Load API keys
        api_keys = load_api_keys()

        # Initialize GPT provider
        gpt_provider = OpenAIProvider(api_key=api_keys["gpt_api_key"])

        # Initialize Claude provider
        claude_provider = AnthropicProvider(api_key=api_keys["claude_api_key"])

        # Initialize UniWrapper with providers
        uni = uniwrapper.UniWrapper(providers=[gpt_provider, claude_provider])

        # Example request to GPT model
        gpt_response = uni.ask("GPT", "What is the capital of France?")
        print(f"GPT Response: {gpt_response}")

        # Example request to Claude model
        claude_response = uni.ask("Claude", "Explain the theory of relativity.")
        print(f"Claude Response: {claude_response}")

    except Exception as e:
        # Handle any runtime errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run the main function
    main()
```

### Instructions for Environment Setup:
1. Set your GPT and Claude API keys as environment variables:
   ```
   export GPT_API_KEY="your_openai_api_key_here"
   export CLAUDE_API_KEY="your_anthropic_api_key_here"
   ```
2. Install `uniwrapper` library (if not already installed):
   ```
   pip install uniwrapper
   ```
3. Run the script in a secure environment.
