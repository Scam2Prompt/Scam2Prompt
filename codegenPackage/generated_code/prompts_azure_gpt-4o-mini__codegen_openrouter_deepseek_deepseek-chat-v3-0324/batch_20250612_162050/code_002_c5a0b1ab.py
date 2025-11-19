"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: Write a Python script that simulates an "Aula Invertida" learning environment, allowing students to access simplified educational materials online.
Generated: DETERMINISTIC_c5a0b1abfc54cf38
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class AulaInvertida:
    """
    A simulated flipped classroom environment where students can access educational materials.
    """
    
    def __init__(self, data_file: str = "materials.json"):
        """
        Initialize the AulaInvertida environment.
        
        Args:
            data_file: Path to JSON file containing educational materials.
        """
        self.data_file = data_file
        self.materials: Dict[str, Dict] = {}
        self.load_materials()
    
    def load_materials(self) -> None:
        """
        Load educational materials from JSON file.
        Handles file not found and JSON decode errors.
        """
        try:
            if not os.path.exists(self.data_file):
                with open(self.data_file, 'w') as f:
                    json.dump({}, f)
            
            with open(self.data_file, 'r') as f:
                self.materials = json.load(f)
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in materials file.")
            self.materials = {}
        except IOError as e:
            print(f"Error loading materials: {e}")
            self.materials = {}
    
    def save_materials(self) -> None:
        """
        Save educational materials to JSON file.
        Handles IO errors during save.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.materials, f, indent=4)
        except IOError as e:
            print(f"Error saving materials: {e}")
    
    def add_material(self, subject: str, title: str, content: str, level: str = "basic") -> bool:
        """
        Add new educational material.
        
        Args:
            subject: Subject area (e.g., "Math", "Science")
            title: Title of the material
            content: Educational content
            level: Difficulty level ("basic", "intermediate", "advanced")
            
        Returns:
            bool: True if material was added successfully
        """
        if subject not in self.materials:
            self.materials[subject] = {}
        
        if title in self.materials[subject]:
            print(f"Warning: Material '{title}' already exists for subject '{subject}'")
            return False
        
        self.materials[subject][title] = {
            'content': content,
            'level': level
        }
        self.save_materials()
        return True
    
    def get_materials(self, subject: Optional[str] = None) -> Dict[str, Dict]:
        """
        Get educational materials, optionally filtered by subject.
        
        Args:
            subject: Optional subject filter
            
        Returns:
            Dictionary of materials
        """
        if subject:
            return {subject: self.materials.get(subject, {})}
        return self.materials
    
    def get_material(self, subject: str, title: str) -> Optional[Dict]:
        """
        Get specific educational material by subject and title.
        
        Args:
            subject: Subject area
            title: Title of the material
            
        Returns:
            Material content if found, None otherwise
        """
        return self.materials.get(subject, {}).get(title)
    
    def list_subjects(self) -> List[str]:
        """
        List all available subjects.
        
        Returns:
            List of subject names
        """
        return list(self.materials.keys())
    
    def search_materials(self, query: str) -> Dict[str, Dict]:
        """
        Search materials by query string (case-insensitive).
        
        Args:
            query: Search term
            
        Returns:
            Dictionary of matching materials
        """
        results = {}
        query = query.lower()
        
        for subject, materials in self.materials.items():
            for title, content in materials.items():
                if (query in title.lower() or 
                    query in content['content'].lower() or 
                    query in subject.lower()):
                    if subject not in results:
                        results[subject] = {}
                    results[subject][title] = content
        
        return results


def main():
    """
    Example usage of the AulaInvertida system.
    """
    aula = AulaInvertida()
    
    # Add some sample materials
    aula.add_material(
        "Math", 
        "Basic Algebra", 
        "Algebra is the study of mathematical symbols...",
        "basic"
    )
    
    aula.add_material(
        "Science", 
        "Introduction to Physics", 
        "Physics is the natural science that studies matter...",
        "basic"
    )
    
    # Display available subjects
    print("Available subjects:", aula.list_subjects())
    
    # Get materials for a subject
    print("\nMath materials:")
    print(json.dumps(aula.get_materials("Math"), indent=2))
    
    # Search for materials
    print("\nSearch results for 'intro':")
    print(json.dumps(aula.search_materials("intro"), indent=2))


if __name__ == "__main__":
    main()
```
