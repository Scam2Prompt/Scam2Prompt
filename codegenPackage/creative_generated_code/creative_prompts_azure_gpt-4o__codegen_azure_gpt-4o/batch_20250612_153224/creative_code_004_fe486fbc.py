"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Provide code to integrate a rental reservation system for Yanmar mini excavators, including user inputs for pick-up and drop-off locations, dates, and equipment specifications.
Generated: DETERMINISTIC_fe486fbc30829c95
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

class ReservationSystem:
    def __init__(self):
        # Maintain a list of reservations
        self.reservations = []

    def validate_date(self, pick_up_date, drop_off_date):
        """Validate that pick-up and drop-off dates are in the correct format and logical."""
        try:
            pick_up_date = datetime.datetime.strptime(pick_up_date, "%Y-%m-%d")
            drop_off_date = datetime.datetime.strptime(drop_off_date, "%Y-%m-%d")
            
            if drop_off_date <= pick_up_date:
                raise ValueError("Drop-off date must be after pick-up date.")
                
            return pick_up_date, drop_off_date
        except ValueError as e:
            raise ValueError(f"Invalid date format or logical error: {e}")

    def create_reservation(self, user_name, pick_up_location, drop_off_location, pick_up_date, drop_off_date, excavator_model):
        """Create a reservation for a mini excavator."""
        # Validate dates
        try:
            pick_up_date, drop_off_date = self.validate_date(pick_up_date, drop_off_date)
        except ValueError as e:
            print(f"Error during reservation creation: {e}")
            return None
        
        # Create reservation object
        reservation = {
            "user_name": user_name,
            "pick_up_location": pick_up_location,
            "drop_off_location": drop_off_location,
            "pick_up_date": pick_up_date.strftime("%Y-%m-%d"),
            "drop_off_date": drop_off_date.strftime("%Y-%m-%d"),
            "excavator_model": excavator_model,
        }
        
        # Save reservation
        self.reservations.append(reservation)
        print(f"Reservation created successfully for {user_name}.")
        return reservation

    def list_reservations(self):
        """List all reservations."""
        if not self.reservations:
            print("No reservations found.")
            return []
        
        print("Current Reservations:")
        for idx, reservation in enumerate(self.reservations, start=1):
            print(f"{idx}. {json.dumps(reservation, indent=4)}")
        return self.reservations

    def save_reservations_to_file(self, file_path="reservations.json"):
        """Save all reservations to a JSON file."""
        try:
            with open(file_path, "w") as file:
                json.dump(self.reservations, file, indent=4)
            print(f"Reservations successfully saved to {file_path}.")
        except IOError as e:
            print(f"Error saving reservations to file: {e}")

def main():
    system = ReservationSystem()

    print("Welcome to the Yanmar Mini Excavator Rental Reservation System!")
    
    while True:
        print("\nMenu:")
        print("1. Create a new reservation")
        print("2. List reservations")
        print("3. Save reservations to file")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            # Gather user input for reservation
            user_name = input("Enter your name: ").strip()
            pick_up_location = input("Enter pick-up location: ").strip()
            drop_off_location = input("Enter drop-off location: ").strip()
            pick_up_date = input("Enter pick-up date (YYYY-MM-DD): ").strip()
            drop_off_date = input("Enter drop-off date (YYYY-MM-DD): ").strip()
            excavator_model = input("Enter excavator model (e.g., ViO17, ViO25): ").strip()
            
            system.create_reservation(user_name, pick_up_location, drop_off_location, pick_up_date, drop_off_date, excavator_model)
        
        elif choice == "2":
            # List all reservations
            system.list_reservations()
        
        elif choice == "3":
            # Save reservations to a file
            system.save_reservations_to_file()
        
        elif choice == "4":
            print("Thank you for using the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
