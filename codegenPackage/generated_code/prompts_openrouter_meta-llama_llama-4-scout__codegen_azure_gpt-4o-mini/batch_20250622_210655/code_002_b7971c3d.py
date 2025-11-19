"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Write a Python script to calculate entry fees for an event based on age groups, including options for lunch, similar to the Holy Saraswati Puja Celebration."
Generated: DETERMINISTIC_b7971c3df5b988c2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_fee_calculator.py

class EventFeeCalculator:
    """
    A class to calculate entry fees for an event based on age groups and lunch options.
    """

    def __init__(self):
        # Define age group fee structure
        self.fee_structure = {
            'child': 5,      # Age 0-12
            'teen': 10,      # Age 13-17
            'adult': 20,     # Age 18-64
            'senior': 15     # Age 65 and above
        }
        # Define lunch options
        self.lunch_fee = 10  # Flat fee for lunch

    def calculate_fee(self, age, wants_lunch):
        """
        Calculate the entry fee based on age and lunch preference.

        :param age: Age of the participant
        :param wants_lunch: Boolean indicating if lunch is required
        :return: Total fee for the event
        """
        try:
            # Determine age group
            if age < 0:
                raise ValueError("Age cannot be negative.")
            elif age <= 12:
                fee = self.fee_structure['child']
            elif age <= 17:
                fee = self.fee_structure['teen']
            elif age <= 64:
                fee = self.fee_structure['adult']
            else:
                fee = self.fee_structure['senior']

            # Add lunch fee if applicable
            if wants_lunch:
                fee += self.lunch_fee

            return fee

        except ValueError as e:
            print(f"Error: {e}")
            return None

def main():
    """
    Main function to run the event fee calculator.
    """
    calculator = EventFeeCalculator()

    # Example input
    try:
        age = int(input("Enter your age: "))
        wants_lunch_input = input("Do you want lunch? (yes/no): ").strip().lower()
        wants_lunch = wants_lunch_input == 'yes'

        # Calculate the fee
        total_fee = calculator.calculate_fee(age, wants_lunch)

        if total_fee is not None:
            print(f"The total entry fee is: ${total_fee}")

    except ValueError:
        print("Invalid input. Please enter a valid age.")

if __name__ == "__main__":
    main()
```
