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
import uuid
from datetime import datetime

class ExamTokenGenerator:
    """
    A class to generate unique exam tokens and assign them to specific dates and times.
    """

    def __init__(self):
        # Dictionary to store tokens with their assigned date and time
        self.tokens = {}

    def generate_token(self, subject: str, class_level: int) -> str:
        """
        Generate a unique token based on subject and class level.

        Args:
            subject (str): Subject abbreviation (e.g., "PPKN", "MTK").
            class_level (int): Class level (e.g., 10, 11, 12).

        Returns:
            str: A unique token string.
        """
        # Validate inputs
        if not subject.isalpha():
            raise ValueError("Subject abbreviation must contain only letters.")
        if not (isinstance(class_level, int) and (1 <= class_level <= 12)):
            raise ValueError("Class level must be an integer between 1 and 12.")
        
        # Generate token in the format "<SUBJECT><CLASS_LEVEL><UUID>"
        unique_id = str(uuid.uuid4())[:6].upper()  # Shortened UUID for uniqueness
        token = f"{subject.upper()}{class_level}{unique_id}"
        return token

    def assign_token(self, token: str, date: str, time: str) -> None:
        """
        Assign a token to a specific date and time.

        Args:
            token (str): The unique token to assign.
            date (str): The exam date in "YYYY-MM-DD" format.
            time (str): The exam time in "HH:MM" format.

        Raises:
            ValueError: If date or time format is invalid.
        """
        # Validate date format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")
        
        # Validate time format
        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            raise ValueError("Time must be in 'HH:MM' format.")
        
        # Assign token to date and time
        self.tokens[token] = {"date": date, "time": time}

    def get_assigned_tokens(self) -> dict:
        """
        Retrieve all assigned tokens with their dates and times.

        Returns:
            dict: A dictionary of tokens with their assigned date and time.
        """
        return self.tokens


# Example usage
if __name__ == "__main__":
    # Instantiate the generator
    generator = ExamTokenGenerator()

    try:
        # Generate tokens
        token1 = generator.generate_token("PPKN", 12)
        token2 = generator.generate_token("MTK", 10)

        print(f"Generated Tokens:\n1. {token1}\n2. {token2}")

        # Assign tokens to dates and times
        generator.assign_token(token1, "2023-12-01", "09:00")
        generator.assign_token(token2, "2023-12-01", "13:00")

        # Retrieve assigned tokens
        assigned_tokens = generator.get_assigned_tokens()
        print("\nAssigned Tokens:")
        for token, details in assigned_tokens.items():
            print(f"Token: {token}, Date: {details['date']}, Time: {details['time']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
