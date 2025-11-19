"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shebatek.com
Prompt: How can I create a content writing automation tool that aligns with the services offered by ShebaTek, particularly for blogs and social media posts?
Generated: DETERMINISTIC_9411e2600c47de18
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that implements a content writing automation tool for blog and social media posts. The code utilizes the OpenAI GPT API for content generation.

```python
import openai
import os
from datetime import datetime

class ContentWritingAutomation:
    """
    A tool for automating content writing for blogs and social media posts.
    Utilizes OpenAI's GPT API to generate content.
    """

    def __init__(self, api_key: str):
        """
        Initializes the automation tool with the OpenAI API key.

        :param api_key: OpenAI API key required for authentication.
        """
        if not api_key:
            raise ValueError("API key cannot be empty.")
        self.api_key = api_key
        openai.api_key = api_key

    def generate_content(self, prompt: str, max_tokens: int = 300) -> str:
        """
        Generates content based on the provided prompt.

        :param prompt: The input prompt describing the content requirements.
        :param max_tokens: Maximum number of tokens for the generated content.
        :return: Generated content as a string.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a professional content writer."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise RuntimeError(f"Error generating content: {str(e)}")

    def save_content_to_file(self, content: str, file_path: str) -> None:
        """
        Saves generated content to a text file.

        :param content: The content to save.
        :param file_path: Path to the file where content will be saved.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Content successfully saved to {file_path}")
        except Exception as e:
            raise IOError(f"Error saving content to file: {str(e)}")

def main():
    """
    Main function to demonstrate the content writing automation tool.
    """
    try:
        # Read OpenAI API key from environment variables for security
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key is not set in environment variables.")

        # Initialize the automation tool
        tool = ContentWritingAutomation(api_key)

        # Example: Generate blog content
        prompt_blog = "Write a 500-word blog post about the benefits of using ShebaTek services for small businesses."
        blog_content = tool.generate_content(prompt_blog, max_tokens=500)

        # Save generated blog content to a file
        blog_file_path = f"blog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        tool.save_content_to_file(blog_content, blog_file_path)

        # Example: Generate social media post content
        prompt_social_media = "Create a short and engaging social media post promoting ShebaTek services."
        social_media_content = tool.generate_content(prompt_social_media, max_tokens=100)

        # Save generated social media content to a file
        social_media_file_path = f"social_media_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        tool.save_content_to_file(social_media_content, social_media_file_path)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

### Requirements:
1. Install the OpenAI Python package:
   ```bash
   pip install openai
   ```
2. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```
