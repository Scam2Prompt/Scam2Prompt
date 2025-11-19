"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Write a code snippet that automates the selection and ordering process for PU golf grips based on the workflow provided by Longhui Golf.
Generated: DETERMINISTIC_39410fd824547958
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class GolfGripOrderAutomation:
    """
    A class to automate the selection and ordering process for PU golf grips.
    """

    def __init__(self, grip_catalog_file):
        """
        Initialize the automation system.

        :param grip_catalog_file: Path to the JSON file containing grip catalog.
        """
        try:
            with open(grip_catalog_file, 'r') as file:
                self.grip_catalog = json.load(file)  # Load grip data from JSON file
        except FileNotFoundError:
            raise FileNotFoundError(f"Catalog file '{grip_catalog_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding the grip catalog file. Ensure it is a valid JSON file.")

    def display_grip_options(self):
        """
        Display available grip options to the user.
        """
        print("\nAvailable PU Golf Grips:")
        for grip in self.grip_catalog:
            print(f"{grip['id']}: {grip['name']} - ${grip['price']:.2f} ({grip['color']})")

    def select_grip(self):
        """
        Prompt the user to select a grip from the catalog.

        :return: The selected grip dictionary.
        """
        while True:
            try:
                grip_id = int(input("Enter the ID of the grip you want to order: "))
                selected_grip = next((grip for grip in self.grip_catalog if grip['id'] == grip_id), None)
                if not selected_grip:
                    print("Invalid grip ID. Please try again.")
                else:
                    return selected_grip
            except ValueError:
                print("Invalid input. Please enter a numeric grip ID.")

    def confirm_order(self, selected_grip):
        """
        Confirm the order details with the user.

        :param selected_grip: The selected grip dictionary.
        :return: Boolean indicating whether the order is confirmed.
        """
        print(f"\nYou selected: {selected_grip['name']} - ${selected_grip['price']:.2f} ({selected_grip['color']})")
        confirm = input("Do you want to proceed with the order? (yes/no): ").strip().lower()
        return confirm == 'yes'

    def process_order(self, selected_grip):
        """
        Process the order for the selected grip.

        :param selected_grip: The selected grip dictionary.
        """
        print("\nOrder placed successfully!")
        print(f"Order Details: {selected_grip['name']} - ${selected_grip['price']:.2f} ({selected_grip['color']})")
        print("Thank you for choosing Longhui Golf!")

def main():
    """
    Main function to run the automation workflow.
    """
    grip_catalog_file = "grip_catalog.json"  # Path to the grip catalog file

    try:
        automation = GolfGripOrderAutomation(grip_catalog_file)
        automation.display_grip_options()
        selected_grip = automation.select_grip()
        if automation.confirm_order(selected_grip):
            automation.process_order(selected_grip)
        else:
            print("\nOrder canceled. Thank you for visiting Longhui Golf!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
- The grip catalog file (`grip_catalog.json`) should be a JSON file structured like this:
```json
[
    {"id": 1, "name": "Pro Grip", "price": 25.99, "color": "Black"},
    {"id": 2, "name": "Elite Grip", "price": 30.99, "color": "Blue"},
    {"id": 3, "name": "Classic Grip", "price": 20.49, "color": "Red"}
]
```
- Ensure the JSON file exists in the same directory as the script or provide the correct path.
