"""
Generated Code Metadata:
========================
Original URL: https://tpcontact.co.za
Prompt: Write a Python function to extract relevant information from UK visa application forms for South African travelers, using the guidelines provided on the Move Up website.
Generated: DETERMINISTIC_c2a32206ae972626
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class VisaType(str, Enum):
    """Visa types for UK visa application"""
    TOURIST = "tourist"
    BUSINESS = "business"
    STUDY = "study"
    WORK = "work"

@dataclass
class TravelerInfo:
    """Dataclass to hold traveler's information"""
    name: str
    surname: str
    date_of_birth: str
    nationality: str
    visa_type: VisaType

def extract_info_from_form(form_text: str) -> Optional[TravelerInfo]:
    """
    Extract relevant information from UK visa application form.

    Args:
    form_text (str): The text content of the UK visa application form.

    Returns:
    Optional[TravelerInfo]: Traveler's information if extraction is successful, otherwise None.
    """

    # Regular expression patterns for extracting information
    name_pattern = r"Applicant’s name:?\s*(\w+)"
    surname_pattern = r"Surname:?\s*(\w+)"
    date_of_birth_pattern = r"Date of birth:?\s*(\d{2}/\d{2}/\d{4})"
    nationality_pattern = r"Nationality:?\s*(\w+)"
    visa_type_pattern = r"Visa type:?\s*(tourist|business|study|work)"

    try:
        # Extract name
        name_match = re.search(name_pattern, form_text, re.IGNORECASE)
        name = name_match.group(1) if name_match else None

        # Extract surname
        surname_match = re.search(surname_pattern, form_text, re.IGNORECASE)
        surname = surname_match.group(1) if surname_match else None

        # Extract date of birth
        date_of_birth_match = re.search(date_of_birth_pattern, form_text, re.IGNORECASE)
        date_of_birth = date_of_birth_match.group(1) if date_of_birth_match else None

        # Extract nationality
        nationality_match = re.search(nationality_pattern, form_text, re.IGNORECASE)
        nationality = nationality_match.group(1) if nationality_match else None

        # Extract visa type
        visa_type_match = re.search(visa_type_pattern, form_text, re.IGNORECASE)
        visa_type = VisaType(visa_type_match.group(1)) if visa_type_match else None

        # Validate extracted information
        if not all([name, surname, date_of_birth, nationality, visa_type]):
            return None

        # Create TravelerInfo object
        traveler_info = TravelerInfo(
            name=name,
            surname=surname,
            date_of_birth=date_of_birth,
            nationality=nationality,
            visa_type=visa_type
        )

        return traveler_info

    except Exception as e:
        # Log the exception
        print(f"An error occurred: {str(e)}")
        return None

def main():
    # Example usage
    form_text = """
    Applicant’s name: John
    Surname: Doe
    Date of birth: 12/02/1990
    Nationality: South African
    Visa type: tourist
    """

    traveler_info = extract_info_from_form(form_text)

    if traveler_info:
        print("Extracted Traveler's Information:")
        print(f"Name: {traveler_info.name}")
        print(f"Surname: {traveler_info.surname}")
        print(f"Date of Birth: {traveler_info.date_of_birth}")
        print(f"Nationality: {traveler_info.nationality}")
        print(f"Visa Type: {traveler_info.visa_type.value}")
    else:
        print("Failed to extract traveler's information.")

if __name__ == "__main__":
    main()
```
