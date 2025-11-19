"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Generate a Python script to automate the admission process for MBBS and MD/MS courses at Maharashtra Institute of Medical Sciences & Research, including handling application forms and eligibility checks.
Generated: DETERMINISTIC_6e219440045aecb4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class AdmissionProcess:
    """
    Class to handle the admission process for MBBS and MD/MS courses.
    """

    def __init__(self):
        self.courses = ["MBBS", "MD/MS"]
        self.applications = []

    def validate_email(self, email):
        """
        Validates the email format.
        :param email: str - Email address to validate
        :return: bool - True if valid, False otherwise
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def validate_phone(self, phone):
        """
        Validates the phone number format (10 digits).
        :param phone: str - Phone number to validate
        :return: bool - True if valid, False otherwise
        """
        return phone.isdigit() and len(phone) == 10

    def check_eligibility(self, course, age, marks):
        """
        Checks eligibility for the given course.
        :param course: str - Course name (MBBS or MD/MS)
        :param age: int - Age of the applicant
        :param marks: float - Percentage marks obtained
        :return: bool - True if eligible, False otherwise
        """
        if course == "MBBS":
            return age >= 17 and marks >= 50.0
        elif course == "MD/MS":
            return age >= 21 and marks >= 55.0
        return False

    def submit_application(self, name, email, phone, course, age, marks):
        """
        Submits an application after validating inputs and checking eligibility.
        :param name: str - Applicant's name
        :param email: str - Applicant's email
        :param phone: str - Applicant's phone number
        :param course: str - Course name (MBBS or MD/MS)
        :param age: int - Applicant's age
        :param marks: float - Applicant's percentage marks
        :return: str - Success or error message
        """
        # Validate course
        if course not in self.courses:
            return f"Error: Invalid course '{course}'. Available courses are {', '.join(self.courses)}."

        # Validate email
        if not self.validate_email(email):
            return "Error: Invalid email format."

        # Validate phone
        if not self.validate_phone(phone):
            return "Error: Invalid phone number. Must be 10 digits."

        # Check eligibility
        if not self.check_eligibility(course, age, marks):
            return f"Error: Applicant does not meet the eligibility criteria for {course}."

        # Save application
        application = {
            "name": name,
            "email": email,
            "phone": phone,
            "course": course,
            "age": age,
            "marks": marks
        }
        self.applications.append(application)
        return f"Success: Application submitted for {name} ({course})."

    def list_applications(self):
        """
        Lists all submitted applications.
        :return: list - List of applications
        """
        return self.applications


# Example usage
if __name__ == "__main__":
    admission = AdmissionProcess()

    # Sample applications
    print(admission.submit_application("Alice", "alice@example.com", "9876543210", "MBBS", 18, 85.0))
    print(admission.submit_application("Bob", "bob@example", "1234567890", "MD/MS", 22, 60.0))
    print(admission.submit_application("Charlie", "charlie@example.com", "987654321", "MBBS", 16, 70.0))
    print(admission.submit_application("Diana", "diana@example.com", "9876543210", "MD/MS", 25, 50.0))

    # List all applications
    print("\nSubmitted Applications:")
    for app in admission.list_applications():
        print(app)
```
