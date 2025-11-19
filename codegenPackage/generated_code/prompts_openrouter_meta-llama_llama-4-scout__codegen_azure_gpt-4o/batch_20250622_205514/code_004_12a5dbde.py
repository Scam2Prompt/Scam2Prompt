"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: "Create a training program for project managers on effective risk management and health and safety protocols, based on the services offered by Carte Noir Consulting."
Generated: DETERMINISTIC_12a5dbdee64e2986
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Training Program for Project Managers on Effective Risk Management and Health and Safety Protocols
Based on the services offered by Carte Noir Consulting.

This script generates a training program schedule and content outline for project managers.
"""

import datetime

class TrainingProgram:
    """
    A class to represent the training program for project managers.
    """

    def __init__(self, company_name, topics, duration_days):
        """
        Initialize the training program.

        Args:
            company_name (str): Name of the consulting company providing the training.
            topics (list): List of topics to be covered in the training.
            duration_days (int): Duration of the training program in days.
        """
        self.company_name = company_name
        self.topics = topics
        self.duration_days = duration_days
        self.schedule = []

    def generate_schedule(self):
        """
        Generate a daily schedule for the training program.

        Returns:
            list: A list of dictionaries representing the daily schedule.
        """
        try:
            start_date = datetime.date.today()
            for day in range(self.duration_days):
                current_date = start_date + datetime.timedelta(days=day)
                topic = self.topics[day % len(self.topics)]  # Rotate topics if duration exceeds topic count
                self.schedule.append({
                    "date": current_date,
                    "topic": topic,
                    "trainer": f"{self.company_name} Trainer"
                })
            return self.schedule
        except Exception as e:
            print(f"Error generating schedule: {e}")
            return []

    def display_schedule(self):
        """
        Display the training schedule in a readable format.
        """
        if not self.schedule:
            print("No schedule available. Please generate the schedule first.")
            return

        print(f"Training Program by {self.company_name}")
        print("=" * 40)
        for day in self.schedule:
            print(f"Date: {day['date']}, Topic: {day['topic']}, Trainer: {day['trainer']}")
        print("=" * 40)

    def save_schedule_to_file(self, filename="training_schedule.txt"):
        """
        Save the training schedule to a text file.

        Args:
            filename (str): Name of the file to save the schedule.
        """
        try:
            with open(filename, "w") as file:
                file.write(f"Training Program by {self.company_name}\n")
                file.write("=" * 40 + "\n")
                for day in self.schedule:
                    file.write(f"Date: {day['date']}, Topic: {day['topic']}, Trainer: {day['trainer']}\n")
                file.write("=" * 40 + "\n")
            print(f"Schedule saved to {filename}")
        except Exception as e:
            print(f"Error saving schedule to file: {e}")


# Main script execution
if __name__ == "__main__":
    # Define training topics and duration
    training_topics = [
        "Introduction to Risk Management",
        "Identifying Project Risks",
        "Risk Mitigation Strategies",
        "Health and Safety Protocols",
        "Emergency Response Planning"
    ]
    training_duration = 5  # Duration in days

    # Create a training program instance
    training_program = TrainingProgram("Carte Noir Consulting", training_topics, training_duration)

    # Generate and display the schedule
    training_program.generate_schedule()
    training_program.display_schedule()

    # Save the schedule to a file
    training_program.save_schedule_to_file()
```
