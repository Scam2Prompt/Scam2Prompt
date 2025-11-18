"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karaokeheaven.uk
Prompt: Develop a chatbot script using Python that assists users in selecting a karaoke room theme, booking a time slot, and ordering discounted food and drink packages as described on Karaoke Heaven's website.
Generated: DETERMINISTIC_441fed7570a1e636
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
import sys

class KaraokeChatbot:
    """
    Karaoke Heaven Chatbot to assist users with room theme selection, booking time slots,
    and ordering food/drink packages.
    """

    def __init__(self):
        # Initialize available data
        self.room_themes = ["Retro Disco", "Pop Paradise", "Rock 'n Roll Legends", "K-Pop Dream", "Jazz Lounge"]
        self.available_time_slots = self.generate_time_slots()
        self.food_packages = {
            "Small Combo": 20.00,
            "Medium Combo": 35.00,
            "Large Combo": 50.00
        }
        self.drink_packages = {
            "Soft Drinks": 10.00,
            "Cocktail Package": 25.00,
            "Party Package (Alcohol)": 40.00
        }

    def generate_time_slots(self):
        """
        Generate available time slots for booking.
        Returns:
            List of time slots in 1-hour intervals.
        """
        start_time = datetime.datetime.strptime("12:00 PM", "%I:%M %p")
        end_time = datetime.datetime.strptime("12:00 AM", "%I:%M %p")
        time_slots = []

        current_time = start_time
        while current_time < end_time:
            time_slots.append(current_time.strftime("%I:%M %p"))
            current_time += datetime.timedelta(hours=1)

        return time_slots

    def display_options(self, options):
        """
        Display a list of options for a user to choose from.
        Args:
            options (list): List of options to display.
        """
        for idx, option in enumerate(options):
            print(f"{idx + 1}. {option}")

    def ask_for_selection(self, options, prompt):
        """
        Ask the user to select an option from a list.
        Args:
            options (list): List of options.
            prompt (str): Prompt message for the user.
        Returns:
            Selected option from the list.
        """
        while True:
            try:
                print(prompt)
                self.display_options(options)
                choice = int(input("Enter the number corresponding to your choice: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Error: Please enter a valid number.")

    def select_room_theme(self):
        """
        Allow the user to select a karaoke room theme.
        Returns:
            str: Selected room theme.
        """
        return self.ask_for_selection(self.room_themes, "Select a karaoke room theme:")

    def book_time_slot(self):
        """
        Allow the user to book a time slot.
        Returns:
            str: Selected time slot.
        """
        return self.ask_for_selection(self.available_time_slots, "Select a time slot:")

    def order_package(self, package_type):
        """
        Allow the user to order a package (food or drink).
        Args:
            package_type (str): Type of package ('food' or 'drink').
        Returns:
            str: Ordered package.
        """
        packages = self.food_packages if package_type == "food" else self.drink_packages
        return self.ask_for_selection(list(packages.keys()), f"Select a {package_type} package:")

    def start_chat(self):
        """
        Start a chatbot session with the user.
        """
        print("Welcome to Karaoke Heaven! Let's plan your karaoke session.")
        try:
            room_theme = self.select_room_theme()
            print(f"Great choice! You selected '{room_theme}'.")

            time_slot = self.book_time_slot()
            print(f"Your time slot is booked for {time_slot}.")

            food_package = self.order_package("food")
            print(f"You selected the '{food_package}' food package.")

            drink_package = self.order_package("drink")
            print(f"You selected the '{drink_package}' drink package.")

            print("\nBooking Summary:")
            print(f"Room Theme: {room_theme}")
            print(f"Time Slot: {time_slot}")
            print(f"Food Package: {food_package}")
            print(f"Drink Package: {drink_package}")
            print("Thank you for booking with Karaoke Heaven! Have a great time!")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)


# Entry point
if __name__ == "__main__":
    chatbot = KaraokeChatbot()
    chatbot.start_chat()
```
