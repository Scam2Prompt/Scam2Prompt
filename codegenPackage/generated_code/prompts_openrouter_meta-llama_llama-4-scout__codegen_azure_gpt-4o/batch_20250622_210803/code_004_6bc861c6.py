"""
Generated Code Metadata:
========================
Original URL: https://trystemedia.com
Prompt: Create a model management system using a programming language of your choice, handling tasks such as model casting, scheduling, and communication, inspired by Tryste Media's model management expertise.
Generated: DETERMINISTIC_6bc861c6e25db7b3
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# model_management_system.py

import datetime
import json

class Model:
    """
    Represents a model in the management system.
    """
    def __init__(self, model_id, name, age, email, phone):
        self.model_id = model_id
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def to_dict(self):
        """
        Converts the model object to a dictionary for serialization.
        """
        return {
            "model_id": self.model_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "phone": self.phone
        }


class Casting:
    """
    Represents a casting event in the management system.
    """
    def __init__(self, casting_id, title, date, location, models=None):
        self.casting_id = casting_id
        self.title = title
        self.date = date
        self.location = location
        self.models = models if models else []

    def add_model(self, model):
        """
        Adds a model to the casting event.
        """
        if model not in self.models:
            self.models.append(model)

    def to_dict(self):
        """
        Converts the casting object to a dictionary for serialization.
        """
        return {
            "casting_id": self.casting_id,
            "title": self.title,
            "date": self.date.strftime('%Y-%m-%d'),
            "location": self.location,
            "models": [model.to_dict() for model in self.models]
        }


class ModelManagementSystem:
    """
    Main system for managing models, castings, and communication.
    """
    def __init__(self):
        self.models = {}
        self.castings = {}

    def add_model(self, model_id, name, age, email, phone):
        """
        Adds a new model to the system.
        """
        if model_id in self.models:
            raise ValueError(f"Model with ID {model_id} already exists.")
        self.models[model_id] = Model(model_id, name, age, email, phone)

    def schedule_casting(self, casting_id, title, date, location):
        """
        Schedules a new casting event.
        """
        if casting_id in self.castings:
            raise ValueError(f"Casting with ID {casting_id} already exists.")
        try:
            casting_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        self.castings[casting_id] = Casting(casting_id, title, casting_date, location)

    def assign_model_to_casting(self, model_id, casting_id):
        """
        Assigns a model to a casting event.
        """
        if model_id not in self.models:
            raise ValueError(f"Model with ID {model_id} does not exist.")
        if casting_id not in self.castings:
            raise ValueError(f"Casting with ID {casting_id} does not exist.")
        model = self.models[model_id]
        casting = self.castings[casting_id]
        casting.add_model(model)

    def get_casting_details(self, casting_id):
        """
        Retrieves details of a casting event.
        """
        if casting_id not in self.castings:
            raise ValueError(f"Casting with ID {casting_id} does not exist.")
        return self.castings[casting_id].to_dict()

    def get_model_details(self, model_id):
        """
        Retrieves details of a model.
        """
        if model_id not in self.models:
            raise ValueError(f"Model with ID {model_id} does not exist.")
        return self.models[model_id].to_dict()

    def save_to_file(self, filename):
        """
        Saves the system data to a JSON file.
        """
        data = {
            "models": {model_id: model.to_dict() for model_id, model in self.models.items()},
            "castings": {casting_id: casting.to_dict() for casting_id, casting in self.castings.items()}
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename):
        """
        Loads system data from a JSON file.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.models = {model_id: Model(**model_data) for model_id, model_data in data["models"].items()}
                self.castings = {
                    casting_id: Casting(
                        casting_id=casting_id,
                        title=casting_data["title"],
                        date=datetime.datetime.strptime(casting_data["date"], '%Y-%m-%d'),
                        location=casting_data["location"],
                        models=[Model(**model_data) for model_data in casting_data["models"]]
                    )
                    for casting_id, casting_data in data["castings"].items()
                }
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON file.")


# Example usage (uncomment to test):
# system = ModelManagementSystem()
# system.add_model("M001", "Alice Johnson", 25, "alice@example.com", "123-456-7890")
# system.schedule_casting("C001", "Fashion Show", "2023-12-01", "New York")
# system.assign_model_to_casting("M001", "C001")
# print(system.get_casting_details("C001"))
# system.save_to_file("system_data.json")
# system.load_from_file("system_data.json")
```
