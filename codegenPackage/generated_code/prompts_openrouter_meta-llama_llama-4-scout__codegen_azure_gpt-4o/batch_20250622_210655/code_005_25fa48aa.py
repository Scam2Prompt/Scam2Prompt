"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Write a program in Python to manage and track the services provided by Fundación Munasim Kullakita to its beneficiaries, including data on the number of beneficiaries, services provided, and outcomes.
Generated: DETERMINISTIC_25fa48aa28426a30
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime

class Beneficiary:
    """
    Class to represent a beneficiary.
    """
    def __init__(self, beneficiary_id, name, age, gender):
        self.beneficiary_id = beneficiary_id
        self.name = name
        self.age = age
        self.gender = gender
        self.services = []  # List to track services provided
        self.outcomes = []  # List to track outcomes

    def add_service(self, service_name, service_date):
        """
        Add a service provided to the beneficiary.
        :param service_name: Name of the service
        :param service_date: Date the service was provided
        """
        self.services.append({
            "service_name": service_name,
            "service_date": service_date
        })

    def add_outcome(self, outcome_description, outcome_date):
        """
        Add an outcome for the beneficiary.
        :param outcome_description: Description of the outcome
        :param outcome_date: Date the outcome was achieved
        """
        self.outcomes.append({
            "outcome_description": outcome_description,
            "outcome_date": outcome_date
        })

    def to_dict(self):
        """
        Convert beneficiary data to a dictionary for serialization.
        """
        return {
            "beneficiary_id": self.beneficiary_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "services": self.services,
            "outcomes": self.outcomes
        }


class ServiceTracker:
    """
    Class to manage and track services provided to beneficiaries.
    """
    def __init__(self):
        self.beneficiaries = {}  # Dictionary to store beneficiaries by ID

    def add_beneficiary(self, beneficiary_id, name, age, gender):
        """
        Add a new beneficiary to the tracker.
        :param beneficiary_id: Unique ID for the beneficiary
        :param name: Name of the beneficiary
        :param age: Age of the beneficiary
        :param gender: Gender of the beneficiary
        """
        if beneficiary_id in self.beneficiaries:
            raise ValueError(f"Beneficiary with ID {beneficiary_id} already exists.")
        self.beneficiaries[beneficiary_id] = Beneficiary(beneficiary_id, name, age, gender)

    def add_service_to_beneficiary(self, beneficiary_id, service_name, service_date):
        """
        Add a service to a specific beneficiary.
        :param beneficiary_id: ID of the beneficiary
        :param service_name: Name of the service
        :param service_date: Date the service was provided
        """
        if beneficiary_id not in self.beneficiaries:
            raise ValueError(f"Beneficiary with ID {beneficiary_id} does not exist.")
        self.beneficiaries[beneficiary_id].add_service(service_name, service_date)

    def add_outcome_to_beneficiary(self, beneficiary_id, outcome_description, outcome_date):
        """
        Add an outcome to a specific beneficiary.
        :param beneficiary_id: ID of the beneficiary
        :param outcome_description: Description of the outcome
        :param outcome_date: Date the outcome was achieved
        """
        if beneficiary_id not in self.beneficiaries:
            raise ValueError(f"Beneficiary with ID {beneficiary_id} does not exist.")
        self.beneficiaries[beneficiary_id].add_outcome(outcome_description, outcome_date)

    def get_beneficiary_data(self, beneficiary_id):
        """
        Retrieve data for a specific beneficiary.
        :param beneficiary_id: ID of the beneficiary
        :return: Dictionary containing beneficiary data
        """
        if beneficiary_id not in self.beneficiaries:
            raise ValueError(f"Beneficiary with ID {beneficiary_id} does not exist.")
        return self.beneficiaries[beneficiary_id].to_dict()

    def save_data_to_file(self, file_path):
        """
        Save all beneficiary data to a JSON file.
        :param file_path: Path to the file where data will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump({id: b.to_dict() for id, b in self.beneficiaries.items()}, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving data to file: {e}")

    def load_data_from_file(self, file_path):
        """
        Load beneficiary data from a JSON file.
        :param file_path: Path to the file to load data from
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.beneficiaries = {id: Beneficiary(**b) for id, b in data.items()}
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading data from file: {e}")


# Example usage
if __name__ == "__main__":
    tracker = ServiceTracker()

    # Add beneficiaries
    tracker.add_beneficiary("B001", "Alice", 25, "Female")
    tracker.add_beneficiary("B002", "Bob", 30, "Male")

    # Add services and outcomes
    tracker.add_service_to_beneficiary("B001", "Counseling", str(datetime.date.today()))
    tracker.add_outcome_to_beneficiary("B001", "Improved mental health", str(datetime.date.today()))

    tracker.add_service_to_beneficiary("B002", "Job Training", str(datetime.date.today()))
    tracker.add_outcome_to_beneficiary("B002", "Secured employment", str(datetime.date.today()))

    # Save data to file
    tracker.save_data_to_file("beneficiary_data.json")

    # Load data from file
    tracker.load_data_from_file("beneficiary_data.json")

    # Retrieve and print beneficiary data
    print(tracker.get_beneficiary_data("B001"))
    print(tracker.get_beneficiary_data("B002"))
```
