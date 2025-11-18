"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Write a program to manage franchise applications and offline/online course registrations for vocational training centers, referencing the features on the RSP Bharat website.
Generated: DETERMINISTIC_03d152a1c90e5c77
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

# Define constants for application types
FRANCHISE_APPLICATION = "Franchise Application"
ONLINE_COURSE_REGISTRATION = "Online Course Registration"
OFFLINE_COURSE_REGISTRATION = "Offline Course Registration"

# Define a class to handle franchise applications and course registrations
class VocationalTrainingCenter:
    def __init__(self):
        # Initialize data storage for applications and registrations
        self.franchise_applications = []
        self.course_registrations = []
    
    # Method to apply for a franchise
    def apply_for_franchise(self, applicant_name, contact_number, email, location):
        try:
            application = {
                "application_type": FRANCHISE_APPLICATION,
                "applicant_name": applicant_name,
                "contact_number": contact_number,
                "email": email,
                "location": location,
                "application_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.franchise_applications.append(application)
            print("Franchise application submitted successfully.")
        except Exception as e:
            print(f"Error in franchise application: {e}")
    
    # Method to register for an online course
    def register_online_course(self, student_name, contact_number, email, course_name):
        try:
            registration = {
                "registration_type": ONLINE_COURSE_REGISTRATION,
                "student_name": student_name,
                "contact_number": contact_number,
                "email": email,
                "course_name": course_name,
                "registration_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.course_registrations.append(registration)
            print("Online course registration submitted successfully.")
        except Exception as e:
            print(f"Error in online course registration: {e}")
    
    # Method to register for an offline course
    def register_offline_course(self, student_name, contact_number, email, course_name, center_location):
        try:
            registration = {
                "registration_type": OFFLINE_COURSE_REGISTRATION,
                "student_name": student_name,
                "contact_number": contact_number,
                "email": email,
                "course_name": course_name,
                "center_location": center_location,
                "registration_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.course_registrations.append(registration)
            print("Offline course registration submitted successfully.")
        except Exception as e:
            print(f"Error in offline course registration: {e}")
    
    # Method to export all data to a JSON file
    def export_data_to_json(self, file_name="vocational_training_data.json"):
        try:
            data = {
                "franchise_applications": self.franchise_applications,
                "course_registrations": self.course_registrations
            }
            with open(file_name, "w") as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Data successfully exported to {file_name}.")
        except Exception as e:
            print(f"Error exporting data to JSON: {e}")

    # Method to view all franchise applications
    def view_franchise_applications(self):
        print("Franchise Applications:")
        for application in self.franchise_applications:
            print(json.dumps(application, indent=4))

    # Method to view all course registrations
    def view_course_registrations(self):
        print("Course Registrations:")
        for registration in self.course_registrations:
            print(json.dumps(registration, indent=4))


# Main execution for testing purposes
if __name__ == "__main__":
    # Create an instance of VocationalTrainingCenter
    vtc = VocationalTrainingCenter()

    # Sample franchise application
    vtc.apply_for_franchise("Alice Smith", "9876543210", "alice@example.com", "Mumbai")

    # Sample online course registration
    vtc.register_online_course("Bob Johnson", "1234567890", "bob@example.com", "Digital Marketing")

    # Sample offline course registration
    vtc.register_offline_course("Charlie Brown", "5678901234", "charlie@example.com", "Graphic Design", "Delhi")

    # View all franchise applications
    vtc.view_franchise_applications()

    # View all course registrations
    vtc.view_course_registrations()

    # Export data to JSON
    vtc.export_data_to_json()
```
