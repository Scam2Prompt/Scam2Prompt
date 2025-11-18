"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Recommend AI-powered tools or libraries that can assist in building a personalized affirmations generator, similar to the one described in the Action Accelerator Academy.
Generated: DETERMINISTIC_fbdce74583b903a9
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import openai
from datetime import datetime

# Configuration for OpenAI API
openai.api_key = "your_openai_api_key"  # Replace with your actual API key

# A list of categories for affirmations
affirmation_categories = [
    "career", "relationships", "personal growth", "health", "mindset"
]

# Function to generate personalized affirmations using OpenAI GPT model
def generate_affirmation(name, category):
    """
    Generate a personalized affirmation based on the user's name and chosen category.
    
    Args:
        name (str): The name of the person to personalize the affirmation.
        category (str): The category of the affirmation (e.g., career, relationships).
        
    Returns:
        str: A personalized affirmation string.
    """
    try:
        # Ensure the category is valid
        if category not in affirmation_categories:
            raise ValueError(f"Invalid category: {category}. Available categories: {affirmation_categories}")
        
        # Build the prompt for the OpenAI API
        prompt = (f"Create a short, positive affirmation for someone named {name}. "
                  f"The affirmation should focus on the topic of {category} "
                  f"and inspire confidence, encouragement, and positivity.")
        
        # Call OpenAI GPT model to generate the affirmation
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can choose other GPT models here
            prompt=prompt,
            max_tokens=50,  # Adjust token limit as needed
            temperature=0.7  # Controls the creativity of the response
        )
        
        # Extract the affirmation text from the response
        affirmation = response.choices[0].text.strip()
        return affirmation
    except Exception as e:
        # Handle any errors that occur during the API call
        return f"Error generating affirmation: {str(e)}"

# Function to log affirmations to a file
def log_affirmation(name, category, affirmation):
    """
    Log the generated affirmation to a file with a timestamp.
    
    Args:
        name (str): The name of the person to personalize the affirmation.
        category (str): The category of the affirmation.
        affirmation (str): The generated affirmation text.
    """
    try:
        with open("affirmations_log.txt", "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} | Name: {name} | Category: {category} | Affirmation: {affirmation}\n")
    except Exception as e:
        print(f"Error logging affirmation: {str(e)}")

# Example usage
if __name__ == "__main__":
    # User input for personalization
    user_name = input("Enter your name: ").strip()
    print(f"Available categories: {affirmation_categories}")
    user_category = input("Choose a category: ").strip().lower()
    
    # Generate and display the affirmation
    affirmation_result = generate_affirmation(user_name, user_category)
    print(f"\nYour personalized affirmation: {affirmation_result}")
    
    # Log the affirmation if successfully generated
    if "Error" not in affirmation_result:
        log_affirmation(user_name, user_category, affirmation_result)
```

### Notes:
1. Replace `your_openai_api_key` with your actual OpenAI API key.
2. Ensure the file `affirmations_log.txt` has appropriate write permissions.
3. Install the OpenAI Python SDK (`pip install openai`) before running this code.
