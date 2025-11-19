"""
Generated Code Metadata:
========================
Original URL: https://bilet-emirates.ru
Prompt: Write code to simulate interactions with Emirates Airlines' IVR system for tasks like baggage inquiries, ticket purchases, and operator connections, based on the contact center details provided.
Generated: DETERMINISTIC_c6655c9a31853b93
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum, auto

class IVROption(Enum):
    BAGGAGE_INQUIRY = auto()
    TICKET_PURCHASE = auto()
    OPERATOR_CONNECTION = auto()
    EXIT = auto()

class EmiratesIVR:
    """Simulates Emirates Airlines IVR system interactions."""
    
    def __init__(self):
        self._current_option = None
        self._call_active = True
    
    def _play_welcome_message(self):
        """Play the welcome message and main menu options."""
        print("\nWelcome to Emirates Airlines automated service.")
        print("Please select from the following options:")
        print("1. Baggage inquiries")
        print("2. Purchase tickets")
        print("3. Speak to a customer service representative")
        print("4. Exit")
    
    def _get_user_input(self):
        """Get and validate user input for menu selection."""
        while True:
            try:
                choice = int(input("\nEnter your choice (1-4): "))
                if 1 <= choice <= 4:
                    return IVROption(choice)
                print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
    
    def _handle_baggage_inquiry(self):
        """Handle baggage inquiry options."""
        print("\nBaggage Information:")
        print("1. Baggage allowance")
        print("2. Lost baggage")
        print("3. Special items")
        print("4. Return to main menu")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-4): "))
                if choice == 1:
                    print("\nStandard baggage allowance: 30kg for Economy, 40kg for Business, 50kg for First Class.")
                elif choice == 2:
                    print("\nPlease visit the baggage service desk at the airport or call +971 4 214 4444.")
                elif choice == 3:
                    print("\nSpecial items like sports equipment require prior approval. Please contact customer service.")
                elif choice == 4:
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
    
    def _handle_ticket_purchase(self):
        """Handle ticket purchase flow."""
        print("\nTicket Purchase:")
        print("1. One-way ticket")
        print("2. Round-trip ticket")
        print("3. Multi-city trip")
        print("4. Return to main menu")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-4): "))
                if choice in (1, 2, 3):
                    self._process_ticket_purchase(choice)
                    return
                elif choice == 4:
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
    
    def _process_ticket_purchase(self, ticket_type):
        """Simulate ticket purchase process."""
        ticket_types = {
            1: "one-way",
            2: "round-trip",
            3: "multi-city"
        }
        print(f"\nProcessing {ticket_types[ticket_type]} ticket purchase...")
        time.sleep(1)
        
        try:
            origin = input("Enter origin city: ").strip()
            destination = input("Enter destination city: ").strip()
            if not origin or not destination:
                raise ValueError("Origin and destination are required.")
            
            print(f"\nSearching for flights from {origin} to {destination}...")
            time.sleep(2)
            
            flights = [
                {"flight_no": "EK" + str(random.randint(100, 999)), "departure": "08:00", "price": random.randint(500, 2000)},
                {"flight_no": "EK" + str(random.randint(100, 999)), "departure": "12:00", "price": random.randint(500, 2000)},
                {"flight_no": "EK" + str(random.randint(100, 999)), "departure": "18:00", "price": random.randint(500, 2000)}
            ]
            
            print("\nAvailable flights:")
            for i, flight in enumerate(flights, 1):
                print(f"{i}. Flight {flight['flight_no']} at {flight['departure']} - ${flight['price']}")
            
            flight_choice = int(input("\nSelect flight (1-3): "))
            if 1 <= flight_choice <= 3:
                selected = flights[flight_choice - 1]
                print(f"\nYou have selected Flight {selected['flight_no']} at {selected['departure']}")
                print(f"Total amount: ${selected['price']}")
                print("Thank you for choosing Emirates!")
            else:
                print("Invalid flight selection.")
        except ValueError as e:
            print(f"Error: {str(e)}")
    
    def _handle_operator_connection(self):
        """Simulate connecting to a customer service representative."""
        print("\nConnecting you to a customer service representative...")
        wait_time = random.randint(1, 5)
        time.sleep(wait_time)
        print(f"\nAll representatives are currently busy. Your estimated wait time is {wait_time} minutes.")
        print("Press 1 to stay on the line or 2 to request a callback.")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-2): "))
                if choice == 1:
                    print("Please hold...")
                    time.sleep(3)
                    print("Representative connected. How may I help you?")
                    return
                elif choice == 2:
                    phone = input("Enter your phone number for callback: ")
                    if len(phone) >= 8:
                        print("We will call you back shortly. Thank you.")
                        return
                    print("Invalid phone number. Please try again.")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")
    
    def run(self):
        """Main method to run the IVR simulation."""
        while self._call_active:
            self._play_welcome_message()
            self._current_option = self._get_user_input()
            
            if self._current_option == IVROption.BAGGAGE_INQUIRY:
                self._handle_baggage_inquiry()
            elif self._current_option == IVROption.TICKET_PURCHASE:
                self._handle_ticket_purchase()
            elif self._current_option == IVROption.OPERATOR_CONNECTION:
                self._handle_operator_connection()
            elif self._current_option == IVROption.EXIT:
                print("\nThank you for calling Emirates Airlines. Have a pleasant day!")
                self._call_active = False

if __name__ == "__main__":
    ivr = EmiratesIVR()
    ivr.run()
```
