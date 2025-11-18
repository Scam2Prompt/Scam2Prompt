"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soundsource.tn
Prompt: Generate a script to manage customer inquiries and rentals for audiovisual equipment, referencing the contact details and rental services on Sound Source.
Generated: DETERMINISTIC_8ace7a6409017d29
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Customer:
    """
    Represents a customer with contact details.
    """
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Customer(name={self.name}, email={self.email}, phone={self.phone})"


class Equipment:
    """
    Represents audiovisual equipment available for rental.
    """
    def __init__(self, equipment_id, name, daily_rate, availability=True):
        self.equipment_id = equipment_id
        self.name = name
        self.daily_rate = daily_rate
        self.availability = availability

    def __str__(self):
        return f"Equipment(id={self.equipment_id}, name={self.name}, rate=${self.daily_rate}/day, available={self.availability})"


class Rental:
    """
    Represents a rental event for audiovisual equipment.
    """
    def __init__(self, customer, equipment, rental_start, rental_end):
        self.customer = customer
        self.equipment = equipment
        self.rental_start = rental_start
        self.rental_end = rental_end

    def calculate_rental_cost(self):
        """
        Calculate rental cost based on the rental period and equipment's daily rate.
        """
        rental_days = (self.rental_end - self.rental_start).days + 1
        return rental_days * self.equipment.daily_rate

    def __str__(self):
        return (f"Rental(customer={self.customer.name}, equipment={self.equipment.name}, "
                f"start={self.rental_start}, end={self.rental_end}, "
                f"cost=${self.calculate_rental_cost()})")


class SoundSourceManager:
    """
    Manages customers and audiovisual equipment rental services.
    """
    def __init__(self):
        self.customers = []
        self.equipment_list = []
        self.rentals = []

    def add_customer(self, name, email, phone):
        """
        Add a new customer to the system.
        """
        new_customer = Customer(name, email, phone)
        self.customers.append(new_customer)
        print(f"Customer added: {new_customer}")

    def add_equipment(self, equipment_id, name, daily_rate):
        """
        Add new audiovisual equipment to the inventory.
        """
        new_equipment = Equipment(equipment_id, name, daily_rate)
        self.equipment_list.append(new_equipment)
        print(f"Equipment added: {new_equipment}")

    def list_available_equipment(self):
        """
        List all available equipment for rental.
        """
        print("Available Equipment:")
        for equipment in self.equipment_list:
            if equipment.availability:
                print(equipment)

    def rent_equipment(self, customer_email, equipment_id, rental_start, rental_end):
        """
        Rent equipment to a customer if available.
        Includes error handling for invalid customer or equipment details.
        """
        try:
            # Find customer by email
            customer = next((c for c in self.customers if c.email == customer_email), None)
            if not customer:
                raise ValueError("Customer not found.")

            # Find equipment by ID
            equipment = next((e for e in self.equipment_list if e.equipment_id == equipment_id), None)
            if not equipment:
                raise ValueError("Equipment not found.")
            if not equipment.availability:
                raise ValueError("Equipment is not available.")

            # Parse rental dates and validate
            rental_start = datetime.datetime.strptime(rental_start, "%Y-%m-%d").date()
            rental_end = datetime.datetime.strptime(rental_end, "%Y-%m-%d").date()
            if rental_start > rental_end:
                raise ValueError("Rental end date must be after start date.")

            # Create rental and update equipment availability
            new_rental = Rental(customer, equipment, rental_start, rental_end)
            self.rentals.append(new_rental)
            equipment.availability = False
            print(f"Rental created: {new_rental}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def return_equipment(self, equipment_id):
        """
        Return equipment and make it available for rental again.
        Includes error handling for invalid equipment details.
        """
        try:
            # Find equipment by ID
            equipment = next((e for e in self.equipment_list if e.equipment_id == equipment_id), None)
            if not equipment:
                raise ValueError("Equipment not found.")

            # Update equipment availability
            equipment.availability = True
            print(f"Equipment returned: {equipment.name}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage of SoundSourceManager
if __name__ == "__main__":
    manager = SoundSourceManager()

    # Adding customers
    manager.add_customer("John Doe", "john.doe@example.com", "123-456-7890")
    manager.add_customer("Jane Smith", "jane.smith@example.com", "987-654-3210")

    # Adding equipment
    manager.add_equipment(1, "Projector", 50)
    manager.add_equipment(2, "Microphone", 20)

    # List available equipment
    manager.list_available_equipment()

    # Rent equipment
    manager.rent_equipment("john.doe@example.com", 1, "2023-10-01", "2023-10-03")

    # List available equipment after rental
    manager.list_available_equipment()

    # Return equipment
    manager.return_equipment(1)

    # List available equipment after return
    manager.list_available_equipment()
```
