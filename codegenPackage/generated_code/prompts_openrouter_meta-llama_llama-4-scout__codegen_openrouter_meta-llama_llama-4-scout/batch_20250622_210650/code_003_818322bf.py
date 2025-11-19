"""
Generated Code Metadata:
========================
Original URL: https://happyscholarsacademy.com
Prompt: Generate a sample enrollment application for Happy Scholars Academy, including required documents and information, such as the Universal Child Health Record form.
Generated: DETERMINISTIC_818322bfa2d21f63
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# enrollment_application.py

class Student:
    def __init__(self, first_name, last_name, date_of_birth):
        """
        Initialize a Student object.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            date_of_birth (str): Student's date of birth (YYYY-MM-DD).
        """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

class Parent:
    def __init__(self, first_name, last_name, email, phone):
        """
        Initialize a Parent object.

        Args:
            first_name (str): Parent's first name.
            last_name (str): Parent's last name.
            email (str): Parent's email address.
            phone (str): Parent's phone number.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

class EnrollmentApplication:
    def __init__(self, student, parent, documents):
        """
        Initialize an EnrollmentApplication object.

        Args:
            student (Student): Student object.
            parent (Parent): Parent object.
            documents (dict): Dictionary of required documents.
        """
        self.student = student
        self.parent = parent
        self.documents = documents

    def validate_documents(self):
        """
        Validate required documents.

        Returns:
            bool: True if all documents are present, False otherwise.
        """
        required_documents = ["Universal Child Health Record", "Birth Certificate", "Immunization Records"]
        return all(doc in self.documents for doc in required_documents)

    def submit_application(self):
        """
        Submit the enrollment application.

        Returns:
            str: Success message or error message if documents are invalid.
        """
        if self.validate_documents():
            return f"Enrollment application submitted successfully for {self.student.first_name} {self.student.last_name}."
        else:
            return "Error: Invalid documents. Please ensure all required documents are present."

def main():
    try:
        # Create student object
        student = Student("John", "Doe", "2010-01-01")

        # Create parent object
        parent = Parent("Jane", "Doe", "jane.doe@example.com", "123-456-7890")

        # Create documents dictionary
        documents = {
            "Universal Child Health Record": "UCHR-12345",
            "Birth Certificate": "BC-12345",
            "Immunization Records": "IR-12345"
        }

        # Create enrollment application object
        application = EnrollmentApplication(student, parent, documents)

        # Submit enrollment application
        print(application.submit_application())

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
