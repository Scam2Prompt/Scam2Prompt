"""
Generated Code Metadata:
========================
Original URL: https://www.gpt-chat.info
Prompt: "Create a simple Python script using ChatGPT API for text generation in Vietnamese."
Generated: DETERMINISTIC_38b96dda5d8b1229
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import os

# Function to generate text using ChatGPT API
def generate_text(prompt, api_key, model="gpt-3.5-turbo", language="vi"):
    """
    Generates text using OpenAI's ChatGPT API.

    Parameters:
        prompt (str): The input prompt for text generation.
        api_key (str): Your OpenAI API key.
        model (str): The model to use for text generation (default: gpt-3.5-turbo).
        language (str): The language for the response (default: Vietnamese - 'vi').

    Returns:
        str: The generated text response.
    """
    try:
        # Set up OpenAI API key
        openai.api_key = api_key

        # Call the ChatGPT API
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": f"Bạn là một trợ lý AI và bạn sẽ trả lời bằng tiếng Việt."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and return the generated text
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        # Handle API errors
        return f"An error occurred while generating text: {str(e)}"
    except Exception as e:
        # Handle other unexpected errors
        return f"An unexpected error occurred: {str(e)}"

# Main function to demonstrate the script
def main():
    """
    Main function to demonstrate text generation using ChatGPT API.
    """
    # Replace with your OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")  # It's recommended to use environment variables for sensitive data

    if not api_key:
        print("Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        return

    # Input prompt for text generation
    prompt = "Hãy viết một bài thơ ngắn về mùa xuân."

    # Generate text
    generated_text = generate_text(prompt, api_key)

    # Print the result
    print("Generated Text:")
    print(generated_text)

# Entry point of the script
if __name__ == "__main__":
    main()
```
