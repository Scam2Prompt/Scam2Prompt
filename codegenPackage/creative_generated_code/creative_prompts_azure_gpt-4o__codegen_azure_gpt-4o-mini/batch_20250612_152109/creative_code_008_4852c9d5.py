"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Create a script that generates assembly instructions for UDIZINE's modular shelving systems, including Vertik and Palo systems, based on user-selected configurations.
Generated: DETERMINISTIC_4852c9d52f631fed
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ShelvingSystem:
    """Base class for a shelving system."""

    def __init__(self, system_name):
        self.system_name = system_name
        self.instructions = []

    def add_instruction(self, instruction):
        """Add a single instruction to the assembly list."""
        self.instructions.append(instruction)

    def generate_instructions(self):
        """Generate the complete assembly instructions."""
        return f"Assembly instructions for {self.system_name}:\n" + "\n".join(self.instructions)

class VertikShelving(ShelvingSystem):
    """Class for Vertik modular shelving system."""

    def __init__(self):
        super().__init__("Vertik")
        self.setup_instructions()

    def setup_instructions(self):
        """Set up the specific instructions for Vertik system."""
        self.add_instruction("Step 1: Assemble the vertical panels.")
        self.add_instruction("Step 2: Attach horizontal shelves at desired heights.")
        self.add_instruction("Step 3: Secure the unit to the wall using brackets.")
        self.add_instruction("Step 4: Finish with decorative end caps.")

class PaloShelving(ShelvingSystem):
    """Class for Palo modular shelving system."""

    def __init__(self):
        super().__init__("Palo")
        self.setup_instructions()

    def setup_instructions(self):
        """Set up the specific instructions for Palo system."""
        self.add_instruction("Step 1: Begin with the base panel.")
        self.add_instruction("Step 2: Attach side panels securely.")
        self.add_instruction("Step 3: Install shelves at specified intervals.")
        self.add_instruction("Step 4: Add finishing touches with trim pieces.")

def get_user_configuration():
    """Prompt user for their shelving configuration choice."""
    while True:
        print("Select a shelving system:")
        print("1. Vertik")
        print("2. Palo")
        choice = input("Enter 1 or 2: ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main function to run the assembly instruction generator."""
    try:
        user_choice = get_user_configuration()
        
        if user_choice == '1':
            shelving_system = VertikShelving()
        else:
            shelving_system = PaloShelving()

        instructions = shelving_system.generate_instructions()
        print(instructions)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
