"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icursor.ai
Prompt: Write a code snippet to integrate an intelligent writing assistant that adapts its style and tone based on user input.
Generated: DETERMINISTIC_05c111cf25cfca1f
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai

# Define a class for the Intelligent Writing Assistant
class IntelligentWritingAssistant:
    def __init__(self, api_key):
        """
        Initializes the Intelligent Writing Assistant with the OpenAI API key.
        
        Args:
            api_key (str): Your OpenAI API key for authenticating requests.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_text(self, prompt, style=None, tone=None):
        """
        Generates text using the OpenAI API based on the provided prompt and optional style and tone.

        Args:
            prompt (str): The input text to guide the generation.
            style (str, optional): The desired writing style (e.g., formal, casual).
            tone (str, optional): The desired tone (e.g., friendly, professional).

        Returns:
            str: The generated text.
        
        Raises:
            ValueError: If the prompt is empty.
            Exception: If there is an error with the OpenAI API call.
        """
        if not prompt:
            raise ValueError("The prompt cannot be empty.")
        
        # Construct the prompt with the style and tone if provided
        styled_prompt = prompt
        if style:
            styled_prompt += f"\n\nPlease write in a {style} style."
        if tone:
            styled_prompt += f"\n\nPlease use a {tone} tone."

        try:
            # Call the OpenAI API to generate text
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Specify the model to use
                messages=[{"role": "user", "content": styled_prompt}]
            )
            # Extract the generated text from the response
            generated_text = response['choices'][0]['message']['content']
            return generated_text
        except Exception as e:
            # Handle any exceptions raised by the OpenAI API
            raise Exception("Error while generating text from the OpenAI API: " + str(e))

# Example usage
if __name__ == "__main__":
    # Replace 'your-api-key' with your actual OpenAI API key
    assistant = IntelligentWritingAssistant(api_key='your-api-key')
    
    try:
        # Get user input
        user_prompt = "Explain the importance of code quality in software development."
        style = "formal"
        tone = "professional"
        
        # Generate text based on the user input
        result = assistant.generate_text(user_prompt, style, tone)
        print("Generated Text:\n", result)
    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An error occurred:", e)
```
