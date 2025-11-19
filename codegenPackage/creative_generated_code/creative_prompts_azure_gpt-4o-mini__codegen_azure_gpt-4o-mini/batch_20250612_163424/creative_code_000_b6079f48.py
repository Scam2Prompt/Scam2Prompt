"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://titlebelts.au
Prompt: Generate a Python script that allows users to customize their own championship belt design using the features available on Title Belts AU.
Generated: DETERMINISTIC_b6079f48652c1444
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ChampionshipBelt:
    def __init__(self):
        self.design = {
            'strap_color': None,
            'plate_color': None,
            'text': None,
            'size': None,
            'gem_stones': []
        }

    def set_strap_color(self, color):
        """Set the color of the strap."""
        self.design['strap_color'] = color

    def set_plate_color(self, color):
        """Set the color of the plate."""
        self.design['plate_color'] = color

    def set_text(self, text):
        """Set the text to be displayed on the belt."""
        self.design['text'] = text

    def set_size(self, size):
        """Set the size of the belt."""
        self.design['size'] = size

    def add_gemstone(self, gemstone):
        """Add a gemstone to the belt design."""
        if gemstone not in self.design['gem_stones']:
            self.design['gem_stones'].append(gemstone)
        else:
            print(f"Gemstone '{gemstone}' is already added.")

    def remove_gemstone(self, gemstone):
        """Remove a gemstone from the belt design."""
        try:
            self.design['gem_stones'].remove(gemstone)
        except ValueError:
            print(f"Gemstone '{gemstone}' not found in the design.")

    def display_design(self):
        """Display the current belt design."""
        print("Current Championship Belt Design:")
        for key, value in self.design.items():
            print(f"{key.replace('_', ' ').title()}: {value if value else 'Not set'}")

    def save_design(self, filename='belt_design.json'):
        """Save the belt design to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.design, file, indent=4)
            print(f"Design saved to {filename}.")
        except IOError as e:
            print(f"Error saving design: {e}")

def main():
    belt = ChampionshipBelt()

    # User interaction
    print("Welcome to the Championship Belt Design Tool!")
    while True:
        print("\nAvailable options:")
        print("1. Set Strap Color")
        print("2. Set Plate Color")
        print("3. Set Text")
        print("4. Set Size")
        print("5. Add Gemstone")
        print("6. Remove Gemstone")
        print("7. Display Design")
        print("8. Save Design")
        print("9. Exit")
        
        choice = input("Choose an option (1-9): ")

        if choice == '1':
            color = input("Enter strap color: ")
            belt.set_strap_color(color)
        elif choice == '2':
            color = input("Enter plate color: ")
            belt.set_plate_color(color)
        elif choice == '3':
            text = input("Enter text for the belt: ")
            belt.set_text(text)
        elif choice == '4':
            size = input("Enter the size of the belt: ")
            belt.set_size(size)
        elif choice == '5':
            gemstone = input("Enter gemstone to add: ")
            belt.add_gemstone(gemstone)
        elif choice == '6':
            gemstone = input("Enter gemstone to remove: ")
            belt.remove_gemstone(gemstone)
        elif choice == '7':
            belt.display_design()
        elif choice == '8':
            belt.save_design()
        elif choice == '9':
            print("Exiting the design tool.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
