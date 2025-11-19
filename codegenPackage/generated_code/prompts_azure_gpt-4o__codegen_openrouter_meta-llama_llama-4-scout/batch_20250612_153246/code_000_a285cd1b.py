"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Write Python code to automate the process of managing onboard provisioning for maritime operations, including tracking food supplies, electrical equipment, and personal protective equipment, as described on the Supply Marine website.
Generated: DETERMINISTIC_a285cd1b6415732a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# onboard_provisioning.py

class Supply:
    def __init__(self, name, quantity, unit):
        """
        Initialize a Supply object.

        Args:
            name (str): Name of the supply.
            quantity (int): Quantity of the supply.
            unit (str): Unit of measurement for the supply.
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"


class FoodSupply(Supply):
    def __init__(self, name, quantity, unit, expiration_date):
        """
        Initialize a FoodSupply object.

        Args:
            name (str): Name of the food supply.
            quantity (int): Quantity of the food supply.
            unit (str): Unit of measurement for the food supply.
            expiration_date (str): Expiration date of the food supply (YYYY-MM-DD).
        """
        super().__init__(name, quantity, unit)
        self.expiration_date = expiration_date

    def __str__(self):
        return f"{super().__str__()} (Expires: {self.expiration_date})"


class ElectricalEquipment(Supply):
    def __init__(self, name, quantity, unit, voltage, wattage):
        """
        Initialize an ElectricalEquipment object.

        Args:
            name (str): Name of the electrical equipment.
            quantity (int): Quantity of the electrical equipment.
            unit (str): Unit of measurement for the electrical equipment.
            voltage (int): Voltage rating of the equipment.
            wattage (int): Wattage rating of the equipment.
        """
        super().__init__(name, quantity, unit)
        self.voltage = voltage
        self.wattage = wattage

    def __str__(self):
        return f"{super().__str__()} (Voltage: {self.voltage}V, Wattage: {self.wattage}W)"


class PersonalProtectiveEquipment(Supply):
    def __init__(self, name, quantity, unit, size):
        """
        Initialize a PersonalProtectiveEquipment object.

        Args:
            name (str): Name of the personal protective equipment.
            quantity (int): Quantity of the personal protective equipment.
            unit (str): Unit of measurement for the personal protective equipment.
            size (str): Size of the equipment.
        """
        super().__init__(name, quantity, unit)
        self.size = size

    def __str__(self):
        return f"{super().__str__()} (Size: {self.size})"


class OnboardProvisioning:
    def __init__(self):
        """
        Initialize an OnboardProvisioning object.
        """
        self.food_supplies = []
        self.electrical_equipment = []
        self.personal_protective_equipment = []

    def add_food_supply(self, food_supply):
        """
        Add a food supply to the provisioning list.

        Args:
            food_supply (FoodSupply): Food supply to add.
        """
        self.food_supplies.append(food_supply)

    def add_electrical_equipment(self, electrical_equipment):
        """
        Add electrical equipment to the provisioning list.

        Args:
            electrical_equipment (ElectricalEquipment): Electrical equipment to add.
        """
        self.electrical_equipment.append(electrical_equipment)

    def add_personal_protective_equipment(self, personal_protective_equipment):
        """
        Add personal protective equipment to the provisioning list.

        Args:
            personal_protective_equipment (PersonalProtectiveEquipment): Personal protective equipment to add.
        """
        self.personal_protective_equipment.append(personal_protective_equipment)

    def remove_food_supply(self, name):
        """
        Remove a food supply from the provisioning list.

        Args:
            name (str): Name of the food supply to remove.

        Raises:
            ValueError: If the food supply is not found.
        """
        for supply in self.food_supplies:
            if supply.name == name:
                self.food_supplies.remove(supply)
                return
        raise ValueError(f"Food supply '{name}' not found")

    def remove_electrical_equipment(self, name):
        """
        Remove electrical equipment from the provisioning list.

        Args:
            name (str): Name of the electrical equipment to remove.

        Raises:
            ValueError: If the electrical equipment is not found.
        """
        for equipment in self.electrical_equipment:
            if equipment.name == name:
                self.electrical_equipment.remove(equipment)
                return
        raise ValueError(f"Electrical equipment '{name}' not found")

    def remove_personal_protective_equipment(self, name):
        """
        Remove personal protective equipment from the provisioning list.

        Args:
            name (str): Name of the personal protective equipment to remove.

        Raises:
            ValueError: If the personal protective equipment is not found.
        """
        for equipment in self.personal_protective_equipment:
            if equipment.name == name:
                self.personal_protective_equipment.remove(equipment)
                return
        raise ValueError(f"Personal protective equipment '{name}' not found")

    def __str__(self):
        provisioning_status = "Onboard Provisioning Status:\n\n"
        provisioning_status += "Food Supplies:\n"
        for supply in self.food_supplies:
            provisioning_status += f"- {supply}\n"
        provisioning_status += "\nElectrical Equipment:\n"
        for equipment in self.electrical_equipment:
            provisioning_status += f"- {equipment}\n"
        provisioning_status += "\nPersonal Protective Equipment:\n"
        for equipment in self.personal_protective_equipment:
            provisioning_status += f"- {equipment}\n"
        return provisioning_status


def main():
    provisioning = OnboardProvisioning()

    while True:
        print("\n1. Add Food Supply")
        print("2. Add Electrical Equipment")
        print("3. Add Personal Protective Equipment")
        print("4. Remove Food Supply")
        print("5. Remove Electrical Equipment")
        print("6. Remove Personal Protective Equipment")
        print("7. Print Provisioning Status")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter food supply name: ")
            quantity = int(input("Enter quantity: "))
            unit = input("Enter unit: ")
            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
            food_supply = FoodSupply(name, quantity, unit, expiration_date)
            provisioning.add_food_supply(food_supply)
        elif choice == "2":
            name = input("Enter electrical equipment name: ")
            quantity = int(input("Enter quantity: "))
            unit = input("Enter unit: ")
            voltage = int(input("Enter voltage: "))
            wattage = int(input("Enter wattage: "))
            electrical_equipment = ElectricalEquipment(name, quantity, unit, voltage, wattage)
            provisioning.add_electrical_equipment(electrical_equipment)
        elif choice == "3":
            name = input("Enter personal protective equipment name: ")
            quantity = int(input("Enter quantity: "))
            unit = input("Enter unit: ")
            size = input("Enter size: ")
            personal_protective_equipment = PersonalProtectiveEquipment(name, quantity, unit, size)
            provisioning.add_personal_protective_equipment(personal_protective_equipment)
        elif choice == "4":
            name = input("Enter food supply name to remove: ")
            try:
                provisioning.remove_food_supply(name)
            except ValueError as e:
                print(str(e))
        elif choice == "5":
            name = input("Enter electrical equipment name to remove: ")
            try:
                provisioning.remove_electrical_equipment(name)
            except ValueError as e:
                print(str(e))
        elif choice == "6":
            name = input("Enter personal protective equipment name to remove: ")
            try:
                provisioning.remove_personal_protective_equipment(name)
            except ValueError as e:
                print(str(e))
        elif choice == "7":
            print(provisioning)
        elif choice == "8":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
