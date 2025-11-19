"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Create a syllabus management system that allows administrators to print class-specific syllabi, similar to the Syllabus module in Him Saral's software.
Generated: DETERMINISTIC_70a81adb4128259f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import Dict, List, Optional

class SyllabusManagementSystem:
    """
    A syllabus management system that allows administrators to manage and print class-specific syllabi.
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the syllabus management system.
        
        Args:
            data_dir (str): Directory to store syllabus data. Defaults to "data".
        """
        self.data_dir = data_dir
        self.syllabi: Dict[str, Dict] = {}
        self.classes: List[str] = []
        
        # Ensure data directory exists
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load existing data
        self._load_data()
    
    def _load_data(self) -> None:
        """Load existing syllabus and class data from files."""
        try:
            # Load syllabi
            syllabi_path = os.path.join(self.data_dir, "syllabi.json")
            if os.path.exists(syllabi_path):
                with open(syllabi_path, "r") as f:
                    self.syllabi = json.load(f)
            
            # Load classes
            classes_path = os.path.join(self.data_dir, "classes.json")
            if os.path.exists(classes_path):
                with open(classes_path, "r") as f:
                    self.classes = json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """Save current syllabus and class data to files."""
        try:
            # Save syllabi
            syllabi_path = os.path.join(self.data_dir, "syllabi.json")
            with open(syllabi_path, "w") as f:
                json.dump(self.syllabi, f, indent=4)
            
            # Save classes
            classes_path = os.path.join(self.data_dir, "classes.json")
            with open(classes_path, "w") as f:
                json.dump(self.classes, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_class(self, class_name: str) -> bool:
        """
        Add a new class to the system.
        
        Args:
            class_name (str): Name of the class to add.
            
        Returns:
            bool: True if class was added, False if it already exists.
        """
        if class_name in self.classes:
            return False
        
        self.classes.append(class_name)
        self._save_data()
        return True
    
    def remove_class(self, class_name: str) -> bool:
        """
        Remove a class from the system.
        
        Args:
            class_name (str): Name of the class to remove.
            
        Returns:
            bool: True if class was removed, False if it didn't exist.
        """
        if class_name not in self.classes:
            return False
        
        self.classes.remove(class_name)
        
        # Remove any associated syllabi
        if class_name in self.syllabi:
            del self.syllabi[class_name]
        
        self._save_data()
        return True
    
    def create_syllabus(self, class_name: str, syllabus_data: Dict) -> bool:
        """
        Create or update a syllabus for a class.
        
        Args:
            class_name (str): Name of the class.
            syllabus_data (Dict): Syllabus data including title, description, topics, etc.
            
        Returns:
            bool: True if syllabus was created/updated, False if class doesn't exist.
        """
        if class_name not in self.classes:
            return False
        
        # Add timestamp
        syllabus_data["last_updated"] = datetime.now().isoformat()
        self.syllabi[class_name] = syllabus_data
        self._save_data()
        return True
    
    def get_syllabus(self, class_name: str) -> Optional[Dict]:
        """
        Get syllabus for a class.
        
        Args:
            class_name (str): Name of the class.
            
        Returns:
            Optional[Dict]: Syllabus data if exists, None otherwise.
        """
        return self.syllabi.get(class_name)
    
    def print_syllabus(self, class_name: str, output_format: str = "text") -> bool:
        """
        Print syllabus for a class in specified format.
        
        Args:
            class_name (str): Name of the class.
            output_format (str): Output format ("text" or "html"). Defaults to "text".
            
        Returns:
            bool: True if printed successfully, False if class/syllabus doesn't exist.
        """
        syllabus = self.get_syllabus(class_name)
        if not syllabus:
            return False
        
        try:
            if output_format == "text":
                self._print_text_syllabus(syllabus)
            elif output_format == "html":
                self._print_html_syllabus(syllabus)
            else:
                print(f"Unsupported format: {output_format}")
                return False
            return True
        except Exception as e:
            print(f"Error printing syllabus: {e}")
            return False
    
    def _print_text_syllabus(self, syllabus: Dict) -> None:
        """Print syllabus in plain text format."""
        print("\n" + "=" * 50)
        print(f"Syllabus: {syllabus.get('title', 'Untitled')}")
        print("=" * 50)
        print(f"Class: {syllabus.get('class_name', 'N/A')}")
        print(f"Instructor: {syllabus.get('instructor', 'N/A')}")
        print(f"Last Updated: {syllabus.get('last_updated', 'N/A')}\n")
        
        print("Description:")
        print(syllabus.get('description', 'No description provided') + "\n")
        
        print("Topics:")
        for i, topic in enumerate(syllabus.get('topics', []), 1):
            print(f"{i}. {topic}")
        
        print("\nGrading:")
        for item, weight in syllabus.get('grading', {}).items():
            print(f"- {item}: {weight}%")
        
        print("\n" + "=" * 50)
    
    def _print_html_syllabus(self, syllabus: Dict) -> None:
        """Print syllabus in HTML format."""
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Syllabus: {syllabus.get('title', 'Untitled')}</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
                h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; }}
                .info {{ margin-bottom: 20px; }}
                .section {{ margin-bottom: 15px; }}
                .topics {{ margin-left: 20px; }}
                .grading {{ margin-left: 20px; }}
            </style>
        </head>
        <body>
            <h1>Syllabus: {syllabus.get('title', 'Untitled')}</h1>
            
            <div class="info">
                <p><strong>Class:</strong> {syllabus.get('class_name', 'N/A')}</p>
                <p><strong>Instructor:</strong> {syllabus.get('instructor', 'N/A')}</p>
                <p><strong>Last Updated:</strong> {syllabus.get('last_updated', 'N/A')}</p>
            </div>
            
            <div class="section">
                <h2>Description</h2>
                <p>{syllabus.get('description', 'No description provided')}</p>
            </div>
            
            <div class="section">
                <h2>Topics</h2>
                <ol class="topics">
                    {''.join(f'<li>{topic}</li>' for topic in syllabus.get('topics', []))}
                </ol>
            </div>
            
            <div class="section">
                <h2>Grading</h2>
                <ul class="grading">
                    {''.join(f'<li>{item}: {weight}%</li>' for item, weight in syllabus.get('grading', {}).items())}
                </ul>
            </div>
        </body>
        </html>
        """
        print(html)
    
    def list_classes(self) -> List[str]:
        """Return list of all classes."""
        return self.classes
    
    def list_syllabi(self) -> List[str]:
        """Return list of classes that have syllabi."""
        return list(self.syllabi.keys())


# Example usage
if __name__ == "__main__":
    sms = SyllabusManagementSystem()
    
    # Add some classes
    sms.add_class("CS101")
    sms.add_class("MATH201")
    
    # Create a syllabus
    cs101_syllabus = {
        "title": "Introduction to Computer Science",
        "class_name": "CS101",
        "instructor": "Dr. Smith",
        "description": "Fundamentals of computer science and
