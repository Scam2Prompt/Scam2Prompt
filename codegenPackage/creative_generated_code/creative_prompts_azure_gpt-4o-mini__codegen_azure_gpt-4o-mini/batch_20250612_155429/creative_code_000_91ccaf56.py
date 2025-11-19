"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casaamalfitana.com
Prompt: Generate a code snippet for a restaurant reservation system that captures user details like name, email, date, and time for a dining experience similar to Casa Amalfitana.
Generated: DETERMINISTIC_91ccaf56ebdb5a21
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from datetime import datetime
import re

class Reservation:
    """Class to represent a restaurant reservation."""

    def __init__(self, name: str, email: str, date: str, time: str):
        """
        Initializes a new reservation instance.

        Args:
            name (str): The name of the person making the reservation.
            email (str): The email address of the person making the reservation.
            date (str): The date of the reservation in 'YYYY-MM-DD' format.
            time (str): The time of the reservation in 'HH:MM' format.

        Raises:
            ValueError: If the date or time format is invalid or if email is invalid.
        """
        self.name = name
        self.email = self.validate_email(email)
        self.date = self.validate_date(date)
        self.time = self.validate_time(time)

    def validate_email(self, email: str) -> str:
        """Validates the given email address format.

        Args:
            email (str): The email address to validate.

        Returns:
            str: The validated email address.

        Raises:
            ValueError: If the email format is invalid.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email address format.")
        return email

    def validate_date(self, date: str) -> datetime:
        """Validates the given date format and converts it to a datetime object.

        Args:
            date (str): The date to validate.

        Returns:
            datetime: The validated date as a datetime object.

        Raises:
            ValueError: If the date format is invalid.
        """
        try:
            return datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

    def validate_time(self, time: str) -> datetime:
        """Validates the given time format and converts it to a datetime object.

        Args:
            time (str): The time to validate.

        Returns:
            datetime: The validated time as a datetime object.

        Raises:
            ValueError: If the time format is invalid.
        """
        try:
            return datetime.strptime(time, '%H:%M')
        except ValueError:
            raise ValueError("Invalid time format. Use 'HH:MM'.")

    def __str__(self):
        """Returns a string representation of the reservation."""
        return f"Reservation for {self.name} on {self.date.date()} at {self.time.strftime('%H:%M')} (Email: {self.email})"


def main():
    """Main function to create a reservation."""
    try:
        # Sample user inputs
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        date = input("Enter reservation date (YYYY-MM-DD): ")
        time = input("Enter reservation time (HH:MM): ")
        
        # Create a reservation instance
        reservation = Reservation(name, email, date, time)
        
        # Print reservation confirmation
        print("Reservation confirmed:")
        print(reservation)
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
