"""
Generated Code Metadata:
========================
Original URL: https://tcs-campaigns.com
Prompt: Create a guided development prompt using the pre-built prompt library from TCS AI Catapult Forward for a new software project.
Generated: DETERMINISTIC_db5d71208c374e3c
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class PromptGenerator:
    """
    A class to generate guided development prompts using the TCS AI Catapult Forward prompt library.
    """
    
    def __init__(self, prompt_library_path: str = "prompt_library.json"):
        """
        Initialize the PromptGenerator with the path to the prompt library JSON file.
        
        Args:
            prompt_library_path (str): Path to the JSON file containing the prompt library.
                                      Defaults to "prompt_library.json".
        """
        self.prompt_library = self._load_prompt_library(prompt_library_path)
    
    def _load_prompt_library(self, file_path: str) -> Dict:
        """
        Load the prompt library from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
            
        Returns:
            Dict: The loaded prompt library.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Prompt library file not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in prompt library: {file_path}", e.doc, e.pos) from e
    
    def get_categories(self) -> List[str]:
        """
        Get the list of available prompt categories.
        
        Returns:
            List[str]: List of category names.
        """
        return list(self.prompt_library.keys())
    
    def get_prompts_by_category(self, category: str) -> List[str]:
        """
        Get all prompts for a specific category.
        
        Args:
            category (str): The category name.
            
        Returns:
            List[str]: List of prompts in the category.
            
        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.prompt_library:
            raise ValueError(f"Category not found: {category}")
        return self.prompt_library[category]
    
    def generate_guided_prompt(self, category: str, project_details: Dict) -> str:
        """
        Generate a guided development prompt for a new software project.
        
        Args:
            category (str): The category of prompts to use.
            project_details (Dict): Dictionary containing project details.
                                   Expected keys: 'name', 'description', 'requirements'.
            
        Returns:
            str: The generated guided prompt.
            
        Raises:
            ValueError: If the category does not exist or project details are incomplete.
        """
        if category not in self.prompt_library:
            raise ValueError(f"Category not found: {category}")
        
        required_keys = ['name', 'description', 'requirements']
        if not all(key in project_details for key in required_keys):
            raise ValueError(f"Project details must include: {required_keys}")
        
        # Select a random prompt from the category (first one for simplicity)
        base_prompt = self.prompt_library[category][0]
        
        guided_prompt = f"""
        Project Name: {project_details['name']}
        Project Description: {project_details['description']}
        Requirements: {project_details['requirements']}
        
        {base_prompt}
        """
        
        return guided_prompt.strip()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize prompt generator
        prompt_gen = PromptGenerator()
        
        # Get available categories
        categories = prompt_gen.get_categories()
        print("Available categories:", categories)
        
        # Example project details
        project_details = {
            'name': 'E-commerce Platform',
            'description': 'A scalable e-commerce platform with AI recommendations',
            'requirements': 'Microservices architecture, Python/React, AWS deployment'
        }
        
        # Generate guided prompt
        guided_prompt = prompt_gen.generate_guided_prompt(
            category="web_development",
            project_details=project_details
        )
        
        print("\nGenerated Guided Prompt:")
        print(guided_prompt)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
