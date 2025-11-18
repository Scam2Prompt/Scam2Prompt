"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openai.cadn.net.cn
Prompt: Create a code snippet demonstrating how to use OpenAI's batch processing API for asynchronous large-scale text generation tasks.
Generated: DETERMINISTIC_f8e1a0cd7f6d4ca8
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import openai
from typing import List

# Set your OpenAI API key here
openai.api_key = "your_api_key_here"

async def generate_text(prompt: str, model: str = "text-davinci-003") -> str:
    """
    Asynchronously generates text using OpenAI's API.

    Args:
        prompt (str): The input prompt for text generation.
        model (str): The model to be used for text generation. Defaults to 'text-davinci-003'.

    Returns:
        str: The generated text.
    """
    try:
        response = await openai.Completion.acreate(
            model=model,
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )
        # Extract generated text from the API response
        return response['choices'][0]['text'].strip()
    except Exception as e:
        # Log the error and handle it gracefully
        print(f"Error generating text for prompt '{prompt}': {e}")
        return ""

async def process_batch(prompts: List[str]) -> List[str]:
    """
    Processes a batch of text generation prompts asynchronously.

    Args:
        prompts (List[str]): A list of input prompts.

    Returns:
        List[str]: A list of generated texts corresponding to the prompts.
    """
    # Use asyncio.gather to run multiple tasks concurrently
    tasks = [generate_text(prompt) for prompt in prompts]
    return await asyncio.gather(*tasks)

def main():
    """
    Main entry point for batch processing.
    """
    # Example prompts for text generation
    prompts = [
        "Write a poem about the ocean.",
        "Explain the concept of recursion in computer science.",
        "Summarize the plot of Hamlet in 100 words."
    ]

    # Run the event loop for batch processing
    try:
        generated_texts = asyncio.run(process_batch(prompts))
        # Print the results
        for i, prompt in enumerate(prompts):
            print(f"Prompt: {prompt}")
            print(f"Generated Text: {generated_texts[i]}")
            print("-" * 40)
    except Exception as e:
        # Graceful error handling for the main function
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
