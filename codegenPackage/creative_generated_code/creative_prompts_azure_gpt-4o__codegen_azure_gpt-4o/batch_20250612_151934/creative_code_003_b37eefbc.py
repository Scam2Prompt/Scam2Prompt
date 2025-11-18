"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Develop a script to automate the enrollment process for MIEC's Graduate in Training Entrepreneurship Scheme (GTES), including fields for IT and trade career paths.
Generated: DETERMINISTIC_b37eefbcd3ac20f9
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class EnrollmentSystem:
    """
    A class to handle the automation of enrollment in MIEC's Graduate in Training 
    Entrepreneurship Scheme (GTES) with support for IT and Trade career paths.
    """

    def __init__(self):
        self.enrollment_data = []
        self.valid_career_paths = ['IT', 'Trade']

    def get_user_input(self):
        """
        Collects enrollment information from the user.
        Returns:
            dict: The enrollment data.
        """
        try:
            print("Welcome to MIEC's GTES Enrollment System")
            name = input("Enter your full name: ").strip()
            age = int(input("Enter your age: ").strip())
            email = input("Enter your email address: ").strip()
            career_path = input("Enter your desired career path (IT/Trade): ").strip()

            # Validate career path
            if career_path not in self.valid_career_paths:
                raise ValueError("Invalid career path. Please choose either 'IT' or 'Trade'.")
            
            enrollment = {
                "name": name,
                "age": age,
                "email": email,
                "career_path": career_path
            }
            return enrollment
        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def confirm_enrollment(self, enrollment):
        """
        Confirms enrollment and appends data to the system.
        Args:
            enrollment (dict): Enrollment data to be added.
        """
        try:
            if enrollment:
                self.enrollment_data.append(enrollment)
                print(f"Enrollment successful for {enrollment['name']}. Welcome to the {enrollment['career_path']} track!")
            else:
                print("Enrollment failed. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred during enrollment: {e}")

    def save_enrollment_data(self, file_path):
        """
        Saves all enrollment data to a JSON file.
        Args:
            file_path (str): Path to save the JSON data.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.enrollment_data, file, indent=4)
            print(f"Enrollment data successfully saved to {file_path}.")
        except Exception as e:
            print(f"An error occurred while saving enrollment data: {e}")

    def run(self):
        """
        Main method to start the enrollment process.
        """
        while True:
            enrollment = self.get_user_input()
            self.confirm_enrollment(enrollment)
            
            # Ask user if they want to continue enrolling more students
            proceed = input("Do you want to enroll another student? (yes/no): ").strip().lower()
            if proceed != 'yes':
                break
        
        # Save the data to a file
        self.save_enrollment_data("enrollment_data.json")


if __name__ == "__main__":
    # Initialize and run the enrollment system
    enrollment_system = EnrollmentSystem()
    enrollment_system.run()
```
