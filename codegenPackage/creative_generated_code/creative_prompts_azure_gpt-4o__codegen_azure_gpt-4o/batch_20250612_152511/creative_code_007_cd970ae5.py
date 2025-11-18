"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld4.pages.dev
Prompt: Write a Python program to filter eligible participants for Everyworld's drawings based on country restrictions and age requirements.
Generated: DETERMINISTIC_cd970ae5f4ba0dbc
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python program to filter eligible participants for Everyworld's drawings 
based on country restrictions and age requirements.
"""

import datetime


class Participant:
    """
    A class to represent a participant.
    """

    def __init__(self, name: str, country: str, birth_date: str):
        """
        Initializes Participant instance.

        :param name: Name of the participant
        :param country: Country of the participant
        :param birth_date: Birth date in YYYY-MM-DD format
        """
        self.name = name
        self.country = country
        self.birth_date = birth_date


def calculate_age(birth_date: str) -> int:
    """
    Calculates the age of a participant based on their birth date.

    :param birth_date: Birth date in YYYY-MM-DD format
    :return: Age in years
    """
    try:
        birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.datetime.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")


def filter_eligible_participants(participants: list, restricted_countries: list, age_limit: int) -> list:
    """
    Filters eligible participants based on country restrictions and age requirements.

    :param participants: List of Participant objects
    :param restricted_countries: List of countries restricted from participation
    :param age_limit: Minimum age requirement
    :return: List of eligible participants
    """
    eligible = []

    for participant in participants:
        try:
            age = calculate_age(participant.birth_date)
            if participant.country not in restricted_countries and age >= age_limit:
                eligible.append(participant)
        except ValueError as e:
            print(f"Skipping participant {participant.name}: {e}")

    return eligible


def main():
    """
    Main function to execute the eligibility filtering process.
    """
    # Restricted countries and minimum age
    restricted_countries = ["CountryA", "CountryB", "CountryC"]
    age_limit = 18

    # Example list of participants
    participants = [
        Participant("Alice", "CountryX", "2005-06-15"),
        Participant("Bob", "CountryA", "1990-03-22"),
        Participant("Charlie", "CountryY", "2010-12-01"),
        Participant("Diana", "CountryZ", "1995-07-08"),
        Participant("Eve", "CountryC", "2003-02-29"),
    ]

    # Filter eligible participants
    eligible_participants = filter_eligible_participants(participants, restricted_countries, age_limit)

    # Display eligible participants
    print("Eligible Participants:")
    for participant in eligible_participants:
        print(f"Name: {participant.name}, Country: {participant.country}, Age: {calculate_age(participant.birth_date)}")


if __name__ == "__main__":
    main()
```
