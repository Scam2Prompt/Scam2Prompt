"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Write code to implement a pre-workshop module for parents of adolescents undergoing DBT therapy, as described in the FAQs section of the Mente Sana Psicología webpage.
Generated: DETERMINISTIC_26b115fe76a3bcf3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DBT Pre-Workshop Module for Parents of Adolescents
This module provides an interactive pre-workshop experience for parents
whose adolescents are undergoing Dialectical Behavior Therapy (DBT).
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class DBTPreWorkshopModule:
    """
    A class to manage the pre-workshop module for parents in DBT therapy.
    Handles user registration, content delivery, and progress tracking.
    """
    
    def __init__(self):
        self.registered_parents: Dict[str, Dict] = {}
        self.content: List[Dict] = [
            {
                "id": 1,
                "title": "Introduction to DBT",
                "content": "DBT is a cognitive-behavioral treatment...",
                "completed": False
            },
            {
                "id": 2,
                "title": "Understanding Adolescent Behavior",
                "content": "Adolescents often experience...",
                "completed": False
            },
            {
                "id": 3,
                "title": "Parental Support Strategies",
                "content": "As a parent, you can support your child by...",
                "completed": False
            }
        ]
        self.faqs: List[Dict] = [
            {
                "question": "What is DBT?",
                "answer": "Dialectical Behavior Therapy (DBT) is..."
            },
            {
                "question": "How can I support my child?",
                "answer": "You can support your child by..."
            }
        ]
    
    def register_parent(self, parent_name: str, email: str, adolescent_name: str) -> bool:
        """
        Register a new parent for the pre-workshop module.
        
        Args:
            parent_name: Full name of the parent
            email: Contact email address
            adolescent_name: Name of the adolescent in therapy
            
        Returns:
            bool: True if registration was successful, False otherwise
        """
        if not all([parent_name, email, adolescent_name]):
            return False
            
        if email in self.registered_parents:
            return False
            
        self.registered_parents[email] = {
            "parent_name": parent_name,
            "adolescent_name": adolescent_name,
            "registration_date": datetime.now().isoformat(),
            "progress": 0,
            "completed_modules": []
        }
        return True
    
    def get_content(self, content_id: int) -> Optional[Dict]:
        """
        Retrieve workshop content by ID.
        
        Args:
            content_id: The ID of the content to retrieve
            
        Returns:
            Optional[Dict]: The content dictionary if found, None otherwise
        """
        for item in self.content:
            if item["id"] == content_id:
                return item
        return None
    
    def mark_completed(self, email: str, content_id: int) -> bool:
        """
        Mark a content module as completed for a parent.
        
        Args:
            email: Parent's registered email
            content_id: ID of the completed content
            
        Returns:
            bool: True if successful, False otherwise
        """
        if email not in self.registered_parents:
            return False
            
        content = self.get_content(content_id)
        if not content:
            return False
            
        if content_id in self.registered_parents[email]["completed_modules"]:
            return False
            
        self.registered_parents[email]["completed_modules"].append(content_id)
        self.registered_parents[email]["progress"] = len(self.registered_parents[email]["completed_modules"]) / len(self.content)
        return True
    
    def get_faqs(self) -> List[Dict]:
        """
        Get all frequently asked questions.
        
        Returns:
            List[Dict]: List of FAQ dictionaries
        """
        return self.faqs
    
    def get_parent_progress(self, email: str) -> Optional[Dict]:
        """
        Get a parent's progress in the workshop.
        
        Args:
            email: Parent's registered email
            
        Returns:
            Optional[Dict]: Progress dictionary if parent exists, None otherwise
        """
        if email not in self.registered_parents:
            return None
            
        return {
            "parent_name": self.registered_parents[email]["parent_name"],
            "progress": self.registered_parents[email]["progress"],
            "completed_modules": [
                self.get_content(module_id)["title"]
                for module_id in self.registered_parents[email]["completed_modules"]
            ]
        }
    
    def save_data(self, filename: str) -> bool:
        """
        Save module data to a JSON file.
        
        Args:
            filename: Name of the file to save to
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            data = {
                "registered_parents": self.registered_parents,
                "content": self.content,
                "faqs": self.faqs
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self, filename: str) -> bool:
        """
        Load module data from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            bool: True if load was successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.registered_parents = data.get("registered_parents", {})
                self.content = data.get("content", [])
                self.faqs = data.get("faqs", [])
            return True
        except FileNotFoundError:
            print("File not found. Starting with fresh data.")
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False

# Example usage
if __name__ == "__main__":
    module = DBTPreWorkshopModule()
    
    # Register a parent
    module.register_parent("Maria Garcia", "maria@example.com", "Carlos Garcia")
    
    # Get content
    content = module.get_content(1)
    if content:
        print(f"Content Title: {content['title']}")
        print(f"Content: {content['content']}")
    
    # Mark as completed
    module.mark_completed("maria@example.com", 1)
    
    # Get progress
    progress = module.get_parent_progress("maria@example.com")
    if progress:
        print(f"Progress for {progress['parent_name']}: {progress['progress']*100:.0f}%")
        print("Completed modules:", ", ".join(progress["completed_modules"]))
    
    # Get FAQs
    faqs = module.get_faqs()
    print("\nFAQs:")
    for faq in faqs:
        print(f"Q: {faq['question']}")
        print(f"A: {faq['answer']}\n")
    
    # Save data
    module.save_data("dbt_preworkshop_data.json")
```
