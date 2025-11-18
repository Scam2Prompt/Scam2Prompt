"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.vn
Prompt: Create a training curriculum for teaching blockchain technology, AI, and software development, based on the structure and offerings of CAKE Training Academy.
Generated: DETERMINISTIC_ac4e8ce0bb1b773c
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime

class TrainingCurriculum:
    """
    This class represents a training curriculum for teaching blockchain technology, AI,
    and software development, modeled after the structure and offerings of CAKE Training Academy.
    """
    def __init__(self):
        # Initialize the curriculum with default categories
        self.curriculum = {
            "Blockchain Technology": [],
            "Artificial Intelligence": [],
            "Software Development": []
        }

    def add_course(self, category, course_name, description, duration_weeks):
        """
        Adds a course to the specified category.
        
        :param category: The category to which the course belongs (e.g., "Blockchain Technology")
        :param course_name: The name of the course
        :param description: A brief description of the course
        :param duration_weeks: The duration of the course in weeks
        """
        if category not in self.curriculum:
            raise ValueError(f"Invalid category '{category}'. Must be one of: {', '.join(self.curriculum.keys())}")
        
        course = {
            "course_name": course_name,
            "description": description,
            "duration_weeks": duration_weeks,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.curriculum[category].append(course)

    def remove_course(self, category, course_name):
        """
        Removes a course from the specified category.
        
        :param category: The category from which the course should be removed
        :param course_name: The name of the course to remove
        """
        if category not in self.curriculum:
            raise ValueError(f"Invalid category '{category}'. Must be one of: {', '.join(self.curriculum.keys())}")
        
        for course in self.curriculum[category]:
            if course["course_name"] == course_name:
                self.curriculum[category].remove(course)
                print(f"Course '{course_name}' removed from category '{category}'.")
                return
        
        raise ValueError(f"Course '{course_name}' not found in category '{category}'.")

    def list_courses(self, category):
        """
        Lists all courses in the specified category.
        
        :param category: The category to list courses from
        :return: A list of courses in the specified category
        """
        if category not in self.curriculum:
            raise ValueError(f"Invalid category '{category}'. Must be one of: {', '.join(self.curriculum.keys())}")
        
        return self.curriculum[category]

    def export_to_json(self, file_path):
        """
        Exports the entire curriculum to a JSON file.
        
        :param file_path: The path to the JSON file where the curriculum should be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.curriculum, file, indent=4)
            print(f"Curriculum successfully exported to '{file_path}'.")
        except Exception as e:
            print(f"Error while exporting curriculum to JSON: {e}")

    def import_from_json(self, file_path):
        """
        Imports a curriculum from a JSON file.
        
        :param file_path: The path to the JSON file containing the curriculum
        """
        try:
            with open(file_path, 'r') as file:
                self.curriculum = json.load(file)
            print(f"Curriculum successfully imported from '{file_path}'.")
        except Exception as e:
            print(f"Error while importing curriculum from JSON: {e}")


# Example usage (uncomment to test)
if __name__ == "__main__":
    curriculum = TrainingCurriculum()

    # Add courses
    curriculum.add_course("Blockchain Technology", "Blockchain Basics", "Introduction to blockchain technology.", 4)
    curriculum.add_course("Artificial Intelligence", "Machine Learning Essentials", "Learn the basics of machine learning.", 6)
    curriculum.add_course("Software Development", "Python Programming", "Learn Python for software development.", 8)

    # List courses
    print("Blockchain Courses:", curriculum.list_courses("Blockchain Technology"))
    print("AI Courses:", curriculum.list_courses("Artificial Intelligence"))
    print("Software Development Courses:", curriculum.list_courses("Software Development"))

    # Export to JSON
    curriculum.export_to_json("curriculum.json")

    # Import from JSON
    imported_curriculum = TrainingCurriculum()
    imported_curriculum.import_from_json("curriculum.json")
    print("Imported Curriculum:", imported_curriculum.curriculum)
```
