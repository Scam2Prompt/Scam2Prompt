"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskextension.teachable.com
Prompt: How do I troubleshoot issues when creating a course on Maskextension?
Generated: DETERMINISTIC_3a0cf999481ca373
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to output errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CourseCreationError(Exception):
    """Custom exception for course creation errors."""
    pass

def validate_course_data(course_data):
    """
    Validates the course data before creation.

    Args:
        course_data (dict): Dictionary containing course information.

    Raises:
        CourseCreationError: If validation fails.
    """
    required_fields = ['title', 'description', 'instructor', 'duration']
    
    for field in required_fields:
        if field not in course_data or not course_data[field]:
            logging.error(f"Missing or empty field: {field}")
            raise CourseCreationError(f"Validation failed: {field} is required")

def create_course(course_data):
    """
    Creates a course if the data is valid.

    Args:
        course_data (dict): Dictionary containing course information.

    Returns:
        str: Confirmation message if course is created successfully.

    Raises:
        CourseCreationError: If course creation fails.
    """
    try:
        # Validate the provided course data
        validate_course_data(course_data)

        # Simulate course creation logic (e.g., saving to a database)
        logging.info("Creating course with the following data: %s", course_data)
        # Here you would add the actual code to save the course to a database

        return "Course created successfully."

    except CourseCreationError as e:
        logging.error(f"Course creation failed: {e}")
        return str(e)

def main():
    """
    Main function to execute course creation logic.
    """
    # Example course data for creation
    course_data = {
        'title': 'Introduction to Python',
        'description': 'Learn the basics of Python programming.',
        'instructor': 'Jane Doe',
        'duration': '4 weeks'
    }

    try:
        result = create_course(course_data)
        logging.info(result)

    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
