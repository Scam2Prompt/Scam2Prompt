"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: How can I use UniWrapper to compare responses from Claude and GPT for the same input prompt?
Generated: DETERMINISTIC_f94420ba90be3e43
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from uniwrapper import Claude, GPT

# Define a function to compare responses from Claude and GPT
async def compare_responses(prompt: str):
    """
    Compare responses from Claude and GPT for a given input prompt.

    Args:
        prompt (str): The input prompt to send to both models.

    Returns:
        dict: A dictionary containing responses from both models.
    """
    # Initialize the models
    claude = Claude()
    gpt = GPT()

    try:
        # Send the prompt to Claude and GPT concurrently
        claude_response, gpt_response = await asyncio.gather(
            claude.generate(prompt),
            gpt.generate(prompt)
        )

        # Return the responses in a structured format
        return {
            "Claude": claude_response,
            "GPT": gpt_response
        }

    except Exception as e:
        # Handle any exceptions that occur during the API calls
        print(f"An error occurred while fetching responses: {e}")
        return {
            "Claude": None,
            "GPT": None,
            "error": str(e)
        }

# Main function to run the comparison
async def main():
    prompt = "What are the benefits of using async programming in Python?"
    responses = await compare_responses(prompt)

    # Print the responses for comparison
    print("Responses Comparison:")
    print(f"Claude: {responses['Claude']}")
    print(f"GPT: {responses['GPT']}")

# Entry point for the script
if __name__ == "__main__":
    asyncio.run(main())
```
