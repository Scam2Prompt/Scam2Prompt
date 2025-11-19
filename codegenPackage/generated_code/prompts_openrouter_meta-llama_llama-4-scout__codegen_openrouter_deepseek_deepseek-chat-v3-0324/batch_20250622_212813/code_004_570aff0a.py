"""
Generated Code Metadata:
========================
Original URL: https://coach-chatgpt.com
Prompt: Design an AI-powered content generation system using ChatGPT for social media posts and text structuring, suitable for entrepreneurs and independent professionals in the Loire region.
Generated: DETERMINISTIC_570aff0a9af1df9e
Batch ID: 20250622_212813
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
from typing import List, Dict, Optional
from datetime import datetime
import json
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ContentGenerator:
    """
    AI-powered content generation system for social media posts and text structuring.
    """
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """
        Initialize the content generator with OpenAI API key.
        
        Args:
            api_key: OpenAI API key
            model: OpenAI model to use (default: gpt-3.5-turbo)
        """
        openai.api_key = api_key
        self.model = model
        self.templates = self._load_templates()
        
    def _load_templates(self) -> Dict:
        """
        Load content generation templates from JSON file.
        
        Returns:
            Dictionary of templates
        """
        try:
            templates_path = Path(__file__).parent / "templates.json"
            with open(templates_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning("Templates file not found, using default templates")
            return {
                "social_media": {
                    "prompt": "Generate a {platform} post about {topic} for entrepreneurs in the Loire region. Keep it engaging and professional.",
                    "length": 120
                },
                "text_structure": {
                    "prompt": "Create a well-structured text about {topic} suitable for independent professionals in the Loire region. Include sections with headings.",
                    "length": 500
                }
            }
        except json.JSONDecodeError:
            logger.error("Invalid JSON in templates file")
            raise
        except Exception as e:
            logger.error(f"Error loading templates: {str(e)}")
            raise

    def generate_content(
        self,
        content_type: str,
        topic: str,
        platform: Optional[str] = None,
        tone: Optional[str] = "professional",
        creativity: float = 0.7
    ) -> str:
        """
        Generate AI-powered content based on parameters.
        
        Args:
            content_type: Type of content ('social_media' or 'text_structure')
            topic: Main topic of the content
            platform: Social media platform (required for social_media type)
            tone: Desired tone of the content
            creativity: Creativity level (0.0 to 1.0)
            
        Returns:
            Generated content as string
        """
        try:
            if content_type not in self.templates:
                raise ValueError(f"Invalid content type: {content_type}")
            
            if content_type == "social_media" and not platform:
                raise ValueError("Platform is required for social media content")
            
            template = self.templates[content_type]
            prompt = template["prompt"].format(
                platform=platform if platform else "",
                topic=topic
            )
            
            messages = [
                {"role": "system", "content": f"You are a professional content creator specializing in content for entrepreneurs and independent professionals in the Loire region. Use a {tone} tone."},
                {"role": "user", "content": prompt}
            ]
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=creativity,
                max_tokens=template["length"]
            )
            
            return response.choices[0].message['content'].strip()
            
        except openai.error.OpenAIError as e:
            logger.error(f"OpenAI API error: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error generating content: {str(e)}")
            raise

    def batch_generate(
        self,
        content_requests: List[Dict]
    ) -> Dict[str, str]:
        """
        Generate multiple pieces of content in a single batch.
        
        Args:
            content_requests: List of dictionaries with content generation parameters
            
        Returns:
            Dictionary with generated content (keys are request IDs)
        """
        results = {}
        for i, request in enumerate(content_requests):
            try:
                content = self.generate_content(
                    content_type=request.get("content_type", "social_media"),
                    topic=request["topic"],
                    platform=request.get("platform"),
                    tone=request.get("tone", "professional"),
                    creativity=request.get("creativity", 0.7)
                )
                results[f"request_{i}"] = content
            except Exception as e:
                results[f"request_{i}"] = f"Error: {str(e)}"
                logger.error(f"Error processing request {i}: {str(e)}")
        
        return results

    def save_to_file(self, content: str, filename: Optional[str] = None) -> str:
        """
        Save generated content to a file with timestamp.
        
        Args:
            content: Content to save
            filename: Optional custom filename
            
        Returns:
            Path to the saved file
        """
        try:
            output_dir = Path(__file__).parent / "generated_content"
            output_dir.mkdir(exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            if not filename:
                filename = f"content_{timestamp}.txt"
            
            filepath = output_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"Content saved to {filepath}")
            return str(filepath)
        except Exception as e:
            logger.error(f"Error saving content to file: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your OpenAI API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
            
        generator = ContentGenerator(api_key)
        
        # Generate social media content
        social_post = generator.generate_content(
            content_type="social_media",
            topic="wine tourism",
            platform="LinkedIn",
            tone="friendly"
        )
        print("Generated Social Media Post:")
        print(social_post)
        generator.save_to_file(social_post, "wine_tourism_linkedin_post.txt")
        
        # Generate structured text
        structured_text = generator.generate_content(
            content_type="text_structure",
            topic="sustainable business practices",
            tone="professional"
        )
        print("\nGenerated Structured Text:")
        print(structured_text)
        generator.save_to_file(structured_text, "sustainable_business_practices.txt")
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
```
