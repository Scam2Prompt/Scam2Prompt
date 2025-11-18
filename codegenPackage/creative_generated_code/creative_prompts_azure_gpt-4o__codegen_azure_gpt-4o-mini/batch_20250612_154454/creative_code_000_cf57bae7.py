"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Write a Python script to generate unique exam tokens for different subjects and classes based on the format used by SMKN 1 Kadipaten (e.g., "PPKN12", "PSAJMTK"). Include functionality to assign tokens to specific dates and times.
Generated: DETERMINISTIC_cf57bae74c9753e7
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
from datetime import datetime, timedelta

class ExamTokenGenerator:
    def __init__(self):
        # Dictionary to store generated tokens with their corresponding date and time
        self.token_storage = {}

    def generate_token(self, subject_code: str, class_code: str) -> str:
        """
        Generate a unique exam token based on subject and class codes.
        
        Parameters:
            subject_code (str): The code representing the subject (e.g., "PPKN").
            class_code (str): The code representing the class (e.g., "12").
        
        Returns:
            str: A unique exam token.
        """
        # Create token format
        token = f"{subject_code}{class_code}"
        unique_token = self._make_unique_token(token)
        return unique_token

    def _make_unique_token(self, token: str) -> str:
        """
        Ensure that the generated token is unique by appending a random suffix.
        
        Parameters:
            token (str): The base token to be made unique.
        
        Returns:
            str: A unique token.
        """
        while True:
            # Generate a random 3-character suffix
            suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
            unique_token = f"{token}{suffix}"
            if unique_token not in self.token_storage:
                self.token_storage[unique_token] = None  # Register the token
                return unique_token

    def assign_token_to_date(self, token: str, date_time: datetime) -> None:
        """
        Assign a token to a specific date and time.
        
        Parameters:
            token (str): The exam token to assign.
            date_time (datetime): The date and time for the exam.
        
        Raises:
            ValueError: If the token is not found.
        """
        if token in self.token_storage:
            self.token_storage[token] = date_time
        else:
            raise ValueError(f"Token {token} not found. Cannot assign to date.")

    def get_exam_schedule(self):
        """
        Retrieve the schedule of all exam tokens and their assigned dates.
        
        Returns:
            dict: A dictionary of tokens and their assigned date and time.
        """
        return {token: date_time.strftime('%Y-%m-%d %H:%M') if date_time else None 
                for token, date_time in self.token_storage.items()}


def main():
    generator = ExamTokenGenerator()

    # Example of generating tokens for different subjects and classes
    subjects = ["PPKN", "PSA", "MTK"]
    classes = ["12", "11", "10"]

    # Generate tokens
    tokens = [generator.generate_token(subject, class_code) for subject in subjects for class_code in classes]

    # Output the generated tokens
    for token in tokens:
        print(f"Generated Token: {token}")

    # Example of assigning tokens to specific dates
    try:
        date_time = datetime.now() + timedelta(days=1)  # Assign token for tomorrow
        for token in tokens:
            generator.assign_token_to_date(token, date_time)
        
        # Retrieve and print the exam schedule
        exam_schedule = generator.get_exam_schedule()
        print("\nExam Schedule:")
        for token, date in exam_schedule.items():
            print(f"Token: {token}, Date & Time: {date}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
