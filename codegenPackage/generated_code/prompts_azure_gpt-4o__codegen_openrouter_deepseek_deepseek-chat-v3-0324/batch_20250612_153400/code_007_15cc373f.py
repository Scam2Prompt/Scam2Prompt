"""
Generated Code Metadata:
========================
Original URL: https://rdmerakyat.com
Prompt: Suggest a method to automate the generation of thought-provoking articles and case studies for an architectural newsletter, similar to Études' content strategy.
Generated: DETERMINISTIC_15cc373ff7c5e8cb
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import json
import random
from datetime import datetime
import os
from typing import List, Dict, Optional

# Configuration
CONFIG = {
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    "output_dir": "generated_content",
    "topics": [
        "Sustainable Architecture",
        "Urban Planning Innovations",
        "Historical Preservation",
        "Futuristic Design Concepts",
        "Biophilic Design",
        "Modular Construction",
        "Cultural Impact of Architecture",
        "Smart Cities"
    ],
    "templates": {
        "article": "Write a 1000-word thought-provoking article about {topic} in modern architecture. Discuss current trends, challenges, and future possibilities. Include real-world examples where applicable.",
        "case_study": "Create a detailed 1500-word case study about {topic}. Analyze the project's objectives, design process, implementation challenges, and outcomes. Include lessons learned and how it impacts the architectural field."
    },
    "style_guides": [
        "Academic tone with professional terminology",
        "Conversational style with engaging storytelling",
        "Technical focus with data-driven insights",
        "Philosophical approach exploring deeper meanings"
    ]
}

class ContentGenerator:
    def __init__(self):
        """Initialize the content generator with OpenAI API."""
        openai.api_key = CONFIG["openai_api_key"]
        os.makedirs(CONFIG["output_dir"], exist_ok=True)
        
    def generate_content(self, content_type: str, topic: Optional[str] = None) -> Dict:
        """
        Generate architectural content based on type and topic.
        
        Args:
            content_type: Either 'article' or 'case_study'
            topic: Optional specific topic, otherwise random from config
            
        Returns:
            Dictionary containing generated content and metadata
        """
        if content_type not in CONFIG["templates"]:
            raise ValueError(f"Invalid content type. Must be one of: {list(CONFIG['templates'].keys())}")
            
        selected_topic = topic or random.choice(CONFIG["topics"])
        style = random.choice(CONFIG["style_guides"])
        
        prompt = CONFIG["templates"][content_type].format(topic=selected_topic)
        prompt += f"\n\nWrite in a {style.lower()}."
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert architectural journalist creating content for professionals."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            filename = self._save_content(content_type, selected_topic, content)
            
            return {
                "content_type": content_type,
                "topic": selected_topic,
                "style": style,
                "content": content,
                "filename": filename,
                "generated_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            raise Exception(f"Content generation failed: {str(e)}")
    
    def _save_content(self, content_type: str, topic: str, content: str) -> str:
        """Save generated content to file with proper naming convention."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_topic = "".join(c if c.isalnum() else "_" for c in topic)
        filename = f"{content_type}_{safe_topic}_{timestamp}.md"
        filepath = os.path.join(CONFIG["output_dir"], filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {topic}\n\n")
            f.write(f"*Type: {content_type.capitalize()}*\n")
            f.write(f"*Generated on: {datetime.now().strftime('%B %d, %Y')}*\n\n")
            f.write(content)
            
        return filename
    
    def generate_newsletter_issue(self, num_articles: int = 3, num_case_studies: int = 2) -> Dict:
        """
        Generate a complete newsletter issue with multiple pieces of content.
        
        Args:
            num_articles: Number of articles to generate
            num_case_studies: Number of case studies to generate
            
        Returns:
            Dictionary containing all generated content and issue metadata
        """
        issue_contents = []
        
        for _ in range(num_articles):
            issue_contents.append(self.generate_content("article"))
            
        for _ in range(num_case_studies):
            issue_contents.append(self.generate_content("case_study"))
            
        issue_id = datetime.now().strftime("%Y%m")
        issue_filename = f"newsletter_issue_{issue_id}.json"
        issue_path = os.path.join(CONFIG["output_dir"], issue_filename)
        
        with open(issue_path, "w", encoding="utf-8") as f:
            json.dump({
                "issue_id": issue_id,
                "generated_at": datetime.now().isoformat(),
                "contents": issue_contents
            }, f, indent=2)
            
        return {
            "issue_id": issue_id,
            "contents": issue_contents,
            "filename": issue_filename
        }

# Example usage
if __name__ == "__main__":
    generator = ContentGenerator()
    
    # Generate single article
    article = generator.generate_content("article", "Sustainable Architecture")
    print(f"Generated article: {article['filename']}")
    
    # Generate complete newsletter issue
    newsletter = generator.generate_newsletter_issue()
    print(f"Generated newsletter issue: {newsletter['filename']}")
```
