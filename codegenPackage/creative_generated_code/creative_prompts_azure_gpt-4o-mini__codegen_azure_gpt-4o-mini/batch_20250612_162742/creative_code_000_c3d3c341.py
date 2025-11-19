"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duolingo.wiki
Prompt: How can I implement a feature to guide users through the Duolingo Super membership activation process using the app's interface?
Generated: DETERMINISTIC_c3d3c3412ca4257e
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DuolingoSuperMembership:
    def __init__(self):
        # Initialize the membership process
        self.membership_active = False

    def display_welcome_message(self):
        """Display a welcome message to the user."""
        print("Welcome to Duolingo! Let's guide you through activating your Super membership.")

    def show_membership_options(self):
        """Display the available membership options to the user."""
        print("Please choose a membership option:")
        print("1. Monthly Subscription - $12.99")
        print("2. Yearly Subscription - $79.99")
        option = input("Enter the number of your choice: ")
        return option

    def handle_membership_selection(self, option):
        """Handle the user's selection for the membership option."""
        try:
            if option == '1':
                self.activate_membership('Monthly Subscription', 12.99)
            elif option == '2':
                self.activate_membership('Yearly Subscription', 79.99)
            else:
                raise ValueError("Invalid option selected. Please choose 1 or 2.")
        except ValueError as e:
            print(e)
            self.show_membership_options()

    def activate_membership(self, plan_name, price):
        """Activate the selected membership plan."""
        print(f"Activating {plan_name} for ${price}...")
        # Simulate membership activation process
        self.membership_active = True
        print(f"Your {plan_name} has been successfully activated!")

    def run_membership_activation_process(self):
        """Run the entire membership activation process."""
        self.display_welcome_message()
        option = self.show_membership_options()
        self.handle_membership_selection(option)
        if self.membership_active:
            print("Thank you for becoming a Duolingo Super member!")

if __name__ == "__main__":
    # Main entry point for running the membership activation process
    membership_process = DuolingoSuperMembership()
    membership_process.run_membership_activation_process()
```
