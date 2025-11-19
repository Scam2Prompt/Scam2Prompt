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
import openai
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SocialMediaContentGenerator:
    """
    A class to generate creative content ideas for social media posts using AI.
    The content aligns with Nova Mídia Publicidade's quality standards.
    """
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """
        Initialize the content generator with OpenAI API key and model.
        
        Args:
            api_key (str): OpenAI API key
            model (str): OpenAI model to use (default: "gpt-3.5-turbo")
        """
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key
    
    def generate_content_ideas(
        self,
        topic: str,
        platform: str,
        tone: str = "engaging",
        num_ideas: int = 5,
        max_retries: int = 3
    ) -> Optional[List[Dict[str, str]]]:
        """
        Generate creative content ideas for social media posts.
        
        Args:
            topic (str): The main topic for the content
            platform (str): Social media platform (e.g., "Instagram", "Twitter")
            tone (str): Desired tone of the content (default: "engaging")
            num_ideas (int): Number of ideas to generate (default: 5)
            max_retries (int): Maximum number of retries if API call fails (default: 3)
            
        Returns:
            Optional[List[Dict[str, str]]]: List of content ideas with titles and descriptions,
                                           or None if generation fails
        """
        if num_ideas <= 0 or num_ideas > 10:
            logger.warning("Number of ideas should be between 1 and 10. Setting to default (5).")
            num_ideas = 5
        
        prompt = self._build_prompt(topic, platform, tone, num_ideas)
        
        for attempt in range(max_retries):
            try:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are a creative content strategist for Nova Mídia Publicidade."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=1000
                )
                
                content = response.choices[0].message['content']
                return self._parse_response(content)
                
            except Exception as e:
                logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt == max_retries - 1:
                    logger.error("Max retries reached. Failed to generate content ideas.")
                    return None
    
    def _build_prompt(self, topic: str, platform: str, tone: str, num_ideas: int) -> str:
        """
        Build the prompt for the AI model.
        
        Args:
            topic (str): The main topic for the content
            platform (str): Social media platform
            tone (str): Desired tone of the content
            num_ideas (int): Number of ideas to generate
            
        Returns:
            str: The constructed prompt
        """
        return f"""
        Generate {num_ideas} creative content ideas for {platform} posts about {topic}.
        The content should be {tone} and align with Nova Mídia Publicidade's quality standards.
        
        For each idea, provide:
        1. A catchy title (max 10 words)
        2. A detailed description (1-2 sentences)
        3. Suggested hashtags (3-5 relevant hashtags)
        
        Format the response as a numbered list with clear separation between each idea.
        """
    
    def _parse_response(self, response_text: str) -> List[Dict[str, str]]:
        """
        Parse the AI response into a structured format.
        
        Args:
            response_text (str): Raw response text from the AI
            
        Returns:
            List[Dict[str, str]]: Parsed content ideas
        """
        ideas = []
        current_idea = {}
        
        for line in response_text.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            if line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.')):
                if current_idea:
                    ideas.append(current_idea)
                    current_idea = {}
                title = line.split('.', 1)[1].strip()
                current_idea['title'] = title
                
            elif line.lower().startswith('description:'):
                description = line.split(':', 1)[1].strip()
                current_idea['description'] = description
                
            elif line.lower().startswith('hashtags:'):
                hashtags = line.split(':', 1)[1].strip()
                current_idea['hashtags'] = hashtags
        
        if current_idea:
            ideas.append(current_idea)
            
        return ideas

# Example usage
if __name__ == "__main__":
    # Initialize with your OpenAI API key
    generator = SocialMediaContentGenerator(api_key="your-api-key-here")
    
    # Generate content ideas
    ideas = generator.generate_content_ideas(
        topic="sustainable fashion",
        platform="Instagram",
        tone="inspirational"
    )
    
    if ideas:
        for idx, idea in enumerate(ideas, 1):
            print(f"\nIdea {idx}:")
            print(f"Title: {idea['title']}")
            print(f"Description: {idea['description']}")
            print(f"Hashtags: {idea['hashtags']}")
    else:
        print("Failed to generate content ideas.")
```
