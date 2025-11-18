"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Write Python code to interact with multiple AI models using UniWrapper's interface, allowing comparison of responses from GPT and Claude based on a single prompt.
Generated: DETERMINISTIC_8e8afac8efc7da23
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uniwrapper
import logging

# Configure logging to capture errors and debug information
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class AIModelComparator:
    """
    A class to interact with multiple AI models using UniWrapper's interface 
    and compare responses based on a single prompt.
    """
    
    def __init__(self, gpt_key: str, claude_key: str):
        """
        Initializes the AIModelComparator with API keys for GPT and Claude.

        Args:
            gpt_key (str): API key for GPT model.
            claude_key (str): API key for Claude model.
        """
        try:
            self.gpt_client = uniwrapper.UniWrapper(model="gpt", api_key=gpt_key)
            self.claude_client = uniwrapper.UniWrapper(model="claude", api_key=claude_key)
            logging.info("Successfully initialized GPT and Claude clients.")
        except Exception as e:
            logging.error(f"Failed to initialize AI model clients: {e}")
            raise

    def get_responses(self, prompt: str):
        """
        Fetches responses for a given prompt from GPT and Claude models.

        Args:
            prompt (str): The input prompt to send to the AI models.

        Returns:
            dict: A dictionary containing responses from GPT and Claude.
        """
        try:
            logging.info(f"Sending prompt to GPT: {prompt}")
            gpt_response = self.gpt_client.get_response(prompt)
            logging.info("Received response from GPT.")

            logging.info(f"Sending prompt to Claude: {prompt}")
            claude_response = self.claude_client.get_response(prompt)
            logging.info("Received response from Claude.")
            
            return {
                "GPT": gpt_response,
                "Claude": claude_response
            }
        except Exception as e:
            logging.error(f"Error while fetching responses: {e}")
            raise

    def compare_responses(self, responses: dict):
        """
        Compares and prints responses from GPT and Claude models.

        Args:
            responses (dict): A dictionary containing responses from GPT and Claude.
        """
        try:
            gpt_response = responses.get("GPT", "No response from GPT.")
            claude_response = responses.get("Claude", "No response from Claude.")
            
            print("=== GPT Response ===")
            print(gpt_response)
            print("\n=== Claude Response ===")
            print(claude_response)
        except Exception as e:
            logging.error(f"Error while comparing responses: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    gpt_api_key = "your_gpt_api_key_here"
    claude_api_key = "your_claude_api_key_here"

    # Initialize the comparator
    comparator = AIModelComparator(gpt_key=gpt_api_key, claude_key=claude_api_key)

    # Get user input prompt
    user_prompt = input("Enter your prompt: ")

    try:
        # Fetch responses
        responses = comparator.get_responses(user_prompt)
        
        # Compare responses
        comparator.compare_responses(responses)
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")
```
