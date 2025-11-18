"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Suggest a Python library for creating a chatbot that can answer questions about ISIV's academic programs, such as "Excel Avanzado" or "Contabilidad Básica."
Generated: DETERMINISTIC_cea31c241065e673
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from the `openai` library to create a chatbot
# This code uses OpenAI's API to handle chatbot interactions
import openai
import os

def create_chatbot(prompt):
    """
    Function to create a chatbot using OpenAI's GPT model.
    It generates responses to questions about ISIV's academic programs.

    Args:
        prompt (str): The user's query about ISIV's academic programs.

    Returns:
        str: The chatbot's response.
    """

    # Load the OpenAI API key from environment variables for security
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    # Configure the OpenAI API client
    openai.api_key = api_key

    try:
        # Make a request to OpenAI's GPT model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the GPT model suitable for chat-based interactions
            messages=[
                {"role": "system", "content": "You are a helpful assistant providing information about ISIV's academic programs."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,  # Limit the response length
            temperature=0.7  # Control randomness in the output
        )
        # Extract and return the chatbot's response
        return response.choices[0].message["content"].strip()

    except openai.error.OpenAIError as e:
        # Handle API errors gracefully
        return f"An error occurred while processing your request: {str(e)}"

# Example usage
if __name__ == "__main__":
    print("Welcome to ISIV's academic program chatbot!")
    try:
        user_query = input("Ask about ISIV's academic programs (e.g., 'Excel Avanzado'): ")
        response = create_chatbot(user_query)
        print("Chatbot response:", response)
    except ValueError as ve:
        print("Configuration error:", ve)
    except Exception as e:
        print("Unexpected error:", e)
```

### Notes:
1. To run this code, you need an OpenAI API key. Set it up as an environment variable `OPENAI_API_KEY`.
2. Make sure you have the OpenAI Python library installed (`pip install openai`).
