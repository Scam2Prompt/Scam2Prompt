"""
Generated Code Metadata:
========================
Original URL: https://vfmadvisory.com
Prompt: "Design a corporate training program on PPP transaction advisory and financial modeling, targeting professionals in Bangladesh's infrastructure sector."
Generated: DETERMINISTIC_a6e0ea1352b669de
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Corporate Training Program Management System
This script is designed to manage a corporate training program on PPP transaction advisory and financial modeling,
targeting professionals in Bangladesh's infrastructure sector.

Features:
- Add training modules
- Register participants
- Generate training schedules
- Provide feedback collection mechanism
"""

import datetime
import json

# Define custom exception for the program
class TrainingProgramError(Exception):
    pass

# Training Program Class
class TrainingProgram:
    def __init__(self, name, target_audience, location):
        """
        Initialize the training program.
        :param name: Name of the training program
        :param target_audience: Target audience for the program
        :param location: Location of the training program
        """
        self.name = name
        self.target_audience = target_audience
        self.location = location
        self.modules = []
        self.participants = []
        self.schedule = {}
        self.feedback = {}

    def add_module(self, module_name, description, duration_hours):
        """
        Add a training module to the program.
        :param module_name: Name of the module
        :param description: Description of the module
        :param duration_hours: Duration of the module in hours
        """
        if duration_hours <= 0:
            raise TrainingProgramError("Module duration must be greater than 0 hours.")
        module = {
            "module_name": module_name,
            "description": description,
            "duration_hours": duration_hours
        }
        self.modules.append(module)

    def register_participant(self, name, email, organization):
        """
        Register a participant for the training program.
        :param name: Name of the participant
        :param email: Email of the participant
        :param organization: Organization of the participant
        """
        if not name or not email or not organization:
            raise TrainingProgramError("Participant details cannot be empty.")
        participant = {
            "name": name,
            "email": email,
            "organization": organization
        }
        self.participants.append(participant)

    def generate_schedule(self, start_date):
        """
        Generate a training schedule based on the modules and start date.
        :param start_date: Start date of the training program (YYYY-MM-DD)
        """
        try:
            current_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            raise TrainingProgramError("Invalid date format. Use YYYY-MM-DD.")

        for module in self.modules:
            self.schedule[module["module_name"]] = {
                "date": current_date.strftime("%Y-%m-%d"),
                "duration_hours": module["duration_hours"]
            }
            current_date += datetime.timedelta(days=1)  # Increment date for next module

    def collect_feedback(self, participant_email, module_name, feedback_text):
        """
        Collect feedback from participants for a specific module.
        :param participant_email: Email of the participant providing feedback
        :param module_name: Name of the module for which feedback is provided
        :param feedback_text: Feedback text
        """
        if not participant_email or not module_name or not feedback_text:
            raise TrainingProgramError("Feedback details cannot be empty.")
        if module_name not in self.schedule:
            raise TrainingProgramError("Module not found in the schedule.")
        self.feedback.setdefault(module_name, []).append({
            "participant_email": participant_email,
            "feedback_text": feedback_text
        })

    def save_to_file(self, filename):
        """
        Save the training program details to a JSON file.
        :param filename: Name of the file to save the details
        """
        data = {
            "name": self.name,
            "target_audience": self.target_audience,
            "location": self.location,
            "modules": self.modules,
            "participants": self.participants,
            "schedule": self.schedule,
            "feedback": self.feedback
        }
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            raise TrainingProgramError(f"Error saving to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a training program
        program = TrainingProgram(
            name="PPP Transaction Advisory and Financial Modeling",
            target_audience="Professionals in Bangladesh's Infrastructure Sector",
            location="Dhaka, Bangladesh"
        )

        # Add modules
        program.add_module("Introduction to PPP", "Overview of Public-Private Partnerships", 3)
        program.add_module("Financial Modeling Basics", "Introduction to financial modeling techniques", 5)

        # Register participants
        program.register_participant("John Doe", "john.doe@example.com", "ABC Corp")
        program.register_participant("Jane Smith", "jane.smith@example.com", "XYZ Ltd")

        # Generate schedule
        program.generate_schedule("2023-11-01")

        # Collect feedback
        program.collect_feedback("john.doe@example.com", "Introduction to PPP", "Very informative session.")
        program.collect_feedback("jane.smith@example.com", "Financial Modeling Basics", "Excellent practical examples.")

        # Save program details to file
        program.save_to_file("training_program.json")

        print("Training program details saved successfully.")
    except TrainingProgramError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
