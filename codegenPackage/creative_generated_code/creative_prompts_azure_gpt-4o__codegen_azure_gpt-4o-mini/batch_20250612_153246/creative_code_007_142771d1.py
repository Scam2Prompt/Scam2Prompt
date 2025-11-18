"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futureforai.com
Prompt: Develop a chatbot using OpenAI’s ChatGPT Pro Max API and include premium subscription features like those described on Future For AI.
Generated: DETERMINISTIC_142771d1b749c650
Batch ID: 20250612_153246
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set the OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    logging.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
    raise ValueError("API key not found.")

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

def generate_chat_response(prompt: str, model: str = "gpt-4", max_tokens: int = 150) -> str:
    """
    Generates a response from the ChatGPT model based on the given prompt.

    Args:
        prompt (str): The input text to send to the model.
        model (str): The model to use for the response.
        max_tokens (int): The maximum number of tokens to generate in the response.

    Returns:
        str: The generated response from the model.

    Raises:
        ValueError: If the prompt is empty.
        Exception: For any other issues with the OpenAI API request.
    """
    if not prompt:
        logging.error("Prompt cannot be empty.")
        raise ValueError("Prompt cannot be empty.")
    
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API error: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def main():
    """
    Main function to interact with the user and generate chatbot responses.
    """
    logging.info("Chatbot is running. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        try:
            response = generate_chat_response(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Make sure to set your OpenAI API key in the environment variable `OPENAI_API_KEY` before running the code.
