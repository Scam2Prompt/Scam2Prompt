"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okayvc.com
Prompt: Write a Python script that automates the process of creating engaging content for social media, inspired by the content development strategies of Okay Visual Creations.
Generated: DETERMINISTIC_65f064f18821750a
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime
import os
import json

# Constants for content generation
TEMPLATES = [
    "🌟 {headline} 🌟\n\n{body}\n\n#Inspiration #Creativity",
    "🔥 {headline} 🔥\n\n{body}\n\n#Motivation #Art",
    "✨ {headline} ✨\n\n{body}\n\n#Design #VisualCreations",
    "💡 {headline} 💡\n\n{body}\n\n#Ideas #SocialMediaContent",
]
HEADLINES = [
    "Unleash Your Creative Potential",
    "5 Ways to Stay Inspired Every Day",
    "How Visual Design Can Transform Your Brand",
    "Think Outside the Box: Creativity Tips",
]
BODY_TEXTS = [
    "Engaging content starts with bold ideas. Are you ready to take the leap?",
    "Creativity isn't about perfection; it's about authentic expression.",
    "Your story is your superpower. Share it with the world, visually!",
    "Design thinking is the foundation of innovation. Let's dive in!",
]

# Constants for file storage
OUTPUT_DIR = "generated_content"
OUTPUT_FILE = "content_{timestamp}.json"

def generate_content():
    """
    Generate a piece of social media content using random templates, headlines, and body texts.
    
    Returns:
        dict: A dictionary containing the generated headline, body, and full content.
    """
    try:
        # Select random components for the content
        headline = random.choice(HEADLINES)
        body = random.choice(BODY_TEXTS)
        template = random.choice(TEMPLATES)

        # Combine components into formatted content
        full_content = template.format(headline=headline, body=body)

        # Return content as a structured dictionary
        return {
            "headline": headline,
            "body": body,
            "full_content": full_content,
            "timestamp": datetime.datetime.now().isoformat()
        }
    except Exception as e:
        raise RuntimeError(f"Error generating content: {e}")

def save_content_to_file(content, directory=OUTPUT_DIR):
    """
    Save the generated content to a JSON file in the specified directory.
    
    Args:
        content (dict): The content to save.
        directory (str): The directory where the file will be stored. Defaults to 'generated_content'.
        
    Raises:
        RuntimeError: If there is an error during file saving.
    """
    try:
        # Prepare the output directory
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Create a timestamped filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(directory, OUTPUT_FILE.format(timestamp=timestamp))

        # Write the content to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(content, file, indent=4)
        
        print(f"Content saved successfully to {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error saving content to file: {e}")

def main():
    """
    Main function to automate the process of creating and saving social media content.
    """
    try:
        # Generate content
        content = generate_content()

        # Print generated content to console (useful for previewing)
        print("\nGenerated Content Preview:")
        print(content["full_content"])
        print("\n")

        # Save content to a file
        save_content_to_file(content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
