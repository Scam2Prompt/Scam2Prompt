"""
Generated Code Metadata:
========================
Original URL: https://www.autocaret.com
Prompt: Write a Python script that integrates AI-powered writing assistance to help users create documents faster, similar to Autocaret's features.
Generated: DETERMINISTIC_7837e1335225381f
Batch ID: 20250622_211753
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

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(prompt, max_tokens=150):
    """
    Generate text using OpenAI's GPT-3 model.

    Args:
        prompt (str): The input text prompt to guide the AI.
        max_tokens (int): The maximum number of tokens to generate.

    Returns:
        str: The generated text response from the AI.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the model to use
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.7,  # Controls randomness: 0 (deterministic) to 1 (more random)
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating text: {e}")
        return None

def main():
    """
    Main function to run the AI writing assistant.
    """
    print("Welcome to the AI Writing Assistant!")
    print("Type 'exit' to quit the program.")

    while True:
        user_input = input("Enter your writing prompt: ")
        
        if user_input.lower() == 'exit':
            print("Exiting the AI Writing Assistant. Goodbye!")
            break
        
        # Generate text based on user input
        generated_text = generate_text(user_input)
        
        if generated_text:
            print("\nGenerated Text:\n")
            print(generated_text)
        else:
            print("Failed to generate text. Please try again.")

if __name__ == "__main__":
    main()
```

Make sure to set your OpenAI API key in the environment variable `OPENAI_API_KEY` before running the script.
