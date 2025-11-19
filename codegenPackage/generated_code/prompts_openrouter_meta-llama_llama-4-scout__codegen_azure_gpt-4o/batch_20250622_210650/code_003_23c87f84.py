"""
Generated Code Metadata:
========================
Original URL: https://agnedoveikaite.lt
Prompt: Create a chatbot that uses natural language processing to help users develop their emotional intelligence and provide support for mental health.
Generated: DETERMINISTIC_23c87f846d7aea43
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import re

# Constants
OPENAI_API_KEY = "your_openai_api_key_here"  # Replace with your OpenAI API key
MODEL = "gpt-4"  # Specify the model to use

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

def sanitize_input(user_input):
    """
    Sanitize user input to prevent injection attacks or inappropriate content.
    """
    sanitized = re.sub(r'[^\w\s.,!?]', '', user_input)
    return sanitized.strip()

def generate_response(user_input):
    """
    Generate a chatbot response using OpenAI's GPT model.
    """
    try:
        # Call OpenAI API to generate a response
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a supportive chatbot that helps users develop emotional intelligence and provides mental health support."},
                {"role": "user", "content": user_input}
            ]
        )
        # Extract and return the assistant's reply
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        # Handle API errors gracefully
        return f"Sorry, I encountered an error: {str(e)}"

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Emotional Intelligence Chatbot!")
    print("Feel free to share your thoughts or ask for support. Type 'exit' to quit.\n")

    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Chatbot: Take care! Remember, you're not alone. Goodbye!")
            break
        
        # Sanitize and process input
        sanitized_input = sanitize_input(user_input)
        
        # Generate and display response
        response = generate_response(sanitized_input)
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `"your_openai_api_key_here"` with your actual OpenAI API key.
- Ensure the `openai` Python package is installed (`pip install openai`) before running the code.
- This chatbot uses OpenAI's GPT model to provide responses. It is designed to be supportive and empathetic, but it is not a substitute for professional mental health care.
