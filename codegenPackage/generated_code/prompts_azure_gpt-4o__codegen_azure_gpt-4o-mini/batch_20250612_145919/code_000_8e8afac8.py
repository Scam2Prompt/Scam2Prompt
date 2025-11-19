"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: Write Python code to interact with multiple AI models using UniWrapper's interface, allowing comparison of responses from GPT and Claude based on a single prompt.
Generated: DETERMINISTIC_8e8afac8efc7da23
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from uniwrapper import UniWrapper, Model

# Define a class to interact with multiple AI models
class AIModelComparer:
    def __init__(self, prompt: str):
        """
        Initialize the AIModelComparer with a prompt.

        :param prompt: The input prompt to send to the AI models.
        """
        self.prompt = prompt
        self.uni_wrapper = UniWrapper()

    async def get_response(self, model: Model) -> str:
        """
        Get a response from a specified AI model.

        :param model: The AI model to query (e.g., GPT or Claude).
        :return: The response from the AI model.
        """
        try:
            response = await self.uni_wrapper.query(model, self.prompt)
            return response
        except Exception as e:
            # Log the error and return a message
            print(f"Error querying {model.name}: {e}")
            return f"Error querying {model.name}"

    async def compare_models(self):
        """
        Compare responses from GPT and Claude models based on the prompt.
        """
        # Define the models to compare
        models = [Model.GPT, Model.CLAUDE]

        # Create a list of tasks to fetch responses concurrently
        tasks = [self.get_response(model) for model in models]

        # Gather responses from all models
        responses = await asyncio.gather(*tasks)

        # Print the responses for comparison
        for model, response in zip(models, responses):
            print(f"Response from {model.name}:\n{response}\n")

def main():
    """
    Main function to execute the AI model comparison.
    """
    prompt = "What are the benefits of using AI in software development?"
    
    # Create an instance of AIModelComparer
    comparer = AIModelComparer(prompt)

    # Run the comparison in an asyncio event loop
    asyncio.run(comparer.compare_models())

if __name__ == "__main__":
    main()
```
