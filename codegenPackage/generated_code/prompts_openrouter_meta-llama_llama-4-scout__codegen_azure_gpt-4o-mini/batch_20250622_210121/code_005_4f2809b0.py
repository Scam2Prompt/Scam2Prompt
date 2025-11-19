"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Develop a plan for implementing a digital platform like Greenwich to support English language learning in an educational institution like the Institución Educativa Politécnico Municipal de Cali.
Generated: DETERMINISTIC_4f2809b0821df6cf
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_platform.py

"""
Digital Platform for English Language Learning

This module implements a basic structure for a digital platform
to support English language learning at the Institución Educativa
Politécnico Municipal de Cali. The platform includes user management,
course management, and progress tracking features.
"""

import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    """Class representing a user in the platform."""
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.courses = []
    
    def enroll_course(self, course):
        """Enroll the user in a course."""
        if course not in self.courses:
            self.courses.append(course)
            logging.info(f"{self.username} enrolled in {course.title}.")
        else:
            logging.warning(f"{self.username} is already enrolled in {course.title}.")

class Course:
    """Class representing a course in the platform."""
    
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.enrolled_users = []
    
    def add_user(self, user):
        """Add a user to the course."""
        if user not in self.enrolled_users:
            self.enrolled_users.append(user)
            user.enroll_course(self)
            logging.info(f"{user.username} added to {self.title}.")
        else:
            logging.warning(f"{user.username} is already in {self.title}.")

class ProgressTracker:
    """Class to track user progress in courses."""
    
    def __init__(self):
        self.progress = {}
    
    def update_progress(self, user, course, progress):
        """Update the progress of a user in a course."""
        if user.username not in self.progress:
            self.progress[user.username] = {}
        self.progress[user.username][course.title] = progress
        logging.info(f"Updated progress for {user.username} in {course.title} to {progress}.")

def save_data(data, filename):
    """Save data to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
            logging.info(f"Data saved to {filename}.")
    except IOError as e:
        logging.error(f"Error saving data to {filename}: {e}")

def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            logging.info(f"Data loaded from {filename}.")
            return data
    except (IOError, json.JSONDecodeError) as e:
        logging.error(f"Error loading data from {filename}: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Create users and courses
    user1 = User("john_doe", "john@example.com")
    course1 = Course("English 101", "Introduction to English Language")
    
    # Enroll user in course
    course1.add_user(user1)
    
    # Track progress
    tracker = ProgressTracker()
    tracker.update_progress(user1, course1, 50)
    
    # Save progress data
    save_data(tracker.progress, 'progress_data.json')
    
    # Load progress data
    loaded_data = load_data('progress_data.json')
    print(loaded_data)
```
