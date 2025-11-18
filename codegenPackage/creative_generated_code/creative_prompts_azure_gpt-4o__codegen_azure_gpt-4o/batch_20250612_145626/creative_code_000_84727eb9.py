"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Write Python code to create a registration form for a basketball training camp, including fields for skill level (beginner/advanced), camp dates, and payment options, as described in the L-Zero basketball camp details.
Generated: DETERMINISTIC_84727eb93af4a18d
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class BasketballCampRegistration:
    """A class to handle registration for L-Zero Basketball Camp."""

    def __init__(self):
        # Initialize fields with default values
        self.name = ""
        self.email = ""
        self.skill_level = ""
        self.camp_dates = []
        self.payment_option = ""

    def validate_email(self, email):
        """Validate email format using regex."""
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_pattern, email)

    def collect_registration_details(self):
        """Interactively collect registration details from the user."""
        try:
            # Collect Participant Name
            self.name = input("Enter your full name: ").strip()
            if not self.name:
                raise ValueError("Name cannot be empty.")

            # Collect Email and validate
            self.email = input("Enter your email address: ").strip()
            if not self.validate_email(self.email):
                raise ValueError("Invalid email address.")

            # Collect Skill Level
            print("Choose your skill level:")
            print("1. Beginner")
            print("2. Advanced")
            skill_choice = input("Enter your choice (1 or 2): ").strip()
            if skill_choice == "1":
                self.skill_level = "Beginner"
            elif skill_choice == "2":
                self.skill_level = "Advanced"
            else:
                raise ValueError("Invalid skill level selection.")

            # Collect Camp Dates
            print("Available camp dates:")
            print("1. June 10 - June 15")
            print("2. July 20 - July 25")
            print("3. August 5 - August 10")
            date_choices = input(
                "Enter the numbers of your chosen camp dates (comma-separated, e.g., 1,2): "
            ).strip()
            date_mapping = {
                "1": "June 10 - June 15",
                "2": "July 20 - July 25",
                "3": "August 5 - August 10",
            }
            self.camp_dates = [date_mapping[choice.strip()] for choice in date_choices.split(",") if choice.strip() in date_mapping]
            if not self.camp_dates:
                raise ValueError("No valid camp dates selected.")

            # Collect Payment Option
            print("Payment options:")
            print("1. Credit Card")
            print("2. PayPal")
            print("3. Bank Transfer")
            payment_choice = input("Enter your choice (1, 2, or 3): ").strip()
            payment_mapping = {
                "1": "Credit Card",
                "2": "PayPal",
                "3": "Bank Transfer",
            }
            self.payment_option = payment_mapping.get(payment_choice)
            if not self.payment_option:
                raise ValueError("Invalid payment option selected.")

        except ValueError as ve:
            print(f"Input Error: {ve}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

        return True

    def display_registration_summary(self):
        """Display the collected registration details."""
        print("\nRegistration Complete!")
        print("Here are your details:")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Skill Level: {self.skill_level}")
        print(f"Camp Dates: {', '.join(self.camp_dates)}")
        print(f"Payment Option: {self.payment_option}")

    def register(self):
        """Main method to handle registration."""
        print("Welcome to L-Zero Basketball Camp Registration!")
        if self.collect_registration_details():
            self.display_registration_summary()
        else:
            print("Registration failed. Please try again.")


if __name__ == "__main__":
    # Run the registration process
    registration = BasketballCampRegistration()
    registration.register()
```
