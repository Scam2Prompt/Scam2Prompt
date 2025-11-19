"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: How can I use UniWrapper to compare responses from Claude and GPT for the same input prompt?
Generated: DETERMINISTIC_f94420ba90be3e43
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from uniwrapper import Wrapper
import json

# Initialize the API wrappers for Claude and GPT
claude_wrapper = Wrapper(api_key='YOUR_CLAUDE_API_KEY', model='claude')
gpt_wrapper = Wrapper(api_key='YOUR_GPT_API_KEY', model='gpt')

def compare_responses(prompt: str) -> None:
    """
    Compare responses from Claude and GPT for a given input prompt.

    Parameters:
    prompt (str): The input prompt to be sent to both models.

    Returns:
    None
    """
    try:
        # Get response from Claude
        claude_response = claude_wrapper.get_response(prompt)
        
        # Get response from GPT
        gpt_response = gpt_wrapper.get_response(prompt)
        
        # Print out the responses for comparison
        print("Claude's Response:")
        print(json.dumps(claude_response, indent=4))
        
        print("\nGPT's Response:")
        print(json.dumps(gpt_response, indent=4))

    except Exception as e:
        # Handle exceptions during API calls
        print(f"An error occurred while comparing responses: {e}")

# Example usage
if __name__ == "__main__":
    user_prompt = "Explain the significance of the Turing Test in AI."
    compare_responses(user_prompt)
```

**Note**: Replace `YOUR_CLAUDE_API_KEY` and `YOUR_GPT_API_KEY` with your actual API keys. The `uniwrapper` library should be installed and configured prior to running this code.
