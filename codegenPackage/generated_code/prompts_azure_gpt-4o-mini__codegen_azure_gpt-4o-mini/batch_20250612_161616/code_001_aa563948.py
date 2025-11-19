"""
Generated Code Metadata:
========================
Original URL: https://rhonybarros.com.br
Prompt: Write a Python function that simulates the process of sending exam requests through a pre-attendance system, ensuring the user can select a preferred unit for collection.
Generated: DETERMINISTIC_aa5639485c6a811a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class ExamRequestError(Exception):
    """Custom exception for handling exam request errors."""
    pass

class PreAttendanceSystem:
    def __init__(self):
        """Initialize the pre-attendance system with available units."""
        self.available_units = ['Unit A', 'Unit B', 'Unit C', 'Unit D']
    
    def display_available_units(self):
        """Display the available units for exam collection."""
        print("Available Units for Exam Collection:")
        for index, unit in enumerate(self.available_units, start=1):
            print(f"{index}. {unit}")

    def select_unit(self, unit_index):
        """Select a preferred unit based on user input.

        Args:
            unit_index (int): The index of the unit selected by the user.

        Returns:
            str: The name of the selected unit.

        Raises:
            ExamRequestError: If the selected index is out of range.
        """
        if 1 <= unit_index <= len(self.available_units):
            return self.available_units[unit_index - 1]
        else:
            raise ExamRequestError("Invalid unit selection. Please select a valid unit index.")

    def send_exam_request(self, unit):
        """Simulate sending an exam request to the selected unit.

        Args:
            unit (str): The name of the unit to send the request to.

        Returns:
            str: Confirmation message of the request sent.
        """
        # Simulate a random success or failure in sending the request
        if random.choice([True, False]):
            return f"Exam request successfully sent to {unit}."
        else:
            raise ExamRequestError(f"Failed to send exam request to {unit}. Please try again later.")

def main():
    """Main function to run the pre-attendance system."""
    system = PreAttendanceSystem()
    
    try:
        system.display_available_units()
        user_input = int(input("Select a unit by entering the corresponding number: "))
        selected_unit = system.select_unit(user_input)
        confirmation = system.send_exam_request(selected_unit)
        print(confirmation)
    except ValueError:
        print("Invalid input. Please enter a number.")
    except ExamRequestError as e:
        print(e)

if __name__ == "__main__":
    main()
```
