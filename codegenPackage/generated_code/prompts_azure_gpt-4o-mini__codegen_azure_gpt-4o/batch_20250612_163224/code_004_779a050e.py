"""
Generated Code Metadata:
========================
Original URL: https://coach-chatgpt.com
Prompt: What are some examples of using ChatGPT for content generation in marketing posts?
Generated: DETERMINISTIC_779a050e53b17102
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import openai
import os

# Function to generate marketing content using ChatGPT
def generate_marketing_content(prompt, api_key, model="gpt-4"):
    """
    Generates marketing content using OpenAI's ChatGPT.

    Parameters:
        prompt (str): The input prompt describing the type of marketing content to generate.
        api_key (str): Your OpenAI API key for authentication.
        model (str): The model to use for content generation (default is 'gpt-4').

    Returns:
        str: The generated marketing content.
    """
    try:
        # Initialize OpenAI API with the provided API key
        openai.api_key = api_key

        # Call the OpenAI API to generate content
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant skilled in marketing content generation."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and return the generated content
        return response['choices'][0]['message']['content']

    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        return f"An error occurred while generating content: {str(e)}"

    except Exception as e:
        # Handle other unexpected errors
        return f"An unexpected error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Load API key from environment variable (best practice for security)
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    else:
        # Define the prompt for marketing content generation
        prompt = "Generate a social media post promoting a new eco-friendly water bottle."

        # Generate the marketing content
        content = generate_marketing_content(prompt, api_key)

        # Print the generated content
        print("Generated Marketing Content:")
        print(content)
```
