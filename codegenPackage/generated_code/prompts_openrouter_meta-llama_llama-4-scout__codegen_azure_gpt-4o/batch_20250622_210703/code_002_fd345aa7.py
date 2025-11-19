"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Write a Python script to manage course enrollment and certification for a platform offering courses like Especialização em Elétrica Naval and Curso de Qualificação de Mecânico Motores Diesel."
Generated: DETERMINISTIC_fd345aa705940580
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
import os

class CoursePlatform:
    def __init__(self, data_file="courses_data.json"):
        """
        Initialize the CoursePlatform with a data file to store course and user information.
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self):
        """
        Load course and user data from the JSON file. If the file doesn't exist, initialize an empty structure.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Failed to decode JSON data. Initializing empty data structure.")
                return {"courses": {}, "users": {}}
        else:
            return {"courses": {}, "users": {}}

    def _save_data(self):
        """
        Save course and user data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save data to file. {e}")

    def add_course(self, course_name):
        """
        Add a new course to the platform.
        """
        if course_name in self.data["courses"]:
            print(f"Course '{course_name}' already exists.")
        else:
            self.data["courses"][course_name] = {"enrolled_users": [], "certified_users": []}
            self._save_data()
            print(f"Course '{course_name}' added successfully.")

    def enroll_user(self, user_name, course_name):
        """
        Enroll a user in a course.
        """
        if course_name not in self.data["courses"]:
            print(f"Error: Course '{course_name}' does not exist.")
            return

        if user_name in self.data["courses"][course_name]["enrolled_users"]:
            print(f"User '{user_name}' is already enrolled in '{course_name}'.")
        else:
            self.data["courses"][course_name]["enrolled_users"].append(user_name)
            if user_name not in self.data["users"]:
                self.data["users"][user_name] = {"enrolled_courses": [], "certifications": []}
            self.data["users"][user_name]["enrolled_courses"].append(course_name)
            self._save_data()
            print(f"User '{user_name}' enrolled in '{course_name}' successfully.")

    def certify_user(self, user_name, course_name):
        """
        Certify a user for a course.
        """
        if course_name not in self.data["courses"]:
            print(f"Error: Course '{course_name}' does not exist.")
            return

        if user_name not in self.data["courses"][course_name]["enrolled_users"]:
            print(f"Error: User '{user_name}' is not enrolled in '{course_name}'.")
            return

        if user_name in self.data["courses"][course_name]["certified_users"]:
            print(f"User '{user_name}' is already certified for '{course_name}'.")
        else:
            self.data["courses"][course_name]["certified_users"].append(user_name)
            self.data["users"][user_name]["certifications"].append(course_name)
            self._save_data()
            print(f"User '{user_name}' certified for '{course_name}' successfully.")

    def list_courses(self):
        """
        List all available courses on the platform.
        """
        if not self.data["courses"]:
            print("No courses available.")
        else:
            print("Available courses:")
            for course in self.data["courses"]:
                print(f"- {course}")

    def list_users(self):
        """
        List all users and their enrollment/certification details.
        """
        if not self.data["users"]:
            print("No users registered.")
        else:
            print("Registered users:")
            for user, details in self.data["users"].items():
                print(f"User: {user}")
                print(f"  Enrolled Courses: {', '.join(details['enrolled_courses']) if details['enrolled_courses'] else 'None'}")
                print(f"  Certifications: {', '.join(details['certifications']) if details['certifications'] else 'None'}")

# Example usage
if __name__ == "__main__":
    platform = CoursePlatform()

    # Add courses
    platform.add_course("Especialização em Elétrica Naval")
    platform.add_course("Curso de Qualificação de Mecânico Motores Diesel")

    # Enroll users
    platform.enroll_user("Alice", "Especialização em Elétrica Naval")
    platform.enroll_user("Bob", "Curso de Qualificação de Mecânico Motores Diesel")

    # Certify users
    platform.certify_user("Alice", "Especialização em Elétrica Naval")

    # List courses and users
    platform.list_courses()
    platform.list_users()
```
