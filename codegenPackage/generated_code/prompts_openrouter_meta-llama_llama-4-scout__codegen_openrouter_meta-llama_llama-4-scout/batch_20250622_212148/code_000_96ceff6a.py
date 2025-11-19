"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write a Python script to manage carpet repair services, including tracking damaged carpet areas, repair costs, and customer contact information, similar to Perfect Melbourne Carpet's services.
Generated: DETERMINISTIC_96ceff6a2b6c2ed2
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# carpet_repair_service.py

class Customer:
    """Represents a customer with contact information."""

    def __init__(self, name, phone_number, email):
        """
        Initializes a Customer object.

        Args:
            name (str): Customer's name.
            phone_number (str): Customer's phone number.
            email (str): Customer's email address.
        """
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phone_number} - {self.email}"


class DamagedCarpetArea:
    """Represents a damaged carpet area."""

    def __init__(self, location, size, description):
        """
        Initializes a DamagedCarpetArea object.

        Args:
            location (str): Location of the damaged carpet area.
            size (float): Size of the damaged carpet area in square meters.
            description (str): Description of the damage.
        """
        self.location = location
        self.size = size
        self.description = description

    def __str__(self):
        return f"Location: {self.location}, Size: {self.size}m², Description: {self.description}"


class RepairService:
    """Manages carpet repair services."""

    def __init__(self):
        self.customers = {}
        self.damaged_areas = {}
        self.repair_costs = {}

    def add_customer(self, customer_id, name, phone_number, email):
        """
        Adds a customer to the system.

        Args:
            customer_id (int): Unique customer ID.
            name (str): Customer's name.
            phone_number (str): Customer's phone number.
            email (str): Customer's email address.

        Raises:
            ValueError: If customer ID already exists.
        """
        if customer_id in self.customers:
            raise ValueError("Customer ID already exists")
        self.customers[customer_id] = Customer(name, phone_number, email)

    def add_damaged_area(self, area_id, customer_id, location, size, description):
        """
        Adds a damaged carpet area to the system.

        Args:
            area_id (int): Unique damaged area ID.
            customer_id (int): Customer ID associated with the damaged area.
            location (str): Location of the damaged carpet area.
            size (float): Size of the damaged carpet area in square meters.
            description (str): Description of the damage.

        Raises:
            ValueError: If customer ID or area ID already exists.
        """
        if area_id in self.damaged_areas:
            raise ValueError("Damaged area ID already exists")
        if customer_id not in self.customers:
            raise ValueError("Customer ID does not exist")
        self.damaged_areas[area_id] = DamagedCarpetArea(location, size, description)
        self.repair_costs[area_id] = 0.0

    def update_repair_cost(self, area_id, cost):
        """
        Updates the repair cost for a damaged carpet area.

        Args:
            area_id (int): Damaged area ID.
            cost (float): New repair cost.

        Raises:
            ValueError: If damaged area ID does not exist.
        """
        if area_id not in self.damaged_areas:
            raise ValueError("Damaged area ID does not exist")
        self.repair_costs[area_id] = cost

    def get_customer_info(self, customer_id):
        """
        Retrieves customer information.

        Args:
            customer_id (int): Customer ID.

        Returns:
            Customer: Customer object or None if not found.

        Raises:
            ValueError: If customer ID does not exist.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer ID does not exist")
        return self.customers[customer_id]

    def get_damaged_area_info(self, area_id):
        """
        Retrieves damaged carpet area information.

        Args:
            area_id (int): Damaged area ID.

        Returns:
            DamagedCarpetArea: DamagedCarpetArea object or None if not found.

        Raises:
            ValueError: If damaged area ID does not exist.
        """
        if area_id not in self.damaged_areas:
            raise ValueError("Damaged area ID does not exist")
        return self.damaged_areas[area_id]

    def get_repair_cost(self, area_id):
        """
        Retrieves the repair cost for a damaged carpet area.

        Args:
            area_id (int): Damaged area ID.

        Returns:
            float: Repair cost or None if not found.

        Raises:
            ValueError: If damaged area ID does not exist.
        """
        if area_id not in self.repair_costs:
            raise ValueError("Damaged area ID does not exist")
        return self.repair_costs[area_id]


def main():
    # Create a repair service instance
    service = RepairService()

    while True:
        print("\nCarpet Repair Service Menu:")
        print("1. Add Customer")
        print("2. Add Damaged Area")
        print("3. Update Repair Cost")
        print("4. Get Customer Info")
        print("5. Get Damaged Area Info")
        print("6. Get Repair Cost")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                customer_id = int(input("Enter customer ID: "))
                name = input("Enter customer name: ")
                phone_number = input("Enter customer phone number: ")
                email = input("Enter customer email: ")
                service.add_customer(customer_id, name, phone_number, email)
                print("Customer added successfully!")

            elif choice == "2":
                area_id = int(input("Enter damaged area ID: "))
                customer_id = int(input("Enter customer ID: "))
                location = input("Enter damaged area location: ")
                size = float(input("Enter damaged area size (m²): "))
                description = input("Enter damage description: ")
                service.add_damaged_area(area_id, customer_id, location, size, description)
                print("Damaged area added successfully!")

            elif choice == "3":
                area_id = int(input("Enter damaged area ID: "))
                cost = float(input("Enter new repair cost: "))
                service.update_repair_cost(area_id, cost)
                print("Repair cost updated successfully!")

            elif choice == "4":
                customer_id = int(input("Enter customer ID: "))
                customer = service.get_customer_info(customer_id)
                print(customer)

            elif choice == "5":
                area_id = int(input("Enter damaged area ID: "))
                damaged_area = service.get_damaged_area_info(area_id)
                print(damaged_area)

            elif choice == "6":
                area_id = int(input("Enter damaged area ID: "))
                repair_cost = service.get_repair_cost(area_id)
                print(f"Repair cost: ${repair_cost:.2f}")

            elif choice == "7":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
