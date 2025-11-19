"""
Generated Code Metadata:
========================
Original URL: https://mimsr.edu.in
Prompt: What are the details of the medical courses offered at MIMSR, including MBBS, MD/MS, and PhD programs, and what are the admission requirements and procedures for these courses?
Generated: DETERMINISTIC_5e50967ab40a5369
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class MedicalCourses:
    def __init__(self):
        # Initialize the details of courses offered
        self.courses = {
            "MBBS": {
                "duration": "5.5 years (including 1 year internship)",
                "eligibility": "10+2 with Physics, Chemistry, Biology, and English (minimum 50% marks)",
                "admission_procedure": [
                    "Qualify NEET (National Eligibility cum Entrance Test)",
                    "Apply through the centralized admission process",
                    "Participate in counseling and secure a seat"
                ]
            },
            "MD/MS": {
                "duration": "3 years",
                "eligibility": "MBBS degree with completion of internship and valid NEET-PG score",
                "admission_procedure": [
                    "Qualify NEET-PG (Postgraduate Medical Entrance Test)",
                    "Apply through the centralized admission process",
                    "Participate in counseling and secure a seat"
                ]
            },
            "PhD": {
                "duration": "3-5 years",
                "eligibility": "Postgraduate degree (MD/MS or equivalent) in relevant field",
                "admission_procedure": [
                    "Submit research proposal and academic credentials",
                    "Qualify entrance exam and/or interview conducted by the institute",
                    "Secure admission based on merit and availability of guides"
                ]
            }
        }

    def get_course_details(self, course_name):
        """
        Fetch details of a specific course.
        :param course_name: Name of the course (e.g., 'MBBS', 'MD/MS', 'PhD')
        :return: Dictionary containing course details or error message if course not found
        """
        try:
            course_details = self.courses.get(course_name.upper())
            if not course_details:
                raise ValueError(f"Course '{course_name}' not found.")
            return course_details
        except ValueError as e:
            return {"error": str(e)}

    def get_all_courses(self):
        """
        Fetch details of all courses offered.
        :return: Dictionary containing all course details
        """
        return self.courses


def main():
    # Create an instance of MedicalCourses
    mimsr_courses = MedicalCourses()

    # Example: Fetch details of a specific course
    course_name = input("Enter the course name (MBBS, MD/MS, PhD): ").strip()
    course_details = mimsr_courses.get_course_details(course_name)
    print("\nCourse Details:")
    print(json.dumps(course_details, indent=4))

    # Example: Fetch details of all courses
    print("\nAll Courses Offered:")
    all_courses = mimsr_courses.get_all_courses()
    print(json.dumps(all_courses, indent=4))


if __name__ == "__main__":
    # Entry point of the program
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
