"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Develop a program to organize and display the syllabus and results for MBBS and MD/MS courses at MIMSR Medical College, referencing the "Syllabus & Results" section.
Generated: DETERMINISTIC_db6452cb630dfd84
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import os

class Course:
    """
    Class representing a course with its syllabus and results.
    """
    def __init__(self, name, syllabus, results):
        """
        Initializes a Course object.
        
        :param name: Name of the course
        :param syllabus: List of syllabus topics
        :param results: Dictionary containing student results
        """
        self.name = name
        self.syllabus = syllabus
        self.results = results

    def display_syllabus(self):
        """
        Display the syllabus topics for the course.
        """
        print(f"Syllabus for {self.name}:")
        for idx, topic in enumerate(self.syllabus, 1):
            print(f"{idx}. {topic}")

    def display_results(self):
        """
        Display the results for the course.
        """
        print(f"Results for {self.name}:")
        for student, result in self.results.items():
            print(f"{student}: {result}")


def load_data():
    """
    Function to load syllabus and results for MBBS and MD/MS courses.
    
    :return: Dictionary of Course objects representing the data
    """
    try:
        # Simulate data (in a real-world scenario, this data could be fetched from a database or file)
        mbbs_syllabus = [
            "Anatomy", "Physiology", "Biochemistry", "Pathology", "Pharmacology",
            "Microbiology", "Forensic Medicine", "Community Medicine", "General Medicine",
            "Surgery", "Orthopedics", "Pediatrics", "Obstetrics and Gynecology"
        ]
        mbbs_results = {
            "Alice": "Pass",
            "Bob": "Pass",
            "Charlie": "Fail"
        }

        mdms_syllabus = [
            "General Medicine Specialization", "Surgical Techniques", "Radiology",
            "Pediatrics Advanced Topics", "Oncology", "Cardiology", "Neurology"
        ]
        mdms_results = {
            "Dr. Smith": "Distinction",
            "Dr. Johnson": "Pass",
            "Dr. Lee": "Pass"
        }

        # Create Course objects
        courses = {
            "MBBS": Course("MBBS", mbbs_syllabus, mbbs_results),
            "MD/MS": Course("MD/MS", mdms_syllabus, mdms_results)
        }

        return courses

    except Exception as e:
        print(f"Error loading data: {e}")
        return {}


def main():
    """
    Main function to organize and display the syllabus and results for MBBS and MD/MS courses.
    """
    print("Welcome to MIMSR Medical College Syllabus & Results Section\n")

    # Load course data
    courses = load_data()

    if not courses:
        print("Could not load course data. Exiting...")
        return

    # Display options to user
    while True:
        print("\nAvailable Courses:")
        for idx, course_name in enumerate(courses.keys(), 1):
            print(f"{idx}. {course_name}")
        print("0. Exit")

        try:
            choice = int(input("\nEnter the number corresponding to the course you want to view: "))

            if choice == 0:
                print("Exiting program. Goodbye!")
                break

            course_name = list(courses.keys())[choice - 1]
            course = courses[course_name]

            print(f"\nYou selected: {course_name}")
            print("1. View Syllabus")
            print("2. View Results")
            action = int(input("Enter 1 or 2 to proceed: "))

            if action == 1:
                course.display_syllabus()
            elif action == 2:
                course.display_results()
            else:
                print("Invalid action. Please try again.")

        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    # Ensure the main function is executed only when the script is run directly
    main()
```
