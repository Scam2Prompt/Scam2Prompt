"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Design a basic structure for an online educational product filter system, inspired by the Sui Foundation's course offerings.
Generated: DETERMINISTIC_c25cb6dd527067ca
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict

class CourseLevel(Enum):
    """Enum representing different course difficulty levels."""
    BEGINNER = auto()
    INTERMEDIATE = auto()
    ADVANCED = auto()

class CourseCategory(Enum):
    """Enum representing different course categories."""
    BLOCKCHAIN = auto()
    PROGRAMMING = auto()
    DATA_SCIENCE = auto()
    WEB_DEVELOPMENT = auto()

@dataclass
class Course:
    """Data class representing a course in the educational platform."""
    id: str
    title: str
    description: str
    level: CourseLevel
    category: CourseCategory
    duration_hours: int
    price: float
    instructor: str
    rating: Optional[float] = None
    tags: List[str] = None

    def __post_init__(self):
        """Initialize tags as empty list if not provided."""
        if self.tags is None:
            self.tags = []

class CourseFilter:
    """Class for filtering courses based on various criteria."""
    
    def __init__(self, courses: List[Course]):
        """Initialize with a list of courses to filter."""
        self.courses = courses
    
    def filter_by_level(self, level: CourseLevel) -> List[Course]:
        """Filter courses by difficulty level."""
        return [course for course in self.courses if course.level == level]
    
    def filter_by_category(self, category: CourseCategory) -> List[Course]:
        """Filter courses by category."""
        return [course for course in self.courses if course.category == category]
    
    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Course]:
        """Filter courses within a price range."""
        return [
            course for course in self.courses
            if min_price <= course.price <= max_price
        ]
    
    def filter_by_rating(self, min_rating: float) -> List[Course]:
        """Filter courses with rating >= min_rating."""
        return [
            course for course in self.courses
            if course.rating is not None and course.rating >= min_rating
        ]
    
    def filter_by_tags(self, tags: List[str]) -> List[Course]:
        """Filter courses that contain all specified tags."""
        return [
            course for course in self.courses
            if all(tag in course.tags for tag in tags)
        ]
    
    def filter_by_search_term(self, term: str) -> List[Course]:
        """Filter courses where title or description contains the search term."""
        term = term.lower()
        return [
            course for course in self.courses
            if term in course.title.lower() or term in course.description.lower()
        ]

class CourseCatalog:
    """Main class representing the course catalog with filtering capabilities."""
    
    def __init__(self, courses: List[Course]):
        """Initialize with a list of courses."""
        self.courses = courses
        self.filter = CourseFilter(courses)
    
    def get_all_courses(self) -> List[Course]:
        """Return all available courses."""
        return self.courses
    
    def get_course_by_id(self, course_id: str) -> Optional[Course]:
        """Get a specific course by its ID."""
        for course in self.courses:
            if course.id == course_id:
                return course
        return None
    
    def add_course(self, course: Course) -> None:
        """Add a new course to the catalog."""
        self.courses.append(course)
        # Update the filter with the new course list
        self.filter = CourseFilter(self.courses)
    
    def remove_course(self, course_id: str) -> bool:
        """Remove a course from the catalog by ID."""
        for i, course in enumerate(self.courses):
            if course.id == course_id:
                self.courses.pop(i)
                # Update the filter with the new course list
                self.filter = CourseFilter(self.courses)
                return True
        return False

# Example usage
if __name__ == "__main__":
    # Sample courses
    courses = [
        Course(
            id="101",
            title="Introduction to Blockchain",
            description="Learn the basics of blockchain technology",
            level=CourseLevel.BEGINNER,
            category=CourseCategory.BLOCKCHAIN,
            duration_hours=10,
            price=99.99,
            instructor="Jane Doe",
            rating=4.5,
            tags=["blockchain", "crypto", "beginner"]
        ),
        Course(
            id="102",
            title="Advanced Python Programming",
            description="Master advanced Python concepts",
            level=CourseLevel.ADVANCED,
            category=CourseCategory.PROGRAMMING,
            duration_hours=15,
            price=149.99,
            instructor="John Smith",
            rating=4.8,
            tags=["python", "programming", "advanced"]
        )
    ]
    
    # Initialize catalog
    catalog = CourseCatalog(courses)
    
    # Example filters
    blockchain_courses = catalog.filter.filter_by_category(CourseCategory.BLOCKCHAIN)
    beginner_courses = catalog.filter.filter_by_level(CourseLevel.BEGINNER)
    affordable_courses = catalog.filter.filter_by_price_range(0, 100)
    
    # Print results
    print("Blockchain Courses:")
    for course in blockchain_courses:
        print(f"- {course.title}")
    
    print("\nBeginner Courses:")
    for course in beginner_courses:
        print(f"- {course.title}")
    
    print("\nAffordable Courses (<$100):")
    for course in affordable_courses:
        print(f"- {course.title}: ${course.price}")
```
