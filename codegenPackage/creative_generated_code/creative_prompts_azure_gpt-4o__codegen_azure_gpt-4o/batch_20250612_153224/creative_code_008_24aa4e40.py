"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Provide example code for a system that tracks and manages the properties and investments of a non-profit organization, similar to the "ممتلكات واستثمارات الجمعية" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_24aa4e40e9af784f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: non_profit_property_manager.py
# Purpose: A system to track and manage the properties and investments of a non-profit organization.

import json
from datetime import datetime


class Property:
    """
    Represents a property owned by the non-profit organization.
    """

    def __init__(self, property_id, name, location, value, acquired_date):
        """
        Initialize a Property object.

        :param property_id: Unique identifier for the property
        :param name: Name of the property
        :param location: Location of the property
        :param value: Monetary value of the property
        :param acquired_date: Date the property was acquired
        """
        self.property_id = property_id
        self.name = name
        self.location = location
        self.value = value
        self.acquired_date = acquired_date

    def to_dict(self):
        """
        Convert the property object to a dictionary.

        :return: Dictionary representation of the property
        """
        return {
            "property_id": self.property_id,
            "name": self.name,
            "location": self.location,
            "value": self.value,
            "acquired_date": self.acquired_date.strftime("%Y-%m-%d"),
        }


class Investment:
    """
    Represents an investment made by the non-profit organization.
    """

    def __init__(self, investment_id, name, amount, return_rate, start_date):
        """
        Initialize an Investment object.

        :param investment_id: Unique identifier for the investment
        :param name: Name of the investment
        :param amount: Monetary amount of the investment
        :param return_rate: Percentage return rate of the investment
        :param start_date: Date the investment started
        """
        self.investment_id = investment_id
        self.name = name
        self.amount = amount
        self.return_rate = return_rate
        self.start_date = start_date

    def to_dict(self):
        """
        Convert the investment object to a dictionary.

        :return: Dictionary representation of the investment
        """
        return {
            "investment_id": self.investment_id,
            "name": self.name,
            "amount": self.amount,
            "return_rate": self.return_rate,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
        }


class NonProfitManager:
    """
    Manages properties and investments for a non-profit organization.
    """

    def __init__(self, data_file="non_profit_data.json"):
        """
        Initialize the manager with an optional data file.

        :param data_file: Path to the JSON file to persist data
        """
        self.properties = []
        self.investments = []
        self.data_file = data_file
        self.load_data()

    def add_property(self, property_obj):
        """
        Add a new property to the system.

        :param property_obj: Property object to add
        """
        self.properties.append(property_obj)
        self.save_data()

    def add_investment(self, investment_obj):
        """
        Add a new investment to the system.

        :param investment_obj: Investment object to add
        """
        self.investments.append(investment_obj)
        self.save_data()

    def get_properties(self):
        """
        Retrieve all properties.

        :return: List of property objects
        """
        return self.properties

    def get_investments(self):
        """
        Retrieve all investments.

        :return: List of investment objects
        """
        return self.investments

    def save_data(self):
        """
        Persist all properties and investments to the data file.
        """
        try:
            data = {
                "properties": [prop.to_dict() for prop in self.properties],
                "investments": [inv.to_dict() for inv in self.investments],
            }
            with open(self.data_file, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        """
        Load properties and investments from the data file.
        """
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                self.properties = [
                    Property(
                        prop["property_id"],
                        prop["name"],
                        prop["location"],
                        prop["value"],
                        datetime.strptime(prop["acquired_date"], "%Y-%m-%d"),
                    )
                    for prop in data.get("properties", [])
                ]
                self.investments = [
                    Investment(
                        inv["investment_id"],
                        inv["name"],
                        inv["amount"],
                        inv["return_rate"],
                        datetime.strptime(inv["start_date"], "%Y-%m-%d"),
                    )
                    for inv in data.get("investments", [])
                ]
        except FileNotFoundError:
            # No data file exists yet, initialize with empty data.
            self.properties = []
            self.investments = []
        except Exception as e:
            print(f"Error loading data: {e}")

# Example usage:
if __name__ == "__main__":
    manager = NonProfitManager()

    # Adding a property
    new_property = Property(
        property_id=1,
        name="Community Center",
        location="123 Main St",
        value=500000,
        acquired_date=datetime(2020, 5, 1),
    )
    manager.add_property(new_property)

    # Adding an investment
    new_investment = Investment(
        investment_id=101,
        name="Green Energy Project",
        amount=20000,
        return_rate=5.5,
        start_date=datetime(2021, 8, 15),
    )
    manager.add_investment(new_investment)

    # Retrieve and display stored data
    print("Properties:")
    for prop in manager.get_properties():
        print(prop.to_dict())

    print("\nInvestments:")
    for inv in manager.get_investments():
        print(inv.to_dict())
```
