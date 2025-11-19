"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Develop a program that compiles a list of technical courses offered in the "کارو دانش" system and outputs them in a structured format.
Generated: DETERMINISTIC_71fd290996c0075a
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class TechnicalCoursesCompiler:
    """
    A class to compile and manage technical courses offered in the "کارو دانش" system.
    
    Attributes:
        courses (List[Dict[str, str]]): A list of technical courses with their details.
    """

    def __init__(self):
        """Initialize the compiler with an empty list of courses."""
        self.courses = []

    def add_course(self, name: str, code: str, duration: str, field: str) -> None:
        """
        Add a new technical course to the compiler.
        
        Args:
            name (str): Name of the course.
            code (str): Unique identifier for the course.
            duration (str): Duration of the course.
            field (str): Field or category of the course.
        
        Raises:
            ValueError: If any of the required fields are empty.
        """
        if not all([name, code, duration, field]):
            raise ValueError("All course fields must be provided.")
        
        self.courses.append({
            "name": name,
            "code": code,
            "duration": duration,
            "field": field
        })

    def remove_course(self, code: str) -> bool:
        """
        Remove a course from the compiler by its code.
        
        Args:
            code (str): Code of the course to remove.
            
        Returns:
            bool: True if the course was found and removed, False otherwise.
        """
        for i, course in enumerate(self.courses):
            if course["code"] == code:
                del self.courses[i]
                return True
        return False

    def get_courses(self) -> List[Dict[str, str]]:
        """
        Get all current technical courses.
        
        Returns:
            List[Dict[str, str]]: A list of all courses.
        """
        return self.courses.copy()

    def search_course(self, query: str, field: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Search for courses by name or field.
        
        Args:
            query (str): Search term to match against course names.
            field (Optional[str]): Field to filter courses by.
            
        Returns:
            List[Dict[str, str]]: A list of matching courses.
        """
        results = []
        for course in self.courses:
            if query.lower() in course["name"].lower():
                if field is None or course["field"].lower() == field.lower():
                    results.append(course)
        return results

    def save_to_file(self, filename: str) -> None:
        """
        Save the current courses to a JSON file.
        
        Args:
            filename (str): Path to the output file.
            
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.courses, f, ensure_ascii=False, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save courses to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load courses from a JSON file.
        
        Args:
            filename (str): Path to the input file.
            
        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("Invalid data format. Expected a list of courses.")
                self.courses = data
        except IOError as e:
            raise IOError(f"Failed to load courses from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")

def main():
    """Example usage of the TechnicalCoursesCompiler."""
    compiler = TechnicalCoursesCompiler()
    
    # Add some sample courses
    compiler.add_course("برق صنعتی", "ELC101", "2 سال", "صنعت")
    compiler.add_course("مکانیک خودرو", "MEC201", "18 ماه", "خودرو")
    compiler.add_course("نجاری", "CAR301", "1 سال", "صنایع چوب")
    
    # Save to file
    compiler.save_to_file("technical_courses.json")
    
    # Load from file
    new_compiler = TechnicalCoursesCompiler()
    new_compiler.load_from_file("technical_courses.json")
    
    # Print all courses
    print("All Courses:")
    for course in new_compiler.get_courses():
        print(f"{course['name']} ({course['code']}) - {course['duration']} - {course['field']}")
    
    # Search for courses
    print("\nSearch Results for 'برق':")
    for course in new_compiler.search_course("برق"):
        print(f"{course['name']} ({course['code']})")

if __name__ == "__main__":
    main()
```
