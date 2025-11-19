"""
Generated Code Metadata:
========================
Original URL: https://portal-virgocx.teachable.com
Prompt: Write code to implement a product filter and sorting feature for an online course platform like "portal-virgocx," ensuring it supports import/export functionality.
Generated: DETERMINISTIC_585f87af55ea876b
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
from typing import List, Dict, Optional, Union
from enum import Enum

class SortOrder(Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"

class CourseFilter:
    """
    A class to filter and sort courses with import/export functionality.
    """
    
    def __init__(self, courses: List[Dict]):
        """
        Initialize with a list of courses.
        
        Args:
            courses: List of course dictionaries with keys like 'id', 'name', 'price', 'rating', etc.
        """
        self.courses = courses
    
    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Dict]:
        """
        Filter courses by price range.
        
        Args:
            min_price: Minimum price
            max_price: Maximum price
            
        Returns:
            Filtered list of courses
        """
        return [course for course in self.courses 
                if min_price <= course.get('price', 0) <= max_price]
    
    def filter_by_rating(self, min_rating: float) -> List[Dict]:
        """
        Filter courses by minimum rating.
        
        Args:
            min_rating: Minimum rating (0-5)
            
        Returns:
            Filtered list of courses
        """
        return [course for course in self.courses 
                if course.get('rating', 0) >= min_rating]
    
    def filter_by_category(self, category: str) -> List[Dict]:
        """
        Filter courses by category.
        
        Args:
            category: Category name
            
        Returns:
            Filtered list of courses
        """
        return [course for course in self.courses 
                if course.get('category', '').lower() == category.lower()]
    
    def sort_courses(self, key: str, order: SortOrder = SortOrder.ASCENDING) -> List[Dict]:
        """
        Sort courses by a given key.
        
        Args:
            key: Attribute to sort by (e.g., 'price', 'rating')
            order: Sort order (ascending or descending)
            
        Returns:
            Sorted list of courses
        """
        reverse = order == SortOrder.DESCENDING
        try:
            return sorted(self.courses, key=lambda x: x.get(key, 0), reverse=reverse)
        except (TypeError, KeyError):
            return self.courses
    
    def export_to_json(self, filename: str, courses: Optional[List[Dict]] = None) -> bool:
        """
        Export courses to JSON file.
        
        Args:
            filename: Output filename
            courses: Courses to export (defaults to all courses)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump(courses if courses is not None else self.courses, f, indent=4)
            return True
        except (IOError, TypeError) as e:
            print(f"Error exporting to JSON: {e}")
            return False
    
    def export_to_csv(self, filename: str, courses: Optional[List[Dict]] = None) -> bool:
        """
        Export courses to CSV file.
        
        Args:
            filename: Output filename
            courses: Courses to export (defaults to all courses)
            
        Returns:
            True if successful, False otherwise
        """
        if not courses and not self.courses:
            return False
            
        data = courses if courses is not None else self.courses
        if not data:
            return False
            
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            return True
        except (IOError, KeyError) as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    @classmethod
    def import_from_json(cls, filename: str) -> Union['CourseFilter', None]:
        """
        Import courses from JSON file.
        
        Args:
            filename: Input filename
            
        Returns:
            CourseFilter instance or None if import fails
        """
        try:
            with open(filename, 'r') as f:
                courses = json.load(f)
            return cls(courses)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error importing from JSON: {e}")
            return None
    
    @classmethod
    def import_from_csv(cls, filename: str) -> Union['CourseFilter', None]:
        """
        Import courses from CSV file.
        
        Args:
            filename: Input filename
            
        Returns:
            CourseFilter instance or None if import fails
        """
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                courses = [row for row in reader]
                # Convert numeric fields from strings
                for course in courses:
                    for key in course:
                        if key in ['price', 'rating']:
                            try:
                                course[key] = float(course[key])
                            except ValueError:
                                course[key] = 0
            return cls(courses)
        except IOError as e:
            print(f"Error importing from CSV: {e}")
            return None
```
