"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openai.cadn.net.cn
Prompt: Can you provide an example of how to implement structured output with the OpenAI API in a chat application?
Generated: DETERMINISTIC_373e3bac96a21038
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chat_response(messages):
    """
    Function to get a structured response from OpenAI's Chat API.

    Args:
        messages (list): A list of messages in the chat format, where each message
                         is a dictionary with 'role' and 'content' keys.

    Returns:
        dict: The structured response from the API, including 'role' and 'content'.
    """
    try:
        # Call the OpenAI Chat API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model to use
            messages=messages,
            temperature=0.7,        # Control the randomness of the output
            max_tokens=150          # Maximum number of tokens to generate
        )
        return response.choices[0].message  # Return the message part of the response

    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        print(f"OpenAI API error: {e}")
        return {"role": "error", "content": str(e)}

    except Exception as e:
        # Handle general exceptions
        print(f"An unexpected error occurred: {e}")
        return {"role": "error", "content": "An unexpected error occurred."}

def main():
    """
    Main function to simulate a chat application interaction.
    """

    # Initial messages for the chat
    chat_history = [
        {"role": "user", "content": "Hello, how can I improve my coding skills?"},
        {"role": "assistant", "content": "Practice regularly and work on projects!"}
    ]

    # Get a response from the OpenAI API
    response = get_chat_response(chat_history)

    # Print the structured output
    if response.get("role") != "error":
        print("Assistant:", response["content"])
    else:
        print("Error:", response["content"])

if __name__ == "__main__":
    main()
```
