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

class KaraokeHeavenChatbot:
    def __init__(self):
        self.themes = ["Classic", "Pop", "Rock", "Jazz", "Hip-Hop"]
        self.time_slots = ["10:00 AM", "12:00 PM", "02:00 PM", "04:00 PM", "06:00 PM", "08:00 PM"]
        self.food_packages = {
            "Basic": {"description": "1 pizza + 1 soft drink", "price": 20},
            "Premium": {"description": "2 pizzas + 2 soft drinks + 1 dessert", "price": 35},
            "Deluxe": {"description": "3 pizzas + 3 soft drinks + 2 desserts", "price": 50},
        }

    def greet_user(self):
        print("Welcome to Karaoke Heaven! I'm here to help you choose a theme, book a time slot, and order food and drinks.")

    def select_theme(self):
        print("Available karaoke room themes:")
        for idx, theme in enumerate(self.themes, start=1):
            print(f"{idx}. {theme}")
        
        theme_choice = input("Please select a theme by entering the corresponding number: ")
        try:
            theme_index = int(theme_choice) - 1
            if 0 <= theme_index < len(self.themes):
                selected_theme = self.themes[theme_index]
                print(f"You have selected the theme: {selected_theme}")
                return selected_theme
            else:
                raise ValueError("Invalid selection.")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            return self.select_theme()

    def book_time_slot(self):
        print("Available time slots:")
        for idx, slot in enumerate(self.time_slots, start=1):
            print(f"{idx}. {slot}")
        
        slot_choice = input("Please select a time slot by entering the corresponding number: ")
        try:
            slot_index = int(slot_choice) - 1
            if 0 <= slot_index < len(self.time_slots):
                selected_slot = self.time_slots[slot_index]
                print(f"You have booked the time slot: {selected_slot}")
                return selected_slot
            else:
                raise ValueError("Invalid selection.")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            return self.book_time_slot()

    def order_food_package(self):
        print("Available food and drink packages:")
        for package, details in self.food_packages.items():
            print(f"{package}: {details['description']} - ${details['price']}")
        
        package_choice = input("Please select a food package by entering the package name: ")
        if package_choice in self.food_packages:
            selected_package = self.food_packages[package_choice]
            print(f"You have selected the package: {package_choice} - {selected_package['description']}")
            return package_choice
        else:
            print("Error: Invalid package name. Please try again.")
            return self.order_food_package()

    def confirm_booking(self, theme, time_slot, food_package):
        print("\nBooking Confirmation:")
        print(f"Selected Theme: {theme}")
        print(f"Time Slot: {time_slot}")
        print(f"Food Package: {food_package} - ${self.food_packages[food_package]['price']}")
        print("Thank you for booking with Karaoke Heaven! Enjoy your time!")

    def run(self):
        self.greet_user()
        theme = self.select_theme()
        time_slot = self.book_time_slot()
        food_package = self.order_food_package()
        self.confirm_booking(theme, time_slot, food_package)

if __name__ == "__main__":
    bot = KaraokeHeavenChatbot()
    bot.run()
```
