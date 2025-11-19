"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Create a simple chatbot script to provide information about Nzotho FET College's courses and programs to prospective students.
Generated: DETERMINISTIC_b226f6fb35f6497b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Course:
    """Class to represent a course offered by Nzotho FET College."""
    
    def __init__(self, name, description, duration, fees):
        self.name = name
        self.description = description
        self.duration = duration
        self.fees = fees

    def to_dict(self):
        """Convert course details to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "duration": self.duration,
            "fees": self.fees
        }

class Chatbot:
    """Simple chatbot to provide information about Nzotho FET College's courses."""
    
    def __init__(self):
        self.courses = self.load_courses()

    def load_courses(self):
        """Load courses from a JSON file."""
        try:
            with open('courses.json', 'r') as file:
                courses_data = json.load(file)
                return [Course(**course) for course in courses_data]
        except FileNotFoundError:
            print("Error: courses.json file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from courses.json.")
            return []

    def get_course_info(self, course_name):
        """Retrieve course information by name."""
        for course in self.courses:
            if course.name.lower() == course_name.lower():
                return course.to_dict()
        return None

    def chat(self):
        """Start the chatbot interaction."""
        print("Welcome to Nzotho FET College Chatbot!")
        print("Type 'exit' to end the chat.")
        
        while True:
            user_input = input("Ask about a course: ")
            if user_input.lower() == 'exit':
                print("Thank you for chatting with us!")
                break
            
            course_info = self.get_course_info(user_input)
            if course_info:
                print(f"Course Name: {course_info['name']}")
                print(f"Description: {course_info['description']}")
                print(f"Duration: {course_info['duration']}")
                print(f"Fees: {course_info['fees']}")
            else:
                print("Sorry, I couldn't find any information about that course.")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
```

**Note:** Ensure you have a `courses.json` file in the same directory with the following structure:

```json
[
    {
        "name": "Computer Science",
        "description": "Learn the fundamentals of computer science.",
        "duration": "3 years",
        "fees": "$3000"
    },
    {
        "name": "Business Management",
        "description": "Gain skills in managing a business effectively.",
        "duration": "2 years",
        "fees": "$2500"
    }
]
```
