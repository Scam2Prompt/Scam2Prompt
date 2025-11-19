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
# Import necessary modules from UniWrapper
from uniwrapper import UniWrapper
from uniwrapper.models import Claude, GPT

# Error handling for exceptions that may occur during initialization or API calls
try:
    # Initialize UniWrapper
    uni_wrapper = UniWrapper()

    # Add AI models to the wrapper
    # Claude model initialization
    claude_model = Claude(api_key="your_claude_api_key")
    uni_wrapper.add_model("Claude", claude_model)

    # GPT model initialization
    gpt_model = GPT(api_key="your_gpt_api_key")
    uni_wrapper.add_model("GPT", gpt_model)

    # Function to interact with both models
    def interact_with_models(prompt):
        """
        Interacts with both Claude and GPT using the provided prompt.
        
        :param prompt: The input prompt for the AI models.
        :return: A dictionary containing responses from both models.
        """
        responses = {}
        try:
            # Get response from Claude
            responses["Claude"] = uni_wrapper.get_model("Claude").generate_response(prompt)

            # Get response from GPT
            responses["GPT"] = uni_wrapper.get_model("GPT").generate_response(prompt)

        except Exception as e:
            # Handle errors during model interaction
            print(f"Error interacting with models: {e}")
            responses["error"] = str(e)

        return responses

    # Example usage of the interact_with_models function
    if __name__ == "__main__":
        # Prompt to be sent to the AI models
        user_prompt = "Explain the concept of machine learning in simple terms."

        # Fetch responses from both Claude and GPT
        model_responses = interact_with_models(user_prompt)

        # Print responses
        print("Responses from AI models:")
        for model_name, response in model_responses.items():
            if model_name != "error":
                print(f"{model_name}: {response}")
            else:
                print("Error occurred:", response)

except Exception as e:
    # Handle exceptions during initialization
    print(f"Error setting up UniWrapper or models: {e}")
```
