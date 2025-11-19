"""
Generated Code Metadata:
========================
Original URL: https://wifistudypdf.com
Prompt: Design a system to categorize and store study materials for various government exams, such as SSC, UPSC, and Bank exams, using wifistudypdf.com as a reference.
Generated: DETERMINISTIC_c2b9534c074f0d51
Batch ID: 20250622_210802
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

class StudyMaterialManager:
    """
    A system to categorize and store study materials for various government exams.
    """

    def __init__(self, storage_path="study_materials"):
        """
        Initialize the StudyMaterialManager with a storage path.
        :param storage_path: Directory where study materials will be stored.
        """
        self.storage_path = storage_path
        self.exam_categories = ["SSC", "UPSC", "Bank"]
        self._initialize_storage()

    def _initialize_storage(self):
        """
        Create the storage directory and subdirectories for each exam category if they don't exist.
        """
        try:
            if not os.path.exists(self.storage_path):
                os.makedirs(self.storage_path)
            for category in self.exam_categories:
                category_path = os.path.join(self.storage_path, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
        except Exception as e:
            print(f"Error initializing storage: {e}")
            raise

    def add_material(self, exam_category, material_name, material_content):
        """
        Add study material to the specified exam category.
        :param exam_category: The category of the exam (e.g., SSC, UPSC, Bank).
        :param material_name: Name of the study material file (e.g., "math_notes.pdf").
        :param material_content: Content of the study material (e.g., text or binary data).
        """
        if exam_category not in self.exam_categories:
            raise ValueError(f"Invalid exam category: {exam_category}. Valid categories are {self.exam_categories}.")
        
        try:
            material_path = os.path.join(self.storage_path, exam_category, material_name)
            with open(material_path, "wb") as file:
                file.write(material_content)
            print(f"Material '{material_name}' added successfully to '{exam_category}' category.")
        except Exception as e:
            print(f"Error adding material: {e}")
            raise

    def list_materials(self, exam_category):
        """
        List all study materials in the specified exam category.
        :param exam_category: The category of the exam (e.g., SSC, UPSC, Bank).
        :return: List of study material file names.
        """
        if exam_category not in self.exam_categories:
            raise ValueError(f"Invalid exam category: {exam_category}. Valid categories are {self.exam_categories}.")
        
        try:
            category_path = os.path.join(self.storage_path, exam_category)
            return os.listdir(category_path)
        except Exception as e:
            print(f"Error listing materials: {e}")
            raise

    def get_material(self, exam_category, material_name):
        """
        Retrieve the content of a specific study material.
        :param exam_category: The category of the exam (e.g., SSC, UPSC, Bank).
        :param material_name: Name of the study material file (e.g., "math_notes.pdf").
        :return: Content of the study material.
        """
        if exam_category not in self.exam_categories:
            raise ValueError(f"Invalid exam category: {exam_category}. Valid categories are {self.exam_categories}.")
        
        try:
            material_path = os.path.join(self.storage_path, exam_category, material_name)
            if not os.path.exists(material_path):
                raise FileNotFoundError(f"Material '{material_name}' not found in '{exam_category}' category.")
            
            with open(material_path, "rb") as file:
                return file.read()
        except Exception as e:
            print(f"Error retrieving material: {e}")
            raise

    def delete_material(self, exam_category, material_name):
        """
        Delete a specific study material from the specified exam category.
        :param exam_category: The category of the exam (e.g., SSC, UPSC, Bank).
        :param material_name: Name of the study material file (e.g., "math_notes.pdf").
        """
        if exam_category not in self.exam_categories:
            raise ValueError(f"Invalid exam category: {exam_category}. Valid categories are {self.exam_categories}.")
        
        try:
            material_path = os.path.join(self.storage_path, exam_category, material_name)
            if not os.path.exists(material_path):
                raise FileNotFoundError(f"Material '{material_name}' not found in '{exam_category}' category.")
            
            os.remove(material_path)
            print(f"Material '{material_name}' deleted successfully from '{exam_category}' category.")
        except Exception as e:
            print(f"Error deleting material: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    manager = StudyMaterialManager()

    # Add a study material
    manager.add_material("SSC", "math_notes.pdf", b"Sample content for math notes.")

    # List materials in SSC category
    print(manager.list_materials("SSC"))

    # Retrieve a study material
    content = manager.get_material("SSC", "math_notes.pdf")
    print(content)

    # Delete a study material
    manager.delete_material("SSC", "math_notes.pdf")
    print(manager.list_materials("SSC"))
```
