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
    Calculates entry fees for an event based on age groups and lunch options.
    """

    def __init__(self):
        # Define age groups and their corresponding fees
        self.age_groups = {
            "child": {"min_age": 0, "max_age": 12, "fee": 100},
            "teen": {"min_age": 13, "max_age": 18, "fee": 200},
            "adult": {"min_age": 19, "max_age": 64, "fee": 500},
            "senior": {"min_age": 65, "max_age": float("inf"), "fee": 300},
        }

        # Define lunch options and their corresponding fees
        self.lunch_options = {"yes": 150, "no": 0}

    def calculate_fee(self, age, lunch_choice):
        """
        Calculates the entry fee based on age and lunch choice.

        Args:
            age (int): The age of the attendee.
            lunch_choice (str): The lunch choice, either "yes" or "no".

        Returns:
            int: The total entry fee.

        Raises:
            ValueError: If the age is not a positive integer or if the lunch choice is invalid.
        """
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")

        if lunch_choice not in self.lunch_options:
            raise ValueError("Invalid lunch choice. Please choose 'yes' or 'no'.")

        # Find the age group
        age_group = next(
            (group for group, details in self.age_groups.items() if details["min_age"] <= age <= details["max_age"]),
            None,
        )

        if age_group is None:
            raise ValueError("Age group not found.")

        # Calculate the total fee
        entry_fee = self.age_groups[age_group]["fee"]
        lunch_fee = self.lunch_options[lunch_choice]
        total_fee = entry_fee + lunch_fee

        return total_fee


def main():
    calculator = EventFeeCalculator()

    print("Holy Saraswati Puja Celebration Entry Fee Calculator")
    print("-----------------------------------------------")

    age = int(input("Enter your age: "))
    lunch_choice = input("Do you want lunch? (yes/no): ").lower()

    try:
        total_fee = calculator.calculate_fee(age, lunch_choice)
        print(f"Your total entry fee is: ${total_fee}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
