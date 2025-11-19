"""
Generated Code Metadata:
========================
Original URL: https://starmissteenindia.com
Prompt: Generate a script that automates the collection of participant data for a modeling event, ensuring compliance with terms and conditions similar to those of Star Miss Teen India 2025.
Generated: DETERMINISTIC_0e4662f32c8533cc
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# participant_data_collector.py

import os
import csv
from datetime import datetime
from typing import Dict

# Define constants for event and data collection
EVENT_NAME = "Star Miss Teen India 2025"
DATA_COLLECTION_FILE = "participant_data.csv"
TERMS_AND_CONDITIONS_FILE = "terms_and_conditions.txt"

def collect_participant_data() -> None:
    """
    Collects participant data for the modeling event and saves it to a CSV file.
    """
    participant_data = []

    while True:
        print("\n1. Add Participant")
        print("2. Stop Collection")
        choice = input("Choose an option: ")

        if choice == "1":
            participant_info = collect_participant_info()
            participant_data.append(participant_info)
        elif choice == "2":
            break
        else:
            print("Invalid option. Please choose again.")

    save_participant_data(participant_data)

def collect_participant_info() -> Dict:
    """
    Collects information for a single participant.
    """
    print("\nEnter participant's information:")

    name = input("Name: ")
    age = input("Age: ")
    contact_number = input("Contact Number: ")
    email = input("Email: ")
    height = input("Height (in cm): ")
    weight = input("Weight (in kg): ")
    has_agreed_to_terms = get_terms_agreement()

    participant_info = {
        "name": name,
        "age": age,
        "contact_number": contact_number,
        "email": email,
        "height": height,
        "weight": weight,
        "has_agreed_to_terms": has_agreed_to_terms
    }

    return participant_info

def get_terms_agreement() -> bool:
    """
    Displays terms and conditions and gets participant's agreement.
    """
    try:
        with open(TERMS_AND_CONDITIONS_FILE, 'r') as file:
            terms_and_conditions = file.read()
            print("\nTerms and Conditions:")
            print(terms_and_conditions)

        agreement = input("\nDo you agree to the terms and conditions? (yes/no): ")
        return agreement.lower() == "yes"
    except FileNotFoundError:
        print(f"Error: {TERMS_AND_CONDITIONS_FILE} not found.")
        return False

def save_participant_data(participant_data: list) -> None:
    """
    Saves participant data to a CSV file.
    """
    fieldnames = ["name", "age", "contact_number", "email", "height", "weight", "has_agreed_to_terms"]

    try:
        with open(DATA_COLLECTION_FILE, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for participant in participant_data:
                writer.writerow(participant)

        print(f"\nParticipant data saved to {DATA_COLLECTION_FILE} successfully.")
    except Exception as e:
        print(f"Error saving participant data: {e}")

if __name__ == "__main__":
    collect_participant_data()
```
