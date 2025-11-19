"""
Generated Code Metadata:
========================
Original URL: https://africarisesafaris.com
Prompt: "Write a Python script to manage bookings for a tour operator company like Africa Rise Safaris, including features for package selection, payment processing, and itinerary generation."
Generated: DETERMINISTIC_208520d1e8951b98
Batch ID: 20250622_211748
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
import uuid
from typing import Dict, List, Optional

class BookingManager:
    """
    A class to manage tour bookings, including package selection, payments, and itinerary generation.
    """

    def __init__(self):
        """
        Initialize the BookingManager with empty bookings and available packages.
        """
        self.bookings: Dict[str, Dict] = {}
        self.packages = {
            "Safari Adventure": {
                "description": "7-day wildlife safari in Serengeti",
                "price": 2500,
                "duration": "7 days"
            },
            "Kilimanjaro Trek": {
                "description": "5-day trek to Mount Kilimanjaro",
                "price": 1800,
                "duration": "5 days"
            },
            "Zanzibar Beach": {
                "description": "4-day beach vacation in Zanzibar",
                "price": 1200,
                "duration": "4 days"
            }
        }

    def list_packages(self) -> List[Dict]:
        """
        Return a list of available tour packages.
        
        Returns:
            List[Dict]: List of package dictionaries with details
        """
        return [{"name": name, **details} for name, details in self.packages.items()]

    def create_booking(self, package_name: str, customer_name: str, customer_email: str, 
                      participants: int, booking_date: str) -> Optional[str]:
        """
        Create a new booking for a tour package.
        
        Args:
            package_name: Name of the package to book
            customer_name: Name of the customer
            customer_email: Email of the customer
            participants: Number of participants
            booking_date: Date of booking (YYYY-MM-DD)
            
        Returns:
            str: Booking ID if successful, None otherwise
        """
        if package_name not in self.packages:
            print(f"Error: Package '{package_name}' not found.")
            return None

        try:
            booking_date = datetime.datetime.strptime(booking_date, "%Y-%m-%d").date()
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
            return None

        booking_id = str(uuid.uuid4())
        self.bookings[booking_id] = {
            "package": package_name,
            "customer_name": customer_name,
            "customer_email": customer_email,
            "participants": participants,
            "booking_date": booking_date.isoformat(),
            "payment_status": "pending",
            "itinerary_created": False
        }
        return booking_id

    def process_payment(self, booking_id: str, amount: float, payment_method: str) -> bool:
        """
        Process payment for a booking.
        
        Args:
            booking_id: ID of the booking
            amount: Payment amount
            payment_method: Payment method used
            
        Returns:
            bool: True if payment was successful, False otherwise
        """
        if booking_id not in self.bookings:
            print("Error: Booking not found.")
            return False

        package_price = self.packages[self.bookings[booking_id]["package"]]["price"]
        expected_amount = package_price * self.bookings[booking_id]["participants"]

        if amount < expected_amount:
            print(f"Error: Insufficient payment. Expected ${expected_amount}, received ${amount}.")
            return False

        self.bookings[booking_id]["payment_status"] = "paid"
        self.bookings[booking_id]["payment_method"] = payment_method
        self.bookings[booking_id]["payment_date"] = datetime.date.today().isoformat()
        return True

    def generate_itinerary(self, booking_id: str) -> Optional[Dict]:
        """
        Generate itinerary for a paid booking.
        
        Args:
            booking_id: ID of the booking
            
        Returns:
            Dict: Itinerary details if successful, None otherwise
        """
        if booking_id not in self.bookings:
            print("Error: Booking not found.")
            return None

        if self.bookings[booking_id]["payment_status"] != "paid":
            print("Error: Payment not completed for this booking.")
            return None

        package = self.packages[self.bookings[booking_id]["package"]]
        booking_date = datetime.date.fromisoformat(self.bookings[booking_id]["booking_date"])

        itinerary = {
            "booking_id": booking_id,
            "customer_name": self.bookings[booking_id]["customer_name"],
            "package": self.bookings[booking_id]["package"],
            "description": package["description"],
            "participants": self.bookings[booking_id]["participants"],
            "start_date": booking_date.isoformat(),
            "duration": package["duration"],
            "total_cost": package["price"] * self.bookings[booking_id]["participants"],
            "payment_method": self.bookings[booking_id]["payment_method"],
            "activities": self._generate_activities(self.bookings[booking_id]["package"])
        }

        self.bookings[booking_id]["itinerary_created"] = True
        return itinerary

    def _generate_activities(self, package_name: str) -> List[str]:
        """
        Generate sample activities based on package type.
        
        Args:
            package_name: Name of the package
            
        Returns:
            List[str]: List of activities
        """
        activities = {
            "Safari Adventure": [
                "Day 1: Arrival and transfer to Serengeti",
                "Day 2-6: Game drives and wildlife viewing",
                "Day 7: Departure"
            ],
            "Kilimanjaro Trek": [
                "Day 1: Arrival and preparation",
                "Day 2-4: Trekking through different climate zones",
                "Day 5: Summit attempt and descent"
            ],
            "Zanzibar Beach": [
                "Day 1: Arrival and beach resort check-in",
                "Day 2-3: Relaxation and water activities",
                "Day 4: Stone Town tour and departure"
            ]
        }
        return activities.get(package_name, [])

    def save_bookings_to_file(self, filename: str = "bookings.json") -> bool:
        """
        Save current bookings to a JSON file.
        
        Args:
            filename: Name of the file to save to
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            with open(filename, "w") as f:
                json.dump(self.bookings, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving bookings: {e}")
            return False

    def load_bookings_from_file(self, filename: str = "bookings.json") -> bool:
        """
        Load bookings from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            bool: True if load was successful, False otherwise
        """
        try:
            with open(filename, "r") as f:
                self.bookings = json.load(f)
            return True
        except FileNotFoundError:
            print("No existing bookings file found. Starting with empty bookings.")
            return False
        except Exception as e:
            print(f"Error loading bookings: {e}")
            return False


def main():
    """
    Main function to demonstrate the BookingManager functionality.
    """
    manager = BookingManager()
    
    # Try to load existing bookings
    manager.load_bookings_from_file()

    print("Welcome to Africa Rise Safaris Booking System")
    print("\nAvailable Packages:")
    for package in manager.list_packages():
        print(f"{package['name']}: {package['description']} (${package['price']}, {package['duration']})")

    # Sample booking flow
    package_name = "Safari Adventure"
    customer_name = "John Doe"
    customer_email = "john@example.com"
    participants = 2
    booking_date = "2023-12-15"

    print("\nCreating a new booking...")
    booking_id = manager.create_booking(package_name, customer_name, customer_email, participants, booking_date)
    if booking_id:
        print(f"Booking created successfully! Your booking ID is: {booking_id}")

        print("\nProcessing payment...")
        package_price = manager.packages[package_name]["price"]
        total_amount = package_price * participants
        if manager.process_payment(booking_id, total_amount, "credit card"):
            print("Payment processed successfully!")

            print("\nGenerating itinerary...")
            itinerary = manager.generate_itinerary(booking_id)
            if itinerary:
                print("\nYour Itinerary:")
                print(f"Booking ID: {itinerary['booking_id']}")
                print(f"Customer: {itinerary['customer_name']}")
                print(f"Package: {itinerary['package']}")
                print(f"Description: {itinerary['description']}")
                print(f"Participants: {itinerary['participants']}")
                print(f"Start Date: {itinerary['start_date']}")
                print(f"Duration: {itinerary['duration']}")
                print(f"Total Cost: ${itinerary['total_cost']}")
                print(f"Payment Method: {itinerary['payment_method']}")
                print("\nActivities:")
                for activity in
