"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Generate a code snippet that demonstrates how to use UniWrapper for multi-model AI interactions with Claude and GPT.
Generated: DETERMINISTIC_d2d06cc08ca2b536
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
from uni_wrapper import UniWrapper
import logging

# Set up logging configuration for better debugging and monitoring
logging.basicConfig(level=logging.INFO)

def main():
    try:
        # Initialize UniWrapper with Claude and GPT models
        # Replace 'YOUR_CLAUDE_API_KEY' and 'YOUR_GPT_API_KEY' with actual API keys
        models = {
            'claude': 'YOUR_CLAUDE_API_KEY',
            'gpt': 'YOUR_GPT_API_KEY'
        }
        
        # Create an instance of UniWrapper
        uni_wrapper = UniWrapper(models)

        # Example input for multi-model interaction
        user_input = "What is the capital of France?"

        # Get response from Claude model
        claude_response = uni_wrapper.query('claude', user_input)
        logging.info(f"Claude's response: {claude_response}")

        # Get response from GPT model
        gpt_response = uni_wrapper.query('gpt', user_input)
        logging.info(f"GPT's response: {gpt_response}")

        # Example of processing both responses
        combined_response = f"Claude says: {claude_response}\nGPT says: {gpt_response}"
        logging.info(combined_response)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
