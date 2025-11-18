"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ferramentaspremimum.shop
Prompt: Write Python code that uses ChatGPT's unlocked version to generate multiple variations of ad copy for A/B testing.
Generated: DETERMINISTIC_301f05d656934039
Batch ID: 20250612_154333
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

# Set the OpenAI API key from environment variables for security
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

def generate_ad_copy(prompt: str, variations: int) -> list:
    """
    Generate multiple variations of ad copy using OpenAI's GPT-3 model.
    
    Args:
        prompt (str): The base prompt for generating ad copy.
        variations (int): The number of variations to generate.
        
    Returns:
        list: A list containing the generated ad copy variations.
        
    Raises:
        ValueError: If variations is less than 1.
        Exception: If the API call fails for any reason.
    """
    
    if variations < 1:
        raise ValueError("The number of variations must be at least 1.")
    
    ad_copies = []
    
    try:
        for _ in range(variations):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,  # Define a limit on the number of tokens
                n=1,
                stop=None
            )
            ad_copy = response.choices[0].message['content'].strip()
            ad_copies.append(ad_copy)
    
    except openai.error.OpenAIError as e:
        # Handle API errors
        print(f"An error occurred while communicating with OpenAI: {e}")
        raise
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        raise

    return ad_copies

if __name__ == "__main__":
    # Example usage
    prompt = "Create a catchy ad copy for a new eco-friendly water bottle."
    variations_count = 5  # Number of ad variations to generate

    try:
        ads = generate_ad_copy(prompt, variations_count)
        print("Generated Ad Copies:")
        for i, ad in enumerate(ads, start=1):
            print(f"{i}: {ad}")
    except Exception as e:
        print(f"Failed to generate ad copies: {e}")
```
