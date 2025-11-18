"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://relivo.se
Prompt: Create a chatbot using a natural language processing library that answers customer questions about Relivo’s ingredients, health benefits, and usage instructions based on the FAQ section.
Generated: DETERMINISTIC_5e28f765cc269746
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import openai

# Load environment variables for API keys (Recommended best practice for sensitive information)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure OpenAI API Key
if not OPENAI_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

openai.api_key = OPENAI_API_KEY

# Predefined FAQ content (replace with real FAQ data)
FAQ_CONTEXT = """
Relivo is a health supplement known for its natural ingredients, health benefits, and easy usage instructions.

Ingredients:
- Relivo is made of herbal extracts like Ashwagandha, Tulsi, and Ginger.

Health Benefits:
- Reduces stress and promotes relaxation.
- Boosts immune system function.
- Aids in digestion and overall gut health.

Usage Instructions:
- Take one capsule daily with water after a meal.
- Consult your doctor before use if pregnant, nursing, or under medication.
"""

# Function to generate a chatbot response
def chatbot_response(user_query):
    """
    This function takes a user query as input, uses OpenAI's GPT model to generate a response
    based on the FAQ_CONTEXT, and returns the response.

    Parameters:
        user_query (str): The customer's question about Relivo.
    
    Returns:
        str: The chatbot's response to the query.
    """
    try:
        # Use OpenAI's ChatGPT API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT model
            prompt=f"The following is a conversation with a chatbot that provides information about Relivo's ingredients, health benefits, and usage instructions based on the FAQ section.\n\nFAQ:\n{FAQ_CONTEXT}\n\nUser: {user_query}\nChatbot:",
            max_tokens=150,  # Limit tokens to control the length of the response
            temperature=0.7,  # Balance creativity and relevance
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Extract and return the chatbot's reply
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors gracefully
        return f"An error occurred while generating the response: {str(e)}"


# Main entry point for testing the chatbot
if __name__ == "__main__":
    print("Relivo Chatbot - Ask me anything about Relivo!")
    print("Type 'exit' to end the chat.\n")

    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the chat if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Get chatbot response and display it
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
```
