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

```python
import openai
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO)

class ContentWriter:
    def __init__(self, api_key: str):
        """
        Initializes the ContentWriter class with OpenAI API key.

        :param api_key: Your OpenAI API key for accessing GPT-3 capabilities.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_blog_post(self, title: str, keywords: List[str], length: int = 800) -> str:
        """
        Generates a blog post based on the provided title and keywords.

        :param title: The title of the blog post.
        :param keywords: A list of keywords to include in the blog post.
        :param length: The desired length of the blog post in words (default: 800).
        :return: The generated blog post as a string.
        """
        prompt = f"Write a {length}-word blog post titled '{title}' including the keywords: {', '.join(keywords)}."
        return self._generate_content(prompt)

    def generate_social_media_post(self, topic: str, platform: str) -> str:
        """
        Generates a social media post based on the provided topic and platform.

        :param topic: The topic for the social media post.
        :param platform: The platform (e.g., Twitter, Facebook, Instagram) for which the post is intended.
        :return: The generated social media post as a string.
        """
        prompt = f"Create a catchy {platform} post about '{topic}'."
        return self._generate_content(prompt)

    def _generate_content(self, prompt: str) -> str:
        """
        Internal method to call OpenAI's API and generate content based on the prompt.

        :param prompt: The prompt to send to the OpenAI API.
        :return: The generated content as a string.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1500  # Adjust based on the length needed
            )
            content = response['choices'][0]['message']['content']
            logging.info("Content generated successfully.")
            return content.strip()
        except Exception as e:
            logging.error(f"An error occurred while generating content: {e}")
            return "Error generating content. Please try again later."

if __name__ == "__main__":
    # Example usage of the ContentWriter class
    try:
        API_KEY = "your_openai_api_key_here"  # Replace with your OpenAI API key
        
        writer = ContentWriter(api_key=API_KEY)
        
        # Generate a blog post
        blog_title = "The Future of Technology"
        blog_keywords = ["AI", "Cloud Computing", "Blockchain"]
        blog_post = writer.generate_blog_post(blog_title, blog_keywords)
        print("Generated Blog Post:\n", blog_post)

        # Generate a social media post
        social_topic = "Exciting New Tech Innovations"
        social_platform = "Twitter"
        social_post = writer.generate_social_media_post(social_topic, social_platform)
        print("\nGenerated Social Media Post:\n", social_post)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
