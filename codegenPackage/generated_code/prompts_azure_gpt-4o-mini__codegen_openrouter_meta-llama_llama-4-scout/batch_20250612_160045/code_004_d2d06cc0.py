"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: Generate a code snippet that demonstrates how to use UniWrapper for multi-model AI interactions with Claude and GPT.
Generated: DETERMINISTIC_d2d06cc08ca2b536
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List
import anthropic
import openai

class UniWrapper:
    """
    A unified wrapper for interacting with multiple AI models.
    """

    def __init__(self, claude_api_key: str, gpt_api_key: str):
        """
        Initialize the UniWrapper with API keys for Claude and GPT.

        Args:
        - claude_api_key (str): The API key for Claude.
        - gpt_api_key (str): The API key for GPT.
        """
        self.claude_client = anthropic.Client(api_key=claude_api_key)
        self.gpt_client = openai.Client(api_key=gpt_api_key)

    def claude_generate(self, prompt: str, max_tokens: int = 1024) -> Dict:
        """
        Generate text using the Claude model.

        Args:
        - prompt (str): The input prompt.
        - max_tokens (int): The maximum number of tokens to generate.

        Returns:
        - Dict: The response from the Claude model.
        """
        try:
            response = self.claude_client.completions.create(
                model="claude-2",
                prompt=prompt,
                max_tokens_to_sample=max_tokens,
            )
            return response
        except Exception as e:
            print(f"Error generating text with Claude: {e}")
            return {}

    def gpt_generate(self, prompt: str, max_tokens: int = 1024) -> Dict:
        """
        Generate text using the GPT model.

        Args:
        - prompt (str): The input prompt.
        - max_tokens (int): The maximum number of tokens to generate.

        Returns:
        - Dict: The response from the GPT model.
        """
        try:
            response = self.gpt_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"content": prompt, "role": "user"}],
                max_tokens=max_tokens,
            )
            return response
        except Exception as e:
            print(f"Error generating text with GPT: {e}")
            return {}

def main():
    # Replace with your actual API keys
    claude_api_key = "YOUR_CLAUDE_API_KEY"
    gpt_api_key = "YOUR_GPT_API_KEY"

    uni_wrapper = UniWrapper(claude_api_key, gpt_api_key)

    # Example usage
    prompt = "Tell me a story about a character who learns a new skill."
    claude_response = uni_wrapper.claude_generate(prompt)
    gpt_response = uni_wrapper.gpt_generate(prompt)

    print("Claude Response:")
    print(claude_response)
    print("\nGPT Response:")
    print(gpt_response)

if __name__ == "__main__":
    main()
```
