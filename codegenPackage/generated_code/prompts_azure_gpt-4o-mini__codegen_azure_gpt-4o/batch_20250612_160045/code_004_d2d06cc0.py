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
# Import necessary modules from UniWrapper
from uniwrapper import UniWrapper, AIModel

# Define a function to demonstrate multi-model AI interactions
def multi_model_interaction():
    """
    Demonstrates how to use UniWrapper for multi-model AI interactions
    with Claude and GPT.
    """
    try:
        # Initialize UniWrapper
        wrapper = UniWrapper()

        # Add Claude model to the wrapper
        claude_model = AIModel(name="Claude", api_key="your_claude_api_key")
        wrapper.add_model(claude_model)

        # Add GPT model to the wrapper
        gpt_model = AIModel(name="GPT", api_key="your_gpt_api_key")
        wrapper.add_model(gpt_model)

        # Define a prompt to interact with both models
        prompt = "Explain the concept of recursion in programming."

        # Interact with Claude model
        claude_response = wrapper.query_model("Claude", prompt)
        print("Claude's Response:")
        print(claude_response)

        # Interact with GPT model
        gpt_response = wrapper.query_model("GPT", prompt)
        print("\nGPT's Response:")
        print(gpt_response)

    except Exception as e:
        # Handle any errors that occur during the interaction
        print(f"An error occurred: {e}")

# Run the multi-model interaction function
if __name__ == "__main__":
    multi_model_interaction()
```

Note: Replace `"your_claude_api_key"` and `"your_gpt_api_key"` with the actual API keys for Claude and GPT models. Ensure that the `uniwrapper` library is installed and properly configured in your environment.
