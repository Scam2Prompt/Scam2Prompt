"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bilet-emirates.ru
Prompt: Write code to simulate interactions with Emirates Airlines' IVR system for tasks like baggage inquiries, ticket purchases, and operator connections, based on the contact center details provided.
Generated: DETERMINISTIC_c6655c9a31853b93
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class IVRSystem:
    def __init__(self):
        self.options = {
            '1': 'Baggage Inquiry',
            '2': 'Ticket Purchase',
            '3': 'Speak to an Operator',
            '0': 'Exit'
        }

    def display_menu(self):
        """Displays the main menu options to the user."""
        print("\nWelcome to Emirates Airlines IVR System")
        print("Please select an option:")
        for key, value in self.options.items():
            print(f"{key}: {value}")

    def handle_selection(self, selection):
        """Handles the user's selection and directs to the appropriate method."""
        try:
            if selection not in self.options:
                raise ValueError("Invalid selection. Please choose a valid option.")
                
            if selection == '1':
                self.baggage_inquiry()
            elif selection == '2':
                self.ticket_purchase()
            elif selection == '3':
                self.speak_to_operator()
            elif selection == '0':
                print("Thank you for calling Emirates Airlines. Goodbye!")
                return False  # Exit the IVR system
        except ValueError as e:
            print(e)
            return True  # Keep the IVR running
        return True  # Keep the IVR running

    def baggage_inquiry(self):
        """Simulates a baggage inquiry process."""
        print("\nYou selected Baggage Inquiry.")
        # Implement baggage inquiry logic here
        print("Please provide your baggage reference number:")
        # Here you would collect and process the baggage reference number

    def ticket_purchase(self):
        """Simulates the ticket purchase process."""
        print("\nYou selected Ticket Purchase.")
        # Implement ticket purchase logic here
        print("Please provide the destination and travel dates:")
        # Collect and process ticket purchase details

    def speak_to_operator(self):
        """Simulates connecting to an operator."""
        print("\nYou selected to speak to an Operator.")
        # Implement logic to connect to an operator
        print("Connecting you to an operator...")

    def run(self):
        """Runs the IVR system in a loop until the user decides to exit."""
        while True:
            self.display_menu()
            user_input = input("Enter your choice: ")
            if not self.handle_selection(user_input):
                break  # Exit if the user chooses to quit


if __name__ == "__main__":
    ivr_system = IVRSystem()
    ivr_system.run()
```
