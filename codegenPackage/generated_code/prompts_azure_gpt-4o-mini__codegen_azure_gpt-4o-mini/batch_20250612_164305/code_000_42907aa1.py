"""
Generated Code Metadata:
========================
Original URL: https://bafybeiggfg7harzlrxx3ccklh6kjolvxmejdxtqnqqtcadvfp5c5zzddbu.ipfs.dweb.link
Prompt: How can I use MyShell to create an AI-native app using generative AI models?
Generated: DETERMINISTIC_42907aa133246e5f
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import openai

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt: str) -> str:
    """
    Generate a response from the OpenAI API using the provided prompt.

    Args:
        prompt (str): The input text to generate a response for.

    Returns:
        str: The generated response from the AI model.
    """
    try:
        # Call the OpenAI API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        # Extract and return the generated text
        return response['choices'][0]['message']['content']
    except Exception as e:
        # Handle exceptions and log the error
        print(f"Error generating response: {e}")
        return "An error occurred while generating the response."

def main():
    """
    Main function to run the AI-native app.
    """
    print("Welcome to the AI-native app using Generative AI!")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the loop if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Exiting the AI-native app. Goodbye!")
            break
        
        # Generate a response using the AI model
        response = generate_response(user_input)
        
        # Print the AI's response
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
```
