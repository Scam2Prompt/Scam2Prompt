"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Create a code snippet that automates the enrollment process for a training program like those offered by SMART Training Resources.
Generated: DETERMINISTIC_51e1d403625aee7f
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_program_enrollment.py

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TrainingProgram:
    def __init__(self, program_id, program_name, start_date, end_date):
        """
        Initialize a TrainingProgram object.

        Args:
            program_id (int): Unique identifier for the program.
            program_name (str): Name of the program.
            start_date (str): Start date of the program in YYYY-MM-DD format.
            end_date (str): End date of the program in YYYY-MM-DD format.
        """
        self.program_id = program_id
        self.program_name = program_name
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

class Participant:
    def __init__(self, participant_id, name, email):
        """
        Initialize a Participant object.

        Args:
            participant_id (int): Unique identifier for the participant.
            name (str): Name of the participant.
            email (str): Email address of the participant.
        """
        self.participant_id = participant_id
        self.name = name
        self.email = email

class Enrollment:
    def __init__(self, program, participant, enrollment_date):
        """
        Initialize an Enrollment object.

        Args:
            program (TrainingProgram): Training program being enrolled in.
            participant (Participant): Participant being enrolled.
            enrollment_date (str): Date of enrollment in YYYY-MM-DD format.
        """
        self.program = program
        self.participant = participant
        self.enrollment_date = datetime.datetime.strptime(enrollment_date, '%Y-%m-%d').date()

def enroll_participant(program, participant):
    """
    Enroll a participant in a training program.

    Args:
        program (TrainingProgram): Training program to enroll in.
        participant (Participant): Participant to enroll.

    Returns:
        Enrollment: Enrollment object representing the new enrollment.

    Raises:
        ValueError: If the participant is already enrolled in the program.
    """
    try:
        # Check if participant is already enrolled
        existing_enrollment = get_enrollment(program.program_id, participant.participant_id)
        if existing_enrollment:
            raise ValueError("Participant is already enrolled in this program.")

        # Create a new enrollment
        enrollment_date = datetime.date.today().strftime('%Y-%m-%d')
        enrollment = Enrollment(program, participant, enrollment_date)

        # Save the enrollment (replace with actual database or storage code)
        # For demonstration purposes, we'll just log the enrollment
        logging.info(f"Enrolled participant {participant.name} in program {program.program_name} on {enrollment_date}")

        return enrollment

    except Exception as e:
        logging.error(f"Error enrolling participant: {str(e)}")
        raise

def get_enrollment(program_id, participant_id):
    """
    Retrieve an existing enrollment for a participant in a program.

    Args:
        program_id (int): ID of the program.
        participant_id (int): ID of the participant.

    Returns:
        Enrollment: Existing enrollment object, or None if not found.

    Raises:
        Exception: If an error occurs retrieving the enrollment.
    """
    try:
        # Replace with actual database or storage code to retrieve enrollment
        # For demonstration purposes, we'll just return None
        return None

    except Exception as e:
        logging.error(f"Error retrieving enrollment: {str(e)}")
        raise

def main():
    # Example usage:
    program = TrainingProgram(1, "SMART Training Resources Program", "2024-09-01", "2024-09-30")
    participant = Participant(1, "John Doe", "john.doe@example.com")

    try:
        enrollment = enroll_participant(program, participant)
        logging.info(f"Enrollment created: program={enrollment.program.program_name}, participant={enrollment.participant.name}, date={enrollment.enrollment_date}")
    except Exception as e:
        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
