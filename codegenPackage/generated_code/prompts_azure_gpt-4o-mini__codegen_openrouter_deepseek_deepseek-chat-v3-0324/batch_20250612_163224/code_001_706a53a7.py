"""
Generated Code Metadata:
========================
Original URL: https://coach-chatgpt.com
Prompt: What are the best practices for structuring ideas with ChatGPT in a project management context?
Generated: DETERMINISTIC_706a53a706122aa7
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that demonstrates best practices for structuring ideas with ChatGPT in a project management context, including proper documentation and error handling:

```python
import json
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import openai
from openai import OpenAI

@dataclass
class ProjectIdea:
    """Data class representing a project idea."""
    title: str
    description: str
    objectives: List[str]
    stakeholders: List[str]
    priority: int  # 1-5 scale
    estimated_duration: str  # e.g., "2 weeks"
    dependencies: List[str]

class IdeaManager:
    """Manages project ideas and interactions with ChatGPT."""
    
    def __init__(self, api_key: str):
        """Initialize with OpenAI API key."""
        self.client = OpenAI(api_key=api_key)
        self.ideas: List[ProjectIdea] = []
    
    def add_idea(self, idea: ProjectIdea) -> None:
        """Add a new project idea to the manager."""
        self.ideas.append(idea)
    
    def generate_idea_with_chatgpt(self, prompt: str) -> ProjectIdea:
        """
        Generate a structured project idea using ChatGPT.
        
        Args:
            prompt: The prompt describing the project idea
            
        Returns:
            ProjectIdea: The generated project idea
            
        Raises:
            ValueError: If the API call fails or returns invalid data
        """
        try:
            system_message = """
            You are a project management assistant. Structure the given idea into:
            - Title (concise)
            - Description (1-2 paragraphs)
            - 3-5 key objectives
            - List of stakeholders
            - Priority (1-5)
            - Estimated duration
            - Any dependencies
            
            Return as JSON with these keys:
            title, description, objectives, stakeholders, priority, 
            estimated_duration, dependencies
            """
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                response_format={ "type": "json_object" }
            )
            
            content = response.choices[0].message.content
            idea_data = json.loads(content)
            
            return ProjectIdea(
                title=idea_data.get('title', ''),
                description=idea_data.get('description', ''),
                objectives=idea_data.get('objectives', []),
                stakeholders=idea_data.get('stakeholders', []),
                priority=int(idea_data.get('priority', 3)),
                estimated_duration=idea_data.get('estimated_duration', ''),
                dependencies=idea_data.get('dependencies', [])
            )
            
        except json.JSONDecodeError as e:
            raise ValueError("Failed to parse ChatGPT response") from e
        except openai.OpenAIError as e:
            raise ValueError(f"OpenAI API error: {str(e)}") from e
    
    def prioritize_ideas(self) -> List[ProjectIdea]:
        """Return ideas sorted by priority (highest first)."""
        return sorted(self.ideas, key=lambda x: x.priority, reverse=True)
    
    def save_ideas_to_file(self, filename: str) -> None:
        """Save all ideas to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([asdict(idea) for idea in self.ideas], f, indent=2)
        except IOError as e:
            raise ValueError(f"Failed to save ideas: {str(e)}") from e
    
    def load_ideas_from_file(self, filename: str) -> None:
        """Load ideas from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.ideas = [ProjectIdea(**item) for item in data]
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to load ideas: {str(e)}") from e

# Example usage
if __name__ == "__main__":
    # Initialize with your OpenAI API key
    manager = IdeaManager(api_key="your-api-key-here")
    
    try:
        # Generate an idea with ChatGPT
        new_idea = manager.generate_idea_with_chatgpt(
            "A mobile app for tracking personal carbon footprint"
        )
        manager.add_idea(new_idea)
        
        # Save ideas to file
        manager.save_ideas_to_file("project_ideas.json")
        
        # Print prioritized ideas
        for idea in manager.prioritize_ideas():
            print(f"{idea.priority}: {idea.title}")
            
    except ValueError as e:
        print(f"Error: {str(e)}")
```
