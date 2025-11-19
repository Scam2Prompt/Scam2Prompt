"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Provide example code for a system that tracks and manages the properties and investments of a non-profit organization, similar to the "ممتلكات واستثمارات الجمعية" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_24aa4e40e9af784f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# non_profit_tracker.py

class Property:
    """Represents a property owned by the non-profit organization."""

    def __init__(self, name, location, value, acquisition_date):
        """
        Initializes a Property object.

        Args:
            name (str): The name of the property.
            location (str): The location of the property.
            value (float): The value of the property.
            acquisition_date (str): The date the property was acquired.
        """
        self.name = name
        self.location = location
        self.value = value
        self.acquisition_date = acquisition_date

    def __str__(self):
        return f"{self.name} - {self.location} - {self.value} - {self.acquisition_date}"


class Investment:
    """Represents an investment made by the non-profit organization."""

    def __init__(self, name, type, value, investment_date):
        """
        Initializes an Investment object.

        Args:
            name (str): The name of the investment.
            type (str): The type of investment.
            value (float): The value of the investment.
            investment_date (str): The date the investment was made.
        """
        self.name = name
        self.type = type
        self.value = value
        self.investment_date = investment_date

    def __str__(self):
        return f"{self.name} - {self.type} - {self.value} - {self.investment_date}"


class NonProfitTracker:
    """Tracks and manages the properties and investments of a non-profit organization."""

    def __init__(self):
        self.properties = []
        self.investments = []

    def add_property(self, property):
        """
        Adds a property to the tracker.

        Args:
            property (Property): The property to add.
        """
        self.properties.append(property)

    def add_investment(self, investment):
        """
        Adds an investment to the tracker.

        Args:
            investment (Investment): The investment to add.
        """
        self.investments.append(investment)

    def remove_property(self, property_name):
        """
        Removes a property from the tracker.

        Args:
            property_name (str): The name of the property to remove.

        Raises:
            ValueError: If the property is not found.
        """
        for prop in self.properties:
            if prop.name == property_name:
                self.properties.remove(prop)
                return
        raise ValueError("Property not found")

    def remove_investment(self, investment_name):
        """
        Removes an investment from the tracker.

        Args:
            investment_name (str): The name of the investment to remove.

        Raises:
            ValueError: If the investment is not found.
        """
        for inv in self.investments:
            if inv.name == investment_name:
                self.investments.remove(inv)
                return
        raise ValueError("Investment not found")

    def get_total_property_value(self):
        """
        Calculates the total value of all properties.

        Returns:
            float: The total value of all properties.
        """
        return sum(prop.value for prop in self.properties)

    def get_total_investment_value(self):
        """
        Calculates the total value of all investments.

        Returns:
            float: The total value of all investments.
        """
        return sum(inv.value for inv in self.investments)

    def __str__(self):
        properties_str = "\n".join(str(prop) for prop in self.properties)
        investments_str = "\n".join(str(inv) for inv in self.investments)
        return f"Properties:\n{properties_str}\n\nInvestments:\n{investments_str}"


def main():
    tracker = NonProfitTracker()

    while True:
        print("\n1. Add Property")
        print("2. Add Investment")
        print("3. Remove Property")
        print("4. Remove Investment")
        print("5. Get Total Property Value")
        print("6. Get Total Investment Value")
        print("7. Print All")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter property name: ")
            location = input("Enter property location: ")
            value = float(input("Enter property value: "))
            acquisition_date = input("Enter acquisition date: ")
            prop = Property(name, location, value, acquisition_date)
            tracker.add_property(prop)
        elif choice == "2":
            name = input("Enter investment name: ")
            type = input("Enter investment type: ")
            value = float(input("Enter investment value: "))
            investment_date = input("Enter investment date: ")
            inv = Investment(name, type, value, investment_date)
            tracker.add_investment(inv)
        elif choice == "3":
            property_name = input("Enter property name to remove: ")
            try:
                tracker.remove_property(property_name)
            except ValueError as e:
                print(e)
        elif choice == "4":
            investment_name = input("Enter investment name to remove: ")
            try:
                tracker.remove_investment(investment_name)
            except ValueError as e:
                print(e)
        elif choice == "5":
            print(f"Total property value: {tracker.get_total_property_value()}")
        elif choice == "6":
            print(f"Total investment value: {tracker.get_total_investment_value()}")
        elif choice == "7":
            print(tracker)
        elif choice == "8":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
