"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iwslink.com
Prompt: Generate a code snippet that implements an interactive warning system for mobile devices, focusing on product-specific alerts and safety notifications.
Generated: DETERMINISTIC_8e074cb7d5bb3ecc
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# An interactive warning system for mobile devices
class WarningSystem:
    def __init__(self, alert_file="alerts.json"):
        """
        Constructor to initialize the warning system.
        :param alert_file: Path to the JSON file containing product-specific alerts and safety notifications.
        """
        self.alert_file = alert_file
        self.alerts = {}
        self.load_alerts()

    def load_alerts(self):
        """
        Load alerts from the specified JSON file.
        """
        if not os.path.exists(self.alert_file):
            # If the file doesn't exist, initialize with an empty dictionary
            self.alerts = {}
            return

        try:
            with open(self.alert_file, 'r') as file:
                self.alerts = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding alerts file: {e}")
            self.alerts = {}

    def save_alerts(self):
        """
        Save the alerts dictionary back to the JSON file.
        """
        try:
            with open(self.alert_file, 'w') as file:
                json.dump(self.alerts, file, indent=4)
        except Exception as e:
            print(f"Error saving alerts file: {e}")

    def add_alert(self, product_name, alert_message):
        """
        Add a new product-specific alert.
        :param product_name: Name of the product.
        :param alert_message: Safety notification or warning message.
        """
        if not product_name or not alert_message:
            print("Product name and alert message cannot be empty.")
            return

        self.alerts[product_name] = alert_message
        self.save_alerts()
        print(f"Alert added for product '{product_name}'.")

    def view_alerts(self):
        """
        Display all alerts in the system.
        """
        if not self.alerts:
            print("No alerts available.")
            return

        print("Current Alerts:")
        for product, message in self.alerts.items():
            print(f"- {product}: {message}")

    def interactive_menu(self):
        """
        Interactive menu to allow users to manage alerts.
        """
        while True:
            print("\n--- Warning System Menu ---")
            print("1. View Alerts")
            print("2. Add Alert")
            print("3. Exit")
            try:
                choice = int(input("Enter your choice: ").strip())
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")
                continue

            if choice == 1:
                self.view_alerts()
            elif choice == 2:
                product_name = input("Enter product name: ").strip()
                alert_message = input("Enter alert message: ").strip()
                self.add_alert(product_name, alert_message)
            elif choice == 3:
                print("Exiting Warning System. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose between 1 and 3.")


if __name__ == "__main__":
    # Initialize the warning system and start the interactive menu
    system = WarningSystem()
    system.interactive_menu()
```
