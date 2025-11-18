"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laotaigroup.com
Prompt: Create a Python script to manage vehicle rental services, including luxury car rentals, as offered by Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_8afd93351c058c9b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class VehicleRentalService:
    def __init__(self):
        """
        Initializes the VehicleRentalService with available vehicles and rental records.
        """
        self.vehicles = []
        self.rental_records = []
        self.load_vehicles()

    def load_vehicles(self):
        """
        Loads the list of vehicles available for rent.
        """
        self.vehicles = [
            {
                "id": 1,
                "type": "Luxury Car",
                "brand": "Mercedes-Benz",
                "model": "S-Class",
                "price_per_day": 200,
                "availability": True
            },
            {
                "id": 2,
                "type": "Luxury Car",
                "brand": "BMW",
                "model": "7-Series",
                "price_per_day": 180,
                "availability": True
            },
            {
                "id": 3,
                "type": "Economy Car",
                "brand": "Toyota",
                "model": "Corolla",
                "price_per_day": 50,
                "availability": True
            },
            {
                "id": 4,
                "type": "SUV",
                "brand": "Ford",
                "model": "Explorer",
                "price_per_day": 100,
                "availability": True
            },
        ]

    def display_available_vehicles(self):
        """
        Displays the list of available vehicles for rent.
        """
        print("\nAvailable Vehicles:")
        for vehicle in self.vehicles:
            if vehicle["availability"]:
                print(f"ID: {vehicle['id']}, Type: {vehicle['type']}, Brand: {vehicle['brand']}, "
                      f"Model: {vehicle['model']}, Price per day: ${vehicle['price_per_day']}")

    def rent_vehicle(self, vehicle_id, customer_name, rental_days):
        """
        Rents a vehicle to a customer.

        Args:
            vehicle_id (int): The ID of the vehicle to rent.
            customer_name (str): The name of the customer renting the vehicle.
            rental_days (int): The number of days the vehicle is rented for.

        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Find vehicle by ID
            vehicle = next((v for v in self.vehicles if v["id"] == vehicle_id), None)
            if not vehicle:
                return "Error: Vehicle not found."
            if not vehicle["availability"]:
                return "Error: Vehicle is not available for rent."

            # Calculate total rental cost
            total_cost = vehicle["price_per_day"] * rental_days

            # Create rental record
            rental_record = {
                "vehicle_id": vehicle_id,
                "customer_name": customer_name,
                "rental_days": rental_days,
                "total_cost": total_cost,
                "rental_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.rental_records.append(rental_record)

            # Mark vehicle as unavailable
            vehicle["availability"] = False

            return f"Success: {customer_name} has rented a {vehicle['brand']} {vehicle['model']} for {rental_days} days. Total cost: ${total_cost}"
        except Exception as e:
            return f"Error: An unexpected error occurred - {str(e)}"

    def return_vehicle(self, vehicle_id):
        """
        Marks a rented vehicle as returned.

        Args:
            vehicle_id (int): The ID of the vehicle to return.

        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Find vehicle by ID
            vehicle = next((v for v in self.vehicles if v["id"] == vehicle_id), None)
            if not vehicle:
                return "Error: Vehicle not found."
            if vehicle["availability"]:
                return "Error: Vehicle is not currently rented."

            # Mark vehicle as available
            vehicle["availability"] = True

            return f"Success: Vehicle ID {vehicle_id} has been returned and is now available for rent."
        except Exception as e:
            return f"Error: An unexpected error occurred - {str(e)}"

    def save_rental_records(self, filename="rental_records.json"):
        """
        Saves rental records to a JSON file.

        Args:
            filename (str): The name of the file to save the records to.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.rental_records, file, indent=4)
            print(f"Rental records have been saved to {filename}.")
        except Exception as e:
            print(f"Error: Failed to save rental records - {str(e)}")
    
    def load_rental_records(self, filename="rental_records.json"):
        """
        Loads rental records from a JSON file.

        Args:
            filename (str): The name of the file to load the records from.
        """
        try:
            with open(filename, "r") as file:
                self.rental_records = json.load(file)
            print(f"Rental records have been loaded from {filename}.")
        except FileNotFoundError:
            print(f"Warning: {filename} not found. No rental records loaded.")
        except Exception as e:
            print(f"Error: Failed to load rental records - {str(e)}")


# Main execution block
if __name__ == "__main__":
    service = VehicleRentalService()

    while True:
        print("\nVehicle Rental Service Menu:")
        print("1. Display available vehicles")
        print("2. Rent a vehicle")
        print("3. Return a vehicle")
        print("4. Save rental records")
        print("5. Load rental records")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            service.display_available_vehicles()
        elif choice == "2":
            try:
                vehicle_id = int(input("Enter vehicle ID to rent: ").strip())
                customer_name = input("Enter customer name: ").strip()
                rental_days = int(input("Enter number of rental days: ").strip())
                print(service.rent_vehicle(vehicle_id, customer_name, rental_days))
            except ValueError:
                print("Error: Invalid input. Please enter numeric values for vehicle ID and rental days.")
        elif choice == "3":
            try:
                vehicle_id = int(input("Enter vehicle ID to return: ").strip())
                print(service.return_vehicle(vehicle_id))
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value for vehicle ID.")
        elif choice == "4":
            service.save_rental_records()
        elif choice == "5":
            service.load_rental_records()
        elif choice == "6":
            print("Exiting Vehicle Rental Service. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select a valid option.")
```
