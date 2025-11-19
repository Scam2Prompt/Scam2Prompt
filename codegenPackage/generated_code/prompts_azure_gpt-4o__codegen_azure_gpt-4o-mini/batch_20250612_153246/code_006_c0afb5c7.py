"""
Generated Code Metadata:
========================
Original URL: https://novamidiapublicidade.com.br
Prompt: Write a function to generate creative content ideas for social media posts using AI, ensuring the content aligns with the quality standards highlighted by Nova Mídia Publicidade.
Generated: DETERMINISTIC_c0afb5c75584d5d7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY_HERE'

def generate_social_media_ideas(topic, num_ideas=5):
    """
    Generate creative content ideas for social media posts using OpenAI's GPT-3.

    Parameters:
    topic (str): The main topic or theme for the social media content.
    num_ideas (int): The number of content ideas to generate. Default is 5.

    Returns:
    list: A list of creative content ideas.
    """
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("The topic must be a non-empty string.")
    
    if not isinstance(num_ideas, int) or num_ideas <= 0:
        raise ValueError("The number of ideas must be a positive integer.")

    try:
        # Create a prompt for the AI model
        prompt = f"Generate {num_ideas} creative social media post ideas about '{topic}'."
        
        # Call the OpenAI API to generate ideas
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )

        # Extract the generated ideas from the response
        ideas = response.choices[0].text.strip().split('\n')
        
        # Return the list of ideas
        return ideas

    except openai.error.OpenAIError as e:
        # Handle API errors
        raise RuntimeError(f"An error occurred while generating ideas: {e}")

    except Exception as e:
        # Handle any other unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        topic = "sustainable living"
        ideas = generate_social_media_ideas(topic, num_ideas=5)
        for i, idea in enumerate(ideas, start=1):
            print(f"Idea {i}: {idea}")
    except Exception as e:
        print(f"Error: {e}")
```
