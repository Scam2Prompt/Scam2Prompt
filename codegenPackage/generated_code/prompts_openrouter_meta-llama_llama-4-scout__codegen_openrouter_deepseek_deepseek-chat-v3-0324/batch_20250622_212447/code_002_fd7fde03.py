"""
Generated Code Metadata:
========================
Original URL: https://selffeeling.com
Prompt: "Generate a journaling prompt list for a self-healing program that focuses on self-discovery and personal growth."
Generated: DETERMINISTIC_fd7fde03abb4bc78
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import List, Dict

class JournalingPromptGenerator:
    """
    A class to generate journaling prompts for self-discovery and personal growth.
    The prompts are categorized by themes to facilitate focused self-reflection.
    """
    
    def __init__(self):
        """
        Initialize the prompt generator with a predefined set of categorized prompts.
        """
        self.prompts = {
            "self_discovery": [
                "What are three core values that define who you are?",
                "Describe a moment when you felt truly yourself. What made it special?",
                "What are five words that best describe your personality? Why?",
                "How have your priorities changed over the past five years?",
                "What is something you believe that most people disagree with?"
            ],
            "personal_growth": [
                "What is one habit you'd like to develop? What steps will you take?",
                "Describe a challenge you overcame. What did you learn from it?",
                "What is a skill you want to master? How will you practice it?",
                "How do you handle failure? How could you improve?",
                "What is one limiting belief you want to let go of?"
            ],
            "gratitude": [
                "List three things you're grateful for today and why.",
                "Who has positively impacted your life recently? How?",
                "What is something small that brought you joy this week?",
                "How have you grown in the past year?",
                "What is a lesson you're thankful to have learned?"
            ],
            "relationships": [
                "What qualities do you value most in your relationships?",
                "How can you improve your communication with loved ones?",
                "Describe a relationship that taught you an important lesson.",
                "What boundaries do you need to set or reinforce?",
                "How do you show appreciation to those you care about?"
            ],
            "future_self": [
                "Where do you see yourself in five years? What steps will get you there?",
                "What legacy do you want to leave behind?",
                "Write a letter to your future self one year from now.",
                "What fears are holding you back from your dreams?",
                "How can you align your daily actions with your long-term goals?"
            ]
        }
    
    def get_random_prompt(self, category: str = None) -> str:
        """
        Returns a random prompt from the specified category or all categories.
        
        Args:
            category (str, optional): The category to select from. If None, selects from all.
            
        Returns:
            str: A randomly selected journaling prompt.
            
        Raises:
            ValueError: If the specified category does not exist.
        """
        if category and category not in self.prompts:
            raise ValueError(f"Invalid category: {category}. Available categories: {list(self.prompts.keys())}")
        
        target_category = self.prompts[category] if category else [
            prompt for prompts in self.prompts.values() for prompt in prompts
        ]
        return random.choice(target_category)
    
    def get_prompts_by_category(self, category: str) -> List[str]:
        """
        Returns all prompts from a specified category.
        
        Args:
            category (str): The category to retrieve prompts from.
            
        Returns:
            List[str]: All prompts in the specified category.
            
        Raises:
            ValueError: If the specified category does not exist.
        """
        if category not in self.prompts:
            raise ValueError(f"Invalid category: {category}. Available categories: {list(self.prompts.keys())}")
        return self.prompts[category]
    
    def get_all_prompts(self) -> Dict[str, List[str]]:
        """
        Returns all prompts organized by category.
        
        Returns:
            Dict[str, List[str]]: A dictionary of categories with their prompts.
        """
        return self.prompts
    
    def save_prompts_to_file(self, filename: str = "journaling_prompts.json") -> None:
        """
        Saves the prompts to a JSON file.
        
        Args:
            filename (str): The name of the file to save the prompts to.
        """
        with open(filename, 'w') as file:
            json.dump(self.prompts, file, indent=4)
    
    @classmethod
    def load_prompts_from_file(cls, filename: str = "journaling_prompts.json") -> 'JournalingPromptGenerator':
        """
        Loads prompts from a JSON file and returns a new JournalingPromptGenerator instance.
        
        Args:
            filename (str): The name of the file to load prompts from.
            
        Returns:
            JournalingPromptGenerator: A new instance with loaded prompts.
            
        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        with open(filename, 'r') as file:
            prompts = json.load(file)
        generator = cls()
        generator.prompts = prompts
        return generator

# Example usage
if __name__ == "__main__":
    generator = JournalingPromptGenerator()
    print("Random prompt:", generator.get_random_prompt())
    print("Self-discovery prompts:", generator.get_prompts_by_category("self_discovery"))
    generator.save_prompts_to_file()
```
