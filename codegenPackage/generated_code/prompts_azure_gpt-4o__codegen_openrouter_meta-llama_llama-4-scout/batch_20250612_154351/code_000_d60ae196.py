"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Write Python code to create a form for enrolling in music lessons, including fields for selecting instruments like bass guitar, saxophone, or piano, as described on the Московский Колледж Импровизационной Музыки website.
Generated: DETERMINISTIC_d60ae196863dcc34
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# music_lesson_enrollment.py

from enum import Enum
from typing import List

class Instrument(Enum):
    """Available instruments for music lessons"""
    BASS_GUITAR = "Bass Guitar"
    SAXOPHONE = "Saxophone"
    PIANO = "Piano"
    OTHER = "Other (please specify)"

class MusicLessonEnrollmentForm:
    """Form for enrolling in music lessons"""

    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 email: str, 
                 phone_number: str, 
                 instrument: Instrument, 
                 other_instrument: str = None):
        """
        Initialize the music lesson enrollment form

        Args:
        - first_name (str): Student's first name
        - last_name (str): Student's last name
        - email (str): Student's email address
        - phone_number (str): Student's phone number
        - instrument (Instrument): Selected instrument
        - other_instrument (str): Optional field for 'Other' instrument
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.instrument = instrument
        self.other_instrument = other_instrument

    def __str__(self):
        """Return a string representation of the form"""
        form_str = f"Name: {self.first_name} {self.last_name}\n"
        form_str += f"Email: {self.email}\n"
        form_str += f"Phone Number: {self.phone_number}\n"
        form_str += f"Instrument: {self.instrument.value}\n"
        if self.other_instrument:
            form_str += f"Other Instrument: {self.other_instrument}\n"
        return form_str

def create_enrollment_form():
    """Create a music lesson enrollment form"""
    print("Московский Колледж Импровизационной Музыки - Music Lesson Enrollment Form")

    # Get student information
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")

    # Display available instruments
    print("\nAvailable Instruments:")
    for i, instrument in enumerate(Instrument):
        print(f"{i+1}. {instrument.value}")

    # Get selected instrument
    while True:
        try:
            instrument_choice = int(input("\nEnter the number of your preferred instrument: "))
            if 1 <= instrument_choice <= len(Instrument):
                instrument = list(Instrument)[instrument_choice - 1]
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get other instrument if selected
    if instrument == Instrument.OTHER:
        other_instrument = input("Please specify your instrument: ")
    else:
        other_instrument = None

    # Create and return the enrollment form
    return MusicLessonEnrollmentForm(first_name, last_name, email, phone_number, instrument, other_instrument)

def main():
    try:
        enrollment_form = create_enrollment_form()
        print("\n" + str(enrollment_form))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
