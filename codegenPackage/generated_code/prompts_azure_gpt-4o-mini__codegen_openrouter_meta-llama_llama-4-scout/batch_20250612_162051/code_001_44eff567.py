"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Write a Python script to automate the tracking of legal cases, inspired by the client-focused approach of the Complexo de Advocacia Dr. Adriano Geoffrey.
Generated: DETERMINISTIC_44eff5679ae3feae
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# legal_case_tracker.py

import datetime
import json
import os

class LegalCase:
    """Represents a legal case with its attributes and methods."""

    def __init__(self, case_id, client_name, case_type, status="Open"):
        """
        Initializes a LegalCase object.

        Args:
            case_id (str): Unique identifier for the case.
            client_name (str): Name of the client.
            case_type (str): Type of the legal case.
            status (str, optional): Status of the case. Defaults to "Open".
        """
        self.case_id = case_id
        self.client_name = client_name
        self.case_type = case_type
        self.status = status
        self.history = []

    def update_status(self, new_status):
        """
        Updates the status of the case.

        Args:
            new_status (str): New status of the case.

        Raises:
            ValueError: If the new status is not a string.
        """
        if not isinstance(new_status, str):
            raise ValueError("Status must be a string")
        self.history.append((datetime.datetime.now(), self.status))
        self.status = new_status

    def add_note(self, note):
        """
        Adds a note to the case history.

        Args:
            note (str): Note to be added.

        Raises:
            ValueError: If the note is not a string.
        """
        if not isinstance(note, str):
            raise ValueError("Note must be a string")
        self.history.append((datetime.datetime.now(), f"Note: {note}"))

    def to_dict(self):
        """Returns a dictionary representation of the case."""
        return {
            "case_id": self.case_id,
            "client_name": self.client_name,
            "case_type": self.case_type,
            "status": self.status,
            "history": self.history,
        }


class LegalCaseTracker:
    """Manages a collection of legal cases."""

    def __init__(self, data_file="legal_cases.json"):
        """
        Initializes a LegalCaseTracker object.

        Args:
            data_file (str, optional): File to store the cases. Defaults to "legal_cases.json".
        """
        self.data_file = data_file
        self.cases = self.load_cases()

    def load_cases(self):
        """
        Loads cases from the data file.

        Returns:
            dict: Dictionary of cases where the key is the case ID and the value is the LegalCase object.
        """
        if not os.path.exists(self.data_file):
            return {}

        with open(self.data_file, "r") as file:
            data = json.load(file)

        cases = {}
        for case_id, case_data in data.items():
            case = LegalCase(
                case_id,
                case_data["client_name"],
                case_data["case_type"],
                case_data["status"],
            )
            case.history = case_data["history"]
            cases[case_id] = case

        return cases

    def save_cases(self):
        """Saves the cases to the data file."""
        data = {}
        for case_id, case in self.cases.items():
            data[case_id] = case.to_dict()

        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def add_case(self, case):
        """
        Adds a new case.

        Args:
            case (LegalCase): Case to be added.

        Raises:
            ValueError: If a case with the same ID already exists.
        """
        if case.case_id in self.cases:
            raise ValueError("Case with the same ID already exists")

        self.cases[case.case_id] = case
        self.save_cases()

    def get_case(self, case_id):
        """
        Retrieves a case by its ID.

        Args:
            case_id (str): ID of the case.

        Returns:
            LegalCase: The case object if found, otherwise None.
        """
        return self.cases.get(case_id)

    def update_case(self, case_id, new_case):
        """
        Updates an existing case.

        Args:
            case_id (str): ID of the case.
            new_case (LegalCase): New case object.

        Raises:
            ValueError: If the case ID does not exist.
        """
        if case_id not in self.cases:
            raise ValueError("Case ID does not exist")

        self.cases[case_id] = new_case
        self.save_cases()


def main():
    tracker = LegalCaseTracker()

    while True:
        print("\n1. Add a new case")
        print("2. Get a case")
        print("3. Update a case")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            case_id = input("Enter case ID: ")
            client_name = input("Enter client name: ")
            case_type = input("Enter case type: ")

            case = LegalCase(case_id, client_name, case_type)
            tracker.add_case(case)
            print("Case added successfully!")

        elif choice == "2":
            case_id = input("Enter case ID: ")
            case = tracker.get_case(case_id)

            if case:
                print(f"Case ID: {case.case_id}")
                print(f"Client Name: {case.client_name}")
                print(f"Case Type: {case.case_type}")
                print(f"Status: {case.status}")
                print("History:")
                for timestamp, event in case.history:
                    print(f"{timestamp}: {event}")
            else:
                print("Case not found!")

        elif choice == "3":
            case_id = input("Enter case ID: ")
            case = tracker.get_case(case_id)

            if case:
                new_status = input("Enter new status: ")
                case.update_status(new_status)

                note = input("Enter a note (optional): ")
                if note:
                    case.add_note(note)

                tracker.update_case(case_id, case)
                print("Case updated successfully!")
            else:
                print("Case not found!")

        elif choice == "4":
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
