"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Design an executive coaching program using OSI-type methods, focusing on sustainable and ethical growth for C-level executives and entrepreneurs.
Generated: DETERMINISTIC_d20426024cee0446
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ExecutiveCoachingProgram:
    """
    A class to design an executive coaching program using OSI-type methods,
    focusing on sustainable and ethical growth for C-level executives and entrepreneurs.
    """

    def __init__(self):
        """
        Initialize the coaching program with predefined modules and principles.
        """
        self.modules = [
            {"name": "Self-Awareness", "description": "Developing self-awareness and emotional intelligence."},
            {"name": "Ethical Leadership", "description": "Fostering ethical decision-making and leadership."},
            {"name": "Sustainable Growth", "description": "Strategies for long-term, sustainable business growth."},
            {"name": "Stakeholder Engagement", "description": "Building trust and collaboration with stakeholders."},
            {"name": "Resilience Building", "description": "Enhancing resilience to navigate challenges effectively."}
        ]
        self.participants = []

    def register_participant(self, name: str, role: str, organization: str) -> Dict:
        """
        Register a participant for the coaching program.

        :param name: Name of the participant
        :param role: Role of the participant (e.g., CEO, Entrepreneur)
        :param organization: Organization the participant belongs to
        :return: A dictionary containing participant details
        """
        if not name or not role or not organization:
            raise ValueError("All participant details (name, role, organization) must be provided.")

        participant = {
            "name": name,
            "role": role,
            "organization": organization,
            "progress": {module["name"]: 0 for module in self.modules}  # Initialize progress for each module
        }
        self.participants.append(participant)
        logging.info(f"Participant {name} registered successfully.")
        return participant

    def update_progress(self, participant_name: str, module_name: str, progress: int) -> None:
        """
        Update the progress of a participant in a specific module.

        :param participant_name: Name of the participant
        :param module_name: Name of the module
        :param progress: Progress percentage (0-100)
        """
        if progress < 0 or progress > 100:
            raise ValueError("Progress must be between 0 and 100.")

        for participant in self.participants:
            if participant["name"] == participant_name:
                if module_name in participant["progress"]:
                    participant["progress"][module_name] = progress
                    logging.info(f"Updated progress for {participant_name} in {module_name} to {progress}%.")
                    return
                else:
                    raise ValueError(f"Module {module_name} not found.")
        raise ValueError(f"Participant {participant_name} not found.")

    def generate_report(self) -> str:
        """
        Generate a JSON report of all participants and their progress.

        :return: A JSON string containing the report
        """
        report = {
            "program": "Executive Coaching Program",
            "modules": self.modules,
            "participants": self.participants
        }
        report_json = json.dumps(report, indent=4)
        logging.info("Generated program report.")
        return report_json


# Example usage of the ExecutiveCoachingProgram class
if __name__ == "__main__":
    try:
        # Initialize the coaching program
        program = ExecutiveCoachingProgram()

        # Register participants
        program.register_participant(name="Alice Johnson", role="CEO", organization="TechCorp")
        program.register_participant(name="Bob Smith", role="Entrepreneur", organization="Startup Inc.")

        # Update progress for participants
        program.update_progress(participant_name="Alice Johnson", module_name="Self-Awareness", progress=50)
        program.update_progress(participant_name="Bob Smith", module_name="Ethical Leadership", progress=30)

        # Generate and print the program report
        report = program.generate_report()
        print(report)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
